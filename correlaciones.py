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

# + tags=[] jupyter={"outputs_hidden": true}
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
        plt.savefig('correlaciones_meteo/Uruguay/Montevideo_' +
                    i.replace('/', '_') + '_' + j.replace('/', '_') +
                    '.pdf')
        plt.show()

# + tags=[] jupyter={"outputs_hidden": true}
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
        plt.savefig('correlaciones_meteo/CostaRica/SanJose' +
                    i.replace('/', '_') + '_' + j.replace('/', '_') +
                    '.pdf')
        plt.show()

# + tags=[] jupyter={"outputs_hidden": true}
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
        plt.savefig('correlaciones_meteo/Ecuador/Quito' +
                    i.replace('/', '_') + '_' + j.replace('/', '_') +
                    '.pdf')
        plt.show()

# + tags=[]
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
        plt.savefig('correlaciones_meteo/Argentina/BuenosAires' +
                    i.replace('/', '_') + '_' + j.replace('/', '_') +
                    '.pdf')
        plt.show()

# + tags=[]
ezeiza = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Argentina')
for j in ['RH[%]']:
    for i in ezeiza.keys()[3:25]:
        plt.plot(ezeiza[j], ezeiza[i]/ezeiza['CT'], '.', label=i)
        plt.legend()
        plt.ylabel(i+ '/EC')
        plt.xlabel(j)
        plt.title('Buenos Aires')
        #plt.savefig('correlaciones_meteo/Argentina/BuenosAires' +
        #            i.replace('/', '_') + '_' + j.replace('/', '_') +
        #            '.pdf')
        plt.show()

# + jupyter={"outputs_hidden": true} tags=[]
#print(ezeiza.keys())
for i in ['PM 2.5 (µg/Nm3)', 'EC', 'EC1', 'EC2', 'EC3', 'EC4', 'EC5', 'EC6']:
    slope, intercept, r_value, p_value, std_err = stats.linregress(ezeiza['RH[%]'], ezeiza[i])
    plt.plot(ezeiza['RH[%]'], ezeiza[i], 'o')
    plt.xlabel('RH')
    plt.ylabel(i)
    plt.plot(ezeiza['RH[%]'], slope * ezeiza['RH[%]'] + intercept)
    plt.show()


# + jupyter={"outputs_hidden": true} tags=[]

for i in ['OC', 'OC1', 'OC2', 'OC3', 'OC4', 'OC5', 'OC6']:
    slope, intercept, r_value, p_value, std_err = stats.linregress(ezeiza['RH[%]'], ezeiza[i])
    plt.plot(ezeiza['RH[%]'], ezeiza[i], 'o')
    plt.xlabel('RH')
    plt.ylabel(i)
    plt.plot(ezeiza['RH[%]'], slope * ezeiza['RH[%]'] + intercept)
    plt.show()


# + tags=[] jupyter={"outputs_hidden": true}
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
        plt.savefig('correlaciones_meteo/Colombia/Medellin' +
                    i.replace('/', '_') + '_' + j.replace('/', '_') +
                    '.pdf')
        plt.show()

# + tags=[] jupyter={"outputs_hidden": true}
medellin = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Colombia')
#medellin['tmpd[C]'].plot()
#plt.show()
for j in ['tmpd[C]', 'RH[%]', 'wspd[m/s]']:
    for i in medellin.keys()[3:25]:
        mask = ~np.isnan(medellin[j]) & ~np.isnan(medellin[i])
        slope, intercept, r_value, p_value, std_err = stats.linregress(medellin[j][mask], medellin[i][mask])
        plt.plot(medellin[j], medellin[i], '.', label=i)
        plt.plot(medellin[j], slope * medellin[j] + intercept)
        #plt.savefig('correlaciones_meteo/Colombia/Medellin' +
        #            i.replace('/', '_') + '_' + j.replace('/', '_') +
        #            '.pdf')
        plt.legend()
        plt.ylabel(i)
        plt.xlabel(j)
        plt.title('Medellín')
        plt.show()
        print((slope * 10).round(4))

# + tags=[] jupyter={"outputs_hidden": true}
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
        plt.savefig('correlaciones_meteo/Brasil/SaoPaulo' +
                    i.replace('/', '_') + '_' + j.replace('/', '_') +
                    '.pdf')
        plt.show()

# + tags=[] jupyter={"outputs_hidden": true}


saopaulo = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Brasil')
#print(saopaulo.keys())
for j in ['tmpd[C]', 'RH[%]', 'wspd[m/s]']:
    for i in saopaulo.keys()[3:7]:
        slope, intercept, r_value, p_value, std_err = stats.linregress(saopaulo[j], saopaulo[i])
        plt.plot(saopaulo[j], saopaulo[i], '.', label=i)
        plt.legend()
        plt.ylabel(i )
        plt.xlabel(j)
        plt.title('Sao Paulo')
        plt.plot(saopaulo[j], slope * saopaulo[j] + intercept)
        #plt.savefig('correlaciones_meteo/Brasil/SaoPaulo' +
        #            i.replace('/', '_') + '_' + j.replace('/', '_') +
        #            '.pdf')
        plt.show()


# + tags=[]


saopaulo = pd.read_excel('Base de datos OC-EC Arcal_conmeteo_proc.xlsx', sheet_name='Brasil')
#print(saopaulo.keys())
for j in ['tmpd[C]', 'RH[%]', 'wspd[m/s]']:
    for i in saopaulo.keys()[3:7]:
        plt.plot(saopaulo[j], saopaulo[i]/saopaulo['TC(ug/m3)'], '.', label=i)
        plt.legend()
        plt.ylabel(i + '/TC')
        plt.xlabel(j)
        plt.title('Sao Paulo')
        #plt.savefig('correlaciones_meteo/Brasil/SaoPaulo' +
        #            i.replace('/', '_') + '_' + j.replace('/', '_') +
        #            '.pdf')
        plt.show()

