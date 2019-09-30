#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:54:02 2019

@author: ana
"""

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):
    def multi(self):
        return self.operando1 * self.operando2

    def divi(self):
        try:
            return self.operando1 / self.operando2
        except ZeroDivisionError:
            return ("Integer division or modulo by zero")

    def operar(self):
        if self.operator == "multiplica":
            return self.multi()
        elif self.operator == "divide":
            return self.divi()
        else:
            return calcoo.Calculadora.operar(self)


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) != 4:
        sys.exit("Usage: calcoo.py operando1 operator operando2")

    operacion = sys.argv[2]

    try:
        operando1 = float(sys.argv[1])
        operando2 = float(sys.argv[3])
    except ValueError:
        sys.exit("Solo se puede enteros y floats")

    # creo mi objeto con los argumentos cogidos por pantalla
    calcu = CalculadoraHija(operando1, operacion, operando2)
    resultado = calcu.operar()
    print(resultado)