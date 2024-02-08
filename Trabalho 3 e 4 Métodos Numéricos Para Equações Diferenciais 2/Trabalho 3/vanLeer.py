import numpy as np
import matplotlib.pyplot as plt

def calculaConcentracao(comprimento, numeroVolumes, t_inicial, t_final, velocidade, alpha, ca, cb, cc):
    DeltaX = comprimento / numeroVolumes
    DeltaT = 0.9* DeltaX/ (velocidade)
    tempo = np.arange(t_inicial, t_final, DeltaT)
    espaco = np.arange(0, comprimento, DeltaX)
    Q = np.zeros(numeroVolumes)
    Q_final = np.zeros(numeroVolumes)

    # Condições iniciais
    for i in range(numeroVolumes):
        if espaco[i] <= comprimento / 2:
            Q[i] = ca
        else:
            Q[i] = cb

    for n in range(len(tempo)):
        Q_novo = np.copy(Q)  # Crie uma cópia de Q para atualizar os valores
        for i in range(1,numeroVolumes-1):
            if tempo[n] >= t_final / 2:
                Q_novo[0] = cc  # contorno inicial

            denominator_plus = Q[i + 1] - Q[i]
            denominator_minus = Q[i] - Q[i - 1]
            C = (velocidade*DeltaT)/DeltaX
            if denominator_plus == 0 or denominator_minus == 0:
                # Adicione uma verificação para evitar divisão por zero
                psi_IMaisMeio = 0.0
                psi_IMenosMeio = 0.0
            else:
                psi_IMaisMeio = (((Q[i] - Q[i - 1]) / denominator_plus) + abs((Q[i] - Q[i - 1]) / denominator_plus)) / (
                        1 + abs((Q[i] - Q[i - 1]) / denominator_plus))
                psi_IMenosMeio = ((Q[i - 1] - Q[i - 2]) / denominator_minus + abs(
                        (Q[i - 1] - Q[i - 2]) / denominator_minus)) / (1 + abs((Q[i - 1] - Q[i - 2]) / denominator_minus))

            if i == 0:  # FTBS
                q_n = Q[i] - (C * (Q[i] - (2 * ca - Q[i])))

            if i == 1:  # FTBS
                q_n = Q[i] - (C * (Q[i] - Q[i - 1]))
            elif i == numeroVolumes - 1:  # penúltimo nó, o i+1 vira i
                q_n = Q[i] - (C * (Q[i] - Q[i - 1]))
            else:  # demais nós interiores
                q_n = Q[i] - (C * (Q[i] - Q[i - 1])) - (C / 2) * (1 - C) * (
                        psi_IMaisMeio * (Q[i + 1] - Q[i]) - psi_IMenosMeio * (Q[i] - Q[i - 1]))

            Q_novo[i] = q_n

        Q = np.copy(Q_novo)  # Atualize Q com os novos valores
        Q_final = np.copy(Q_novo)

    return espaco, Q_final

def calculaConcentracaoFTBS(comprimento, numeroVolumes, t_inicial, t_final, velocidade, alpha, ca, cb, cc):
    DeltaX = comprimento / numeroVolumes
    DeltaT = 0.9*DeltaX/velocidade
    tempo = np.arange(t_inicial, t_final, DeltaT)
    espaco = np.arange(0, comprimento, DeltaX)
    Q = np.zeros(numeroVolumes)
    Q_final = np.zeros(numeroVolumes)

    # Condições iniciais
    for i in range(numeroVolumes):
        if espaco[i] <= comprimento / 2:
            Q[i] = ca
        else:
            Q[i] = cb

    for n in range(len(tempo)):
        Q_novo = np.copy(Q)  # Crie uma cópia de Q para atualizar os valores
        for i in range(numeroVolumes):
            if tempo[n] >= t_final / 2:
                Q_novo[0] = cc #contorno inicial
                # Q_novo[-1] = cc #contorno final
            C = velocidade*(DeltaT / DeltaX)
            if i == 0:
                q_n = Q[i] - (C * (Q[i] - (2 * ca - Q[i])))
            # elif i == numeroVolumes - 1:
            #     q_n = Q[i] - (DeltaT / DeltaX) * (
            #         velocidade * (Q[i] - Q[i - 1]) - alpha * (Q[i] - 2 * Q[i] + Q[i - 1]) / (DeltaX)
            #     )
            else:
                q_n = Q[i] - (C*((Q[i] - Q[i - 1]) ))

            Q_novo[i] = q_n

        Q = np.copy(Q_novo)  # Atualize Q com os novos valores
        Q_final = np.copy(Q_novo)

    return espaco, Q_final

