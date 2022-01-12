# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:light,ipynb
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
fechas = pd.read_csv('fechas.csv')
fechas['ezeiza'] = pd.to_datetime(fechas['buenos_aires'], format='%d/%m/%Y')
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
#display(ezeiza)

ezeiza24hs_mean = ezeiza.resample('24H', offset='12h').mean() # Resampleo para tener promedios diarios

#display(ezeiza24hs_mean)
ezeiza24hs_sum = ezeiza.resample('24H', offset='12h').sum() # Resampleo para tener promedios diarios

ezeiza_comb = pd.concat([ezeiza24hs_mean[['wdir', 'wspd[m/s]', 'clht[km]', 'hzvs[km]', 'tmpd[C]',
                                          'slvp[hPa]', 'press[hPa]', 'sky[octas]', 'skyOpaque[octas]', 'RH[%]']],
                         ezeiza24hs_sum[['prcp[mm]', 'prcpPeriod[hours]']]], axis=1)

#display(ezeiza_comb)
ezeiza_comb.index = ezeiza_comb.index.normalize()
ezeiza_comb = (ezeiza_comb.reindex(index = fechas['ezeiza'].to_list()))
ezeiza_comb.to_excel('ezeiza_meteo2.xlsx')

#with pd.
#display(fechas['ezeiza'])
