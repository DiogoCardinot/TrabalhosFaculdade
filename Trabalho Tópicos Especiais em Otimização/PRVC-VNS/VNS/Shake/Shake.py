import random
import copy
from BuscaLocal.VizinhancasVND.VizInterSwap import swapInter
from BuscaLocal.VizinhancasVND.VizInterrealocacao import realocacaoInterna

def Shake(kmax, rotas, dm, demanda, capacidade):
    # Cria uma cópia profunda das rotas iniciais para aplicar a operação de Shake
    shaked = copy.deepcopy(rotas)

    # Loop para realizar o Shake até o número máximo de iterações (kmax)
    for i in range(kmax):
        # Gera um número aleatório entre 1 e 2 para escolher a operação de Shake
        j = random.randint(1, 2)

        if j == 1:
            # Aplica a operação de Inter-Swap (troca de elementos entre duas rotas)
            # print("isw")
            shaked = swapInter(shaked, False, True, dm, demanda, capacidade)
        elif j == 2:
            # Aplica a operação de Inter-Relocate (mudança de localização entre duas rotas)
            # print("ir")
            shaked = realocacaoInterna(shaked, False, True, dm, demanda, capacidade)

    # Retorna as rotas resultantes da aplicação do Shake
    return shaked