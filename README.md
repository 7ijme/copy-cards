# Copy Cards

## Het Spel

De speler trekt een kaart uit een doos waardoor het niet zichtbaar is welke kaart gepakt wordt. In die doos zit een kaartspel. Er wordt genoteerd welke kaart er getrokken is en de kaart wordt terug gestopt. Dit doet de speler nog tien keer. Als er geen dubbele kaart getrokken wordt, wint de speler. Als dat wel gebeurt wint het casino. Als er drie kaarten getrokken zijn en het casino heeft nog niet gewonnen, kan de speler nog zijn inzet verdubbelen. Als de speler wint, krijgt hij zijn inzet dubbel terug, maar als hij verliest, is hij zijn inzet kwijt. 

## De kansen

### Birthday Paradox

Dit spel is gebaseerd op het [Birthday paradox](https://en.wikipedia.org/wiki/Birthday_problem). Het lijk intuïtief dat er redelijk wat mensen nodig zijn om de kans 50\% te maken dat er 2 mensen dezelde verjaardag hebben. Echter zijn er maar 23 nodig. De formule om dit te berekenen is:
$P(c)=1-\frac{n!}{(n-k)!*n^{k}}$. In deze formule is $n$ het aantal verjaardagen, en $k$ het aantal mensen.

### Verwachtingswaarde

Met de vorige formule kunnen we de verwachtingswaarde berekenen.
$$P(c)=1-\frac{52!}{(52-10)!\*52^{10}}\approx60.2\%$$
Nadat de speler 3 kaarten heeft getrokken, kan hij zijn inzet verdubbelen. Dit zijn de kansen dat het casino wint voor het verdubbelen, na het verdubbelen en dat de speler wint.
$$P(c_{1-3})=1-\frac{52!}{(52-3)!\*52^{3}}\approx5.7\%$$
$$P(c_{4-10})=1-((1-\frac{52!}{(52-3)!\*52^{3}})+\frac{52!}{(52-10)!\*52^{10}})\approx54.6\%$$
$$P(p)=\frac{52!}{(52-10)!\*52^{10}}\approx39.7\%$$
### Geld
Dus verdient het casino ongeveer:
$$m(g,s,d)=g(s\*0.056+s(b+1)\*0.547-s(b+1)\*.397)$$
Waar $m$ geld is, $g$ het aantal spellen, $s$ de inzet en $d$ of de speler z'n inzet verdubbelt na 3 zetten (dit is een waarde van 0 of 1, een boolean).
Stel dat dit spel $10 000$ keer gespeeld wordt, en de speler verdubbelt elke keer bij de derde kaart zijn inzet van €10.
$$m(10000,10,1)=10000\*3.56=€35600$$
### Normaalverdeling
Laten we het spel weer 10000 keer spelen.
Als $n$ groter wordt, kunnen we aanemen dat:
$$\mathcal{B}(n,p)\sim\mathcal{N}(np,\sqrt{np(1-p})$$
Nu berekenen we de waarden van $\mu$ en $\sigma$ berekenen.
$$\mu=np=10000\*0.602=6020$$
$$\sigma=\sqrt{np(1-p)}=\sqrt{10000\*0.602\*(1-0.602)}\approx48.9$$
Deze kunnen we gebruiken om een normaalverdeling te plotten.

![graph](https://github.com/7ijme/copy-cards/assets/68817281/e0fb2e32-8928-489a-8deb-a48666952229)

Hier kunnen we zien dat de kans  65.9\% is dat het casino 6000 of meer keer wint van de 10000.
## Installeren
Om het spel te spelen moet je 1 van de volgende dingen doen:

Ga naar [releases](https://github.com/7ijme/copy-cards/releases/latest) en download het bestand voor jouw OS.

Je kan het spel ook installeren met `cargo`
```sh
cargo install copy-cards
```

Als dit niet werkt, of je wilt lokaal het project bouwen:
```sh
git clone https://github.com/7ijme/copy-cards
cd copy-cards
cargo build --release
```

Nu kan je het spel spelen, veel plezier!
