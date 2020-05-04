import pandas as pd
from pandas import DataFrame
from pandas.plotting import register_matplotlib_converters
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
register_matplotlib_converters()

plt.style.use(['ggplot','dark_background','seaborn-darkgrid','fivethirtyeight'])

df_covid=DataFrame(pd.read_csv("China.csv",usecols=['dateRep','cases'],parse_dates=['dateRep']))
df_covid.sort_values('dateRep', inplace=True)
df_covid.set_index('dateRep',inplace=True)
fig, ax = plt.subplots(figsize=(15,7))
ax.xaxis.set_major_locator(mdates.WeekdayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
ax.bar(df_covid.index, df_covid['cases'])
plt.show()


print(df_covid)
