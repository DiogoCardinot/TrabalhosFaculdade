import FaseConstrucao as construcao
import numpy as np
import random
import copy


def realocacaoInterna(rotas, melhor, aleatorio, dm, demanda, capacidade):
    if aleatorio:
        nova = copy.deepcopy(rotas)
        ePossivel = False
        contagem = 0
        while not ePossivel and contagem < 100:
            u = random.randint(0, len(nova) - 1)
            v = random.randint(0, len(nova) - 1)
            
            while u == v:
                u = random.randint(0, len(nova) - 1)
                v = random.randint(0, len(nova) - 1)
            
            if len(nova[u]) - 2 == 1:
                aleatorio = 1
            else:
                aleatorio = random.randint(1, len(nova[u]) - 2)
            
            contagem += 1
            
            if construcao.demandaRota(nova[v], demanda) + demanda[nova[u][aleatorio] - 1][1] <= capacidade:
                ePossivel = True
                
                if len(nova[v]) - 2 == 1:
                    aleatorioPara = 1
                else:
                    aleatorioPara = random.randint(1, len(nova[v]) - 2)
                
                nova[v] = np.insert(nova[v], aleatorioPara, nova[u][aleatorio])
                nova[u] = np.delete(nova[u], aleatorio)

        if ePossivel:
            nova = [x for x in nova if len(x) > 2]
            return nova
        else:
            return rotas
    else:
        if melhor:
            melhorRealo = copy.deepcopy(rotas)
            for i in range(len(rotas)):
                for j in range(len(rotas)):
                    if i != j:
                        for k in range(1, len(rotas[i]) - 1):
                            if construcao.demandaRota(rotas[j], demanda) + demanda[rotas[i][k] - 1][1] <= capacidade:
                                for m in range(1, len(rotas[j])):
                                    nova = copy.deepcopy(rotas)
                                    nova[j] = np.insert(nova[j], m, nova[i][k])
                                    nova[i] = np.delete(nova[i], k)

                                    if construcao.custoTotal(nova, dm) < construcao.custoTotal(melhorRealo, dm):
                                        melhorRealo = copy.deepcopy(nova)
            return melhorRealo
        else:
            for i in range(len(rotas)):
                for j in range(len(rotas)):
                    if i != j:
                        for k in range(1, len(rotas[i]) - 1):
                            if construcao.demandaRota(rotas[j], demanda) + demanda[rotas[i][k] - 1][1] <= capacidade:
                                for m in range(1, len(rotas[j])):
                                    nova = copy.deepcopy(rotas)
                                    nova[j] = np.insert(nova[j], m, nova[i][k])
                                    nova[i] = np.delete(nova[i], k)

                                    if construcao.custoTotal(nova, dm) < construcao.custoTotal(rotas, dm):
                                        return nova
            return rotas
  
