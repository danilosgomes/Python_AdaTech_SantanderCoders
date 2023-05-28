# > Sexto Código

"""
  Laços e Repetição - While

  - enquanto uma condição estja sendo satisfeita, o laço continua

"""

##Joguinho com WHILE

num_sorteado = 15
num_escolhido = int(input('Digite um número:'))

while(num_escolhido != num_sorteado):
    num_escolhido = int(input('Digite novamente:'))
    

if(num_escolhido == num_sorteado):
    print('Para Bens!')

"""
  Perceba que não possui chaves nos laços, logo caso queria acrescentar coisas ao laço, coloque na coluna dentro da repetição e a linha abaixo.
"""   