
import matplotlib.pyplot as plt
import numpy as np

import mpmath

V=[0.08333,-32.08333,1279,-15623.666,84244.1666,-236957.5,375911.666,-340071.666,164062.5,-32812.5]


def Calcula(p_i,q_w,mi,k,h,r_w,phi,c_t,r_e):

    passo_tempo=1000
    
    numero_passos=1000
    n=10
    a=1
    tempo=[]
    X=[]
    p_w = []
    for j in range(1,numero_passos+1):
        tempo.append(j*passo_tempo)
        
        soma=0.0

        for i in range(1,n+1):
            s=(np.log(2)/tempo[j-1])*i
            r = r_w
            eta = k/(phi*mi*c_t)

            A = mpmath.besseli(0,(np.sqrt(s/eta))*r)
            B = mpmath.besselk(1,(np.sqrt(s/eta))*r_e)
            C = mpmath.besseli(1,(np.sqrt(s/eta))*r_e)
            D = mpmath.besselk(0,(np.sqrt(s/eta))*r)

            E = mpmath.besseli(1,(np.sqrt(s/eta))*r_e)
            F = mpmath.besselk(1,(np.sqrt(s/eta))*r_w)
            G = mpmath.besseli(1,(np.sqrt(s/eta))*r_w)
            H = mpmath.besselk(1,(np.sqrt(s/eta))*r_e)

            F_Laplace = ((q_w*mi)/(2*(np.pi)*k*h)) * ( ((A*B)+(C*D)) /( (s*r_w*(np.sqrt(s/eta)))*( (E*F)-(G*H) ) ))
            
            soma=soma+(V[i-1]*F_Laplace)
        X.append(float((np.log(2)/tempo[j-1])*soma))
        
        # p_w.append(float(p_i)-X[j-1])
    return tempo, X
    
   
def CalculaDerivada(p_i,q_w,mi,k,h,r_w,phi,c_t,r_e):
    dados = Calcula(p_i,q_w,mi,k,h,r_w,phi,c_t,r_e)
    derivada = []
    tempo=[]
    deltaP = dados[1]
    deltaT = dados[0]
    for j in range(1,len(deltaP)-1):
        L=j-1
        R =j+1
        B1 = ((deltaP[j] - deltaP[L])/(np.log(deltaT[j]/deltaT[L]))) *((np.log(deltaT[R]/deltaT[j]))/(np.log(deltaT[R]/deltaT[L]))) 
        B2 = ((deltaP[R] - deltaP[j])/(np.log(deltaT[R]/deltaT[j]))) *((np.log(deltaT[j]/deltaT[L]))/(np.log(deltaT[R]/deltaT[L])))
        derivada.append(B1+B2)
        tempo.append(deltaT[j])

    return tempo, derivada

def VariacaoPressao(p_i,q_w,mi,k,h,r_w,phi,c_t,r_e):
    Pwf = Calcula(p_i,q_w,mi,k,h,r_w,phi,c_t,r_e)
    DerivadaPwf = CalculaDerivada(p_i,q_w,mi,k,h,r_w,phi,c_t,r_e)

    fig , (a1, a2)= plt.subplots(1,2)

    a1.set_xscale('log')
    a1.set_yscale('log')
    a1.set_xlabel(r'$log(t)$')
    a1.set_ylabel(r'$log(\Delta_p)$')
    a1.set_title(r'Variação de pressão')
    a1.plot(Pwf[0],Pwf[1], color='purple', label=r'$\Delta_p$')
    
    a2.plot(DerivadaPwf[0],DerivadaPwf[1], color='black', label=r'$\dot{\Delta_p}$')
    a2.set_xscale('log')
    a2.set_yscale('log')
    a2.set_xlabel(r'$log(t)$')
    a2.set_ylabel(r'$log(\Delta_p \prime)$')
    a2.set_title(r'Derivada da variação de pressão')
    plt.suptitle(r'Variação de Pressão')
    plt.show()


