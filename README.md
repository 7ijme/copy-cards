# Copy Cards - The Casino Game

This is a group project we had to do for an advanced maths course. We had to create our own casino game, and calculate how much money the casino would earn off of that game.

## Maths
This game is inspired by the [Birthday Paradox](https://en.wikipedia.org/wiki/Birthday_problem). This paradox suggests that you only need 23 people to have more than a 50% chance of two of those people sharing the same birthday. This doesn't sound intuitive at all, and we used this to our advantage to fool the players.

The formula for the Birthday Paradox is as follows:
$$P(s)=\frac{n!}{(n-k)!*n^k}$$
Where n is the number of birthdays, and k is the number of people.

In this game, we have a deck of 52 cards. We draw a card, note which one it was, put it back, and then draw a card again. We do this a total of 10 times. The percentage of the casino winning is:
$$P(s)=1-\frac{52!}{(52-10)!*52^{10}}\approx60.2\\%$$

After drawing 4 cards, the player can choose to double their bet. The percentage of the casino then is:
$$P(s_4)=1-\frac{(52-4)!}{(52-10)!*52^{6}}\approx55.3\\%$$

When we play the game 10 000 times, we get the following values.

$$μ=np=10000*0.602=6020$$
$$σ=\sqrt{np(1-p)}=\sqrt{10000\*0.602\*(1-0.602)}\approx48.9$$
We can use this data to create a normal distribution which showcases that the casino wins the majority of the games.
![graph](https://github.com/7ijme/copy-cards/assets/68817281/e0fb2e32-8928-489a-8deb-a48666952229)

The graph shows the casino has a 65.9% chance of winning more than 6000/10000 games.
