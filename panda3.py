# import json
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Load the data from the provided JSON file
# with open('moreData.json') as f:
#     data = json.load(f)
#
# # Prepare data for plots
# games_played = [entry["gamesPlayed"] for entry in data]
# money_per_round_all = [entry["moneyOnRound"] for entry in data]
#
# # 1. Histogram of Games Played
# plt.figure(figsize=(10, 6))
# plt.hist(games_played, bins=30, color='skyblue', edgecolor='black')
# plt.title("Distribution of Games Played Until Bankruptcy")
# plt.xlabel("Number of Rounds Played in a Game")
# plt.ylabel("Frequency")
# plt.grid(axis='y', alpha=0.75)

# import json
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.stats import poisson
#
# # Load the data from the JSON file
# with open('moreData.json') as f:
#     data = json.load(f)
#
# # Prepare the data for the histogram
# games_played = [entry["gamesPlayed"] for entry in data]
#
# # Calculate the mean number of games played (lambda for Poisson)
# lambda_poisson = np.mean(games_played)
#
# # Generate Poisson distribution values starting from 10 games
# x_values = np.arange(10, max(games_played) + 1)
# poisson_dist = poisson.pmf(x_values, lambda_poisson)
#
# # Scale the Poisson distribution to match the peak of the histogram
# hist, bin_edges = np.histogram(games_played, bins=np.arange(10, max(games_played) + 2))
# scaling_factor = hist.max() / poisson_dist.max()
# poisson_dist_scaled = poisson_dist * scaling_factor
#
# # Plot histogram of games played with x-axis starting from 10
# plt.figure(figsize=(10, 6))
# plt.hist(games_played, bins=np.arange(10, max(games_played) + 2), color='skyblue', edgecolor='black', alpha=0.6, label="Simulated Data")
# plt.plot(x_values, poisson_dist_scaled, color='red', linestyle='--', linewidth=2, label=f"Poisson Distribution\n(λ={lambda_poisson:.2f})")
# plt.xlim(10, max(games_played))
# plt.title("Distribution of Games Played Until Bankruptcy with Poisson Fit")
# plt.xlabel("Number of Rounds Played in a Game")
# plt.ylabel("Frequency")
# plt.legend()
# plt.grid(axis='y', alpha=0.75)
# plt.show()

