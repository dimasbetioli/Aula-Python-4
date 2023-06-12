import random

# Função para gerar uma matriz não singular de dimensão (n x n)
def gerar_matriz_nao_singular(n):
    # Gera uma matriz vazia
    matriz = [[0] * n for _ in range(n)]
    
    # Preenche a matriz com valores aleatórios
    for i in range(n):
        for j in range(n):
            matriz[i][j] = random.randint(1, 10)  # Valores aleatórios entre 1 e 10
    
    return matriz

# Função para gerar um vetor de termos independentes de dimensão (n x 1)
def gerar_vetor_termos_independentes(n):
    # Gera um vetor vazio
    vetor = [0] * n
    
    # Preenche o vetor com valores aleatórios
    for i in range(n):
        vetor[i] = random.randint(1, 10)  # Valores aleatórios entre 1 e 10
    
    return vetor

# Função para resolver o sistema de equações lineares Ax = b
def resolver_sistema(matriz, vetor):
    # Verifica se a matriz é quadrada
    n = len(matriz)
    if len(vetor) != n:
        raise ValueError("A matriz e o vetor devem ter o mesmo número de linhas")
    
    # Verifica se a matriz é não singular
    for i in range(n):
        if matriz[i][i] == 0:
            raise ValueError("A matriz é singular")
    
    # Implementa o método de eliminação de Gauss
    for i in range(n):
        pivo = matriz[i][i]
        
        # Divide a linha pelo pivô
        for j in range(n):
            matriz[i][j] /= pivo
        vetor[i] /= pivo
        
        # Elimina as outras linhas
        for k in range(i+1, n):
            fator = matriz[k][i]
            for j in range(i, n):
                matriz[k][j] -= fator * matriz[i][j]
            vetor[k] -= fator * vetor[i]
    
    # Implementa o método de retrosubstituição
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = vetor[i]
        for j in range(i+1, n):
            x[i] -= matriz[i][j] * x[j]
    
    return x

# Dimensão do sistema de equações
n = int(input("Digite a dimensão do sistema: "))

# Gera a matriz não singular e o vetor de termos independentes
A = gerar_matriz_nao_singular(n)
b = gerar_vetor_termos_independentes(n)

# Imprime a matriz e o vetor
print("Matriz A:")
for linha in A:
    print(linha)
print("\nVetor b:")
print(b)

# Resolve o sistema de equações
x = resolver_sistema(A, b)

# Imprime a solução
print("\nSolução x:")
print(x)
