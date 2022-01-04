# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr
import datetime as dt

# + tags=[]
df = pd.read_csv('obs_2019_2020_cured.csv', skiprows=1, delimiter=r"\s+", parse_dates=True)
for i in range(len(df['datetime'])):
    fecha = df['datetime'][i]
    try:
        df['datetime'][i] = dt.datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        fecha = df['datetime'][i]
        fecha = fecha.replace('T24', 'T23')
        fecha  = dt.datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S")
        df['datetime'][i] = fecha + dt.timedelta(hours=1)

df.index = pd.to_datetime(df['datetime'])
display(df)


# +
df['ventilation'] = df['wsp'] * df['PBLH']

plt.plot(df['ventilation'])
print(df['ventilation'].idxmax())
print(df['PBLH'])

# + tags=[]
df_daily_sum = df.resample(rule="24H", offset="12H").sum()

#display(df_daily_sum)



# Mean resample with a max of 6 NaN in PBLH
# Add a column with 1 if data is not NaN, 0 if data is NaN
df['data coverage'] = (~np.isnan(df['PBLH'])).astype(int)
df_daily_average = df.resample(rule="24H", offset="12H").mean()
# Specify a threshold on data coverage of 80% 
threshold = 0.74
#df_daily_average.loc[df['data coverage'] < threshold, 'values'] = np.NaN
#print(df_daily_average.head)
plt.plot(df_daily_average['data coverage'])
plt.show()
#display(df_daily_average)

plt.figure(figsize=(15,6))
plt.plot(df_daily_average['ventilation'])
plt.title('Vent_coef')
plt.show()
plt.figure(figsize=(15,6))
plt.title('PBLH')
plt.plot(df_daily_average['PBLH'])
plt.show()

print(df_daily_average['PBLH'].idxmin())
# +
for i in df.keys():
    print(i, max(df[i]), min(df[i]))

#plt.plot(df['ventilation'])

plt.plot(df['PBLH']*1)

# + tags=[]
d = {'Precip': df_daily_sum['precip_rate'], 'HR': df_daily_average['RH'], 'T': df_daily_average['T'], 'ventil_coef': df_daily_average['wsp'] * df_daily_average}
df_out = pd.DataFrame()



