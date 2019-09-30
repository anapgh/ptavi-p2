#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 10:45:26 2019

@author: ana
"""
import sys


class Calculadora():  # clase madre
    def __init__(self, operando1, operator, operando2):
        "Esto es el método iniciliazador"
        self.operando1 = operando1
        self.operator = operator
        self.operando2 = operando2

    def suma(self):
        return self.operando1 + self.operando2

    def resta(self):
        return self.operando1 - self.operando2

    def operar(self):
        if self.operator == "suma":
            return self.suma()
        elif self.operator == "resta":
            return self.resta()
        else:
            return("Operacion no valida")

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) != 4:
        sys.exit("Usage: calcoo.py operando1 operator operando2")

    operacion = (sys.argv[2])

    try:
        operando1 = float(sys.argv[1])
        operando2 = float(sys.argv[3])
    except ValueError:
        sys.exit("Solo se puede enteros y floats")

    # creo mi objeto con los argumentos cogidos por pantalla
    calcu = Calculadora(operando1, operacion, operando2)
    resultado = calcu.operar()
    print(resultado)