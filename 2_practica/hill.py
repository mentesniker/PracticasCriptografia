#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
import random
import math
import numpy as np
from utils import CryptographyException

class Hill():

    def __init__(self, alphabet, n, key=None):
        """
        Constructor de clase, recibiendo un alfabeto completamente necesario pero
        podría no recibir una llave de cifrado, en cuyo caso, hay que generar una,
        para el caso del tama\xc3Ho de la llave, hay que asegurarse que tiene raíz entera.
        :param alphabet: una cadena con todos los elementos del alfabeto.
        :param n: el tama\xc3o de la llave, obligatorio siempre.
        :param key: una cadena que corresponde a la llave, en caso de ser una llave inválida
        arrojar una CryptographyException.
        """
        self.alphabet = alphabet
        self.n = n
        decimal, entera = math.modf(math.sqrt(self.n))
        if key and decimal==0:
            self.key = self.generate_key(key)
        elif key or not decimal==0:
        	raise CryptographyException()
        else:
            self.key = self.generate_key()
            
    def cipher(self, message):
    	"""
        Aplica el algoritmo de cifrado con respecto al criptosistema de Hill, el cual recordando
        que todas las operaciones son mod |alphabet|.
        :param message: El mensaje a enviar que debe ser cifrado.
        :return: Un criptotexto correspondiente al mensaje, este debe de estar en representación de
        cadena, no lista.
        """
    	message = message.replace(" ","")
    	ciphermessage = ""
    	raiz = int(math.sqrt(self.n))
    	i=0
    	while i<len(message):
    		a = []
    		for j in range(raiz):
    			a.append(self.alphabet.index(message[i]))
    			i+=1
    		matriz=np.array(a).reshape(raiz,1)
    		mult = np.dot(self.key, a)
    		ciphermessage += self.cipher_sqrt_chars(mult)

    	return ciphermessage

    def cipher_sqrt_chars(self,matriz):
        """
        Funcion auxiliar que hace el cifrado de dos caracteres,utilizando
        el cifrado hill.
        :param indice: el indice desde el cual empezamos a tomar los caracteres
        del mensaje que se recibe como parametro.
        :param message: el mensaje que queremos cifrar
        :return: un string con los dos caracteres cifrados.
        """
        resultado = ""
        raiz = int(math.sqrt(self.n))
        for i in range(raiz):
        	resultado += self.alphabet[int(matriz[i]%len(self.alphabet))]
        return resultado

    def decipher(self, message):
        print(self.key)
        message = message.replace(" ","")
        ciphermessage = ""
        raiz = int(math.sqrt(self.n))
        inversa = np.linalg.inv(self.key)
        i=0
        while i<len(message):
        	a = []
        	for j in range(raiz):
        		a.append(self.alphabet.index(message[i]))
        		i+=1
        	matriz=np.array(a).reshape(raiz,1)
        	mult = np.dot(inversa, a)
        	ciphermessage += self.cipher_sqrt_chars(mult)
        return ciphermessage

    def generate_key(self, key=None):
    	raiz=int(math.sqrt(self.n))
    	b = []
    	llave=""
    	if key:
    	    llave=key
    	else:
            for i in range(self.n):
            	llave += self.alphabet[random.randint(0,len(self.alphabet)-1)]
    	
    	for j in range(self.n):
    		b.append(self.alphabet.index(llave[j]))
        
    	matriz=np.array(b).reshape(raiz,raiz)
    	determinante=np.linalg.det(matriz)
    	while determinante==0:
    		llave=""
    		b = []
    		for k in range(self.n):
    			llave += self.alphabet[random.randint(0,len(self.alphabet)-1)]
    		matriz=np.array(b).reshape(raiz,raiz)
    		determinante=np.linalg.det(matriz)
    	return matriz

    
alphabet = "ABCDEFGHIJKLMN\xc3OPQRSTUVWXYZ"
key2 = "EBAY"

cipher = Hill(alphabet, 4, "DBBB")
