"""for n in range(1, 101):
    if n / 1 == n and n / n == 1:
        print ('O número %d é primo' %(n))"""

"""for n in range(1, 101):
    if n%2 == 1:
        print ('O número %d é primo' %(n))"""

"""for n in range(2, 101):
    if 101 % n :
        print ('O número %d é primo' %(n))"""

"""num = 1
topo = 100
while num <= topo:
    if num%2 == 1:
        num = num + 1
        print ('O número %d é primo' %(num))"""

"""num = 1
topo = 100
while num <= topo:
    if num != 1 or num % 2 != 0:
        num = num + 1
        print ('O número %d é primo' %(num))"""

"""numeros = []

for i in range(1, 100):
    numeros.append(i+1)
for n in numeros:
    if numeros % n == 0:
        print('O número %d é Primo!' %(n))
    else:
        print('O número %d não é Primo!' %(n))"""

"""numeros = range(1, 100)
for n in numeros:
    if numeros % n == 0:
        print('O número %d é Primo!' %(n))
    else:
        print('O número %d não é Primo!' %(n))"""


def primeNumber(numero):
    divisoes = 0
    for c in range(1, numero + 1):
        if numero % c == 0:
            divisoes += 1
        if divisoes == 2:
            print('O número %d é Primo!' % (c))
        else:
            print('O número %d não é Primo!' % (c))


numbers = range(1, 100 + 1)

for n in numbers:
    primeNumber(n)


