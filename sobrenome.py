# Lê a quantidade de nomes que serão inseridos
qntd = int(input())

# Inicializa variáveis auxiliares
conta = 0  
vogais = {"a", "e", "i", "o", "u"}  
cont = 0  

# Loop para processar cada nome
while cont < qntd: 
    conta = 0  # Reseta o contador de consoantes consecutivas para cada nome
    nome = input("")  # Lê o nome do usuário
    nomeminusculo = nome.lower()  # Converte o nome para letras minúsculas
    
    # Itera sobre cada letra do nome
    for letra in nomeminusculo:
        if letra not in vogais:
            conta += 1  
            if conta == 3:
                break
        else:
            # Reseta o contador se encontrar uma vogal
            conta = 0
            
    # Verifica se o nome é "fácil" ou "não fácil" com base no número de consoantes consecutivas
    if conta >= 3:
        print(f"{nome.capitalize()} nao eh facil")  # Nome não é fácil
    else:
        print(f"{nome.capitalize()} eh facil")  # Nome é fácil
    
    cont += 1  

