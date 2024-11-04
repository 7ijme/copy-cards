import pandas as pd
import json
import matplotlib.pyplot as plt

open_file = open('moreData.json')
data = json.load(open_file)
open_file.close()

df = pd.DataFrame(data)

ax = df['gamesPlayed'].value_counts().sort_index().plot(kind='bar')
tick_labels = ax.get_xticks()
ax.set_xticks(tick_labels[::5])  # Show every 5th tick

# Rotate x-axis labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
ax.set_xlabel('Games Played')

plt.tight_layout()

# Save the figure
ax.get_figure().savefig('more_games_played.png')
plt.show()  # Optional, to display the plot

