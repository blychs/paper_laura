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

quito = pd.read_csv('ARCAL_ISH/quito2.csv', delimiter=',') # quito2 es abrir y volver a cerrar en excel para que ponga bien los delimiters, si no mezcla ; y ,
quito = quito[(quito['date[yyyymmddHHMM]'] >= 201904031200)]
fechas = pd.read_csv('fechas.csv')
fechas['quito'] = pd.to_datetime(fechas['quito'], format='%d/%m/%Y')

display(quito)
# Reemplazo los valores que son nan
quito['wdir'] = quito['wdir'].where(quito['wdir'] < 999)
quito['clht[km]'] = quito['clht[km]'].where(quito['clht[km]'] < 99)
quito['dptp[C]'] = quito['dptp[C]'].where(quito['dptp[C]'] < 999)
quito['slvp[hPa]'] = quito['slvp[hPa]'].where(quito['slvp[hPa]'] < 9999)
quito['press[hPa]'] = quito['press[hPa]'].where(quito['press[hPa]'] < 9999)
quito['prcp[mm]'] = quito['prcp[mm]'].where(quito['prcp[mm]'] < 999)
quito['sky[octas]'] = quito['sky[octas]'].where(quito['sky[octas]'] > 99)
quito['skyOpaque[octas]'] = quito['skyOpaque[octas]'].where(quito['skyOpaque[octas]'] < 99)

# Parsing de fecha
datetime = pd.to_datetime(quito['date[yyyymmddHHMM]'], format='%Y%m%d%H%M')
quito['date'] = datetime

# Reordeno columnas y seteo el índice (el reordenamiento en realidad es innecesario)

#cols = quito.columns.tolist()
#cols = cols[-1:] + cols[:-1] # Mando la última columna (date) al principio
#quito = quito[cols]
#display(quito)
quito = quito.set_index('date')

quito = quito.groupby(level=-1).sum()

quito24hs_mean = quito.resample('24H', offset='12h').mean() # Resampleo para tener promedios diarios

quito24hs_sum = quito.resample('24H', offset='12h').sum() # Resampleo para tener promedios diarios

quito_comb = pd.concat([quito24hs_mean[['wdir', 'wspd[m/s]', 'clht[km]', 'hzvs[km]', 'tmpd[C]',
                                          'slvp[hPa]', 'press[hPa]', 'sky[octas]', 'skyOpaque[octas]']],
                         quito24hs_sum[['prcp[mm]', 'prcpPeriod[hours]']]], axis=1)

quito_comb.index = quito_comb.index.normalize()
quito_comb = (quito_comb.reindex(index = fechas['quito'].to_list()))
quito_comb.to_excel('quito_meteo.xlsx')

#display(fechas['quito'])
