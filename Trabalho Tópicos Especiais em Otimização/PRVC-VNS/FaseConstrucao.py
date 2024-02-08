import math
import numpy as np

#Para classificar com base na demanda do nó (a demanda é fornecida pela segunda coluna do array demand, ou seja, a coluna 1).
def obterChave1(item):
    return item[1]

def obterChave2(item):
    return item[2]
    
    
def coeficienteEconomia(dm, dimensao, demanda, capacidade):
      # Função para calcular o coeficiente de economia para cada possível conexão entre dois nós de demanda.

    # Inicializa uma matriz de zeros para armazenar as economias, onde cada linha representa uma possível conexão e as colunas são: [nó_i, nó_j, economia]
    coefEconomia = np.zeros((math.floor(((dimensao-2)*(dimensao-1))/2), 3), dtype=np.int)
    z = 0  # Inicializa o índice para percorrer a matriz de economias

    # Loop aninhado para percorrer todos os pares de nós de demanda possíveis
    for i in range(0, dimensao):
        for j in range(0, dimensao):
            # Verifica se i é diferente de j, j não é 0 e a soma das demandas de i e j é menor ou igual à capacidade
            if i > j and j != 0 and (demanda[i][1] + demanda[j][1] <= capacidade):
                # Armazena as informações da economia na matriz
                coefEconomia[z][0] = i
                coefEconomia[z][1] = j
                coefEconomia[z][2] = dm[i][0] + dm[j][0] - dm[i][j]
                z = z + 1  # Atualiza o índice para a próxima linha da matriz

    end1 = False
    j = 0

    # Loop para remover linhas irrelevantes da matriz de economias
    while not end1:
        if (coefEconomia[j][0] == 0) and (coefEconomia[j][1] == 0) and (coefEconomia[j][2] == 0):
            coefEconomia = np.delete(coefEconomia, (j), axis=0)
            j = 0  # Reinicia o índice após a remoção
        else:
            j = j + 1

        # Verifica se o índice alcançou o final da matriz
        if j == len(coefEconomia):
            end1 = True

    # Ordena a matriz de economias com base em uma função de comparação personalizada (obter_chave_2)
    coefEconomia = sorted(coefEconomia, key=obterChave2, reverse=True)

    # Retorna a matriz de economias ordenada
    return coefEconomia
    
# Função para calcular o custo de uma rota específica dentro de uma solução.
def custoRota(rota, dm):
       # Inicializa a variável de custo.
    custo = 0
    # Itera sobre os índices da rota, exceto o último elemento.
    for j in range(0, len(rota) - 1):
        # Verifica se o nó atual é maior que o próximo nó na rota.
        if rota[j] > rota[j + 1]:
            # Se sim, adiciona à soma o valor da distância entre os nós na matriz de distâncias.
            custo += dm[rota[j] - 1][rota[j + 1] - 1]
        else:
            # Se não, adiciona à soma o valor da distância entre os nós na matriz de distâncias.
            custo += dm[rota[j + 1] - 1][rota[j] - 1]
            
    # Retorna o custo total da rota.
    return custo


# Retorna o custo total da solução, que é a soma dos custos de cada rota.
def custoTotal(rotas, dm):
    custo = 0
    # Calcula o custo total como a soma dos custos de cada rota.
    for i in range(0, len(rotas)):
        custo += custoRota(rotas[i], dm)
    return custo

  
# Função para calcular a demanda total de uma rota.
def demandaRota(rota, demanda):
    # Inicializa a variável de demanda total da rota.
    demanda_rota = 0
    # Itera sobre os índices da rota.
    for i in range(0, len(rota)):
        # Adiciona à demanda total o valor da demanda do nó na matriz de demanda.
        demanda_rota += demanda[rota[i] - 1][1]
    # Retorna a demanda total da rota.
    return demanda_rota
    
    

        
    