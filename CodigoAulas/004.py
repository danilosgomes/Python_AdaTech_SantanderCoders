# > Quarto Código

"""
  Conversao de tipos 
  - Solução do 'Terceiro Código'
  - Todas as variáveis recebem 'str' automaticamente
  - para mudar isso utilizamos o tipo da variável e a variável desejada ex:

  num = int(input())
  num = float(input())

"""
num_ss = '25'

print(num_ss, type(num_ss))

num_int = int(num_ss)

print(num_int, type(num_int))

"""
  Solução para o 'Terceiro Código'

  num1 = input('Digite o primeiro número:')
  num2 = input('Digite o segundo número:')

  ------------------------------------------

  Neste caso, devemos definir o tipo antes do input e fechar com '()'

  num1 = int(input('Digite o primeiro número:'))
  num2 = int(input('Digite o segundo número:'))

"""