import FaseConstrucao as construcao
import copy
from BuscaLocal.VND.vnd import VND  # Adjust the import statement accordingly
from VNS.Shake.Shake import Shake
import time

def VNS(rotas, duracao, custo, dm, demanda, capacidade, kmax):
    # Registra o tempo de início do algoritmo
    inicio = time.time()
    # Inicializa a variável de custo inicial
    custo_inicial = custo
    # Realiza uma cópia profunda das rotas iniciais
    roteamento = copy.deepcopy(rotas)
    # Aplica a Busca por Vizinhança Variável (VND) nas rotas iniciais
    novas_rotas = VND(roteamento, custo, dm, demanda, capacidade)
    i = 1  # Inicializa o contador de iterações

    # Loop principal do algoritmo VNS
    while time.time() < inicio + duracao:
        # Aplica a operação de Shake para diversificar as soluções
        agitado = Shake(i % kmax, novas_rotas, dm, demanda, capacidade)

        # Aplica a VND nas soluções obtidas após o Shake
        otimo_agitado = VND(agitado, custo, dm, demanda, capacidade)
        # Calcula o custo da solução obtida após o Shake e VND
        custo_novo = construcao.custoTotal(otimo_agitado, dm)

        # Verifica se a nova solução é melhor que a atual
        if custo_novo < custo_inicial:
            custo_inicial = custo_novo
            novas_rotas = copy.deepcopy(otimo_agitado)
            i = 1  # Reinicia o contador, pois houve melhoria
        else:
            i = i + 1  # Incrementa o contador se não houve melhoria

    # Retorna as rotas finais obtidas pelo VNS
    return novas_rotas