def calculaConcentracaoSuperBee(comprimento, numeroVolumes, t_inicial, t_final, velocidade, alpha, ca, cb, cc):
    DeltaX = comprimento / numeroVolumes
    DeltaT = 0.1* DeltaX/ (velocidade)
    tempo = np.arange(t_inicial, t_final, DeltaT)
    espaco = np.arange(0, comprimento, DeltaX)
    Q = np.zeros(numeroVolumes)
    Q_final = np.zeros(numeroVolumes)

    # Condições iniciais
    for i in range(numeroVolumes):
        if espaco[i] <= comprimento / 2:
            Q[i] = ca
        else:
            Q[i] = cb

    for n in range(len(tempo)):
        Q_novo = np.copy(Q)  # Crie uma cópia de Q para atualizar os valores
        for i in range(1,numeroVolumes-1):
            if tempo[n] >= t_final / 2:
                Q_novo[0] = cc #contorno inicial

            denominator_plus = Q[i + 1] - Q[i]
            denominator_minus = Q[i] - Q[i - 1]
            C = (velocidade*DeltaT)/DeltaX
            if denominator_plus == 0 or denominator_minus == 0:
                # Adicione uma verificação para evitar divisão por zero
                psi_IMaisMeio = 0.0
                psi_IMenosMeio = 0.0
            else:
                psi_IMaisMeio = max(0 , min(1, 2*((Q[i]-Q[i-1])/(Q[i+1]-Q[i]))), min(2, ((Q[i]-Q[i-1])/(Q[i+1]-Q[i]))))
                psi_IMenosMeio = max(0, min(1, 2*((Q[i-1]-Q[i-2])/(Q[i]-Q[i-1]))), min(2, ((Q[i-1]-Q[i-2])/(Q[i]-Q[i-1]))))
            

            #O QUE FAZER NO psi_IMaisMeioFinal quando o denominador da 0?
            
            if i == 0: #FTBS
                q_n = Q[i] - (C  * (Q[i] - (2 * ca - Q[i])))
            elif i==1: #FTBS
                q_n = Q[i] - (C  * (Q[i] - Q[i-1]))
            elif(i == numeroVolumes - 1): #ultimo nó o i+1 vira i
                q_n = Q[i] - (C  * (Q[i] - Q[i-1]))
            else: #demais nós interiores
                q_n = Q[i] - (C  * (Q[i] - Q[i-1])) - (C/2)*(1-C)*(psi_IMaisMeio*(Q[i+1] - Q[i]) - psi_IMenosMeio*(Q[i]-Q[i-1]))

            Q_novo[i] = q_n

        Q = np.copy(Q_novo)  # Atualize Q com os novos valores
        Q_final = np.copy(Q_novo)

    return espaco, Q_final

