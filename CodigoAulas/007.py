# > Sétimo Código

"""
  Laços e Repetição - For

  - enquanto uma condição estja sendo satisfeita, o laço continua

"""
 # 0,1,2,3,4,5,6,7,8,9
for i in range(10):
    print(i)
# 1,2,3,4,5,6,7,8,9
for i in range(1, 10):
    print(i)
# 0,3,6,9
for i in range(0, 12, 3):
    print(i)

"""
  Implementando variáveis dentro de uma string

  input(f"Digita a nota {i})

  Acrescentamos o 'f' no incio da string e usamos '{}' para acrescentar a variável
"""
total = 0.0

for i in range (1,4):
    nota = float(input(f"Digite a nota {i}:"))
    total += nota

print('Média =', total/3)