def VariacaoPi(pi_inicial, pi_final, passoP_i,q_w,mi,k,h,r_w,phi,c_t,r_e):
    
    Pi = np.arange(pi_inicial,pi_final, passoP_i)
    fig , (a1, a2)= plt.subplots(1,2)
    for i in range(len(Pi)):
        DerivadaDeltaP = CalculaDerivada(Pi[i],q_w,mi,k,h,r_w,phi,c_t,r_e)
        deltaP= Calcula(Pi[i],q_w,mi,k,h,r_w,phi,c_t,r_e)
        
        a1.set_xscale('log')
        a1.set_yscale('log')
        a1.set_xlabel(r'$log(t)$')
        a1.set_ylabel(r'$log(\Delta_p)$')
        a1.set_title(r'Variação de pressão')
        a1.plot(deltaP[0],deltaP[1], label=r'$p_i = $' + str(Pi[i]))
        a1.legend(title = r'$p_i$', loc=0)

        a2.plot(DerivadaDeltaP[0],DerivadaDeltaP[1], label=r'$p_i = $' + str(Pi[i]))
        a2.legend(title = r'$p_i$', loc=0)
        a2.set_xscale('log')
        a2.set_yscale('log')
        a2.set_xlabel(r'$log(t)$')
        a2.set_ylabel(r'$log(\Delta_p \prime)$')
        a2.set_title(r'Derivada da variação de pressão')
    
    plt.suptitle(r'$Sensibilidade$ $Variação$ $da$ $Pressão$ $Inicial$')
    plt.show()


def VariacaoQw(p_i,qw_inicial, qw_final, passo_qw,mi,k,h,r_w,phi,c_t,r_e):
    Qw= np.arange(qw_inicial,qw_final,passo_qw)
    fig , (a1, a2)= plt.subplots(1,2)
    for i in range(len(Qw)):
        deltaP= Calcula(p_i,Qw[i],mi,k,h,r_w,phi,c_t,r_e)
        DerivadaDeltaP = CalculaDerivada(p_i,Qw[i],mi,k,h,r_w,phi,c_t,r_e)
            
        a1.set_xscale('log')
        a1.set_yscale('log')
        a1.set_xlabel(r'$log(t)$')
        a1.set_ylabel(r'$log(\Delta_p)$')
        a1.set_title(r'Variação de pressão')
        a1.plot(deltaP[0],deltaP[1], label=r'$q_w = $' + str(Qw[i]))
        a1.legend(title = r'$q_w$', loc=0)

        a2.plot(DerivadaDeltaP[0],DerivadaDeltaP[1], label=r'$q_w = $' + str(Qw[i]))
        a2.legend(title = r'$q_w$', loc=0)
        a2.set_xscale('log')
        a2.set_yscale('log')
        a2.set_xlabel(r'$log(t)$')
        a2.set_ylabel(r'$log(\Delta_p \prime)$')
        a2.set_title(r'Derivada da variação de pressão')

    plt.suptitle(r'$Sensibilidade$ $Variação$ $da$ $Vazão$')
    plt.show()


def VariacaoMi(p_i,q_w,mi_inicial, mi_final, passo_mi ,k,h,r_w,phi,c_t,r_e):
    Mi= np.arange(mi_inicial,mi_final,passo_mi)
    fig , (a1, a2)= plt.subplots(1,2)
    for i in range(len(Mi)):
        deltaP= Calcula(p_i,q_w,Mi[i],k,h,r_w,phi,c_t,r_e)
        DerivadaDeltaP= CalculaDerivada(p_i,q_w,Mi[i],k,h,r_w,phi,c_t,r_e)


        a1.set_xscale('log')
        a1.set_yscale('log')
        a1.set_xlabel(r'$log(t)$')
        a1.set_ylabel(r'$log(\Delta_p)$')
        a1.set_title(r'Variação de pressão')
        a1.plot(deltaP[0],deltaP[1], label=r'$\mu = $' + str(Mi[i]))
        a1.legend(title = r'$\mu$', loc=0)

        a2.plot(DerivadaDeltaP[0],DerivadaDeltaP[1], label=r'$\mu = $' + str(Mi[i]))
        a2.legend(title = r'$\mu$', loc=0)
        a2.set_xscale('log')
        a2.set_yscale('log')
        a2.set_xlabel(r'$log(t)$')
        a2.set_ylabel(r'$log(\Delta_p \prime)$')
        a2.set_title(r'Derivada da variação de pressão')

    plt.suptitle(r'$Sensibilidade$ $Variação$ $da$ $Viscosidade$')
    plt.show()


