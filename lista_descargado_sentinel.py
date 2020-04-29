# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:51:55 2020

@author: fneir
"""

import glob
import os
import pandas as pd
os.chdir('F:/CIREN_guardar_aqui/11 SENTINEL 2A/')
os.getcwd()

ruta = glob.glob('Sentinel-2 Primera entrega/*.zip')
ruta = ruta + glob.glob('Sentinel-2 Segunda entrega/**/**/**.zip', recursive=True)

sentinel = pd.DataFrame(ruta)
sentinel.columns = ['ruta']

sentinel['archivo'] = [(i.split('\\')[-1]) for i in ruta]
sentinel['imagen'] = [(i.split('\\')[-1])[:-4] for i in ruta]

sentinel['mision'] = [(i.split('\\')[-1])[:3] for i in ruta]
sentinel['tile'] = [(i.split('_')[-2])[1:] for i in sentinel.imagen]

sentinel['FechaCaptura'] = [i[11:19] for i in sentinel.imagen]
sentinel['año'] = [(i[:4]) for i in sentinel.FechaCaptura]
sentinel['mes'] = [(i[4:6]) for i in sentinel.FechaCaptura]
sentinel['dia'] = [(i[-2:]) for i in sentinel.FechaCaptura]

reg05 = ['19HCD','19HBD','19HBC','19HDD','19HCE','18HYH','19HBE','18HYJ']
reg13 = ['19HBD','19HCD','19HBC','19HDD','19HCC','19HDC','18HYH']
reg06 = ['18HYG', '18HYH', '19HBB', '19HBC', '19HCB', '19HCC', '19HDB', '19HDC']
reg07 = ['18HXF', '18HYE', '18HYF', '18HYG', '19HBA', '19HBB', '19HBV',
         '19HCA', '19HCB', '19HCV']
reg16 = ['19HCV', '19HCU', '19HBV', '19HBU', '19HBA', '18HYF',
         '18HYE', '18HYD', '18HXF', '18HXE']
reg08 = ['18HXD','19HCU','19HBT','18HYE','19HBV','19HCV','18HYC','18HXC',
         '18HXE','18HWC','19HBU','18HYD','19HCT']

sentinel['reg05'] = (sentinel.tile).isin(reg05)
sentinel['reg13'] = (sentinel.tile).isin(reg13)

sentinel['reg06'] = (sentinel.tile).isin(reg06)
sentinel['reg07'] = (sentinel.tile).isin(reg07)
sentinel['reg08'] = (sentinel.tile).isin(reg08)
sentinel['reg16'] = (sentinel.tile).isin(reg16)

sentinel.to_csv('D:/Desktop/sentinel.csv', sep=',' )


