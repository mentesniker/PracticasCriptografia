#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import os, sys
import random
class Hill():

    def __init__(self, alphabet, n, key=None):
        """
        Constructor de clase, recibiendo un alfabeto completamente necesario pero
        podría no recibir una llave de cifrado, en cuyo caso, hay que generar una,
        para el caso del tamañHo de la llave, hay que asegurarse que tiene raíz entera.
        :param alphabet: una cadena con todos los elementos del alfabeto.
        :param n: el tamaño de la llave, obligatorio siempre.
        :param key: una cadena que corresponde a la llave, en caso de ser una llave inválida
        arrojar una CryptographyException.
        """
    
        self.alphabet = alphabet
        self.n = n
        if(key):
            self.key = key
        elif(key):
            raise CryptographyException('Invalid key!!')
        else:
            self.key = generate_key()
            
    def cipher(self, message):
        """
        Aplica el algoritmo de cifrado con respecto al criptosistema de Hill, el cual recordando
        que todas las operaciones son mod |alphabet|.
        :param messa{ge: El mensaje a enviar que debe ser cifrado.
        :return: Un criptotexto correspondiente al mensaje, este debe de estar en representación de
        cadena, no lista.
        """
        encripted_message = ""
        for i in range(self.n-1):
            encripted_number = 0 
            for j in range((self.n)):
                print(i,j)
                print(self.n * i +j)
                encripted_number +=(ord(self.key[(i*self.n + j)]) * ord(message[j]))%27
            encripted_message += chr(encripted_number)
        return encripted_message
  

    def decipher(self, ciphered):
        """
        Usando el algoritmo de decifrado, recibiendo una cadena que se asegura que fue cifrada
        previamente con el algoritmo de Hill, obtiene el texto plano correspondiente.
        :param ciphered: El criptotexto de algún mensaje posible.
        :return: El texto plano correspondiente a manera de cadena.
        """
        det = 1/calculate_determinant(self.key)
        invers = ""
        resolved = ""
        for i in range(self.n):
            for j in range(self.n):
	            invers += self.key[j*self.n+i]*det
        for i in range(self.n):
            for j in range(self.n):
                resolved += chr((invers[i*self.n + j] * ord(ciphered[j]))%27)
        return resolved
        
        
    def _generate_key(self):
        self.key = ""
        for i in range(self.n**2):
            self.key+=chr(random.randint(self.n))
            
        
        
alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
cipher = None
key2 = "EBAY"

prueba=Hill(alphabet,4,key2)

cifrado=prueba.cipher("UN MENSAJE CON Ñ")

print(cifrado)
