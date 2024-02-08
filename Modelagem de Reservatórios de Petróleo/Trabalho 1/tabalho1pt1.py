import math 
import matplotlib.pyplot as plt
import numpy as np


def Eta(k,phi,mi,c_t, variacaoPressaoPoco,p_i,tempo):
    eta = k/(phi*mi*c_t)
    x_inicial=0
    x_final = 50000
    # t= np.arange(t_inicial,t_final,10000)

    x= np.arange(x_inicial,x_final,100)

    p=[]

    for i in range(len(x)):
        p.append(p_i-variacaoPressaoPoco*(math.erfc(x[i]/(np.sqrt(4*eta*tempo)))))

    return x, p

def PressaoEscoamento(k,phi,mi,c_t, variacaoPressaoPoco,p_i,tempo):
    Pressao = Eta(k,phi,mi,c_t, variacaoPressaoPoco,p_i,tempo)
    #PLOT p(x) para um tempo fixo
    plt.plot(Pressao[0],Pressao[1], color='purple')
    plt.xlabel(r'$X$')
    plt.ylabel(r'$p(x)$')
    plt.title(r'$Pressão$ $no$ $Escoamento$')
    plt.show()

def SensibilidadeK(k_inicial,k_final,passo_k ,phi,mi,c_t, variacaoPressaoPoco,p_i,tempo):
    K=np.arange(k_inicial,k_final,passo_k)
    for i in range(len(K)):
        a = Eta(K[i],phi,mi,c_t, variacaoPressaoPoco,p_i,tempo)
        plt.plot(a[0],a[1], label=str(K[i]))
        plt.legend(title = "K", loc=0)

    plt.xlabel(r'$X$')
    plt.ylabel(r'$p(x)$')
    plt.title(r'$Sensibilidade$ $Variação$ $da$ $Permeabilidade$')
    plt.show()



def SensibilidadeMi(k,phi,mi_inicial, mi_final,passo_mi,c_t, variacaoPressaoPoco,p_i,tempo):
    Mi=np.arange(mi_inicial,mi_final,passo_mi)
    for i in range(len(Mi)):
        a = Eta(k,phi,Mi[i],c_t, variacaoPressaoPoco,p_i,tempo)
        plt.plot(a[0],a[1], label=str(Mi[i]))
        plt.legend(title = r'$\mu$', loc=0)

    plt.xlabel(r'$X$')
    plt.ylabel(r'$p(x)$')
    plt.title(r'$Sensibilidade$ $Variação$ $da$ $Viscosidade$')
    plt.show()


def SensibilidadeCt(k,phi,mi,c_tinicial, c_tfinal, passoc_t, variacaoPressaoPoco,p_i,tempo):
    Ct=np.arange(c_tinicial, c_tfinal, passoc_t)
    for i in range(len(Ct)):
        a = Eta(k,phi,mi,Ct[i], variacaoPressaoPoco,p_i,tempo)
        plt.plot(a[0],a[1], label=str(Ct[i]))
        plt.legend(title = r'$C_t$', loc=0)

    plt.xlabel(r'$X$')
    plt.ylabel(r'$p(x)$')
    plt.title(r'$Sensibilidade$ $Variação$ $da$ $Compressibilidade$ $Total$')
    plt.show()


def SensibilidadePorosidade(k,phi_inicial, phi_final, passo_phi,mi,c_t, variacaoPressaoPoco,p_i,tempo):
    Phi=np.arange(phi_inicial, phi_final, passo_phi)
    for i in range(len(Phi)):
        a = Eta(k,Phi[i],mi,c_t, variacaoPressaoPoco,p_i,tempo)
        plt.plot(a[0],a[1], label=str(Phi[i]))
        plt.legend(title = r'$\phi$', loc=0)

    plt.xlabel(r'$X$')
    plt.ylabel(r'$p(x)$')
    plt.title(r'$Sensibilidade$ $Variação$ $da$ $Porosidade$ ')
    plt.show()



def SensibilidadePressaoInicial(k,phi,mi,c_t, variacaoPressaoPoco,p_iinicial, p_ifinal, passo_pi,tempo):
    Pi=np.arange(p_iinicial, p_ifinal, passo_pi)
    for i in range(len(Pi)):
        a = Eta(k,phi,mi,c_t, variacaoPressaoPoco,Pi[i],tempo)
        plt.plot(a[0],a[1], label=str(Pi[i]))
        plt.legend(title = r'$p_i$', loc=0)

    plt.xlabel(r'$X$')
    plt.ylabel(r'$p(x)$')
    plt.title(r'$Sensibilidade$ $Variação$ $da$ $Pressão$ $Inicial$ ')
    plt.show()