def VariacaoPermeabilidade(p_i,q_w,mi,k_inicial, k_final, passo_k,h,r_w,phi,c_t,r_e):
    K= np.arange(k_inicial,k_final,passo_k)
    fig , (a1, a2)= plt.subplots(1,2)
    for i in range(len(K)):
        deltaP= Calcula(p_i,q_w,mi,K[i],h,r_w,phi,c_t,r_e)
        DerivadaDeltaP=CalculaDerivada(p_i,q_w,mi,K[i],h,r_w,phi,c_t,r_e)

        
        a1.set_xscale('log')
        a1.set_yscale('log')
        a1.set_xlabel(r'$log(t)$')
        a1.set_ylabel(r'$log(\Delta_p)$')
        a1.set_title(r'Variação de pressão')
        a1.plot(deltaP[0],deltaP[1], label=r'$k = $' + str(K[i]))
        a1.legend(title = r'$k$', loc=0)

        a2.plot(DerivadaDeltaP[0],DerivadaDeltaP[1], label=r'$k = $' + str(K[i]))
        a2.legend(title = r'$k$', loc=0)
        a2.set_xscale('log')
        a2.set_yscale('log')
        a2.set_xlabel(r'$log(t)$')
        a2.set_ylabel(r'$log(\Delta_p \prime)$')
        a2.set_title(r'Derivada da variação de pressão')

    plt.suptitle(r'$Sensibilidade$ $Variação$ $da$ $Permeabilidade$')
    plt.show()


def VariacaoEspessura(p_i,q_w,mi,k,h_inicial, h_final, passo_h,r_w,phi,c_t,r_e):
    H= np.arange(h_inicial,h_final,passo_h)
    fig , (a1, a2)= plt.subplots(1,2)
    for i in range(len(H)):
        deltaP= Calcula(p_i,q_w,mi,k,H[i],r_w,phi,c_t,r_e)
        DerivadaDeltaP = CalculaDerivada(p_i,q_w,mi,k,H[i],r_w,phi,c_t,r_e)

        a1.set_xscale('log')
        a1.set_yscale('log')
        a1.set_xlabel(r'$log(t)$')
        a1.set_ylabel(r'$log(\Delta_p)$')
        a1.set_title(r'Variação de pressão')
        a1.plot(deltaP[0],deltaP[1], label=r'$h = $' + str(H[i]))
        a1.legend(title = r'$h$', loc=0)

        a2.plot(DerivadaDeltaP[0],DerivadaDeltaP[1], label=r'$h = $' + str(H[i]))
        a2.legend(title = r'$h$', loc=0)
        a2.set_xscale('log')
        a2.set_yscale('log')
        a2.set_xlabel(r'$log(t)$')
        a2.set_ylabel(r'$log(\Delta_p \prime)$')
        a2.set_title(r'Derivada da variação de pressão')

    plt.suptitle(r'$Sensibilidade$ $Variação$ $da$ $Espessura$')
    plt.show()

    
def VariacaoRaioPoco(p_i,q_w,mi,k,h,rw_inicial, rw_final, passo_rw,phi,c_t,r_e):
    Rw= np.arange(rw_inicial,rw_final,passo_rw)
    fig , (a1, a2)= plt.subplots(1,2)
    for i in range(len(Rw)):
        deltaP= Calcula(p_i,q_w,mi,k,h,Rw[i],phi,c_t,r_e)
        DerivadaDeltaP = CalculaDerivada(p_i,q_w,mi,k,h,Rw[i],phi,c_t,r_e)

        a1.set_xscale('log')
        a1.set_yscale('log')
        a1.set_xlabel(r'$log(t)$')
        a1.set_ylabel(r'$log(\Delta_p)$')
        a1.set_title(r'Variação de pressão')
        a1.plot(deltaP[0],deltaP[1],  label=r'$r_w = $' + str(Rw[i]))
        a1.legend(title = r'$r_w$', loc=0)

        a2.plot(DerivadaDeltaP[0],DerivadaDeltaP[1],  label=r'$r_w = $' + str(Rw[i]))
        a2.legend(title = r'$r_w$', loc=0)
        a2.set_xscale('log')
        a2.set_yscale('log')
        a2.set_xlabel(r'$log(t)$')
        a2.set_ylabel(r'$log(\Delta_p \prime)$')
        a2.set_title(r'Derivada da variação de pressão')


    plt.suptitle(r'$Sensibilidade$ $Variação$ $do$ $Raio$ $do$ $Poço$')
    plt.show()