def calculaConcentracaoHQUICK(comprimento, numeroVolumes, t_inicial, t_final, velocidade, alpha, ca, cb, cc):
    DeltaX = comprimento / numeroVolumes
    DeltaT = 0.9* DeltaX/ (velocidade)
    tempo = np.arange(t_inicial, t_final, DeltaT)
    espaco = np.arange(0, comprimento, DeltaX)
    Q = np.zeros(numeroVolumes)
    Q_final = np.zeros(numeroVolumes)

    # Condições iniciais
    for i in range(numeroVolumes):
        if espaco[i] <= comprimento / 2:
            Q[i] = ca
        else:
            Q[i] = cb

    for n in range(len(tempo)):
        Q_novo = np.copy(Q)  # Crie uma cópia de Q para atualizar os valores
        for i in range(1,numeroVolumes-1):
            if tempo[n] >= t_final / 2:
                Q_novo[0] = cc #contorno inicial

            C = (velocidade*DeltaT)/DeltaX

            denominator_plus = Q[i + 1] - Q[i]
            denominator_minus = Q[i] - Q[i - 1]
            C = (velocidade*DeltaT)/DeltaX
            if denominator_plus == 0 or denominator_minus == 0:
                # Adicione uma verificação para evitar divisão por zero
                psi_IMaisMeio = 0.0
                psi_IMenosMeio = 0.0
            else:
                psi_IMaisMeio = (2*((Q[i]-Q[i-1])/(Q[i+1]-Q[i]) + abs(((Q[i]-Q[i-1])/(Q[i+1]-Q[i])))) )/(3 + ((Q[i]-Q[i-1])/(Q[i+1]-Q[i])))
                psi_IMenosMeio = (2* ((Q[i-1]-Q[i-2])/(Q[i]-Q[i-1]) + abs((Q[i-1]-Q[i-2])/(Q[i]-Q[i-1]))))/(3 + ((Q[i-1]-Q[i-2])/(Q[i]-Q[i-1])))
            
            
            if i == 0: #FTBS
                q_n = Q[i] - (C  * (Q[i] - (2 * ca - Q[i])))
            elif i==1: #FTBS
                q_n = Q[i] - (C  * (Q[i] - Q[i-1]))
            elif(i == numeroVolumes - 1): #ultimo nó o i+1 vira i
                q_n = Q[i] - (C  * (Q[i] - Q[i-1]))
            else: #demais nós interiores
                q_n = Q[i] - (C  * (Q[i] - Q[i-1])) - (C/2)*(1-C)*(psi_IMaisMeio*(Q[i+1] - Q[i]) - psi_IMenosMeio*(Q[i]-Q[i-1]))

            Q_novo[i] = q_n

        Q = np.copy(Q_novo)  # Atualize Q com os novos valores
        Q_final = np.copy(Q_novo)

    return espaco, Q_final


def PlotaGrafico(comprimento,  numeroVolumes, t_inicial, t_final, velocidade, alpha,ca, cb, cc):
    volume, Solucao = calculaConcentracao(comprimento,  numeroVolumes, t_inicial, t_final, velocidade, alpha,ca, cb, cc)
    volumeFTBS, SolucaoFTBS = calculaConcentracaoFTBS(comprimento,  numeroVolumes, t_inicial, t_final, velocidade, alpha,ca, cb, cc)
    volumeSB, SolucaoSB = calculaConcentracaoSuperBee(comprimento,  numeroVolumes, t_inicial, t_final, velocidade, alpha,ca, cb, cc)
    volumeHQuick, SolucaoHQuick = calculaConcentracaoHQUICK(comprimento,  numeroVolumes, t_inicial, t_final, velocidade, alpha,ca, cb, cc)
    plt.title(r'$Concentração$ $\times$ $Comprimento$')
    plt.plot(volume,Solucao, label='$Van Leer$')
    # plt.plot(volumeFTBS,SolucaoFTBS, label='$FTBS$')
    # plt.plot(volumeSB, SolucaoSB, label='$Super Bee$')
    # plt.plot(volumeHQuick, SolucaoHQuick, label='$HQuick$')
    plt.xlabel(r'$Comprimento$')
    plt.ylabel(r'$Concentração$')
    plt.legend(title = r'$Métodos$', loc=0)

    plt.show()


