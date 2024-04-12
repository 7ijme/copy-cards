# Copy Cards

## What is it?
This is a group project I had to work on where we had to create a casino game and calculate all the juicy maths behind it.

## The Game

The player draws a card out of a closed box. The card gets noted a put back. The player does this a total of 10 times. If the same card gets drawn twice the player loses, and if that doesn't happen, the player wins. After 3 cards drawn, the player can decide to double their bet. When the player wins, they get back double their bet, and when they lose, the casino keeps the money.

## Chances

### Birthday Paradox

This game is based on the [Birthday paradox](https://en.wikipedia.org/wiki/Birthday_problem). It sounds intuitive that you need quite a lot of people to have a 50% chance of 2 people sharing a birthday. However, you only need 23 people. The formula to calculate this is:
$P(c)=1-\frac{n!}{(n-k)!\cdot n^{k}}$. In this formula $n$ is the amount of birthdays (normally 365), and $k$ is the amount of people.

### Expected value

With the previous formula we can calculate the expected value.
$$P(c)=1-\frac{52!}{(52-10)!\cdot52^{10}}\approx60.2\\%$$
After 3 cards drawn, the played can double their bet. These are the chances the casino wins before the doubling, after the doubling and the player winning.
$$P(c_{1-3})=1-\frac{52!}{(52-3)!\cdot52^{3}}\approx5.7\\%$$
$$P(c_{4-10})=1-((1-\frac{52!}{(52-3)!\cdot52^{3}})+\frac{52!}{(52-10)!\cdot52^{10}})\approx54.6\\%$$
$$P(p)=\frac{52!}{(52-10)!\cdot52^{10}}\approx39.7\\%$$

### Money
Therefore, the casino approximately earns:
$$m(g,s,d)=g\\cdot(s\cdot0.056+s(b+1)\cdot0.547-s(b+1)\cdot.397)$$
Where $m$ is money, $g$ is the amount of games, $s$ is the bet and $d$ is whether the player doubles down (this is a boolean value, 0 or 1).
Imagine the game get played $10 000$ times, and the player doubles down every time he draws his third card. His initial bet is €10.
$$m(10000,10,1)=10000\cdot3.56=€35600$$

### Normal distribution
Let's play the game 10000 times again.
When $n$ gets closer to infinity, we can assume that:

$$\mathcal{B}(n,p)\sim\mathcal{N}(np,\sqrt{np(1-p})$$
Now we can calculate the values of $\mu$ and $\sigma$.

$$\mu=np=10000\cdot0.602=6020$$

$$\sigma=\sqrt{np(1-p)}=\sqrt{10000\cdot0.602\cdot(1-0.602)}\approx48.9$$
We can use this to plot a graph.

![graph](https://github.com/7ijme/copy-cards/assets/68817281/e0fb2e32-8928-489a-8deb-a48666952229)

We can see that there is a 65.9\% chance of the casuno winning 6000 or more of the 10000 games.

## Installation
To play the game you have to do one of these things:

Go to [releases](https://github.com/7ijme/copy-cards/releases/latest) and download the file corresponding to your OS.

You can also install the game with `cargo`. Beware that you do need [Rust](https://www.rust-lang.org/tools/install) installed.
```sh
cargo install copy-cards
```

If that doesn't work, or you want to build locally, here's what to do. You need [Rust](https://www.rust-lang.org/tools/install) installed for this too.
```sh
git clone https://github.com/7ijme/copy-cards
cd copy-cards
cargo build --release
```

Now you can play the game, have fun!
