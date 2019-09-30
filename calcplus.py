#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:03:42 2019

@author: ana
"""
import sys
import calcoohija


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: calcplus.py fichero")

    _, input = sys.argv

    fichero = open(input, 'r')
    datos = fichero.readlines()

    for linea in datos:
        try:
            s = linea.split(',')
            operacion = s[0]
            op1 = float(s[1])
            x = 2
            while x != len(s):
                op2 = float(s[x])
                x += 1
                calcu = calcoohija.CalculadoraHija(op1, operacion, op2)
                resultado = calcu.operar()
                op1 = resultado

            print(resultado)
        except ValueError:
            print("Valor introducido no valido")

    fichero.close()
