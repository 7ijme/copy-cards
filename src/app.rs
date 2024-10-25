// - This file contains the main application logic.

use crate::tui;
use crossterm::event::{self, Event, KeyCode, KeyEvent, KeyEventKind};
use ratatui::{
    prelude::*,
    symbols::border,
    widgets::{block::*, *},
};
use small_card_deck::{Card, Deck};
use std::io;
use serde::{Deserialize, Serialize};
use serde_json;
use std::fs::OpenOptions;
use std::io::{Read, Write, Seek, SeekFrom};

#[derive(Debug, Default)]
pub struct App {
    money: u32,
    exit: bool,
    deck: Deck,
    cards_drawn: Vec<Card>,
    doubled: bool,
    lost: bool,
    won: bool,
    game_over: bool,
    games_played: u32,
    amount_won: u32,
    i: u16,
}

#[derive(Serialize, Deserialize, Debug)]
struct GameData {
    games_played: u32,
    amount_won: u32,
    ratio: f32,
}

impl App {
    /// runs the application's main loop until the user quits
    pub fn run(&mut self, terminal: &mut tui::Tui) -> io::Result<()> {
        self.deck = Deck::new();
        self.money = 100;

        while !self.exit {
            terminal.draw(|frame| self.render_frame(frame))?;
            // self.handle_events()?;
            self.handle_draw();

            // check if press q to quit
            // if event::poll(std::time::Duration::from_millis(1))? {
            //     self.handle_events()?;
            // }

            if self.game_over {
                let ratio = if self.games_played == 0 {
                    0.0
                } else {
                    self.amount_won as f32 / self.games_played as f32
                };
                // write to file the ratio of games won
                // data.json
                // form [{games_played: 0, amount_won: 0, ratio: 0.0}]
                // if file does not exist, create it
                // if file exists, read it and append the new data

                add_game_data("data.json", self.games_played, self.amount_won, ratio)?;

                if self.i == 49 {
                    self.exit();
                }
                self.i += 1;
                self.game_over = false;
                self.games_played = 0;
                self.money = 100;
                self.deck = Deck::new();
                self.amount_won = 0;

                // get ratio of games won

            }
        }
        Ok(())
    }

    fn render_frame(&self, frame: &mut Frame) {
        frame.render_widget(self, frame.size());
    }

    fn handle_events(&mut self) -> io::Result<()> {
        match event::read()? {
            // it's important to check that the event is a key press event as
            // crossterm also emits key release and repeat events on Windows.
            Event::Key(key_event) if key_event.kind == KeyEventKind::Press => {
                self.handle_key_event(key_event)
            }
            _ => {}
        };
        Ok(())
    }

    fn handle_key_event(&mut self, key_event: KeyEvent) {
        match key_event.code {
            KeyCode::Char('q') => self.exit(),
            KeyCode::Char('y') => self.handle_double(),
            KeyCode::Enter | KeyCode::Char(' ') => self.handle_draw(),
            _ => {}
        }
    }

    fn handle_draw(&mut self) {
        if self.game_over {
            return;
        }

        if self.lost {
            self.lost = false;
            self.cards_drawn.clear();
            if self.money < 10 {
                self.handle_game_over();
                return;
            }
        }

        if self.won {
            self.won = false;
            self.cards_drawn.clear();
        }

        if self.cards_drawn.len() == 0 {
            self.bet();
            self.games_played += 1;
        }

        self.deck.shuffle();
        let card = self.deck.peek().unwrap();
        if self.cards_drawn.contains(card) {
            self.cards_drawn.push(card.clone());
            self.handle_loss();
            return;
        } else {
            self.cards_drawn.push(card.clone());
        }

        if self.cards_drawn.len() == 10 {
            self.handle_win();
        }
    }

    fn handle_loss(&mut self) {
        self.lost = true;
        self.doubled = false;
    }

    fn handle_win(&mut self) {
        self.return_money();
        self.doubled = false;
        self.won = true;
        self.amount_won += 1;
    }

    fn handle_double(&mut self) {
        if self.cards_drawn.len() == 3 && !self.doubled && self.money >= 10 {
            self.doubled = true;
            self.bet();
        }
    }

    fn exit(&mut self) {
        self.exit = true;
    }

    fn bet(&mut self) {
        if self.money < 10 {
            self.handle_game_over();
            return;
        }
        self.money -= 10;
    }

    fn handle_game_over(&mut self) {
        self.game_over = true;
    }

