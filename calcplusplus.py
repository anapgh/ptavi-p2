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
                opera, op1 = linea[0], float(linea[1])
            except ValueError:
                print("Valor introducido no valido")
                continue
            for op2 in linea[2:]:
                try:
                    calcu = calcoohija.CalculadoraHija(op1, opera, float(op2))
                    resultado = calcu.operar()
                    op1 = resultado
                except ValueError:
                    print("Valor introducido no valido")
            print(resultado)

    csvarchivo.close()
