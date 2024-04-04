use copy_cards::{Card, Deck};

fn main() {
    let mut deck = Deck::new();
    deck.shuffle();

    let mut money = 100;
    let mut game_count = 0;

    println!("Welcome to the game of Copy Cards!");
    println!("In this game, you will draw 10 cards from a deck of 52 cards.");
    println!("If there are any duplicate cards, you lose!");
    println!("You start with $100. Each round costs $10 to play.");
    println!("After the 4th card is drawn, you can choose to double your bet.");
    println!("Ready for your first card?");

    loop {
        if money < 10 {
            println!("You're out of money! Game over!");
            println!("You played {} games.", game_count);
            return;
        }

        game_count += 1;
        money -= 10;

        let mut drawn_cards: Vec<Card> = Vec::new();

        // every time we press enter we draw a card
        let mut doubled_bet = false;
        for i in 0..10 {
            if i == 4 {
                println!("You've drawn 4 cards! Would you like to double your bet? (y/n)");
                let mut input = String::new();
                let _ = std::io::stdin().read_line(&mut input);

                if input.trim() == "y" {
                    money -= 10;
                    doubled_bet = true;
                }
            } else {
                let _ = std::io::stdin().read_line(&mut String::new());
            }

            let card = deck.peek().unwrap();
            println!("You drew a: {}", card);

            if drawn_cards.contains(card) {
                println!("You drew a duplicate card! You lose!");
                break;
            }

            drawn_cards.push(card.clone());
            deck.shuffle();

            if i == 9 {
                println!("Congratulations! You drew 10 unique cards and won the game!");
                money += if doubled_bet { 40 } else { 20 };
                break;
            }
            println!("Press enter to draw another card...");
        }

        println!("You currently have ${}.", money);
    }
}
