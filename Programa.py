#    Bueno el programa es sencillo, consiste en q primero te va a pedir que ingreses 2 numeros.
##   Luego te va a Imprimir los numeros que hay entre ellos, comenzando por el mas pequeno.
###  Despues te va a contar cuantos hay entre ellos y cuantos son pares.
#### Por ultimo te va a Calcular la suma de los numeros pares.


p = 0
cp = 0
c = 0
n = 0
h = 0

h1 = input('Ingresa el primer numero: ')
h2 = input('Ingresa el segundo numero: ') 


if h1 > h2:
    n = h2
    h = h1
else:
    n = h1
    h = h2
while n < h:
    n += 1
    if n == h:
        break
    c += 1
    print n,
    if n%2 == 0:
        cp += 1
        p += n
        
print '\nEntre % i y %i hay %i numeros siendo %i pares' % (h1, h2, c, cp)
print 'La suma de los pares es: %i' % p
