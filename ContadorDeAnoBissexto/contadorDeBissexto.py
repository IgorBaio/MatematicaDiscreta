# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 22:02:09 2020

@author: Igori
"""

ano = int(input("Digite o ano: "))
'''
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("Ano bissexto")
        else:
            print("Ano normal")
    else:
        print("Ano normal")
else:
    print("Ano normal")
'''

if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print("Ano bissexto")
else:
    print("Ano normal")
    
#nao gostei da fonte, anos bissextos como 2020 e 2016 nao estao sendo reconhcidos