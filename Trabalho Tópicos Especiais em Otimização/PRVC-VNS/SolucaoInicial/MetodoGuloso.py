import numpy as np
import FaseConstrucao as construcao


def proximoNo(disponiveis, capacidade, dm, demanda, atual):
    # Inicializa variáveis para armazenar a distância mínima e o próximo nó.
    minimo = float('inf')
    proximo_no = -1
    
    # Itera sobre os nós disponíveis para encontrar o mais próximo que pode ser atendido.
    for i in disponiveis:
        # Verifica se a demanda do nó é menor ou igual à capacidade do veículo e se a soma das distâncias até o nó e a partir do nó é menor que a distância mínima atual.
        if demanda[i - 1][1] <= capacidade and dm[i - 1][atual - 1] + dm[atual - 1][i - 1] < minimo:
            # Atualiza a distância mínima e o próximo nó.
            minimo = max(dm[i - 1][atual - 1], dm[atual - 1][i - 1])
            proximo_no = i
    
    # Retorna o próximo nó mais próximo que pode ser atendido.
    return proximo_no

# Função que constrói uma rota com os nós disponíveis.
# Retorna uma rota (lista de nós) construída de acordo com a lógica gulosa.
def construirRota(disponiveis, capacidade, dm, demanda):
    # Inicializa variáveis para o nó inicial, a rota, a capacidade atual e o próximo nó.
    atual = 1
    rota = [1]
    capacidade_atual = capacidade
    proximo_no = proximoNo(disponiveis, capacidade_atual, dm, demanda, atual)
    
    # Enquanto houver um próximo nó disponível na rota, continue construindo a rota.
    while proximo_no != -1:
        # Adiciona o próximo nó à rota.
        rota.append(proximo_no)
        # Atualiza o nó atual e a capacidade do veículo.
        atual = proximo_no
        capacidade_atual -= demanda[proximo_no - 1][1]
        
        # Remove o nó da lista de nós disponíveis.
        for i in disponiveis:
            if i == proximo_no:
                disponiveis.remove(i)
        
        # Encontra o próximo nó disponível mais próximo.
        proximo_no = proximoNo(disponiveis, capacidade_atual, dm, demanda, atual)
    
    # Adiciona novamente o nó inicial ao final da rota.
    rota.append(1)
    # Converte a rota para um array numpy.
    rota = np.asarray(rota)
    
    # Retorna a rota construída.
    return rota


# Função que implementa o método guloso para a construção de uma solução inicial.
def guloso(capacidade, dm, demanda, dimensao):
    # Inicializa uma lista para armazenar as rotas construídas.
    rotas = []
    # Inicializa uma lista de nós disponíveis, excluindo o nó inicial (depósito).
    disponiveis = list(range(2, dimensao + 1))
    
    # Enquanto houver nós disponíveis, continue construindo rotas.
    while len(disponiveis) > 0:
        # Chama a função construirRota para construir uma rota com os nós disponíveis.
        rota = construirRota(disponiveis, capacidade, dm, demanda)
        # Adiciona a rota à lista de rotas.
        rotas.append(rota)
    
    # Exibe informações sobre a solução gulosa.
    print("SOLUÇÃO GULOSA")
    print("Número de veículos: ", len(rotas))
    for x in rotas:
        print(x, " custo:", construcao.custoRota(x, dm), ", demanda:", construcao.demandaRota(x, demanda))
    print("Custo total: ", construcao.custoTotal(rotas, dm))
    print()
    
    # Retorna a lista de rotas construídas.
    return rotas
