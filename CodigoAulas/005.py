# > Quinto Código

"""
  Controle de fluxo com condicionais
  if, elif e else

  com os simbolos de comparação:
  - == igual
  - != diferente
  - > maiorq
  - < menorq
  - >= maior igualq
  - <= menor igualq
  - | ou or OU
  - & ou and E
"""

num1 = int(input())
num2 = int(input())

if (num1 + num2) > 5:
    print('Número maior que 5')
elif (num1 + num2) == 5:
    print('Número igual a 5')
else:
    print('Número menor que 5')