    fn return_money(&mut self) {
        self.money += if self.doubled { 40 } else { 20 };
    }
}

impl Widget for &App {
    fn render(self, area: Rect, buf: &mut Buffer) {
        let title = Title::from(" Copy Cards ".bold());
        let instructions = Title::from(Line::from(vec![
            " Draw new card ".into(),
            "<Enter | Space>".blue().bold(),
            " Double bet (at 3rd card drawn) ".into(),
            "<Y>".blue().bold(),
            " Quit ".into(),
            "<Q> ".blue().bold(),
        ]));
        let block = Block::default()
            .title(title.alignment(Alignment::Center))
            .title(
                instructions
                    .alignment(Alignment::Center)
                    .position(Position::Bottom),
            )
            .borders(Borders::ALL)
            .border_style(Style::default().fg(Color::White))
            .border_type(BorderType::Rounded)
            .border_set(border::THICK);

        let description_text = Text::from(vec![
            Line::from(vec![
                "Iteration".into(),
                self.i.to_string().yellow(),
                " - ".into(),
                "Money: ".into(),
                (self.money.to_string() + "$").green(),
            ]),
            Line::from(vec![
                // explain the game
                "The goal is to draw 10 cards without drawing the same card twice.".into(),
            ]),
            Line::from(vec![
                "You can double your bet at the ".into(),
                "3rd".yellow(),
                " card drawn.".into(),
            ]),
        ]);

        Paragraph::new(description_text)
            .centered()
            .block(block)
            .render(area, buf);

        if self.game_over {
            let gameover_text = Text::from(vec![Line::from("Game Over".red().bold())]);
            let new_area = area.clone().inner(&Margin {
                horizontal: area.width - 2,
                vertical: (area.height - 3) / 2,
            });
            // create padding around the cards_drawn
            Paragraph::new(gameover_text)
                .alignment(Alignment::Center)
                // create padding around the cards
                .block(
                    Block::default()
                        .borders(Borders::NONE)
                        .title_alignment(Alignment::Center)
                        // .padding(Padding::vertical(new_area.height / 2 - 1)),
                )
                .render(new_area, buf);
        } else {
            let cards = self
                .cards_drawn
                .iter()
                .map(|card| card.to_string())
                .collect::<Vec<_>>();
            let cards = cards.join("   ");

            let has_doubled_text = if self.doubled {
                "Doubled".green()
            } else {
                "Not doubled".red()
            };

            let status_text = if self.won {
                "Won".green()
            } else if self.lost {
                "Lost ".red()
            } else {
                "Playing".yellow()
            };

            let information = vec![
                "Cards Drawn: ".into(),
                self.cards_drawn.len().to_string().yellow(),
                " - ".into(),
                has_doubled_text,
                " - ".into(),
                status_text,
            ];

            let text = Text::from(vec![Line::from(information), Line::from(cards)]);
            let new_area = area.clone().inner(&Margin {
                horizontal: area.width / 4,
                vertical: (area.height - 3) / 2,
            });

            Paragraph::new(text)
                .alignment(Alignment::Center)
                .block(Block::default().borders(Borders::NONE))
                .render(new_area, buf);
        }
    }
}
fn add_game_data(path: &str, games_played: u32, amount_won: u32, ratio: f32) -> std::io::Result<()> {
     // Open the file with read, write, and create options
    let mut file = OpenOptions::new()
        .read(true)
        .write(true)
        .create(true)
        .open(path)?;

    // Check if the file is empty; if so, write an empty array (`[]`) to initialize it
    let mut content = String::new();
    file.read_to_string(&mut content)?;

    let mut data: Vec<GameData> = if content.trim().is_empty() {
        // Write `[]` to initialize and flush immediately
        file.write_all(b"[]")?;
        file.flush()?;
        Vec::new() // Start with an empty Vec in memory
    } else {
        // If the file is not empty, parse the existing JSON content
        // Reset the cursor to the start for reading the file's content
        file.seek(SeekFrom::Start(0))?;
        serde_json::from_str(&content)?
    };

    // Add the new entry
    let new_entry = GameData {
        games_played,
        amount_won,
        ratio,
    };
    data.push(new_entry);

    // Serialize the updated data
    let updated_content = serde_json::to_string_pretty(&data)?;

    // Re-open the file in truncate mode to clear old content and write updated data
    let mut file = OpenOptions::new()
        .write(true)
        .truncate(true)
        .open(path)?;

    file.write_all(updated_content.as_bytes())?;

    Ok(())
}
