import json
import matplotlib.pyplot as plt
import numpy as np

# JSON-bestand inlezen
with open('moreData.json') as file:
    data = json.load(file)

# Extract data for plotting
# games_played = np.array([entry['gamesPlayed'] for entry in data])
# games_won = np.array([entry['gamesWon'] for entry in data])
# win_percentage = np.where(games_played > 0, (games_won / games_played) * 100, 0)
# print(np.mean(win_percentage))


#NOTE: werkt
# total_games = sum([entry['gamesPlayed'] for entry in data])
# total_wins = sum([entry['gamesWon'] for entry in data])
# print(f'Totaal aantal gespeelde spellen: {total_games}')
# print(f'Totaal aantal gewonnen spellen: {total_wins}')
# print(f'Percentage gewonnen spellen: {total_wins / total_games * 100:.2f}%')

# Plot 1: Aantal gespeelde en gewonnen spellen per game
# plt.figure(figsize=(10, 5))
# plt.plot(games_played, label='Games Played', marker='o')
# plt.plot(games_won, label='Games Won', marker='x')
# plt.xlabel('Game Index')
# plt.ylabel('Aantal Spellen')
# plt.title('Aantal Gespeelde en Gewonnen Spellen per Game')
# plt.legend()
# plt.grid(True)
#
# # Plot 2: Boxplot voor de verdeling van moneyOnRound
# plt.figure(figsize=(10, 5))
# plt.boxplot(money_on_round, patch_artist=True)
# plt.xlabel('Game Index')
# plt.ylabel('Money on Round')
# plt.title('Verdeling van Money on Round per Game')

# Plot 3: Percentage gewonnen spellen per game
# window_size = 50  # Pas de vengrootte aan om de gladheid te regelen
# smooth_win_percentage = np.convolve(win_percentage, np.ones(window_size)/window_size, mode='valid')
#
# plt.figure(figsize=(10, 5))
# plt.plot(smooth_win_percentage, label='Win Percentage', color='green', marker='^')
# plt.xlabel('Game Index')
# plt.ylabel('Win Percentage (%)')
# plt.title('Percentage Gewonnen Spellen per Game')
# plt.ylim(0, 100)
# plt.grid(True)
# #
# # # Toon de plots
# plt.show()


# pogin 2
# import json
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.stats import poisson
#
# # JSON-bestand inlezen
# with open('moreData.json') as file:
#     data = json.load(file)
#
# # Extract money per round data
# all_money = [amount for entry in data for amount in entry['moneyOnRound']]
#
# # Bereken het gemiddelde voor de Poisson-verdeling
# lambda_param = np.mean(all_money)
#
# # Maak een histogram van de bedragen per ronde
# plt.figure(figsize=(10, 5))
# count, bins, ignored = plt.hist(all_money, bins=30, density=True, alpha=0.6, color='blue', label='Observed Data')
#
# # Voeg de Poisson-verdeling toe
# x_values = np.arange(0, int(max(all_money))+1)
# poisson_values = poisson.pmf(x_values, lambda_param)
# plt.plot(x_values, poisson_values, 'r-', marker='o', label='Poisson Distribution (λ = {:.2f})'.format(lambda_param))
#
# plt.xlabel('Money on Round')
# plt.ylabel('Frequency Density')
# plt.title('Histogram van Geld per Ronde met Poisson-verdeling')
# plt.legend()
# plt.grid(True)
#
# # Toon de plot
# plt.show()

# poging 3
# import json
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.stats import norm
#
# # JSON-bestand inlezen
# with open('moreData.json') as file:
#     data = json.load(file)
#
# # Extract money per round data, met een controle voor 'moneyOnRound'
# all_money = [amount for entry in data if 'moneyOnRound' in entry for amount in entry['moneyOnRound']]
#
# # Controleer of de lijst niet leeg is
# if all_money:
#     # Bereken het gemiddelde en de standaarddeviatie voor de normale verdeling
#     mean = np.mean(all_money)
#     std_dev = np.std(all_money)
#
#     # Maak een histogram van de bedragen per ronde met logaritmische x-as
#     plt.figure(figsize=(10, 5))
#     count, bins, ignored = plt.hist(all_money, bins=30, density=True, alpha=0.6, color='blue', label='Observed Data')
#     
#     # Voeg de normale verdeling toe
#     x_values = np.linspace(min(all_money), max(all_money), 1000)
#     normal_values = norm.pdf(x_values, mean, std_dev)
#     plt.plot(x_values, normal_values, 'r-', lw=2, label='Normal Distribution (μ = {:.2f}, σ = {:.2f})'.format(mean, std_dev))
#
#     plt.xscale('log')  # Logaritmische schaal voor de x-as
#     plt.xlabel('Money on Round (log scale)')
#     plt.ylabel('Frequency Density')
#     plt.title('Histogram van Geld per Ronde met Normale Verdeling (log schaal)')
#     plt.legend()
#     plt.grid(True, which="both", ls="--")  # Zorgt ervoor dat het raster past bij de log schaal
#
#     # Toon de plot
#     plt.show()
# else:
#     print("Geen geld per ronde data gevonden in het JSON-bestand.")
#

