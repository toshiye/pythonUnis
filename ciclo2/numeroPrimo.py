num = int(input('Digite um número: '))

divisoes = 0

for c in range(1, num+1):
    if num % c == 0:
        divisoes += 1
if divisoes == 2:
    print('Verdadeiro, o número %d é primo!' %(num))
else:
    print('Falso, o número %d não é primo!' %(num))