def Refinamento(comprimento,  numeroVolumesInicial, numeroVolumesFinal,passoVolume, t_inicial, t_final, velocidade, alpha,ca, cb, cc):
    volumes = [25,50,100,200,400]
    for i in range(len(volumes)):
        volume, Solucao = calculaConcentracao(comprimento,  volumes[i], t_inicial, t_final, velocidade, alpha,ca, cb, cc)
        plt.plot(volume,Solucao, label=str(volumes[i]))
        plt.legend(title = r'$Numero$ $de$ $Volumes$', loc=0)
        
    plt.title(r'Refinamento de malha')
    plt.xlabel(r'$Comprimento$')
    plt.ylabel(r'$Concentração$')
    plt.show()

def SensibilidadeVelocidade(comprimento,  numeroVolumes, t_inicial, t_final, velocidadeInicial, velocidadeFinal, alpha,ca, cb, cc,qtdComparacoes):
    passoVelocidade = (velocidadeFinal-velocidadeInicial)/qtdComparacoes
    velocidades = np.arange(velocidadeInicial,velocidadeFinal, passoVelocidade)
    for i in range(len(velocidades)):
        volume, Solucao = calculaConcentracao(comprimento,  numeroVolumes, t_inicial, t_final, velocidades[i], alpha,ca, cb, cc)
        plt.plot(volume,Solucao, label=str("%.2f" %velocidades[i]))
        plt.legend(title = r'$ \overline{u}$', loc=0)
        
    plt.title(r'$Sens. Velocidade$')
    plt.xlabel(r'$Comprimento$')
    plt.ylabel(r'$Concentração$')
    plt.show()


def Sensibilidadeca(comprimento,  numeroVolumes, t_inicial, t_final, velocidade, alpha,caInicial, caFinal, cb, cc,qtdComparacoes):
    passoca=float((caFinal-caInicial)/qtdComparacoes)
    cas = np.arange(caInicial,caFinal, passoca)
    for i in range(len(cas)):
        volume, Solucao = calculaConcentracao(comprimento,  numeroVolumes, t_inicial, t_final, velocidade, alpha, cas[i], cb, cc)
        plt.plot(volume,Solucao, label=str("%.2f" %cas[i]))
        plt.legend(title = r'$c_a$', loc=0)
        
    plt.title(r'$Sens. c_a$')
    plt.xlabel(r'$Comprimento$')
    plt.ylabel(r'$Concentração$')
    plt.show()


def Sensibilidadecb(comprimento,  numeroVolumes, t_inicial, t_final, velocidade, alpha,ca, cbInicial, cbFinal, cc,qtdComparacoes):
    passocb=float((cbFinal-cbInicial)/qtdComparacoes)
    cbs = np.arange(cbInicial,cbFinal, passocb)
    for i in range(len(cbs)):
        volume, Solucao = calculaConcentracao(comprimento,  numeroVolumes, t_inicial, t_final, velocidade, alpha, ca, cbs[i], cc)
        plt.plot(volume,Solucao, label=str("%.2f" %cbs[i]))
        plt.legend(title = r'$c_b$', loc=0)
        
    plt.title(r'$Sens. c_b$')
    plt.xlabel(r'$Comprimento$')
    plt.ylabel(r'$Concentração$')
    plt.show()



def Sensibilidadecc(comprimento,  numeroVolumes, t_inicial, t_final, velocidade, alpha,ca, cb, ccInicial, ccFinal, qtdComparacoes):
    passocc=float((ccFinal-ccInicial)/qtdComparacoes)
    ccs = np.arange(ccInicial, ccFinal, passocc)
    for i in range(len(ccs)):
        volume, Solucao = calculaConcentracao(comprimento,  numeroVolumes, t_inicial, t_final, velocidade, alpha, ca, cb, ccs[i])
        plt.plot(volume,Solucao, label=str("%.2f" %ccs[i]))
        plt.legend(title = r'$c_c$', loc=0)
        
    plt.title(r'$Sens. c_c$')
    plt.xlabel(r'$Comprimento$')
    plt.ylabel(r'$Concentração$')
    plt.show()

