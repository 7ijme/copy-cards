use copy_cards::{Card, Deck};
use crossterm::event::{self, Event, KeyCode, KeyEvent, KeyEventKind};
use ratatui::{
    prelude::*,
    symbols::border,
    widgets::{block::*, *},
};
use std::io;

mod tui;

fn main() -> io::Result<()> {
    let mut terminal = tui::init()?;
    let app_result = App::default().run(&mut terminal);
    tui::restore()?;
    app_result
}

#[derive(Debug, Default)]
pub struct App {
    money: u8,
    exit: bool,
    deck: Deck,
    cards_drawn: Vec<Card>,
    doubled: bool,
    lost: bool,
    game_over: bool,
    games_played: u8,
}

impl App {
    /// runs the application's main loop until the user quits
    pub fn run(&mut self, terminal: &mut tui::Tui) -> io::Result<()> {
        self.deck = Deck::new();
        self.money = 100;
        while !self.exit {
            terminal.draw(|frame| self.render_frame(frame))?;
            self.handle_events()?;
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
            return;
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
        self.cards_drawn.clear();
        self.doubled = false;
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

        let has_doubled_text = if self.doubled {
            "Doubled".green()
        } else {
            "Not doubled".red()
        };

        let text = Text::from(vec![
            Line::from(vec![
                "Games played: ".into(),
                self.games_played.to_string().yellow(),
                " - ".into(),
                "Money: ".into(),
                (self.money.to_string() + "$").green(),
                " - ".into(),
                has_doubled_text,
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

        Paragraph::new(text)
            .centered()
            .block(block)
            .render(area, buf);

        if self.game_over {
            let text = Text::from(vec![Line::from("Game Over".red().bold())]);
            let new_area = area.clone().inner(&Margin {
                horizontal: area.width,
                vertical: (area.height - 3) / 2,
            });
            // create padding around the cards_drawn
            Paragraph::new(text)
                .alignment(Alignment::Center)
                .block(
                    Block::default()
                        .borders(Borders::NONE)
                        .title_alignment(Alignment::Center)
                        .padding(Padding::vertical(new_area.height / 2 - 1)),
                )
                .render(new_area, buf);
        } else {
            let cards = self
                .cards_drawn
                .iter()
                .map(|card| card.to_string())
                .collect::<Vec<_>>();
            let cards = cards.join("   ");
            let text = Text::from(vec![Line::from(cards)]);
            let new_area = area.clone().inner(&Margin {
                horizontal: area.width,
                vertical: (area.height - 3) / 2,
            });
            // create padding around the cards
            Paragraph::new(text)
                .alignment(Alignment::Center)
                .block(
                    Block::default()
                        .borders(Borders::NONE)
                        .title(format!(
                            " Cards Drawn: {} {}",
                            self.cards_drawn.len(),
                            if self.lost { "- Lost " } else { "" }
                        ))
                        .title_alignment(Alignment::Center),
                )
                .render(new_area, buf);
        }
    }
}
