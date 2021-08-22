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

# +
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr

medellin = pd.read_csv('ARCAL_ISH/medellin2.csv', delimiter=',') # medellin2 es abrir y volver a cerrar en excel para que ponga bien los delimiters, si no mezcla ; y ,
medellin = medellin[(medellin['date[yyyymmddHHMM]'] >= 201904031200)]
fechas = pd.read_csv('fechas.csv')
fechas['medellin'] = pd.to_datetime(fechas['medellin'], format='%d/%m/%Y')

display(medellin)
# Reemplazo los valores que son nan
medellin['wdir'] = medellin['wdir'].where(medellin['wdir'] < 999)
medellin['clht[km]'] = medellin['clht[km]'].where(medellin['clht[km]'] < 99)
medellin['dptp[C]'] = medellin['dptp[C]'].where(medellin['dptp[C]'] < 999)
medellin['slvp[hPa]'] = medellin['slvp[hPa]'].where(medellin['slvp[hPa]'] < 9999)
medellin['press[hPa]'] = medellin['press[hPa]'].where(medellin['press[hPa]'] < 9999)
medellin['prcp[mm]'] = medellin['prcp[mm]'].where(medellin['prcp[mm]'] < 999)
medellin['sky[octas]'] = medellin['sky[octas]'].where(medellin['sky[octas]'] > 99)
medellin['skyOpaque[octas]'] = medellin['skyOpaque[octas]'].where(medellin['skyOpaque[octas]'] < 99)

# Parsing de fecha
datetime = pd.to_datetime(medellin['date[yyyymmddHHMM]'], format='%Y%m%d%H%M')
medellin['date'] = datetime

# Reordeno columnas y seteo el índice (el reordenamiento en realidad es innecesario)

#cols = medellin.columns.tolist()
#cols = cols[-1:] + cols[:-1] # Mando la última columna (date) al principio
#medellin = medellin[cols]
#display(medellin)
medellin = medellin.set_index('date')

medellin = medellin.groupby(level=-1).sum()

medellin24hs_mean = medellin.resample('24H', offset='12h').mean() # Resampleo para tener promedios diarios

medellin24hs_sum = medellin.resample('24H', offset='12h').sum() # Resampleo para tener promedios diarios

medellin_comb = pd.concat([medellin24hs_mean[['wdir', 'wspd[m/s]', 'clht[km]', 'hzvs[km]', 'tmpd[C]',
                                          'slvp[hPa]', 'press[hPa]', 'sky[octas]', 'skyOpaque[octas]']],
                         medellin24hs_sum[['prcp[mm]', 'prcpPeriod[hours]']]], axis=1)

medellin_comb.index = medellin_comb.index.normalize()
medellin_comb = (medellin_comb.reindex(index = fechas['medellin'].to_list()))
medellin_comb.to_excel('medellin_meteo.xlsx')

#display(fechas['medellin'])
