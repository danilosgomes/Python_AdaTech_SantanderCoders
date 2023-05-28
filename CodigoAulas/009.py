# >  Nono Código

"""
  Métodos e Funções com Array

  -Veremos
"""

#append | Adiciona ao final da Array

Array = [4,7,2,32]

print(Array)

Array.append(4)

print(Array)

#insert | Adiciona um elemento ao incie indicado (indicie, elemento) | (2,10)

Array.insert(2,10)

print(Array)

#extend |Junta dois arrays, colocando a Array adicionada ao final da Array principal

Array2 = [3,5,7,9]

print(Array2)

Array.extend(Array2)

print(Array)

#pop | Remove elementos, caso não definido o elmento, o ultimo elemento é eliminado | Definimos com 'pop(x)'

Array2.pop()

print(Array2)

Array2.pop(2)

#remove | Procura um elemneto que seja igual ao elemento definido e elimina | No caso o primeiro elemento que ele encontrar

Array.remove(10)

print(Array)

#count | Conta quantas vezes aquele elemento aparece no Array

Array.append(12)
print(Array)
Array.append(12)
print(Array)

print(Array.count(12))

#index | Informa o indicie de determinado elemento dentro do Array | O primeiiro elemento que ele encontrar

print(Array.index(12))

#sort | Ordena o Array, quando usado apenas 'sort()', ordena em ordem crescente, caso utilizado o 'reverse==True' ordena em ordem decrescente.

Array.sort()
print(Array)

Array.sort(reverse=True)
print(Array)

"""
  Funções em Arrays
"""

#len | O tamanho da Array

print(len(Array))

#sum | A soma dos elementos da Array

print(sum(Array2))

#max |O maior valor do Array

print(max(Array))

#min | O menor valor do Array

print(min(Array2))
