#_*_ coding:latin1 _*_

s = 'Camel'

#Concatena��o
print 'The ' + s + ' run away!'

#interpola��o
print 'tamanho de %s => %d' %(s, len(s))

#String tratada como sequ�ncia
for ch in s: print ch

#Strings s�o objetos
if s.startswith('C'): print s.upper()

#o que acontecer�?
print 3 * s
#o 3 * s � consistente com s + s + s