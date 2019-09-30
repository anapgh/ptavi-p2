#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:03:42 2019

@author: ana
"""
import sys
import calcoohija


if __name__ == "__main__":
    if len(sys.argv) != 2 :
        sys.exit("Usage: calcplus.py fichero")
        
    _, input = sys.argv
        
    fichero = open(input,'r')
    datos = fichero.readlines()
     
    
    for linea in datos:
        try:
            s = linea.split(',')
            operacion = s[0]
            operando1 = float(s[1])
            x = 2
            while  x != len(s): 
                operando2 = float(s[x])
                x += 1
                calcu = calcoohija.CalculadoraHija(operando1, operacion, operando2)
                resultado = calcu.operar() 
                operando1 = resultado
            
            print(resultado)
               
        except ValueError:
           print(str("Valor introducido no valido"))
           
    fichero.close()


