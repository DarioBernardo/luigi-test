import os

import pandas as pd
import matplotlib.pyplot as plt
from settings import DATA_FOLDER


# Read the data

df_london = pd.read_csv(os.path.join(DATA_FOLDER, "london_temperature.csv"), sep=',', parse_dates=[0], encoding='utf-8')
# Set the date column as index (WAY 1)
df_london = df_london.set_index('date')
df_london.index.name=None
df_london.index = df_london.index.date
df_london.columns = ['max_london','min_london']

# Read the data and set the index to date column (WAY 2)
df_rome = pd.read_csv(os.path.join(DATA_FOLDER, "rome_temperature.csv"), sep=',', parse_dates=[0], index_col=0, encoding='utf-8')
df_rome.index.name=None
df_rome.index = df_rome.index.date
df_rome.columns = ['max_rome','min_rome']


df_terme = pd.read_csv(os.path.join(DATA_FOLDER, "terme_temperature.csv"), sep=',', parse_dates=[0], index_col=0, encoding='utf-8')
df_terme.index.name=None
df_terme.columns = ['max_terme','min_terme']

df_stockholm = pd.read_csv(os.path.join(DATA_FOLDER, "stockholm_temperature.csv"), sep=',', parse_dates=[0], index_col=0, encoding='utf-8')
df_stockholm.index.name=None
df_stockholm.columns = ['max_stockholm','min_stockholm']


#print(df_london.head())

#df_new = pd.concat([df_rome['max_rome'], df_london['max_london'], df_stockholm['max_stockholm']], axis=1)
#df_new.plot()



df_london['max_london'].plot()
df_rome['max_rome'].plot()
df_terme['max_terme'].plot()
df_stockholm['max_stockholm'].plot()


plt.legend(loc='best')
plt.show()