def VariacaoPorosidade(p_i,q_w,mi,k,h,r_w,phi_inicial, phi_final, passo_phi,c_t,r_e):
    Phi= np.arange(phi_inicial,phi_final,passo_phi)
    fig , (a1, a2)= plt.subplots(1,2)
    for i in range(len(Phi)):
        deltaP= Calcula(p_i,q_w,mi,k,h,r_w,Phi[i],c_t,r_e)
        DerivadaDeltaP = CalculaDerivada(p_i,q_w,mi,k,h,r_w,Phi[i],c_t,r_e) 

        a1.set_xscale('log')
        a1.set_yscale('log')
        a1.set_xlabel(r'$log(t)$')
        a1.set_ylabel(r'$log(\Delta_p)$')
        a1.set_title(r'Variação de pressão')
        a1.plot(deltaP[0],deltaP[1],  label=r'$\phi = $' + str(Phi[i]))
        a1.legend(title = r'$\phi$', loc=0)

        a2.plot(DerivadaDeltaP[0],DerivadaDeltaP[1], label=r'$\phi = $' + str(Phi[i]))
        a2.legend(title = r'$\phi$', loc=0)
        a2.set_xscale('log')
        a2.set_yscale('log')
        a2.set_xlabel(r'$log(t)$')
        a2.set_ylabel(r'$log(\Delta_p \prime)$')
        a2.set_title(r'Derivada da variação de pressão')


    plt.suptitle(r'$Sensibilidade$ $Variação$ $da$ $Porosidade$')
    plt.show()


def VariacaoCompressibilidadeTotal(p_i,q_w,mi,k,h,r_w,phi,ct_inicial,ct_final,passo_ct,r_e):
    Ct= np.arange(ct_inicial,ct_final,passo_ct)
    fig , (a1, a2)= plt.subplots(1,2)
    for i in range(len(Ct)):
        deltaP= Calcula(p_i,q_w,mi,k,h,r_w,phi,Ct[i],r_e)
        DerivadaDeltaP = CalculaDerivada(p_i,q_w,mi,k,h,r_w,phi,Ct[i],r_e)

        a1.set_xscale('log')
        a1.set_yscale('log')
        a1.set_xlabel(r'$log(t)$')
        a1.set_ylabel(r'$log(\Delta_p)$')
        a1.set_title(r'Variação de pressão')
        a1.plot(deltaP[0],deltaP[1],  label=r'$c_t = $' + str(Ct[i]))
        a1.legend(title = r'$c_t$', loc=0)

        a2.plot(DerivadaDeltaP[0],DerivadaDeltaP[1], label=r'$c_t = $' + str(Ct[i]))
        a2.legend(title = r'$c_t$', loc=0)
        a2.set_xscale('log')
        a2.set_yscale('log')
        a2.set_xlabel(r'$log(t)$')
        a2.set_ylabel(r'$log(\Delta_p \prime)$')
        a2.set_title(r'Derivada da variação de pressão')

    plt.suptitle(r'$Sensibilidade$ $Variação$ $da$ $Compressibilidade$ $Total$')
    plt.show()


