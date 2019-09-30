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
        s = linea.split(',')
        try:
            operacion, op1 = s[0], float(s[1])
        except ValueError:
            print("Valor introducido no valido")
            continue
        for op2 in s[2:]:
            try:
                calcu = calcoohija.CalculadoraHija(op1, operacion, float(op2))
                resultado = calcu.operar()
                op1 = resultado
            except ValueError:
                print("Valor introducido no valido")
        print(resultado)

    fichero.close()
