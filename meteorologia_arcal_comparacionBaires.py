# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + tags=[]
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr

ezeiza = pd.read_csv('ARCAL_ISH/ezeiza2.csv', delimiter=',') # ezeiza2 es abrir y volver a cerrar en excel para que ponga bien los delimiters, si no mezcla ; y ,
ezeiza = ezeiza[(ezeiza['date[yyyymmddHHMM]'] >= 201904031200)]
ezeiza = ezeiza[(ezeiza['date[yyyymmddHHMM]'] <= 202004011200)]
fechas = pd.read_csv('fechas.csv')
fechas['buenos_aires'] = pd.to_datetime(fechas['buenos_aires'], format='%d/%m/%Y')
# Reemplazo los valores que son nan
ezeiza['wdir'] = ezeiza['wdir'].where(ezeiza['wdir'] < 999)
ezeiza['wspd[m/s]'] = ezeiza['wspd[m/s]'].where(ezeiza['wspd[m/s]'] < 999)
ezeiza['clht[km]'] = ezeiza['clht[km]'].where(ezeiza['clht[km]'] < 99)
ezeiza['dptp[C]'] = ezeiza['dptp[C]'].where(ezeiza['dptp[C]'] < 999)
ezeiza['slvp[hPa]'] = ezeiza['slvp[hPa]'].where(ezeiza['slvp[hPa]'] < 9999)
ezeiza['press[hPa]'] = ezeiza['press[hPa]'].where(ezeiza['press[hPa]'] < 9999)
ezeiza['prcp[mm]'] = ezeiza['prcp[mm]'].where(ezeiza['prcp[mm]'] < 999)
ezeiza['sky[octas]'] = ezeiza['sky[octas]'].where(ezeiza['sky[octas]'] > 99)
ezeiza['skyOpaque[octas]'] = ezeiza['skyOpaque[octas]'].where(ezeiza['skyOpaque[octas]'] < 99)
ezeiza['tmpd[C]'] = ezeiza['tmpd[C]'].where(ezeiza['tmpd[C]'] < 99)

# Calculo RH como rh=100*(EXP((17.625*d)/(243.04+d))/EXP((17.625*t)/(243.04+t)));
# donde d=dewpoint (dptp) y t=dry temp (tmpd), aprox de August-Roche-Magnus
d = ezeiza['dptp[C]']
t = ezeiza['tmpd[C]']
ezeiza['RH[%]'] = 100 * (np.exp((17.625 * d)/(243.04 + d)) / np.exp((17.625 * t)/(243.04 + t)))
# 

#Promedio fechas que están dobles

ezeiza = ezeiza.groupby('date[yyyymmddHHMM]').mean().reset_index()



# Parsing de fecha
datetime = pd.to_datetime(ezeiza['date[yyyymmddHHMM]'], format='%Y%m%d%H%M')
ezeiza['date'] = datetime
# Reordeno columnas-
cols = ezeiza.columns.tolist()
cols = cols[-1:] + cols[:-1] # Mando la última columna (date) al principio
ezeiza = ezeiza[cols]
#display(ezeiza)
ezeiza = ezeiza.set_index('date')

#display(ezeiza)

ezeiza = ezeiza.groupby(level=0).sum()
display(ezeiza)
#
#ezeiza24hs_mean = ezeiza.resample('24H', offset='12h').mean() # Resampleo para tener promedios diarios
#
##display(ezeiza24hs_mean)
#ezeiza24hs_sum = ezeiza.resample('24H', offset='12h').sum() # Resampleo para tener promedios diarios
#
#ezeiza_comb = pd.concat([ezeiza24hs_mean[['wdir', 'wspd[m/s]', 'clht[km]', 'hzvs[km]', 'tmpd[C]',
#                                          'slvp[hPa]', 'press[hPa]', 'sky[octas]', 'skyOpaque[octas]', 'RH[%]']],
#                         ezeiza24hs_sum[['prcp[mm]', 'prcpPeriod[hours]']]], axis=1)
#
##display(ezeiza_comb)
#ezeiza_comb.index = ezeiza_comb.index.normalize()
#ezeiza_comb = (ezeiza_comb.reindex(index = fechas['ezeiza'].to_list()))
#ezeiza_comb.to_excel('ezeiza_meteo2.xlsx')
#
##with pd.
#display(fechas['ezeiza'])

# + tags=[]
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr

obsbaires = pd.read_csv('ARCAL_ISH/obsbaires2.csv', delimiter=';') # obsbaires2 es abrir y volver a cerrar en excel para que ponga bien los delimiters, si no mezcla ; y ,
obsbaires = obsbaires[(obsbaires['date[yyyymmddHHMM]'] >= 201904031200)]
obsbaires = obsbaires[(obsbaires['date[yyyymmddHHMM]'] <= 202004011200)]
fechas = pd.read_csv('fechas.csv')
fechas['buenos_aires'] = pd.to_datetime(fechas['buenos_aires'], format='%d/%m/%Y')
# Reemplazo los valores que son nan
obsbaires['wdir'] = obsbaires['wdir'].where(obsbaires['wdir'] < 999)
obsbaires['wspd[m/s]'] = obsbaires['wspd[m/s]'].where(obsbaires['wspd[m/s]'] < 999)
obsbaires['clht[km]'] = obsbaires['clht[km]'].where(obsbaires['clht[km]'] < 99)
obsbaires['dptp[C]'] = obsbaires['dptp[C]'].where(obsbaires['dptp[C]'] < 999)
obsbaires['slvp[hPa]'] = obsbaires['slvp[hPa]'].where(obsbaires['slvp[hPa]'] < 9999)
obsbaires['press[hPa]'] = obsbaires['press[hPa]'].where(obsbaires['press[hPa]'] < 9999)
obsbaires['prcp[mm]'] = obsbaires['prcp[mm]'].where(obsbaires['prcp[mm]'] < 999)
obsbaires['sky[octas]'] = obsbaires['sky[octas]'].where(obsbaires['sky[octas]'] > 99)
obsbaires['skyOpaque[octas]'] = obsbaires['skyOpaque[octas]'].where(obsbaires['skyOpaque[octas]'] < 99)
obsbaires['tmpd[C]'] = obsbaires['tmpd[C]'].where(obsbaires['tmpd[C]'] < 99)

# Calculo RH como rh=100*(EXP((17.625*d)/(243.04+d))/EXP((17.625*t)/(243.04+t)));
# donde d=dewpoint (dptp) y t=dry temp (tmpd), aprox de August-Roche-Magnus
d = obsbaires['dptp[C]']
t = obsbaires['tmpd[C]']
obsbaires['RH[%]'] = 100 * (np.exp((17.625 * d)/(243.04 + d)) / np.exp((17.625 * t)/(243.04 + t)))
# 

#Promedio fechas que están dobles
obsbaires = obsbaires.groupby('date[yyyymmddHHMM]').mean().reset_index()



# Parsing de fecha
datetime = pd.to_datetime(obsbaires['date[yyyymmddHHMM]'], format='%Y%m%d%H%M')
obsbaires['date'] = datetime
# Reordeno columnas-
cols = obsbaires.columns.tolist()
cols = cols[-1:] + cols[:-1] # Mando la última columna (date) al principio
obsbaires = obsbaires[cols]
#display(obsbaires)
obsbaires = obsbaires.set_index('date')

#display(obsbaires)

obsbaires = obsbaires.groupby(level=0).sum()
display(obsbaires)
#
#obsbaires24hs_mean = obsbaires.resample('24H', offset='12h').mean() # Resampleo para tener promedios diarios
#
##display(obsbaires24hs_mean)
#obsbaires24hs_sum = obsbaires.resample('24H', offset='12h').sum() # Resampleo para tener promedios diarios
#
#obsbaires_comb = pd.concat([obsbaires24hs_mean[['wdir', 'wspd[m/s]', 'clht[km]', 'hzvs[km]', 'tmpd[C]',
#                                          'slvp[hPa]', 'press[hPa]', 'sky[octas]', 'skyOpaque[octas]', 'RH[%]']],
#                         obsbaires24hs_sum[['prcp[mm]', 'prcpPeriod[hours]']]], axis=1)
#
##display(obsbaires_comb)
#obsbaires_comb.index = obsbaires_comb.index.normalize()
#obsbaires_comb = (obsbaires_comb.reindex(index = fechas['obsbaires'].to_list()))
#obsbaires_comb.to_excel('obsbaires_meteo2.xlsx')
#
##with pd.
#display(fechas['obsbaires'])

# +
from scipy import stats

interseccion = ezeiza.index.intersection(obsbaires.index)
comp_ezeiza = ezeiza[ezeiza.index.isin(interseccion)]
comp_obs = obsbaires[obsbaires.index.isin(interseccion)]
slope, intercep, r_value, p_value, std_error = stats.linregress(comp_ezeiza['RH[%]'], comp_obs['RH[%]'])
plt.plot(comp_ezeiza['RH[%]'], comp_obs['RH[%]'], '.')
plt.xlabel('RH Ezeiza')
plt.ylabel('RH Observatorio')
plt.plot([0, 100], [0,100], 'k-', label='y=x')
plt.plot(comp_ezeiza['RH[%]'], slope * comp_ezeiza['RH[%]'] + intercep,
         label=f'{slope.round(3)} * ezeiza + {intercep.round(3)}\nR^2 = {(r_value**2).round(3)}')
plt.legend()
plt.show()
print(f'R**2 = {r_value**2}\np-value = {p_value}')

salida = pd.DataFrame()
salida['ezeiza'] = comp_ezeiza['RH[%]']
salida['obsbaires'] = comp_obs['RH[%]']
display(salida)
salida.to_excel('RH_eze_obs.xlsx')
# -


