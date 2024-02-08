import FaseConstrucao as construcao
import numpy as np
import random
import copy

def swapInter(rotas, melhor, aleatorio, dm, demanda, capacidade):
    # Verifica se a opção aleatorio está ativada para aplicar uma versão aleatória do VizInterSwap
    if aleatorio:
        ePossivel = False
        nova = copy.deepcopy(rotas)
        contagem = 0
        # Loop para tentar realizar o VizInterSwap aleatório até ser possível ou até 100 tentativas
        while not ePossivel and contagem < 100:
            ePossivel = True
            c = random.sample(range(len(nova)), 2)
            b = random.randint(1, len(nova[c[0]]) - 2)
            a = random.randint(1, len(nova[c[1]]) - 2)
            nova[c[0]][b], nova[c[1]][a] = nova[c[1]][a], nova[c[0]][b]
            # Verifica se a demanda de cada rota após o VizInterSwap é menor ou igual à capacidade
            for rota in nova:
                if construcao.demandaRota(rota, demanda) > capacidade:
                    ePossivel = False
                    nova = copy.deepcopy(rotas)
            contagem += 1
        # Se o VizInterSwap aleatório for possível, retorna a nova configuração; caso contrário, retorna a configuração original
        if ePossivel:
            # for x in nova: print(x)
            return nova
        else:
            return rotas
    else:
        # Verifica se a opção melhor está ativada para aplicar a versão determinística do VizInterSwap
        if melhor:
            melhorVizInterSwap = copy.deepcopy(rotas)
            # Loop duplo para iterar sobre todas as combinações possíveis de rotas i e j
            for i in range(len(rotas)):
                for j in range(len(rotas)):
                    if i != j:
                        # Loop duplo para iterar sobre todos os pares de clientes k e m nas rotas i e j, respectivamente
                        for k in range(1, len(rotas[i]) - 1):
                            for m in range(1, len(rotas[j]) - 1):
                                ePossivel = True
                                nova = copy.deepcopy(rotas)
                                nova[i][k], nova[j][m] = nova[j][m], nova[i][k]
                                # Verifica se a demanda de cada rota após o VizInterSwap é menor ou igual à capacidade
                                for rota in nova:
                                    if construcao.demandaRota(rota, demanda) > capacidade:
                                        ePossivel = False
                                # Verifica se o custo total após o VizInterSwap é menor do que antes
                                if ePossivel and construcao.custoTotal(rotas, dm) > construcao.custoTotal(nova, dm):
                                    melhorVizInterSwap = copy.deepcopy(nova)
            return melhorVizInterSwap
        else:
            # Loop duplo para iterar sobre todas as combinações possíveis de rotas i e j
            for i in range(len(rotas)):
                for j in range(len(rotas)):
                    if i != j:
                        # Loop duplo para iterar sobre todos os pares de clientes k e m nas rotas i e j, respectivamente
                        for k in range(1, len(rotas[i]) - 1):
                            for m in range(1, len(rotas[j]) - 1):
                                ePossivel = True
                                nova = copy.deepcopy(rotas)
                                nova[i][k], nova[j][m] = nova[j][m], nova[i][k]
                                # Verifica se a demanda de cada rota após o VizInterSwap é menor ou igual à capacidade
                                for rota in nova:
                                    if construcao.demandaRota(rota, demanda) > capacidade:
                                        ePossivel = False
                                # Verifica se o custo total após o VizInterSwap é menor do que antes
                                if ePossivel and construcao.custoTotal(rotas, dm) > construcao.custoTotal(nova, dm):
                                    # Retorna a nova configuração se encontrou uma melhoria
                                    return nova
            # Retorna a configuração original se nenhuma melhoria foi encontrada
            return rotas
