#_*_ coding:latin1 _*_

s = 'Camel'

#Concatenação
print 'The ' + s + ' run away!'

#interpolação
print 'tamanho de %s => %d' %(s, len(s))

#String tratada como sequência
for ch in s: print ch

#Strings são objetos
if s.startswith('C'): print s.upper()

#o que acontecerá?
print 3 * s
#o 3 * s é consistente com s + s + s