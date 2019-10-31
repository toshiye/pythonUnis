num = int(input('Digite um número:'))

tot = 0

for c in range(1, num+1):
    if num % c == 0:
        print('\33[34m')
        tot += 1
    else:
        print('\33[m')
    print ('{} '.format(c), end='')
print('\n\33[mO número {} foi divisível {} vezes.'.format(num, tot))

if tot == 2:
    print('E por isso ele é Primo!')
else:
    print('E por isso ele não é Primo!')