def VariacaoRaioExterno(p_i,q_w,mi,k,h,r_w,phi,c_t,re_inicial, re_final, passo_re):
    Re= np.arange(re_inicial,re_final,passo_re)
    fig , (a1, a2)= plt.subplots(1,2)
    for i in range(len(Re)):
        deltaP= Calcula(p_i,q_w,mi,k,h,r_w,phi,c_t,Re[i])
        DerivadaDeltaP = CalculaDerivada(p_i,q_w,mi,k,h,r_w,phi,c_t,Re[i])
        
        a1.set_xscale('log')
        a1.set_yscale('log')
        a1.set_xlabel(r'$log(t)$')
        a1.set_ylabel(r'$log(\Delta_p)$')
        a1.set_title(r'Variação de pressão')
        a1.plot(deltaP[0],deltaP[1],  label=r'$r_e = $' + str(Re[i]))
        a1.legend(title = r'$r_e$', loc=0)

        a2.plot(DerivadaDeltaP[0],DerivadaDeltaP[1], label=r'$r_e = $' + str(Re[i]))
        a2.legend(title = r'$r_e$', loc=0)
        a2.set_xscale('log')
        a2.set_yscale('log')
        a2.set_xlabel(r'$log(t)$')
        a2.set_ylabel(r'$log(\Delta_p \prime)$')
        a2.set_title(r'Derivada da variação de pressão')

    plt.suptitle(r'$Sensibilidade$ $Variação$ $do$ $Raio$ $Externo$')
    plt.show()

# VariacaoPressao(p_i=30*10**(6),q_w=5*10**(-5),mi=10**(-3),k=2*10**(-13),h=100,r_w=0.15,phi=0.2,c_t=10**(-9),r_e=1000)
#se colocar o re de 1000, usar 10000 no numero de passos e trocar a porosidade para -14

VariacaoPi(pi_inicial=10*10**(6),pi_final= 100*10**(6), passoP_i=20*10**(6),q_w=5*10**(-5),mi=10**(-3),k=2*10**(-13),h=100,r_w=0.15,phi=0.2,c_t=10**(-9),r_e=1000)

VariacaoQw(p_i=30*10**(6),qw_inicial=1*10**(-5), qw_final=8*10**(-5), passo_qw=1*10**(-5),mi=10**(-3),k=2*10**(-13),h=100,r_w=0.15,phi=0.2,c_t=10**(-9),r_e=1000)

VariacaoMi(p_i=30*10**(6),q_w=5*10**(-5),mi_inicial=10**(-3), mi_final=5*10**(-3), passo_mi=0.5*10**(-3), k=2*10**(-13),h=100,r_w=0.15,phi=0.2,c_t=10**(-9),r_e=1000)

VariacaoPermeabilidade(p_i=30*10**(6),q_w=5*10**(-5),mi=10**(-3),k_inicial=1*10**(-13), k_final=8*10**(-13), passo_k=0.5*10**(-13),h=100,r_w=0.15,phi=0.2,c_t=10**(-9),r_e=1000)

VariacaoEspessura(p_i=30*10**(6),q_w=5*10**(-5),mi=10**(-3),k=2*10**(-13),h_inicial=50, h_final=200, passo_h=10,r_w=0.15,phi=0.2,c_t=10**(-9),r_e=1000)

VariacaoRaioPoco(p_i=30*10**(6),q_w=5*10**(-5),mi=10**(-3),k=2*10**(-13),h=100,rw_inicial=0.05, rw_final=0.20, passo_rw=0.02,phi=0.2,c_t=10**(-9),r_e=1000)

VariacaoPorosidade(p_i=30*10**(6),q_w=5*10**(-5),mi=10**(-3),k=2*10**(-13),h=100,r_w=0.15,phi_inicial=0.1, phi_final=0.7, passo_phi=0.05,c_t=10**(-9),r_e=1000)

VariacaoCompressibilidadeTotal(p_i=30*10**(6),q_w=5*10**(-5),mi=10**(-3),k=2*10**(-13),h=100,r_w=0.15,phi=0.2,ct_inicial=10**(-9),ct_final=8*10**(-9),passo_ct=0.5*10**(-9),r_e=1000)

VariacaoRaioExterno(p_i=30*10**(6),q_w=5*10**(-5),mi=10**(-3),k=2*10**(-13),h=100,r_w=0.15,phi=0.2,c_t=10**(-9),re_inicial=1000, re_final=100000, passo_re=10000)
