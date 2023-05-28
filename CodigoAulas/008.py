# > Oitavo Código

"""
  Estrutura de Arrays

  -Array
"""

#Criar Array Vazia

Array = []
Array = list()

#As Arrays no pyton não tem seleção de tipos de variáveis

Array = [1, 1.4, "Olá mundo!"]

#Imprimindo Array

for i in range(0,3):
  print(Array[i])

#Acessando os ultimos elementos da Array | Utilizamos os números negativos

for i in range(-3,0):
  print(Array[i])

print(Array[-1])
print(Array[-2])
print(Array[-3])

#Acessando os indicies de [x:n](x até n) | Note que é o indicie menor que n | Ou podemos não definir um fim, ele irá até o fim da Array [2:] | Ou podemos definir quantas casas queremos pular [0:9:3]

print(Array[0:3])

#Para saber o tamanho da Array utilizamos 'len(array)'

print('Tamanho da lista:', len(Array))