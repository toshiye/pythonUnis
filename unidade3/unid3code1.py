#!/usr/bin/env python
#_*_ coding:latin1 _*_

#Uma linha de código que mostra o resultado de 7 vezes 3
print 7 * 3

#Uma linha quebrada por contra-barra
a = 7 * 3 + \
    5 / 2

#Uma lista (quebrada por vírgula)
b = ['a', 'b', 'c',
     'd', 'e']

#Uma chamada de função (quebrada por vírgula)
c = range(1,
          11)

#imprime todos na tela
print a, b, c

#Para i na lista 234, 654, 378, 798:
for i in [234, 654, 378, 798]:
    #Se o resto dividindo por 3 for igual a zero:
    if i % 3 == 0:
        #imprime...
        print i, '/3=', i / 3