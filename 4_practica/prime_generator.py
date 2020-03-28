from random import randint
from random import randrange
import datetime
def big_int(size=None):
    """
    Generador de números aleatorios de un tamaño fijo recibido como parámetro, si el parámetro es
    menor que 100 o None, entonces la función no le hace caso y genera uno de tamaño arbitrario,
    máximo es de 150 dígitos.
    :return: Un número del tamaño descrito.
    El algoritmo implementado es linear congruential generator
    Nos basamos de la pagina http://pi.math.cornell.edu/~mec/Winter2009/Luo/Linear%20Congruential%20Generator/linear%20congruential%20gen1.html
    para garantizar que no hace un ciclo y empieza a repetir digitos.
    Esto sucede asi porque m y c son primos relativos y a-1 divide a todos los factores primos de m
    """
    if(size < 100):
        size = 120
    elif(size is None):
        size = 120
    date_object = datetime.date.today()
    time = datetime.datetime.now()
    numero = ""
    x = 2
    m = 1299827
    a = 2
    c = int(date_object.year) + int(date_object.month) + int(date_object.month) + int(date_object.day) + int(time.hour) + int(time.minute) + int(time.second)
    i = 0
    while(i < size and len(numero) < size):
        x = (a*x + c)%m
        numero += str(x)
        i += 1
    return int(numero[0:size])

def miller_rabin(n):
    """
    Implementación del test de primalidad de Miller-Rabin.
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    pass


def wilson(n):
    """
    Implementaión del test de primalidad de Wilson, basado en el teorema de Wilson,
    (p-1)! ≡ -1 mod p
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    pass