def SensibilidadeTempoFinal(comprimento,  numeroVolumes, t_inicial, t_final, velocidade, alpha,ca, cb, cc, qtdComparacoes):
    passoTempo=float((t_final-t_inicial)/qtdComparacoes)
    tempos = np.arange(t_inicial+passoTempo, t_final+passoTempo, passoTempo)
    for i in range(len(tempos)):
        volume, Solucao = calculaConcentracao(comprimento,  numeroVolumes, t_inicial, tempos[i], velocidade, alpha, ca, cb, cc)
        plt.plot(volume,Solucao, label=str(tempos[i]))
        plt.legend(title = r'$T_f$', loc=0)
        
    plt.title(r'$Sens. T_f$')
    plt.xlabel(r'$Comprimento$')
    plt.ylabel(r'$Concentração$')
    plt.show()    

def SensibilidadeComprimento(comprimento_inicial, comprimento_final,  numeroVolumes, t_inicial, t_final, velocidade, alpha,ca, cb, cc, qtdComparacoes):
    passoComprimento=float((comprimento_final-comprimento_inicial)/qtdComparacoes)
    comprimentos = [30,40,50,60,70]
    for i in range(len(comprimentos)):
        volume, Solucao = calculaConcentracao(comprimentos[i],  numeroVolumes, t_inicial, t_final, velocidade, alpha, ca, cb, cc)
        plt.plot(volume,Solucao, label=str("%.2f" %comprimentos[i]))
        plt.legend(title = r'$L_x$', loc=0)
        
    plt.title(r'$Sens. Comprimento$')
    plt.xlabel(r'$Comprimento$')
    plt.ylabel(r'$Concentração$')
    plt.show()  


PlotaGrafico(comprimento=50, numeroVolumes=500,t_inicial= 0,t_final=5,velocidade=1,alpha= 0,ca=0.8,cb= 0.1,cc= 1.0)
Refinamento(comprimento=50,numeroVolumesInicial= 100,numeroVolumesFinal=500,passoVolume=100, t_inicial=0,t_final= 5,velocidade=1,alpha= 0,ca=0.8, cb=0.1, cc=1.0)
SensibilidadeVelocidade(comprimento = 50,numeroVolumes= 500,t_inicial=0,t_final=5,velocidadeInicial=1,velocidadeFinal=5, alpha=0,ca=0.8,cb= 0.1, cc=1.0, qtdComparacoes=5)
Sensibilidadeca(comprimento=50, numeroVolumes=500, t_inicial=0, t_final=5, velocidade=1, alpha=0,caInicial=0.4, caFinal=0.9,  cb=0.2, cc=1.0, qtdComparacoes=5)
Sensibilidadecb(comprimento=50, numeroVolumes=500, t_inicial=0, t_final=5, velocidade=1, alpha=0,ca=0.8, cbInicial = 0.1, cbFinal=0.5,  cc=1.0, qtdComparacoes=5)
Sensibilidadecc(comprimento=50, numeroVolumes=500, t_inicial=0, t_final=5, velocidade=1, alpha=0,ca=0.8, cb=0.1, ccInicial=0.5, ccFinal = 1, qtdComparacoes=5 )
SensibilidadeTempoFinal(comprimento=50, numeroVolumes=500, t_inicial=0, t_final=5, velocidade=1, alpha=0,ca=0.8, cb=0.1, cc=1.0, qtdComparacoes=5 )
SensibilidadeComprimento(comprimento_inicial=30, comprimento_final=70, numeroVolumes=500, t_inicial=0, t_final=5, velocidade=1, alpha=0,ca=0.8, cb=0.1, cc=1.0, qtdComparacoes=5 )
