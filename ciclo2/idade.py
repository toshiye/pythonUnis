input = int(input('Digite o número de dias para que eu calcule sua idade: '))

ano = input / 365
input %= 365

mes = input / 30
input %= 30

dia = input

"""print ('Você tem '+ ano +' anos, '+ mes +' meses e '+ dia +' dias de vida')"""
print ('Você tem %s ano(s), %s mes(es) e %s dia(s) de vida' %(str(int(ano)), str(int(mes)), str(int(dia))))