def SensibilidadeVariacaoPressaoPoco(k,phi,mi,c_t, variacaoPressaoPoco_inicial, variacaoPressaoPoco_final, passo_variacaoPressaoPoco,p_i,tempo):
    VPP=np.arange(variacaoPressaoPoco_inicial, variacaoPressaoPoco_final, passo_variacaoPressaoPoco)
    for i in range(len(VPP)):
        a = Eta(k,phi,mi,c_t, VPP[i],p_i,tempo)
        plt.plot(a[0],a[1], label=str(VPP[i]))
        plt.legend(title = r'$\Delta_{pw}$', loc=0)

    plt.xlabel(r'$X$')
    plt.ylabel(r'$p(x)$')
    plt.title(r'$Sensibilidade$ $Variação$ $da$ $Variação$ $da$ $Pressão$ $no$ $Poço$ ')
    plt.show()


def SensibilidadeTempo(k,phi,mi,c_t, variacaoPressaoPoco,p_i, tempo_inicial,tempo_final,passoTempo):
    T=np.arange(tempo_inicial,tempo_final,passoTempo)
    for i in range(len(T)):
        a = Eta(k,phi,mi,c_t, variacaoPressaoPoco,p_i,T[i])
        plt.plot(a[0],a[1], label=str(T[i]))
        plt.legend(title = "T", loc=0)

    plt.xlabel(r'$X$')
    plt.ylabel(r'$p(x)$')
    plt.title(r'$Sensibilidade$ $Variação$ $do$ $Tempo$')
    plt.show()





p_i = 30*10**6
k= 2*10**(-13)
phi= 0.2
mi= 10**(-3)
c_t= 10**(-9)
variacaoPressaoPoco = 10.46*10**6



# Eta(k,phi,mi,c_t, variacaoPressaoPoco,p_i,tempo)
# Eta(2*10**(-13),0.2,10**(-3),10**(-9), 10.46*10**6,30*10**6,100000000)

PressaoEscoamento(2*10**(-13),0.2,10**(-3),10**(-9), 10.46*10**6,30*10**6,100000000)

# SensibilidadeK(k_inicial,k_final,passo_k ,phi,mi,c_t, variacaoPressaoPoco,p_i,tempo)
# SensibilidadeK(0.5*10**(-13),5*10**(-13),1*10**(-13) ,0.2,10**(-3),10**(-9), 10.46*10**6,30*10**6,100000000)

# SensibilidadeMi(k,phi,mi_inicial, mi_final,passo_mi,c_t, variacaoPressaoPoco,p_i,tempo)
# SensibilidadeMi(2*10**(-13),0.2,10**(-3), 6*10**(-3),1*10**(-3),10**(-9), 10.46*10**6,30*10**6,100000000)

# SensibilidadeCt(k,phi,mi,c_tinicial, c_tfinal, passoc_t, variacaoPressaoPoco,p_i,tempo)
# SensibilidadeCt(2*10**(-13),0.2,10**(-3),10**(-9), 6*10**(-9), 1*10**(-9), 10.46*10**6,30*10**6,100000000)

# SensibilidadePorosidade(k,phi_inicial, phi_final, passo_phi,mi,c_t, variacaoPressaoPoco,p_i,tempo)
# SensibilidadePorosidade(2*10**(-13),0.1, 0.6, 0.05,10**(-3),10**(-9), 10.46*10**6,30*10**6,100000000)

# SensibilidadePressaoInicial(k,phi,mi,c_t, variacaoPressaoPoco,p_iinicial, p_ifinal, passo_pi,tempo)
# SensibilidadePressaoInicial(2*10**(-13),0.2,10**(-3),10**(-9), 10.46*10**6,20*10**6,50*10**6,5*10**6,100000000 )

# SensibilidadeVariacaoPressaoPoco(k,phi,mi,c_t, variacaoPressaoPoco_inicial, variacaoPressaoPoco_final, passo_variacaoPressaoPoco,p_i,tempo)
# SensibilidadeVariacaoPressaoPoco(2*10**(-13),0.2,10**(-3),10**(-9), 10*10**6, 30*10**6, 5*10**6,30*10**6,100000000)

# SensibilidadeTempo(k,phi,mi,c_t, variacaoPressaoPoco,p_i, tempo_inicial,tempo_final,passoTempo)
# SensibilidadeTempo(2*10**(-13),0.2,10**(-3),10**(-9),10.46*10**6,30*10**6,1000000,100000000,10000000)