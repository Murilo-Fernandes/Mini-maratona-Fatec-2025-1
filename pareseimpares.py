# Lê a quantidade de números que serão inseridos
qntd = int(input())

# Inicializa as listas para armazenar os números, pares e ímpares
numeros = []
pares = []
impares = []

# Variáveis auxiliares para controle
i = 0

# Loop para ler os números e separá-los em pares e ímpares
while i < qntd:
    acumula = 0
    acumula = int(input())
    # Adiciona o número à lista de números
    numeros.append(acumula)
    # Verifica se o número é par e adicionar na lista
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    else:
        # Adiciona o número à lista de ímpares
        impares.append(numeros[i])
    i += 1

# Ordena a lista de pares em ordem crescente
pares.sort()
# Ordena a lista de ímpares em ordem decrescente
impares.sort(reverse=True)

# Imprime os números pares ordenados
for num in pares:
    print(num)

# Imprime os números ímpares ordenados
for num in impares:
    print(num)