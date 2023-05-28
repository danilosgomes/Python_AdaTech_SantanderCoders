# > Segundo Código

# '#' define um comentário
#  3 '""' (aspas duplas) define um comentário em multilinhas, ex:

"""
teste1
teste2
teste3
teste4

"""
variavel = 26 #Crição de variável

print(variavel)

#Tipos variáveis

inteiro = 23          #Variável int       
decimal = 1.0         #Variável float
string = 'Caracter'   #Variável str
boolean1 = True       #Variável bool | Escreve true com T maiúsculo
boolean2 = False      #Variável bool | Escreve false com F maiúsculo 

#Visualizar tipos variáveis

print(type(inteiro))   #<class 'int'>
print(type(decimal))  #<class 'float'>
print(type(string))    #<class 'str'>  
print(type(boolean1)) #<class 'bool'> 

#Solicitar dados e armazenar

num = input('Digite um número:')
print('Número digitado =', num)