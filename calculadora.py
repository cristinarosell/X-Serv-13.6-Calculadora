#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Calculadora para realizar funciones básicas:
sumar, restar, multiplicar y dividir

Para ejecutarlo, desde la shell:
$ python calculadora.py función operando1 operando2

Nombres de las funciones: suma, resta, mult, div

"""

import sys


def suma(op1, op2):
    return op1 + op2


def resta(op1, op2):
    return op1 - op2


def multiplicacion(op1, op2):
    return op1 * op2


def division(op1, op2):
    try:
        return op1 / op2
    except ZeroDivisionError:
        print "Error al dividir entre 0"
        sys.exit()


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print
        sys.exit("Usage: $ python calculadora.py funcion operando1 operando2")

    operacion = sys.argv[1]
    operaciones_posibles = ["suma", "resta", "mult", "div"]
    if operacion not in operaciones_posibles:
        print "Error: " + operacion + " no es una operación válida."
        print
        sys.exit()

    try:
        operando1 = float(sys.argv[2])
        operando2 = float(sys.argv[3])
    except ValueError:
        print "Error: el operando no es válido, introducir un número."
        print
        sys.exit()

    if operacion == "suma":
        print suma(operando1, operando2)
    elif operacion == "resta":
        print resta(operando1, operando2)
    elif operacion == "mult":
        print multiplicacion(operando1, operando2)
    elif operacion == "div":
        print division(operando1, operando2)
    else:

        print "Error: " + operacion + " no es una operación válida"
        print "(suma, resta, mult y div)"
        print
        sys.exit()
