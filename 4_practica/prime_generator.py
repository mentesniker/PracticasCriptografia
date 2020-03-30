from random import randint
from random import randrange
import datetime
import operator, functools

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
    if (size is None) or (size < 100):
    	size = randint(100,150)
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
    if n==2 or n==3:
    	return True
    r, d = discompose(n)
    k = randint(1,3)
    for i in range(k):
    	a = randint(2,n-2)
    	x = (a**d) % n
    	if x!=1 and x!=n-1:
    		for j in range(r-1):
    			x = (x**2) % n
    			if x!=n-1:
    				return False
    return True

def discompose(n):
	"""
	Función auxiliar que permite hacer la siguiente descomposición
	de un número n.
	n = ((2**r)*d)+1
	:param n: El número a descomponer.
	:return r: El elemento r de la descomposición.
	:return d: El elemento d de la descomposición.
	"""
	r = 1
	d = 1
	for i in range(n):
		for j in range(n):
			if n == ((2**r)*d)+1:
				return r, d
			d+=1
		r+=1
		d=1
	return 1, 1

def wilson(n):
    """
    Implementaión del test de primalidad de Wilson, basado en el teorema de Wilson,
    (p-1)! ≡ -1 mod p
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    numbers = list(range(n))
    fact = functools.reduce(operator.mul, numbers[2:len(numbers)], 1)
    return fact%n == -1%n