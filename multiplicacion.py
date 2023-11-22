# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 18:24:05 2023

@author: ulise
"""

def multiplica(a,b): 
    variable1=a+9
    variable2=b*3
    resultado=variable1+variable2
    print("Empezando for")
    for i in range(1, 5): 
        print(i)
        resultado=resultado * i
        
        print(resultado)
    
multiplica(3,6)