
from BuscaLocal.VizinhancasVND.Viz2OPT import twoOpt
from BuscaLocal.VizinhancasVND.VizInterrealocacao import realocacaoInterna
from BuscaLocal.VizinhancasVND.VizInterSwap import swapInter
import FaseConstrucao as construcao
import copy

def VND(rotas, custo, dm, demanda, capacidade):
    # Inicializa uma variável para indicar se houve melhoria
    melhoria = True
    # Cria uma cópia profunda das rotas iniciais
    rotas_atuais = copy.deepcopy(rotas)

    # Loop principal para execução da Busca por Vizinhança Variável (VND)
    while melhoria:
        t = 0  # Inicializa um contador para verificar melhorias em cada vizinhança

        # Itera sobre todas as rotas existentes
        for i in range(len(rotas_atuais)):
            # Aplica a operação de two-opt (invertendo dois arcos da rota)
            nova_rota = twoOpt(rotas_atuais[i], False, False, dm)

            # Verifica se a rota resultante da aplicação do two-opt possui custo menor
            if construcao.custoRota(rotas_atuais[i], dm) > construcao.custoRota(nova_rota, dm):
                rotas_atuais[i] = copy.deepcopy(nova_rota)  # Atualiza a rota para a nova rota encontrada
                t = t + 1  # Incrementa o contador de melhorias
                #print("2opt")
                break

        # Verifica se houve alguma melhoria aplicando two-opt
        if t > 0:
            continue

        # Aplica a operação de Inter-Relocate (mudança de localização entre duas rotas)
        nova_rota_interna = realocacaoInterna(rotas_atuais, False, False, dm, demanda, capacidade)
        # Verifica se a rota resultante da aplicação do Inter-Relocate possui custo menor
        if construcao.custoTotal(rotas_atuais, dm) > construcao.custoTotal(nova_rota_interna, dm):
            rotas_atuais = copy.deepcopy(nova_rota_interna)  # Atualiza as rotas para as novas rotas encontradas
            #print("VizInterrealocacao")
            continue

        # Aplica a operação de Inter-Swap (troca de elementos entre duas rotas)
        nova_rota_swap = swapInter(rotas_atuais, False, False, dm, demanda, capacidade)
        # Verifica se a rota resultante da aplicação do Inter-Swap possui custo menor
        if construcao.custoTotal(rotas_atuais, dm) > construcao.custoTotal(nova_rota_swap, dm):
            rotas_atuais = copy.deepcopy(nova_rota_swap)  # Atualiza as rotas para as novas rotas encontradas
            #print("VizInterSwap")
            continue

        # Se nenhuma melhoria foi encontrada, encerra o loop principal
        melhoria = False

    # Retorna as rotas resultantes da aplicação do VND
    return rotas_atuais
                
        
    
    
