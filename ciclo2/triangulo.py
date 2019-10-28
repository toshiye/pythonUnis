import math

vA = float(input('Digite o primeiro valor: '))

vB = float(input('Digite o segundo valor: '))

vC = float(input('Digite o terceiro valor: '))

triangulo = ''

if (vB - vC < vA < vB + vC or vA - vC < vB < vA + vC or vA - vB < vC < vA + vB) :
    FHs = (vA + vB + vC) / 2
    heron = math.sqrt(FHs(FHs - vA) * (FHs - vB) * (FHs - vC))
    triangulo = 'Este é um triangulo e sua área é %f.' %(str(float(heron)))
    """triangulo = (vC * altura) / 2"""
else
    triangulo = 'Este não é um triangulo.'