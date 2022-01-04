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

# + jupyter={"outputs_hidden": true} tags=[]
uruguay = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Uruguay')
#uruguay['tmpd[C]'].plot()
#plt.show()
for j in ['tmpd[C]', 'RH[%]', 'wspd[m/s]']:
    for i in uruguay.keys()[4:26]:
        plt.plot(uruguay[j], uruguay[i], '.', label=i)
        plt.legend()
        plt.ylabel(i)
        plt.xlabel(j)
        plt.title('Montevideo')
        plt.show()

# + jupyter={"outputs_hidden": true} tags=[]
san_jose = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Costa Rica')
#san_jose['tmpd[C]'].plot()
#plt.show()
for j in ['tmpd[C]', 'RH[%]', 'wspd[m/s]']:
    for i in san_jose.keys()[3:25]:
        plt.plot(san_jose[j], san_jose[i], '.', label=i)
        plt.legend()
        plt.ylabel(i)
        plt.xlabel(j)
        plt.title('San José')
        plt.show()

# + jupyter={"outputs_hidden": true} tags=[]
quito = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Ecuador')
#quito['tmpd[C]'].plot()
#plt.show()
for j in ['tmpd[C]', 'RH[%]', 'wspd[m/s]']:
    for i in quito.keys()[3:25]:
        plt.plot(quito[j], quito[i], '.', label=i)
        plt.legend()
        plt.ylabel(i)
        plt.xlabel(j)
        plt.title('Quito')
        plt.show()

# + jupyter={"outputs_hidden": true} tags=[]
ezeiza = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Argentina')
#ezeiza['tmpd[C]'].plot()
#plt.show()
for j in ['tmpd[C]', 'RH[%]', 'wspd[m/s]']:
    for i in ezeiza.keys()[3:25]:
        plt.plot(ezeiza[j], ezeiza[i], '.', label=i)
        plt.legend()
        plt.ylabel(i)
        plt.xlabel(j)
        plt.title('Buenos Aires')
        plt.show()

# + jupyter={"outputs_hidden": true} tags=[]
medellin = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Colombia')
#medellin['tmpd[C]'].plot()
#plt.show()
for j in ['tmpd[C]', 'RH[%]', 'wspd[m/s]']:
    for i in medellin.keys()[3:25]:
        plt.plot(medellin[j], medellin[i], '.', label=i)
        plt.legend()
        plt.ylabel(i)
        plt.xlabel(j)
        plt.title('Medellín')
        plt.show()

# + tags=[]
saopaulo = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Brasil')
#saopaulo['tmpd[C]'].plot()
#plt.show()
for j in ['tmpd[C]', 'RH[%]', 'wspd[m/s]']:
    for i in saopaulo.keys()[3:7]:
        plt.plot(saopaulo[j], saopaulo[i], '.', label=i)
        plt.legend()
        plt.ylabel(i)
        plt.xlabel(j)
        plt.title('Sao Paulo')
        plt.show()
