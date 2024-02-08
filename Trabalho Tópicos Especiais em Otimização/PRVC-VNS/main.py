import TratamentoInstancias as pf
import FaseConstrucao as construcao
import numpy as np
from SolucaoInicial.MetodoGuloso import guloso
from VNS.vns import VNS
import time

# Lista com as instâncias disponíveis
# instancias = ["A-n32-k5", "A-n33-k6", "A-n37-k6", "A-n44-k6", "A-n53-k7", "A-n61-k9", "A-n69-k9","A-n80-k10"]
# instancias = ["B-n31-k5", "B-n39-k5", "B-n41-k6","B-n45-k5", "B-n50-k7", "B-n57-k9", "B-n63-k10", "B-n78-k10"]
# instancias = ["E-n22-k4","E-n30-k3", "E-n51-k5", "E-n76-k10", "E-n101-k14"]
# instancias = ["F-n72-k4"]
instancias = ["P-n16-k8", "P-n45-k5", "P-n70-k10", "P-n101-k4"]

# Exibe o menu de opções para escolha da instância
print("Escolha uma instância")
for x in range(0, len(instancias)):
    print(x + 1, "-", instancias[x])

# Lê a escolha do usuário
instanciaEscolhida = input()

# Determina o tipo de instância (explícita ou 2D)
if (instanciaEscolhida == "eil13") or (instanciaEscolhida == "eil31") or (instanciaEscolhida == "eil7"):
    Type = "expl"
else:
    Type = "2d"

# Obtém informações sobre a instância escolhida
melhorValor = pf.dadosInstancia(instanciaEscolhida)
capacidade = pf.capacidadeVeiculo(instanciaEscolhida)
demanda = pf.demandaNo(instanciaEscolhida)
dimensao = len(demanda)

# Exibe informações sobre a instância
print("Capacidade:", capacidade)
print("Demanda:")
print(demanda)
print("Matriz de distância:")
matrizDistancia = pf.matrizDistancia(instanciaEscolhida, dimensao)
print()
print("Ótimo:  ", melhorValor)

# Aplica o algoritmo guloso para a construção da solução inicial
solucaoInicial = guloso(capacidade, matrizDistancia, demanda, dimensao)
custoSolucaoInicial = construcao.custoTotal(solucaoInicial, matrizDistancia)

soma = 0
print("Defina o limite de tempo para a execução do algoritmo (s)")
timer = int(input())

# Crie um vetor para armazenar os custos
vetor_custos = []


# Executa o VNS (Variable Neighborhood Search) para otimizar a solução inicial construída pelo guloso
for i in range(0, 10):
    tempoComeco = time.time()
    novaSolucao = VNS(solucaoInicial, timer, custoSolucaoInicial, matrizDistancia, demanda, capacidade, 10)
    
    # Exibe as rotas e suas informações otimizadas
    for x in novaSolucao:
        print(x - np.ones((len(x),), dtype=int), " custo:", construcao.custoRota(x, matrizDistancia), ", demanda:", construcao.demandaRota(x, demanda))
    
    custoNovaSolucao = construcao.custoTotal(novaSolucao, matrizDistancia)
    
    # Adiciona o custo ao vetor
    vetor_custos.append(custoNovaSolucao)
    
    print(custoNovaSolucao, len(novaSolucao))
    print()
    tempoFinal = time.time()
    timer = tempoFinal- tempoComeco
    print("Timer:", timer)

# Exibe o vetor de custos
print("Vetor de Custos:", vetor_custos)

# Calcula a soma dos custos
soma = sum(vetor_custos)
print("Soma dos Custos:", soma)
print("Menor Custo:", min(vetor_custos))
print("Maior Custo:", max(vetor_custos))

# Calcula a média dos custos das soluções otimizadas
print("Media: ", soma / 10)
print()