# poging 4
# import json
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.stats import norm
#
# # JSON-bestand inlezen
# with open('moreData.json') as file:
#     data = json.load(file)
#
# # Extract money per round data, met een controle voor 'moneyOnRound'
# all_money = [amount for entry in data if 'moneyOnRound' in entry for amount in entry['moneyOnRound']]
#
# # Controleer of de lijst niet leeg is
# if all_money:
#     # Bereken het gemiddelde en de standaarddeviatie voor de normale verdeling
#     mean = np.mean(all_money)
#     std_dev = np.std(all_money)
#
#     # Maak een histogram van de bedragen per ronde
#     plt.figure(figsize=(10, 5))
#     count, bins, ignored = plt.hist(all_money, bins=30, density=True, alpha=0.6, color='blue', label='Observed Data')
#     
#     # Voeg de normale verdeling toe
#     x_values = np.linspace(min(all_money), max(all_money), 1000)
#     normal_values = norm.pdf(x_values, mean, std_dev)
#     plt.plot(x_values, normal_values, 'r-', lw=2, label='Normal Distribution (μ = {:.2f}, σ = {:.2f})'.format(mean, std_dev))
#
#     plt.xlabel('Money on Round')
#     plt.ylabel('Frequency Density')
#     plt.title('Histogram van Geld per Ronde met Normale Verdeling')
#     plt.legend()
#     plt.grid(True)
#
#     # Toon de plot
#     plt.show()
# else:
#     print("Geen geld per ronde data gevonden in het JSON-bestand.")

# poging 5
# import json
# import matplotlib.pyplot as plt
# import numpy as np
#
# # JSON-bestand inlezen
# with open('moreData.json') as file:
#     data = json.load(file)
#
# # Selecteer een paar willekeurige spellen om te plotten (bijv. 5 spellen)
# num_games_to_plot = 5
# selected_games = np.random.choice(data, num_games_to_plot, replace=False)
#
# # Plot het verloop van elk geselecteerd spel
# plt.figure(figsize=(12, 6))
#
# for i, game in enumerate(selected_games):
#     # Begin saldo bij 100
#     balance = 100
#     # Bereken de cumulatieve balans per ronde
#     balance_per_round = [balance + sum(game['moneyOnRound'][:round_index + 1]) for round_index in range(len(game['moneyOnRound']))]
#     plt.plot(balance_per_round, label=f'Spel {i + 1}')
#
# plt.xlabel('Ronde')
# plt.ylabel('Balans (€)')
# plt.title('Verloop van het saldo per spel over de rondes')
# plt.legend()
# plt.grid(True)
#
# # Toon de plot
# plt.show()
#

# poging 6
# import json
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Stel dat je JSON-bestand is opgeslagen als 'games.json'
# with open('moreData.json') as f:
#     data = json.load(f)
#
# # Initializeer variabelen
# total_rounds = max(len(game['moneyOnRound']) for game in data)  # Aantal ronden
# average_money = np.zeros(total_rounds)
#
# # Bereken het gemiddelde geld per ronde
# for game in data:
#     money = 100  # Begin met 100 geld
#     for i, money_change in enumerate(game['moneyOnRound']):
#         money += money_change
#         average_money[i] += money
#
# # Bereken het gemiddelde per ronde
# average_money /= len(data)
#
# # Plot de gegevens
# plt.figure(figsize=(10, 5))
# plt.plot(range(1, total_rounds + 1), average_money, label='Gemiddeld Geld', color='blue')
# plt.axhline(y=100, color='red', linestyle='--', label='Begin Geld (100)')
# plt.title('Gemiddeld Geld per Ronde')
# plt.xlabel('Ronde')
# plt.ylabel('Geld')
# plt.legend()
# plt.grid()
# plt.show()
#

