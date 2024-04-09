// - This file contains the deck, card, and suit types

use rand::seq::SliceRandom;
use std::fmt::Display;

#[derive(Debug, Clone, PartialEq)]
pub enum Suit {
    Hearts,
    Diamonds,
    Clubs,
    Spades,
}

impl Suit {
    fn to_string(&self) -> String {
        match self {
            Suit::Hearts => "♥".to_string(),
            Suit::Diamonds => "♦".to_string(),
            Suit::Clubs => "♣".to_string(),
            Suit::Spades => "♠".to_string(),
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
pub enum Value {
    Ace,
    Two,
    Three,
    Four,
    Five,
    Six,
    Seven,
    Eight,
    Nine,
    Ten,
    Jack,
    Queen,
    King,
}

impl Value {
    fn to_string(&self) -> String {
        match self {
            Value::Ace => "A".to_string(),
            Value::Two => "2".to_string(),
            Value::Three => "3".to_string(),
            Value::Four => "4".to_string(),
            Value::Five => "5".to_string(),
            Value::Six => "6".to_string(),
            Value::Seven => "7".to_string(),
            Value::Eight => "8".to_string(),
            Value::Nine => "9".to_string(),
            Value::Ten => "10".to_string(),
            Value::Jack => "J".to_string(),
            Value::Queen => "Q".to_string(),
            Value::King => "K".to_string(),
        }
    }
}

impl Display for Value {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.to_string())
    }
}

#[derive(Debug, Clone)]
pub struct Card {
    suit: Suit,
    value: Value,
}

impl PartialEq for Card {
    fn eq(&self, other: &Self) -> bool {
        self.suit == other.suit && self.value == other.value
    }
}

impl Card {
    fn new(suit: Suit, value: Value) -> Self {
        Card { suit, value }
    }

    fn to_string(&self) -> String {
        format!("{}{}", self.value.to_string(), self.suit.to_string())
    }
}

impl Display for Card {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.to_string())
    }
}

#[derive(Debug, Clone, Default)]
pub struct Deck {
    cards: Vec<Card>,
}

impl Deck {
    pub fn new() -> Self {
        let mut cards = Vec::new();
        let suits = vec![Suit::Hearts, Suit::Diamonds, Suit::Clubs, Suit::Spades];
        let values = vec![
            Value::Ace,
            Value::Two,
            Value::Three,
            Value::Four,
            Value::Five,
            Value::Six,
            Value::Seven,
            Value::Eight,
            Value::Nine,
            Value::Ten,
            Value::Jack,
            Value::Queen,
            Value::King,
        ];

        for suit in suits.iter() {
            for value in values.iter() {
                cards.push(Card::new(suit.clone(), value.clone()));
            }
        }

        Deck { cards }
    }

    pub fn shuffle(&mut self) {
        self.cards.shuffle(&mut rand::thread_rng());
    }

    pub fn peek(&self) -> Option<&Card> {
        self.cards.first()
    }
}

impl Display for Deck {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        for card in self.cards.iter() {
            write!(f, "{} ", card)?;
        }
        Ok(())
    }
}
