import math

vA = float(input('Digite o primeiro valor: '))

vB = float(input('Digite o segundo valor: '))

vC = float(input('Digite o terceiro valor: '))

if (vB - vC < vA < vB + vC or vA - vC < vB < vA + vC or vA - vB < vC < vA + vB) :
    FHs = (vA + vB + vC) / 2

    if (FHs - vA > 0 and FHs - vB > 0 and FHs - vC > 0):
        heronFormula = math.sqrt(FHs * (FHs - vA) * (FHs - vB) * (FHs - vC))
        print('Este é um triangulo e sua área é %.2f.' % (float(heronFormula)))
    else:
        print ('Este não é um triangulo.')