#!/usr/bin/env python
#_*_ coding:latin1 _*_

#N�meros
#Convertendo de real para inteiro
print 'int(3.14) =', int(3.14)

#Convertendo de inteiro para real
print 'float(5) =', float(5)

#Calculo entre inteiro e real resulta em real
print '5.0 / 2 + 3 =', 5.0 / 2 + 3

#Inteiros em outra base
print "int('20', 8) =", int('20', 8) #base 8
print "int('20', 16) =", int('20', 16) #base 16

#Opera��es com n�meros compolexos
c = 3 + 4j
print 'c =', c
print 'Parte Real: ', c.real
print 'Parte imagin�ria: ', c.imag
print 'Conjugado: ', c.conjugate()