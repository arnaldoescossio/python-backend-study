# ❌ Anti-pattern (Java-style)
users = ["Ana", "Carlos", "Maria"]
for i in range(len(users)):
    print(users[i])

# ✅ Pythonic
for user in users:
    print(user)

# 📌 Regra:
# Use índice só quando realmente precisar

# 1. Iterando sobre uma lista
frutas = ["maçã", "banana", "cereja"]

for fruta in frutas:
    print(fruta)

# 2. Iterando sobre uma string
mensagem = "Olá, Mundo!"    
for caractere in mensagem:
    print(caractere)

# 3. Iterando sobre um dicionário
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
for chave in pessoa:
    print(f"{chave}: {pessoa[chave]}")  

# 4. Usando a função range()
for numero in range(5):
    print(numero)

# 5. Iterando sobre uma lista com índice usando enumerate()
cores = ["vermelho", "verde", "azul"]
for indice, cor in enumerate(cores):
    print(f"{indice}: {cor}")   

# 6. Iterando sobre duas listas simultaneamente usando zip()
nomes = ["Ana", "Bruno", "Carla"]
idades = [25, 30, 22]   
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos.")

# 7. Iterando sobre um dicionário com itens()
produto = {"nome": "Notebook", "preço": 2500.0, "estoque": 10}
for chave, valor in produto.items():
    print(f"{chave}: {valor}")

# 8. Iterando sobre uma lista com condição
numeros = [1, 2, 3, 4, 5, 6]
for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} é par")

# 🧠 Regra:
# continue → pular dado inválido
# break → encerra loop quando condição for satisfeita
for numero in numeros:
    if numero % 2 != 0:
        continue  # Pula números ímpares
    if numero > 4:
        break  # Encerra o loop quando encontrar um número par maior que 4
    print(f"{numero} é par e menor ou igual a 4")

# 9. Iterando sobre uma lista aninhada
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for linha in matriz:
    for elemento in linha:
        print(elemento)
