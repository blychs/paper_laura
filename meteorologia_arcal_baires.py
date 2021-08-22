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

# +
baires = pd.read_csv('ARCAL_ISH/obsbaires.csv', delimiter=';')
baires = baires[(baires['date[yyyymmddHHMM]'] >= 201904031200) & (baires['date[yyyymmddHHMM]'] <= 202003090000)]
fechas = pd.read_csv('fechas')
fechas = pd.to_datetime(fechas['buenos_aires'], format='%d/%m/%Y')
display(fechas)
display(baires)

# Reemplazo los valores que son nan
baires['wdir'] = baires['wdir'].where(baires['wdir'] < 999)
baires['clht[km]'] = baires['clht[km]'].where(baires['clht[km]'] < 99)
baires['dptp[C]'] = baires['dptp[C]'].where(baires['dptp[C]'] < 999)
baires['slvp[hPa]'] = baires['slvp[hPa]'].where(baires['slvp[hPa]'] < 9999)
baires['press[hPa]'] = baires['press[hPa]'].where(baires['press[hPa]'] < 9999)
baires['prcp[mm]'] = baires['prcp[mm]'].where(baires['prcp[mm]'] < 999)
baires['sky[octas]'] = baires['sky[octas]'].where(baires['sky[octas]'] > 99)
baires['skyOpaque[octas]'] = baires['skyOpaque[octas]'].where(baires['skyOpaque[octas]'] < 99)

# Parsing de fecha
datetime = pd.to_datetime(baires['date[yyyymmddHHMM]'], format='%Y%m%d%H%M')
baires['date'] = datetime
# Reordeno columnas-
cols = baires.columns.tolist()
cols = cols[-1:] + cols[:-1] # Mando la última columna (date) al principio
baires = baires[cols]

display(baires)

# +
baires24hs_mean = baires.set_index('date')
baires24hs_sum = baires.set_index('date')

baires24hs_mean = baires24hs_mean.resample('24H', offset='12h').mean() # Resampleo para tener promedios diarios


baires24hs_sum = baires24hs_sum.resample('24H', offset='12h').sum() # Resampleo para tener promedios diarios


baires_comb = pd.concat([baires24hs_mean[['wdir', 'wspd[m/s]', 'clht[km]', 'hzvs[km]', 'tmpd[C]',
                                          'slvp[hPa]', 'press[hPa]', 'sky[octas]', 'skyOpaque[octas]']],
                         baires24hs_sum[['prcp[mm]', 'prcpPeriod[hours]']]], axis=1)

baires_comb.insert(0, 'ID', range(1, 1+len(baires_comb)))
display(baires_comb.loc['2020-01-21 12:00:00'])
baires_comb.iloc[::3, :]
display(baires_comb)
baires_comb.to_excel('baires_meteo.xlsx')

baires_comb.index[1]
