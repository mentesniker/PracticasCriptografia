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
        encripted_number = 0
        encripted_message = ""
        k = 0
        j = 0
        i = 0
        message = message.replace(" ","")
        while(k < len(message)):
            while(j < len(message)):
                while(i < self.n and j < len(message)):
                    encripted_number += (self.alphabet.find(self.key[i])) * (self.alphabet.find(message[j]))
                    j += 1
                    i += 1 
                i = 0
            encripted_message += self.alphabet[encripted_number%26]
            encripted_number = 0
            k += 1
        print(encripted_message)

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
