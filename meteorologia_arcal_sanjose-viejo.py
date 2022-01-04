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
sanjose = pd.read_csv('ARCAL_ISH/sanjose2.csv', delimiter=',') # sanjose2 es abrir y volver a cerrar en excel para que ponga bien los delimiters, si no mezcla ; y ,
sanjose = sanjose[(sanjose['date[yyyymmddHHMM]'] >= 201904031200)]
fechas = pd.read_csv('fechas.csv')
fechas['sanjose'] = pd.to_datetime(fechas['sanjose'], format='%d/%m/%Y')
# Reemplazo los valores que son nan
sanjose['wdir'] = sanjose['wdir'].where(sanjose['wdir'] < 999)
sanjose['clht[km]'] = sanjose['clht[km]'].where(sanjose['clht[km]'] < 99)
sanjose['dptp[C]'] = sanjose['dptp[C]'].where(sanjose['dptp[C]'] < 999)
sanjose['slvp[hPa]'] = sanjose['slvp[hPa]'].where(sanjose['slvp[hPa]'] < 9999)
sanjose['press[hPa]'] = sanjose['press[hPa]'].where(sanjose['press[hPa]'] < 9999)
sanjose['prcp[mm]'] = sanjose['prcp[mm]'].where(sanjose['prcp[mm]'] < 999)
sanjose['sky[octas]'] = sanjose['sky[octas]'].where(sanjose['sky[octas]'] > 99)
sanjose['skyOpaque[octas]'] = sanjose['skyOpaque[octas]'].where(sanjose['skyOpaque[octas]'] < 99)

# Parsing de fecha
datetime = pd.to_datetime(sanjose['date[yyyymmddHHMM]'], format='%Y%m%d%H%M')
sanjose['date'] = datetime
# Reordeno columnas-
cols = sanjose.columns.tolist()
cols = cols[-1:] + cols[:-1] # Mando la última columna (date) al principio
sanjose = sanjose[cols]
display(sanjose)
sanjose = sanjose.set_index('date')

display(sanjose)

# + tags=[]
sanjose = sanjose.groupby(level=0).sum()
display(sanjose)

sanjose24hs_mean = sanjose.resample('24H', offset='12h').mean() # Resampleo para tener promedios diarios

display(sanjose24hs_mean)
sanjose24hs_sum = sanjose.resample('24H', offset='12h').sum() # Resampleo para tener promedios diarios

sanjose_comb = pd.concat([sanjose24hs_mean[['wdir', 'wspd[m/s]', 'clht[km]', 'hzvs[km]', 'tmpd[C]',
                                          'slvp[hPa]', 'press[hPa]', 'sky[octas]', 'skyOpaque[octas]']],
                         sanjose24hs_sum[['prcp[mm]', 'prcpPeriod[hours]']]], axis=1)

display(sanjose_comb)
sanjose_comb.index = sanjose_comb.index.normalize()
sanjose_comb = (sanjose_comb.reindex(index = fechas['sanjose'].to_list()))
sanjose_comb.to_excel('sanjose_meteo.xlsx')

display(fechas['sanjose'])