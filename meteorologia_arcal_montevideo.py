# -*- coding: utf-8 -*-
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

# + tags=[]
montevideo = pd.read_csv('ARCAL_ISH/montevideo2.csv', delimiter=',') # montevideo2 es abrir y volver a cerrar en excel para que ponga bien los delimiters, si no mezcla ; y ,
montevideo = montevideo[(montevideo['date[yyyymmddHHMM]'] >= 201904031200)]
fechas = pd.read_csv('fechas.csv')
fechas['montevideo'] = pd.to_datetime(fechas['montevideo'], format='%d/%m/%Y')
# Reemplazo los valores que son nan
montevideo['wdir'] = montevideo['wdir'].where(montevideo['wdir'] < 999)
montevideo['clht[km]'] = montevideo['clht[km]'].where(montevideo['clht[km]'] < 99)
montevideo['dptp[C]'] = montevideo['dptp[C]'].where(montevideo['dptp[C]'] < 999)
montevideo['slvp[hPa]'] = montevideo['slvp[hPa]'].where(montevideo['slvp[hPa]'] < 9999)
montevideo['press[hPa]'] = montevideo['press[hPa]'].where(montevideo['press[hPa]'] < 9999)
montevideo['prcp[mm]'] = montevideo['prcp[mm]'].where(montevideo['prcp[mm]'] < 999)
montevideo['sky[octas]'] = montevideo['sky[octas]'].where(montevideo['sky[octas]'] > 99)
montevideo['skyOpaque[octas]'] = montevideo['skyOpaque[octas]'].where(montevideo['skyOpaque[octas]'] < 99)
montevideo['tmpd[C]'] = montevideo['tmpd[C]'].where(montevideo['tmpd[C]'] < 99)

# Calculo RH como rh=100*(EXP((17.625*d)/(243.04+d))/EXP((17.625*t)/(243.04+t)));
# donde d=dewpoint (dptp) y t=dry temp (tmpd), aprox de August-Roche-Magnus
d = montevideo['dptp[C]']
t = montevideo['tmpd[C]']
montevideo['RH[%]'] = 100 * (np.exp((17.625 * d)/(243.04 + d)) / np.exp((17.625 * t)/(243.04 + t)))
# 

#Promedio fechas que están dobles
montevideo = montevideo.groupby('date[yyyymmddHHMM]').mean().reset_index()



# Parsing de fecha
datetime = pd.to_datetime(montevideo['date[yyyymmddHHMM]'], format='%Y%m%d%H%M')
montevideo['date'] = datetime
# Reordeno columnas-
cols = montevideo.columns.tolist()
cols = cols[-1:] + cols[:-1] # Mando la última columna (date) al principio
montevideo = montevideo[cols]
display(montevideo)
montevideo = montevideo.set_index('date')
montevideo['RH[%]'].plot()

display(montevideo)
# -

plt.ylim([0,150])
montevideo['tmpd[C]'].plot(style='.')

# + tags=[]
montevideo = montevideo.groupby(level=0).sum()
display(montevideo)

montevideo24hs_mean = montevideo.resample('24H', offset='12h').mean() # Resampleo para tener promedios diarios

display(montevideo24hs_mean)
montevideo24hs_sum = montevideo.resample('24H', offset='12h').sum() # Resampleo para tener promedios diarios

montevideo_comb = pd.concat([montevideo24hs_mean[['wdir', 'wspd[m/s]', 'clht[km]', 'hzvs[km]', 'tmpd[C]',
                                          'slvp[hPa]', 'press[hPa]', 'sky[octas]', 'skyOpaque[octas]', 'RH[%]']],
                         montevideo24hs_sum[['prcp[mm]', 'prcpPeriod[hours]']]], axis=1)

display(montevideo_comb)
montevideo_comb.index = montevideo_comb.index.normalize()
montevideo_comb = (montevideo_comb.reindex(index = fechas['montevideo'].to_list()))
montevideo_comb.to_excel('montevideo_meteo2.xlsx')

#with pd.
display(fechas['montevideo'])
# -
montevideo_comb['RH[%]'].plot(style='.')