# poging 7
# import json
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Stel dat je JSON-bestand is opgeslagen als 'games.json'
# with open('moreData.json') as f:
#     data = json.load(f)
#
# # Aantal ronden bepalen
# max_rounds = max(len(game['moneyOnRound']) for game in data)
#
# # Geldbalans per ronde bijhouden
# money_per_round = np.zeros((len(data), max_rounds))
#
# # Verwerk elke game
# for game_index, game in enumerate(data):
#     money = 100  # Begin met 100 geld
#     for round_index, money_change in enumerate(game['moneyOnRound']):
#         money += money_change
#         money_per_round[game_index, round_index] = money
#
# # Gemiddeld geld per ronde berekenen
# average_money = np.mean(money_per_round, axis=0)
#
# # Plot de gegevens
# plt.figure(figsize=(10, 5))
# plt.plot(range(1, max_rounds + 1), average_money, label='Gemiddeld Geld per Ronde', color='blue')
# plt.axhline(y=100, color='red', linestyle='--', label='Begin Geld (100)')
# plt.title('Geld per Ronde')
# plt.xlabel('Ronde')
# plt.ylabel('Geld')
# plt.legend()
# plt.grid()
# plt.show()
#


# poging 8
import json
import numpy as np
import matplotlib.pyplot as plt

# Laad de JSON-gegevens
with open('moreData.json') as file:
    data = json.load(file)

# Initialiseer variabelen om de totalen bij te houden
total_money_per_round = {}
total_games_per_round = {}

# Loop door de gegevens om totalen per ronde te berekenen
for game in data:
    for round_index, money in enumerate(game['moneyOnRound']):
        if round_index not in total_money_per_round:
            total_money_per_round[round_index] = 0
            total_games_per_round[round_index] = 0
            
        total_money_per_round[round_index] += money
        total_games_per_round[round_index] += 1

# Bereken het gemiddelde per ronde
average_money_per_round = {round_index: total_money_per_round[round_index] / total_games_per_round[round_index] 
                            for round_index in total_money_per_round}

# Bereid de gegevens voor op de plot
rounds = list(average_money_per_round.keys())
average_money = list(average_money_per_round.values())

# Plot de gemiddelde lijn
plt.figure(figsize=(10, 5))
plt.plot(rounds, average_money, label='Gemiddeld Geld per Ronde', color='blue')
plt.xlabel('Ronde')
plt.ylabel('Geld (in euro)')
plt.title('Gemiddeld Geld per Ronde')
plt.axhline(0, color='gray', linewidth=0.5, linestyle='--')  # Horizontale lijn bij 0
plt.grid()
plt.legend()
plt.show()


# import json
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Laad de JSON-gegevens
# with open('moreData.json') as file:
#     data = json.load(file)
#
# # Initialiseer variabelen om de totalen bij te houden
# total_money_per_round = {}
# total_games_per_round = {}
#
# # Loop door de gegevens om totalen per ronde te berekenen
# for game in data:
#     for round_index, money in enumerate(game['moneyOnRound']):
#         if round_index not in total_money_per_round:
#             total_money_per_round[round_index] = 0
#             total_games_per_round[round_index] = 0
#             
#         total_money_per_round[round_index] += money
#         total_games_per_round[round_index] += 1
#
# # Bereken het gemiddelde per ronde
# average_money_per_round = {round_index: total_money_per_round[round_index] / total_games_per_round[round_index] 
#                             for round_index in total_money_per_round}
#
# # Bereid de gegevens voor op de plot
# rounds = list(average_money_per_round.keys())
# average_money = list(average_money_per_round.values())
#
# # Maak de scatter plot
# plt.figure(figsize=(10, 5))
# plt.scatter(rounds, average_money, label='Gemiddeld Geld per Ronde', color='blue', marker='o')
# plt.xlabel('Ronde')
# plt.ylabel('Geld (in euro)')
# plt.title('Gemiddeld Geld per Ronde (Scatter Plot)')
# plt.axhline(0, color='gray', linewidth=0.5, linestyle='--')  # Horizontale lijn bij 0
# plt.grid()
# plt.legend()
# plt.show()
#

# poging 10
# import json
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Laad de JSON-gegevens
# with open('moreData.json') as file:
#     data = json.load(file)
#
# # Initialiseer lijsten om de gegevens voor de scatter plot te verzamelen
# rounds = []
# money_values = []
#
# # Loop door de gegevens om alle geldbedragen per ronde te verzamelen
# for game in data:
#     for round_index, money in enumerate(game['moneyOnRound']):
#         rounds.append(round_index)  # Voeg ronde-index toe
#         money_values.append(money)   # Voeg geldbedrag toe
#
# # Maak de scatter plot
# plt.figure(figsize=(10, 5))
# plt.scatter(rounds, money_values, label='Geldbedragen per Ronde', color='blue', marker='o')
# plt.xlabel('Ronde')
# plt.ylabel('Geld (in euro)')
# plt.title('Geldbedragen per Ronde (Scatter Plot)')
# plt.axhline(0, color='gray', linewidth=0.5, linestyle='--')  # Horizontale lijn bij 0
# plt.grid()
# plt.legend()
# plt.show()
#
