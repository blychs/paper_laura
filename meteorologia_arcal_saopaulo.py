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

# + tags=[]
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr

saopaulo = pd.read_csv('ARCAL_ISH/saopaulo2.csv', delimiter=',') # saopaulo2 es abrir y volver a cerrar en excel para que ponga bien los delimiters, si no mezcla ; y ,
saopaulo = saopaulo[(saopaulo['date[yyyymmddHHMM]'] >= 201904031200)]
fechas = pd.read_csv('fechas.csv')
fechas['saopaulo'] = pd.to_datetime(fechas['saopaulo'], format='%d/%m/%Y')
# Reemplazo los valores que son nan
saopaulo['wdir'] = saopaulo['wdir'].where(saopaulo['wdir'] < 999)
saopaulo['wspd[m/s]'] = saopaulo['wspd[m/s]'].where(saopaulo['wspd[m/s]'] < 999)
saopaulo['clht[km]'] = saopaulo['clht[km]'].where(saopaulo['clht[km]'] < 99)
saopaulo['dptp[C]'] = saopaulo['dptp[C]'].where(saopaulo['dptp[C]'] < 999)
saopaulo['slvp[hPa]'] = saopaulo['slvp[hPa]'].where(saopaulo['slvp[hPa]'] < 9999)
saopaulo['press[hPa]'] = saopaulo['press[hPa]'].where(saopaulo['press[hPa]'] < 9999)
saopaulo['prcp[mm]'] = saopaulo['prcp[mm]'].where(saopaulo['prcp[mm]'] < 999)
saopaulo['sky[octas]'] = saopaulo['sky[octas]'].where(saopaulo['sky[octas]'] > 99)
saopaulo['skyOpaque[octas]'] = saopaulo['skyOpaque[octas]'].where(saopaulo['skyOpaque[octas]'] < 99)
saopaulo['tmpd[C]'] = saopaulo['tmpd[C]'].where(saopaulo['tmpd[C]'] < 99)

# Calculo RH como rh=100*(EXP((17.625*d)/(243.04+d))/EXP((17.625*t)/(243.04+t)));
# donde d=dewpoint (dptp) y t=dry temp (tmpd), aprox de August-Roche-Magnus
d = saopaulo['dptp[C]']
t = saopaulo['tmpd[C]']
saopaulo['RH[%]'] = 100 * (np.exp((17.625 * d)/(243.04 + d)) / np.exp((17.625 * t)/(243.04 + t)))
# 

#Promedio fechas que están dobles
saopaulo = saopaulo.groupby('date[yyyymmddHHMM]').mean().reset_index()



# Parsing de fecha
datetime = pd.to_datetime(saopaulo['date[yyyymmddHHMM]'], format='%Y%m%d%H%M')
saopaulo['date'] = datetime
# Reordeno columnas-
cols = saopaulo.columns.tolist()
cols = cols[-1:] + cols[:-1] # Mando la última columna (date) al principio
saopaulo = saopaulo[cols]
#display(saopaulo)
saopaulo = saopaulo.set_index('date')

#display(saopaulo)

saopaulo = saopaulo.groupby(level=0).sum()
#display(saopaulo)

saopaulo24hs_mean = saopaulo.resample('24H', offset='12h').mean() # Resampleo para tener promedios diarios

#display(saopaulo24hs_mean)
saopaulo24hs_sum = saopaulo.resample('24H', offset='12h').sum() # Resampleo para tener promedios diarios

saopaulo_comb = pd.concat([saopaulo24hs_mean[['wdir', 'wspd[m/s]', 'clht[km]', 'hzvs[km]', 'tmpd[C]',
                                          'slvp[hPa]', 'press[hPa]', 'sky[octas]', 'skyOpaque[octas]', 'RH[%]']],
                         saopaulo24hs_sum[['prcp[mm]', 'prcpPeriod[hours]']]], axis=1)

#display(saopaulo_comb)
saopaulo_comb.index = saopaulo_comb.index.normalize()
saopaulo_comb = (saopaulo_comb.reindex(index = fechas['saopaulo'].to_list()))
saopaulo_comb.to_excel('saopaulo_meteo2.xlsx')

#with pd.
#display(fechas['saopaulo'])