# NICE ONE
# import json
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.stats import poisson
#
# # Load the data from the JSON file
# with open('moreData.json') as f:
#     data = json.load(f)
#
# # Prepare the data for the histogram
# games_played = [entry["gamesPlayed"] for entry in data]
#
# # Calculate the mean number of games played and reduce it slightly
# lambda_poisson = np.mean(games_played) * 0.9  # Adjust the 0.9 factor as needed
#
# # Generate shifted x-values and Poisson distribution values
# x_values = np.arange(10, max(games_played) + 1)
# shift = 10  # Adjust this value if the curve is still misaligned
# poisson_dist = poisson.pmf(x_values - shift, lambda_poisson)
#
# # Scale the Poisson distribution to match the peak of the histogram
# hist, bin_edges = np.histogram(games_played, bins=np.arange(10, max(games_played) + 2))
# scaling_factor = hist.max() / poisson_dist.max()
# poisson_dist_scaled = poisson_dist * scaling_factor
#
# # Find the peak frequency and corresponding bin center
# peak_frequency = hist.max()
# peak_index = np.argmax(hist)
# peak_bin_center = (bin_edges[peak_index] + bin_edges[peak_index + 1]) / 2
#
# # Plot histogram of games played with adjusted Poisson fit
# plt.figure(figsize=(10, 6))
# plt.hist(games_played, bins=np.arange(10, max(games_played) + 2), color='skyblue', edgecolor='black', alpha=0.6, label="Simulated Data")
# # plt.plot(x_values, poisson_dist_scaled, color='red', linestyle='--', linewidth=2, label=f"Adjusted Poisson Distribution\n(λ={lambda_poisson:.2f})")
#
# # Annotate the peak
# plt.annotate(f'Peak: {peak_index}', xy=(peak_bin_center, peak_frequency),
#              xytext=(peak_bin_center - 20, peak_frequency + 50),
#              arrowprops=dict(facecolor='black', arrowstyle="->"),
#              fontsize=12, color='black')
#
# plt.xlim(10, max(games_played))
# plt.title("Distribution of Games Played Until Bankruptcy with Adjusted Poisson Fit")
# plt.xlabel("Number of Rounds Played in a Game")
# plt.ylabel("Frequency")
# plt.legend()
# plt.grid(axis='y', alpha=0.75)
# plt.show()
#
# import json
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.stats import nbinom, lognorm
#
# # Load the data from the JSON file
# with open('moreData.json') as f:
#     data = json.load(f)
#
# # Prepare the data for the histogram
# games_played = [entry["gamesPlayed"] for entry in data]
#
# # Plot histogram of games played
# plt.figure(figsize=(10, 6))
# hist_values, bins, _ = plt.hist(games_played, bins=np.arange(10, max(games_played) + 2), 
#                                 color='skyblue', edgecolor='black', alpha=0.6, label="Simulated Data")
#
# # Calculate bin centers for plotting distributions
# bin_centers = (bins[:-1] + bins[1:]) / 2
#
# # Fit and plot Negative Binomial Distribution
# mean_games = np.mean(games_played)
# var_games = np.var(games_played)
# if var_games > mean_games:  # Check to ensure overdispersion
#     p = mean_games / var_games  # Parameter p of the negative binomial
#     r = mean_games**2 / (var_games - mean_games)  # Parameter r of the negative binomial
#
#     nbinom_dist = nbinom.pmf(bin_centers, r, p)
#     if nbinom_dist.max() > 0:  # Check if scaling is possible
#         nbinom_scaled = nbinom_dist * (hist_values.max() / nbinom_dist.max())
#         plt.plot(bin_centers, nbinom_scaled, color='green', linestyle='--', linewidth=2, label=f"Negative Binomial\n(r={r:.2f}, p={p:.2f})")
#     else:
#         print("Warning: Negative binomial distribution values are all zero.")
# else:
#     print("Warning: Data does not show overdispersion, skipping negative binomial fit.")
#
# # Fit and plot Log-normal Distribution
# shape, loc, scale = lognorm.fit(games_played, floc=0)  # Fit log-normal with location fixed at 0
# lognorm_dist = lognorm.pdf(bin_centers, shape, loc=loc, scale=scale)
# lognorm_scaled = lognorm_dist * (hist_values.max() / lognorm_dist.max())
# plt.plot(bin_centers, lognorm_scaled, color='purple', linestyle='--', linewidth=2, label=f"Log-normal\n(shape={shape:.2f})")
#
# # Annotate the peak frequency
# peak_frequency = hist_values.max()
# peak_index = np.argmax(hist_values)
# peak_bin_center = bin_centers[peak_index]
# plt.annotate(f'Peak: {peak_frequency}', xy=(peak_bin_center, peak_frequency),
#              xytext=(peak_bin_center + 20, peak_frequency + 50),
#              arrowprops=dict(facecolor='black', arrowstyle="->"),
#              fontsize=12, color='black')
#
# # Final plot adjustments
# plt.xlim(10, max(games_played))
# plt.title("Distribution of Games Played Until Bankruptcy with Various Fits")
# plt.xlabel("Number of Rounds Played in a Game")
# plt.ylabel("Frequency")
# plt.legend()
# plt.grid(axis='y', alpha=0.75)
# plt.show()

import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import lognorm

# Load the data from the JSON file
with open('evenMoreData.json') as f:
    data = json.load(f)

# Prepare the data for the histogram
games_played = [entry["gamesPlayed"] for entry in data]

# Plot histogram of games played
plt.figure(figsize=(10, 6))
hist_values, bins, _ = plt.hist(games_played, bins=np.arange(10, max(games_played) + 2), 
                                color='skyblue', edgecolor='black', alpha=0.6, label="Simulated Data")

# Calculate bin centers for plotting the log-normal distribution
bin_centers = (bins[:-1] + bins[1:]) / 2

# Fit and plot Log-normal Distribution
shape, loc, scale = lognorm.fit(games_played, floc=0)  # Fit log-normal with location fixed at 0
lognorm_dist = lognorm.pdf(bin_centers, shape, loc=loc, scale=scale)
lognorm_scaled = lognorm_dist * (hist_values.max() / lognorm_dist.max())
plt.plot(bin_centers, lognorm_scaled, color='purple', linestyle='--', linewidth=2, label=f"Log-normal\n(shape={shape:.2f})")

# Annotate the peak frequency
peak_frequency = hist_values.max()
peak_index = np.argmax(hist_values)
peak_bin_center = bin_centers[peak_index]
plt.annotate(f'Peak: {peak_index}', xy=(peak_bin_center, peak_frequency),
             xytext=(peak_bin_center + 20, peak_frequency + 50),
             arrowprops=dict(facecolor='black', arrowstyle="->"),
             fontsize=12, color='black')

# Final plot adjustments
plt.xlim(10, max(games_played))
plt.title("Distribution of Games Played Until Bankruptcy with Log-normal Fit")
plt.xlabel("Number of Rounds Played in a Game")
plt.ylabel("Frequency")
plt.legend()
plt.grid(axis='y', alpha=0.75)
plt.show()
