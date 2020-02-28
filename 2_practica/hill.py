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
        if(key and is_valid(key)):
            self.key = key
        elif(key):
            self.key = generate_key()
        else:
            raise CryptographyException('Invalid key!!')
            
    def cipher(self, message):
        """
        Aplica el algoritmo de cifrado con respecto al criptosistema de Hill, el cual recordando
        que todas las operaciones son mod |alphabet|.
        :param message: El mensaje a enviar que debe ser cifrado.
        :return: Un criptotexto correspondiente al mensaje, este debe de estar en representación de
        cadena, no lista.
        """
        encripted_message = ""
        for i in range(len(self.key)):
            encripted_number = 0 
            for j in range(len(self.key)):
                encripted_number += ord(self.key[i*self.n + j]) * ord(message[j])
            encripted_message += chr(encripted_number)
        return encripted_message
            

    def decipher(self, ciphered):
        """
        Usando el algoritmo de decifrado, recibiendo una cadena que se asegura que fue cifrada
        previamente con el algoritmo de Hill, obtiene el texto plano correspondiente.
        :param ciphered: El criptotexto de algún mensaje posible.
        :return: El texto plano correspondiente a manera de cadena.
        """
        
    def _generate_key(self):
        self.key = ""
        for i in range(self.n**2):
            self.key+=chr(random.randint(self.n))
            
        
        
        
        