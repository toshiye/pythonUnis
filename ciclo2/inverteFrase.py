frase = str(input('Digite aqui uma frase: '))

inv = ' '.join(p[::-1] for p in frase.split())

print ('Sua frase totalmente invertida é : %s' %(frase[::-1]))

print ('Somente as palavras de sua frase invertidas mas ainda na mesma ordem é: %s' %(inv))

