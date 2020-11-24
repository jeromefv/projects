from NBA_19_20_PF_PA_functions import smart_bin

import pandas as pd

# %matplotlib inline
import matplotlib.pyplot as plt

nba_pf = pd.read_csv("NBA_2020_pts_for.csv")
nba_pf_columns = nba_pf.columns.values
pts_for = nba_pf_columns[-1]
NBA_PTS_FOR = nba_pf[pts_for]
nba_pf_bins = smart_bin(NBA_PTS_FOR, 8)

nba_pa = pd.read_csv("NBA_2020_pts_against.csv")
nba_pa_columns = nba_pa.columns.values
pts_against = nba_pa_columns[-1]
NBA_PTS_AGAINST = nba_pa[pts_against]
nba_pa_bins = smart_bin(NBA_PTS_AGAINST, 8)

figure = plt.figure(figsize = [12, 18])
figure.suptitle("NBA 19/20 Season Average Scores", size = 24)

ax1 = figure.add_subplot(2,1,1)
ax1.hist(NBA_PTS_FOR, bins = nba_pf_bins, color = "blue", edgecolor = "black", label = "PTS FOR")
ax1.legend(fontsize = "large")
ax1.set_xlabel("Average Points", size = 18)
ax1.set_ylabel("Number of Teams", size = 18)

ax2 = figure.add_subplot(2,1,2)
ax2.hist(NBA_PTS_AGAINST, bins = nba_pa_bins, color = "red", edgecolor = "black", label = "PTS AGAINST")
ax2.set_xlabel("Average Points", size = 18)
ax2.set_ylabel("Number of Teams", size = 18)
ax2.legend(fontsize= "large")

plt.show()
# plt.savefig("nba_19_20_seasonpts.png")