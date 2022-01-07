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
from scipy import stats

# + tags=[] jupyter={"source_hidden": true}
resultados = pd.DataFrame()

uruguay = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Uruguay')
j = 'RH[%]'
i ='PM 2.5 (µg/Nm3)'
mask = ~np.isnan(uruguay[j]) & ~np.isnan(uruguay[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(uruguay[j][mask] / 30 * 100, uruguay[i][mask])
print(f'Montevideo \t {j} vs (PM2.5 / 30 * 100) \t pendiente = {round(slope, 4)} \t ordenada = {round(intercept,4)} \t R = {round(r_value ** 2,4)}')

san_jose = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Costa Rica')
j = 'RH[%]'
i ='PM2,5'
mask = ~np.isnan(san_jose[j]) & ~np.isnan(san_jose[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(san_jose[j][mask] / 30 * 100, san_jose[i][mask])
print(f'San José \t {j} vs (PM2.5 / 30 * 100) \t pendiente = {round(slope, 4)} \t ordenada = {round(intercept,4)} \t R = {round(r_value ** 2,4)}')

quito = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Ecuador')
j = 'RH[%]'
i ='PM 2.5 (µg/Nm3)'
mask = ~np.isnan(quito[j]) & ~np.isnan(quito[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(quito[j][mask] / 30 * 100, quito[i][mask])
print(f'Quito \t\t {j} vs (PM2.5 / 30 * 100) \t pendiente = {round(slope, 4)} \t ordenada = {round(intercept,4)} \t R = {round(r_value ** 2,4)}')

ezeiza = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Argentina')
j = 'RH[%]'
i ='PM 2.5 (µg/Nm3)'
mask = ~np.isnan(ezeiza[j]) & ~np.isnan(ezeiza[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(ezeiza[j][mask] / 30 * 100, ezeiza[i][mask])
print(f'Buenos Aires \t {j} vs (PM2.5 / 30 * 100) \t pendiente = {round(slope, 4)} \t ordenada = {round(intercept,4)} \t R = {round(r_value ** 2,4)}')

medellin = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Colombia')
j = 'RH[%]'
i ='PM2,5'
mask = ~np.isnan(medellin[j]) & ~np.isnan(medellin[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(medellin[j][mask] / 30 * 100, medellin[i][mask])
print(f'Medellín \t {j} vs (PM2.5 / 30 * 100) \t pendiente = {round(slope, 4)} \t ordenada = {round(intercept,4)} \t R = {round(r_value ** 2,4)}')

saopaulo = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Brasil')
j = 'RH[%]'
i ='PM2.5'
mask = ~np.isnan(saopaulo[j]) & ~np.isnan(saopaulo[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(saopaulo[j][mask] / 30 * 100, saopaulo[i][mask])
print(f'Sao Paulo \t {j} vs (PM2.5 / 30 * 100) \t pendiente = {round(slope, 4)} \t ordenada = {round(intercept,4)} \t R = {round(r_value ** 2,4)}')

# + tags=[] jupyter={"source_hidden": true}
resultados = pd.DataFrame()

uruguay = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Uruguay')
j = 'tmpd[C]'
i ='PM 2.5 (µg/Nm3)'
mask = ~np.isnan(uruguay[j]) & ~np.isnan(uruguay[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(uruguay[j][mask] / 30 * 100, uruguay[i][mask])
print(f'Montevideo \t {j} vs (PM2.5 / 30 * 100) \t pendiente = {round(slope, 4)} \t ordenada = {round(intercept,4)} \t R = {round(r_value ** 2,4)}')

san_jose = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Costa Rica')
j = 'tmpd[C]'
i ='PM2,5'
mask = ~np.isnan(san_jose[j]) & ~np.isnan(san_jose[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(san_jose[j][mask] / 30 * 100, san_jose[i][mask])
print(f'San José \t {j} vs (PM2.5 / 30 * 100) \t pendiente = {round(slope, 4)} \t ordenada = {round(intercept,4)} \t R = {round(r_value ** 2,4)}')

quito = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Ecuador')
j = 'tmpd[C]'
i ='PM 2.5 (µg/Nm3)'
mask = ~np.isnan(quito[j]) & ~np.isnan(quito[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(quito[j][mask] / 30 * 100, quito[i][mask])
print(f'Quito \t\t {j} vs (PM2.5 / 30 * 100) \t pendiente = {round(slope, 4)} \t ordenada = {round(intercept,4)} \t R = {round(r_value ** 2,4)}')

ezeiza = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Argentina')
j = 'tmpd[C]'
i ='PM 2.5 (µg/Nm3)'
mask = ~np.isnan(ezeiza[j]) & ~np.isnan(ezeiza[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(ezeiza[j][mask] / 30 * 100, ezeiza[i][mask])
print(f'Buenos Aires \t {j} vs (PM2.5 / 30 * 100) \t pendiente = {round(slope, 4)} \t ordenada = {round(intercept,4)} \t R = {round(r_value ** 2,4)}')

medellin = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Colombia')
j = 'tmpd[C]'
i ='PM2,5'
mask = ~np.isnan(medellin[j]) & ~np.isnan(medellin[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(medellin[j][mask] / 30 * 100, medellin[i][mask])
print(f'Medellín \t {j} vs (PM2.5 / 30 * 100) \t pendiente = {round(slope, 4)} \t ordenada = {round(intercept,4)} \t R = {round(r_value ** 2,4)}')

saopaulo = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Brasil')
j = 'tmpd[C]'
i ='PM2.5'
mask = ~np.isnan(saopaulo[j]) & ~np.isnan(saopaulo[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(saopaulo[j][mask] / 30 * 100, saopaulo[i][mask])
print(f'Sao Paulo \t {j} vs (PM2.5 / 30 * 100) \t pendiente = {round(slope, 4)} \t ordenada = {round(intercept,4)} \t R = {round(r_value ** 2,4)}')

# + jupyter={"source_hidden": true} tags=[]
resultados = pd.DataFrame()

uruguay = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Uruguay')
j = 'wspd[m/s]'
i ='PM 2.5 (µg/Nm3)'
mask = ~np.isnan(uruguay[j]) & ~np.isnan(uruguay[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(uruguay[j][mask] / 30 * 100, uruguay[i][mask])
print(f'Montevideo \t {j} vs (PM2.5 / 30 * 100) \t pendiente = {round(slope, 4)} \t ordenada = {round(intercept,4)} \t R = {round(r_value ** 2,4)}')

san_jose = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Costa Rica')
j = 'wspd[m/s]'
i ='PM2,5'
mask = ~np.isnan(san_jose[j]) & ~np.isnan(san_jose[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(san_jose[j][mask] / 30 * 100, san_jose[i][mask])
print(f'San José \t {j} vs (PM2.5 / 30 * 100) \t pendiente = {round(slope, 4)} \t ordenada = {round(intercept,4)} \t R = {round(r_value ** 2,4)}')

quito = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Ecuador')
j = 'wspd[m/s]'
i ='PM 2.5 (µg/Nm3)'
mask = ~np.isnan(quito[j]) & ~np.isnan(quito[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(quito[j][mask] / 30 * 100, quito[i][mask])
print(f'Quito \t\t {j} vs (PM2.5 / 30 * 100) \t pendiente = {round(slope, 4)} \t ordenada = {round(intercept,4)} \t R = {round(r_value ** 2,4)}')

ezeiza = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Argentina')
j = 'wspd[m/s]'
i ='PM 2.5 (µg/Nm3)'
mask = ~np.isnan(ezeiza[j]) & ~np.isnan(ezeiza[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(ezeiza[j][mask] / 30 * 100, ezeiza[i][mask])
print(f'Buenos Aires \t {j} vs (PM2.5 / 30 * 100) \t pendiente = {round(slope, 4)} \t ordenada = {round(intercept,4)} \t R = {round(r_value ** 2,4)}')

medellin = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Colombia')
j = 'wspd[m/s]'
i ='PM2,5'
mask = ~np.isnan(medellin[j]) & ~np.isnan(medellin[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(medellin[j][mask] / 30 * 100, medellin[i][mask])
print(f'Medellín \t {j} vs (PM2.5 / 30 * 100) \t pendiente = {round(slope, 4)} \t ordenada = {round(intercept,4)} \t R = {round(r_value ** 2,4)}')

saopaulo = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Brasil')
j = 'wspd[m/s]'
i ='PM2.5'
mask = ~np.isnan(saopaulo[j]) & ~np.isnan(saopaulo[i])
slope, intercept, r_value, p_value, std_err = stats.linregress(saopaulo[j][mask] / 30 * 100, saopaulo[i][mask])
print(f'Sao Paulo \t {j} vs (PM2.5 / 30 * 100) \t pendiente = {round(slope, 4)} \t ordenada = {round(intercept,4)} \t R = {round(r_value ** 2,4)}')
# -

plt.plot(saopaulo['Fecha'], saopaulo['wspd[m/s]'], 'o-')
plt.xticks(rotation=45, ha="right")
plt.ylabel('wspd[m/s]')
plt.show()
saopaulo_idx = saopaulo.set_index('Fecha')

