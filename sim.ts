import fs from "node:fs";

enum Suit {
  HEARTS = "♥",
  DIAMONDS = "♦",
  CLUBS = "♣",
  SPADES = "♠",
}
enum Rank {
  TWO = "2",
  THREE = "3",
  FOUR = "4",
  FIVE = "5",
  SIX = "6",
  SEVEN = "7",
  EIGHT = "8",
  NINE = "9",
  TEN = "10",
  JACK = "J",
  QUEEN = "Q",
  KING = "K",
  ACE = "A",
}

type Card = `${Rank}${Suit}`;

class SimDeck {
  cards: Card[];
  money: number;
  gamesPlayed: number;
  gamesWon: number;
  moneyOnRound: number[];
  foundCards: Set<Card>;
  constructor() {
    this.cards = [];
    this.money = 100;
    this.gamesPlayed = 0;
    this.gamesWon = 0;
    this.moneyOnRound = [this.money];
    this.foundCards = new Set();
	this.roundLost = false;
    for (const suit in Suit) {
      for (const rank in Rank) {
        this.cards.push(`${rank}${suit}`);
      }
    }
  }
  random() {
    const card = this.cards[Math.floor(Math.random() * this.cards.length)];

	if (this.foundCards.has(card)) {
		this.roundLost = true;
		return;
	}

	this.foundCards.add(card);
  }
  handleRound() {
    this.gamesPlayed++;
    if (this.roundLost) {
	  this.roundLost = false;
      this.money -= 10;
    } else {
      this.money += 10;
      this.gamesWon++;
    }
	this.foundCards.clear();
    this.moneyOnRound.push(this.money);
  }
  play() {
    while (this.money > 0) {
	  for (let i = 0; i < 10; i++) {
		this.random();
		if (this.roundLost) break;
	  }
      this.handleRound();
    }
  }
  data() {
    return {
      gamesPlayed: this.gamesPlayed,
      gamesWon: this.gamesWon,
      moneyOnRound: this.moneyOnRound,
    };
  }
}

const data = [];
for (let i = 0; i < 10000; i++) {
  const deck = new SimDeck();
  deck.play();
  data.push(deck.data());
}
console.log(data);
const totalGamesPlayed = data.reduce((acc, d) => acc + d.gamesPlayed, 0);
const totalGamesWon = data.reduce((acc, d) => acc + d.gamesWon, 0);
const averageWinRate = (totalGamesWon / totalGamesPlayed) * 100;
console.log(`Average win rate: ${averageWinRate}%`);
// get from input when running the script
const input = process.argv[2];
fs.writeFileSync(input || "moreData.json", JSON.stringify(data));
