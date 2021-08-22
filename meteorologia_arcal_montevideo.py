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
montevideo = pd.read_csv('ARCAL_ISH/montevideo.csv', delimiter=';')
montevideo = montevideo[(montevideo['date[yyyymmddHHMM]'] >= 201904031200) & (montevideo['date[yyyymmddHHMM]'] <= 202003090000)]
fechas = pd.read_csv('fechas.csv')
fechas['montevideo'] = pd.to_datetime(fechas['montevideo'], format='%d/%m/%Y')
display(fechas)
display(montevideo)

# Reemplazo los valores que son nan
montevideo['wdir'] = montevideo['wdir'].where(montevideo['wdir'] < 999)
montevideo['clht[km]'] = montevideo['clht[km]'].where(montevideo['clht[km]'] < 99)
montevideo['dptp[C]'] = montevideo['dptp[C]'].where(montevideo['dptp[C]'] < 999)
montevideo['slvp[hPa]'] = montevideo['slvp[hPa]'].where(montevideo['slvp[hPa]'] < 9999)
montevideo['press[hPa]'] = montevideo['press[hPa]'].where(montevideo['press[hPa]'] < 9999)
montevideo['prcp[mm]'] = montevideo['prcp[mm]'].where(montevideo['prcp[mm]'] < 999)
montevideo['sky[octas]'] = montevideo['sky[octas]'].where(montevideo['sky[octas]'] > 99)
montevideo['skyOpaque[octas]'] = montevideo['skyOpaque[octas]'].where(montevideo['skyOpaque[octas]'] < 99)

# Parsing de fecha
datetime = pd.to_datetime(montevideo['date[yyyymmddHHMM]'], format='%Y%m%d%H%M')
montevideo['date'] = datetime
# Reordeno columnas-
cols = montevideo.columns.tolist()
cols = cols[-1:] + cols[:-1] # Mando la última columna (date) al principio
montevideo = montevideo[cols]

display(montevideo)

# + tags=[]
montevideo24hs_mean = montevideo.set_index('date')
montevideo24hs_sum = montevideo.set_index('date')

montevideo24hs_mean = montevideo24hs_mean.resample('24H', offset='12h').mean() # Resampleo para tener promedios diarios


montevideo24hs_sum = montevideo24hs_sum.resample('24H', offset='12h').sum() # Resampleo para tener promedios diarios


montevideo_comb = pd.concat([montevideo24hs_mean[['wdir', 'wspd[m/s]', 'clht[km]', 'hzvs[km]', 'tmpd[C]',
                                          'slvp[hPa]', 'press[hPa]', 'sky[octas]', 'skyOpaque[octas]']],
                         montevideo24hs_sum[['prcp[mm]', 'prcpPeriod[hours]']]], axis=1)

display(montevideo_comb.loc['2019-07-11 12:00:00'])
montevideo_comb.index = montevideo_comb.index.normalize()
montevideo_comb = (montevideo_comb.reindex(index = fechas['montevideo'].to_list()))
montevideo_comb.to_excel('montevideo_meteo.xlsx')

display(fechas['montevideo'])
