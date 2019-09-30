#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:53:56 2019

@author: ana
"""

import sys
import calcoohija
import csv


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: calcplus.py fichero")

    _, input = sys.argv

    with open(input) as csvarchivo:
        datos = csv.reader(csvarchivo)
        for linea in datos:
            try:
                operacion = linea[0]
                op1 = float(linea[1])
                x = 2
                while x != len(linea):
                    op2 = float(linea[x])
                    x += 1
                    calcu = calcoohija.CalculadoraHija(op1, operacion, op2)
                    resultado = calcu.operar()
                    op1 = resultado

                print(resultado)

            except ValueError:
                print("Valor introducido no valido")

    csvarchivo.close()
