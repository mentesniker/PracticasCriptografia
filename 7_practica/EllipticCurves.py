#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
from utils import modinv

class Curve():

    def __init__(self, A, B, p):
        """
        Construcutor de clase que va a representar a la curva elíptica de la
        forma y^2 = x^3 + Ax + B (mod p).
        :param A: primer coeficiente de la curva.
        :param B: segundo coeficiente de la curva.
        :param p: el tamaño del campo sobre el cual se hace la curva.
        """
        self.A = A
        self.B = B
        self.p = p

    def is_on_curve(self, point):
        """
        Método de clase regresa true si un punto está en la curva, éste punto 
        está representado a manera de tupla, como (x, y).
        :param point: Una tupla de enteros representando a un punto.
        :return: true si el punto está en la curva, false en otro caso.
        """
        if point is None:
        	return True
        evaluado = ((point[0]**3) + (self.A*point[0]) + self.B) % self.p
        return pow(point[1], 2, self.p) == evaluado

    def determinant(self):
        """
        Regresa el determinante de una curva, recordando que su determinante
        es calculado de la forma 4A^3 + 27B^2.
        :return: El entero con el valor del determinante.
        """
        return 4*(self.A**3) + 27*(self.B**2)

def add_points(p, q, curve):
    """
    Dados un par de puntos y una curva elíptica, calcula el punto de la suma
    bajo la curva elíptica recibida como parámetro, se asume que p y q ya 
    forman parte de la curva.
    :param p: una tupla representando un punto de la curva.
    :param q: una tupla representando un punto de la curva.
    :param curve: una instancia de la clase de este script.
    :return: Una tupla que contiene el resultado de la suma o None en caso de
    que haya sido evaluada al punto infinito.
    """
    if p is None:
        return q
    if q is None:
        return p
    if p[0]==q[0] and -p[1]==q[1]:
        return None
    if p[0]==q[0]:
    	return None
    lambdaC = calculate_lambda(p, q, curve)
    x3 = pow(lambdaC, 2) - p[0] - q[0]
    y3 = (lambdaC * (p[0]-x3)) - p[1]
    return (x3, y3)

def calculate_lambda(p, q, curve):
	if p==q:
		return (3*pow(p[0],2) + curve.A) * modinv(2*p[1], curve.p)
	return (p[1]-q[1]) * modinv((p[0]-q[0])%curve.p, curve.p)

def scalar_multiplication(p, k, curve):
    """
    Dado un escalar del campo, k, calcula el punto kP bajo la definición
    de curvas elípticas.
    :param p: una tupla representando un punto de la curva.
    :param k: el escalar a multiplicar por el punto. 
    :param curve: la curva sobre la cual se calculan las operaciones.
    :return: una tupla representando a kP o None si al sumar ese punto cayó 
    en algún momento al punto infinito.
    """
    if k==1:
    	return p
    punto = scalar_multiplication(p, k-1, curve)
    if add_points(p, punto, curve) is None:
    	return None
    return (p[0]+punto[0], p[1]+punto[1])




c = Curve(2, 3, 97)

print(c.is_on_curve((17, 10)))
print(c.is_on_curve((95, 31)))
print(not c.is_on_curve((13, 13)))
print(c.is_on_curve(None))
print(c.determinant() == 275)

P, Q = (17, 10), (95, 31)

p_plus_q = add_points(P, Q, c)
print(p_plus_q)
print(c.is_on_curve(p_plus_q))
inf = add_points(P, (17, 87), c)
print(c.is_on_curve(inf) and inf == None)
p_plus_p = add_points(P, P, c)
print(c.is_on_curve(p_plus_p))

one_p = scalar_multiplication(P, 1, c)
print(c.is_on_curve(one_p))
k = 1
while one_p != None:
	k += 1
	one_p = add_points(P, one_p, c)	
print(scalar_multiplication(P, k, c))
print(P)
print(k)
print(scalar_multiplication(P, k, c) == None)
