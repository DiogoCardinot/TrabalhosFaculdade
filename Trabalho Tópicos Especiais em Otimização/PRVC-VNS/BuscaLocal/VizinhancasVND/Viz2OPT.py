import FaseConstrucao as construcao
import numpy as np
import random
import copy

def twoOpt(dados, melhor, aleatorio, dm):
    # Verifica se a opção aleatorio está ativada para aplicar uma versão aleatória do two-opt
    if aleatorio:
        # Verifica se há pelo menos 4 elementos na lista para realizar a operação
        if len(dados) <= 3:
            return dados
        # Gera índices aleatórios i e j para a aplicação da operação two-opt
        i = random.randint(1, len(dados) - 3)
        j = random.randint(i + 2, len(dados) - 1)
        # Garante que i e j não sejam adjacentes
        while abs(i - j) == len(dados) - 2:
            i = random.randint(1, len(dados) - 3)
            j = random.randint(i + 2, len(dados) - 1)
        meio = dados[i:j]
        novo = np.append(dados[0:i], np.append(meio[::-1], dados[j:len(dados)]))
        return novo
    else:
        # Verifica se a opção melhor está ativada para aplicar a versão determinística do two-opt
        if melhor:
            # Verifica se há pelo menos 4 elementos na lista para realizar a operação
            if len(dados) <= 3:
                return dados
            melhor2opt = dados
            # Loop duplo para iterar sobre todas as combinações possíveis de i e j
            for i in range(1, len(dados)):
                for j in range(i + 2, len(dados)):
                    # Garante que i e j não sejam adjacentes
                    if dados[i - 1] != dados[j]:
                        meio = dados[i:j]
                        novo = np.append(dados[0:i], np.append(meio[::-1], dados[j:len(dados)]))
                        # Verifica se a nova configuração tem um custo menor
                        if construcao.custoRota(novo, dm) < construcao.custoRota(dados, dm):
                            melhor2opt = copy.deepcopy(novo)
            return melhor2opt
        else:
            # Verifica se há pelo menos 4 elementos na lista para realizar a operação
            if len(dados) <= 3:
                return dados
            # Loop duplo para iterar sobre todas as combinações possíveis de i e j
            for i in range(1, len(dados)):
                for j in range(i + 2, len(dados)):
                    # Garante que i e j não sejam adjacentes
                    if dados[i - 1] != dados[j]:
                        meio = dados[i:j]
                        novo = np.append(dados[0:i], np.append(meio[::-1], dados[j:len(dados)]))
                        # Verifica se a nova configuração tem um custo menor
                        if construcao.custoRota(novo, dm) < construcao.custoRota(dados, dm):
                            return novo
            return dados

def aleatorioTwoOpt(dados):
    # Versão aleatória do two-opt
    if len(dados) <= 3:
        return dados
    i = random.randint(1, len(dados) - 3)
    j = random.randint(i + 2, len(dados) - 1)
    # Garante que i e j não sejam adjacentes
    while abs(i - j) == len(dados) - 2:
        i = random.randint(1, len(dados) - 3)
        j = random.randint(i + 2, len(dados) - 1)
    meio = dados[i:j]
    novo = np.append(dados[0:i], np.append(meio[::-1], dados[j:len(dados)]))
    return novo


