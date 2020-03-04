#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import os, sys
import random
import math

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
            self.generate_key()
            
    def cipher(self, message):
        message = message.replace(" ","")
        ciphermessage = ""
        if(len(message)%2 != 0):
            message += "A"
        i = 0
        while(i < len(message)):
            ciphermessage += self.cipher_sqrt_chars(i,message)
            i += int(math.sqrt(len(self.key)))
        return ciphermessage

    def cipher_sqrt_chars(self,indice,message):
        """
        Funcion auxiliar que hace el cifrado de dos caracteres,utilizando
        el cifrado hill.
        :param indice: el indice desde el cual empezamos a tomar los caracteres
        del mensaje que se recibe como parametro.
        :param message: el mensaje que queremos cifrar
        :return: un string con los dos caracteres cifrados.
        """
        encripted_message = ""
        encripted_number = 0
        i = indice
        j = 0
        k = 0
        sqrt_n = int(math.sqrt(len(self.key)))
        while(j < len(self.key)):
            encripted_number += self.alphabet.find(self.key[k]) * (self.alphabet.find(message[i]))
            i += 1
            k += 1
            j += 1
            if(j % sqrt_n == 0):
                i = indice
                encripted_message += self.alphabet[encripted_number%27]
                encripted_number = 0
        return encripted_message


    def decipher(self, ciphered):
        """
        Usando el algoritmo de decifrado, recibiendo una cadena que se asegura que fue cifrada
        previamente con el algoritmo de Hill, obtiene el texto plano correspondiente.
        :param ciphered: El criptotexto de algún mensaje posible.
        :return: El texto plano correspondiente a manera de cadena.
        """
        det = 1/self.calculate_determinant(self.key)
        invers = ""
        resolved = ""
        encripted_message = ""
        encripted_number = 0
        i = indice
        j = 0
        k = 0
        sqrt_n = int(math.sqrt(len(self.key)))
        while(j < len(self.key)):
            encripted_number += self.alphabet.find(self.key[k]) * (self.alphabet.find(message[i]))
            i += 1
            k += 1
            j += 1
            if(j % sqrt_n == 0):
                i = indice
                resolved += self.alphabet[encripted_number%27]
                encripted_number = 0
       
        return resolved
        
        
    def generate_key(self):
        self.key = ""
        for i in range(self.n):
            self.key+= self.alphabet[random.randint(0,self.n)]
            
    #Pre: len(key) == 4    
    def calculate_determinant(self, key):
        return self.alphabet.find(key[0])*self.alphabet.find(key[3])-self.alphabet.find(key[2])*self.alphabet.find(key[1])  
             
alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
cipher = None
key2 = "EBAY"

prueba=Hill(alphabet,4)

cifrado=prueba.cipher("UN MENSAJE CON Ñ")

print(cifrado)

criptotext = prueba.cipher("UN MENSAJE DE LONGITUD PAR")
print(criptotext)

c1 = prueba.cipher("UN MENSAJE CON Ñ")
print(c1)
#print(prueba.decipher(c1) == "UNMENSAJECONÑA")
c2 = prueba.cipher("UN MENSAJE DE LONGITUD PAR")
#print(prueba.decipher(c2) == "UNMENSAJEDELONGITUDPAR")
print(c2)
