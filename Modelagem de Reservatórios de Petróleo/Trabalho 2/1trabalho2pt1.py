
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
    deltaP = dados[1]
    deltaT = dados[0]
    for j in range(1,len(deltaP)-1):
        L=j-1
        R =j+1
        B1 = ((deltaP[j] - deltaP[L])/(np.log(deltaT[j]/deltaT[L]))) *((np.log(deltaT[R]/deltaT[j]))/(np.log(deltaT[R]/deltaT[L]))) 
        B2 = ((deltaP[R] - deltaP[j])/(np.log(deltaT[R]/deltaT[j]))) *((np.log(deltaT[j]/deltaT[L]))/(np.log(deltaT[R]/deltaT[L])))
        derivada.append(B1+B2)
    derivada.insert(0, deltaP[0])
    derivada.insert(len(deltaP)-1, deltaP[len(deltaP)-1])

    return deltaT, derivada

def pwf(p_i,q_w,mi,k,h,r_w,phi,c_t,r_e):
    Pwf = Calcula(p_i,q_w,mi,k,h,r_w,phi,c_t,r_e)
    DerivadaPwf = CalculaDerivada(p_i,q_w,mi,k,h,r_w,phi,c_t,r_e)

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel(r'$log(t)$')
    plt.ylabel(r'$log(\Delta_p)$')
    plt.title(r'Pressão no Poço ao longo do tempo')
    plt.plot(Pwf[0],Pwf[1], color='purple', label=r'$\Delta_p$')
    plt.legend(title = r'$\Delta_p$', loc=0)
    plt.plot(DerivadaPwf[0],DerivadaPwf[1], color='black', label=r'Derivada')
    plt.legend(title = r'Derivada', loc=0)
    plt.show()


def VariacaoPi(pi_inicial, pi_final, passoP_i,q_w,mi,k,h,r_w,phi,c_t,r_e):
    Pi = np.arange(pi_inicial,pi_final, passoP_i)
    for i in range(len(Pi)):
        a= Calcula(Pi[i],q_w,mi,k,h,r_w,phi,c_t,r_e)
        plt.xscale('log')
       
        plt.plot(a[0],a[1], label=str(Pi[i]))
        plt.legend(title = r'$p_i$', loc=0)

    plt.xlabel(r'$log(t)$')
    plt.ylabel(r'$pwf$')
    plt.title(r'$Sensibilidade$ $Variação$ $da$ $Pressão$ $Inicial$')
    plt.show()


def VariacaoQw(p_i,qw_inicial, qw_final, passo_qw,mi,k,h,r_w,phi,c_t,r_e):
    Qw= np.arange(qw_inicial,qw_final,passo_qw)
    for i in range(len(Qw)):
        a= Calcula(p_i,Qw[i],mi,k,h,r_w,phi,c_t,r_e)
        b = CalculaDerivada(p_i,Qw[i],mi,k,h,r_w,phi,c_t,r_e)
        plt.xscale('log')
        plt.yscale('log')
        
        plt.plot(a[0],a[1], label=str(Qw[i]))
        plt.legend(title = r'$\Delta_p \rightarrow{} q_{w}$', loc=0)
        plt.plot(b[0],b[1], label=str(Qw[i]))
        plt.legend(title = r'$Derivada \rightarrow{} q_{w}$', loc=0)

    plt.xlabel(r'$log(t)$')
    plt.ylabel(r'$pwf$')
    plt.title(r'$Sensibilidade$ $Variação$ $da$ $Vazão$')
    plt.show()


def VariacaoMi(p_i,q_w,mi_inicial, mi_final, passo_mi ,k,h,r_w,phi,c_t,r_e):
    Mi= np.arange(mi_inicial,mi_final,passo_mi)
    for i in range(len(Mi)):
        a= Calcula(p_i,q_w,Mi[i],k,h,r_w,phi,c_t,r_e)
        plt.xscale('log')
   
        plt.plot(a[0],a[1], label=str(Mi[i]))
        plt.legend(title = r'$\mu$', loc=0)

    plt.xlabel(r'$log(t)$')
    plt.ylabel(r'$pwf$')
    plt.title(r'$Sensibilidade$ $Variação$ $da$ $Viscosidade$')
    plt.show()


def VariacaoPermeabilidade(p_i,q_w,mi,k_inicial, k_final, passo_k,h,r_w,phi,c_t,r_e):
    K= np.arange(k_inicial,k_final,passo_k)
    for i in range(len(K)):
        a= Calcula(p_i,q_w,mi,K[i],h,r_w,phi,c_t,r_e)
        plt.xscale('log')
        
        plt.plot(a[0],a[1], label=str(K[i]))
        plt.legend(title = r'$K$', loc=0)

    plt.xlabel(r'$log(t)$')
    plt.ylabel(r'$pwf$')
    plt.title(r'$Sensibilidade$ $Variação$ $da$ $Permeabilidade$')
    plt.show()


def VariacaoEspessura(p_i,q_w,mi,k,h_inicial, h_final, passo_h,r_w,phi,c_t,r_e):
    H= np.arange(h_inicial,h_final,passo_h)
    for i in range(len(H)):
        a= Calcula(p_i,q_w,mi,k,H[i],r_w,phi,c_t,r_e)
        plt.xscale('log')
       
        plt.plot(a[0],a[1], label=str(H[i]))
        plt.legend(title = r'$h$', loc=0)

    plt.xlabel(r'$log(t)$')
    plt.ylabel(r'$pwf$')
    plt.title(r'$Sensibilidade$ $Variação$ $da$ $Espessura$')
    plt.show()

    
def VariacaoRaioPoco(p_i,q_w,mi,k,h,rw_inicial, rw_final, passo_rw,phi,c_t,r_e):
    Rw= np.arange(rw_inicial,rw_final,passo_rw)
    for i in range(len(Rw)):
        a= Calcula(p_i,q_w,mi,k,h,Rw[i],phi,c_t,r_e)
        plt.xscale('log')
        
        plt.plot(a[0],a[1], label=str(Rw[i]))
        plt.legend(title = r'$r_{w}$', loc=0)

    plt.xlabel(r'$log(t)$')
    plt.ylabel(r'$pwf$')
    plt.title(r'$Sensibilidade$ $Variação$ $do$ $Raio$ $do$ $Poço$')
    plt.show()


def VariacaoPorosidade(p_i,q_w,mi,k,h,r_w,phi_inicial, phi_final, passo_phi,c_t,r_e):
    Phi= np.arange(phi_inicial,phi_final,passo_phi)
    for i in range(len(Phi)):
        a= Calcula(p_i,q_w,mi,k,h,r_w,Phi[i],c_t,r_e)
        plt.xscale('log')
        
        plt.plot(a[0],a[1], label=str(Phi[i]))
        plt.legend(title = r'$\phi$', loc=0)

    plt.xlabel(r'$log(t)$')
    plt.ylabel(r'$pwf$')
    plt.title(r'$Sensibilidade$ $Variação$ $da$ $Porosidade$')
    plt.show()


def VariacaoCompressibilidadeTotal(p_i,q_w,mi,k,h,r_w,phi,ct_inicial,ct_final,passo_ct,r_e):
    Ct= np.arange(ct_inicial,ct_final,passo_ct)
    for i in range(len(Ct)):
        a= Calcula(p_i,q_w,mi,k,h,r_w,phi,Ct[i],r_e)
        plt.xscale('log')
        
        plt.plot(a[0],a[1], label=str(Ct[i]))
        plt.legend(title = r'$c_t$', loc=0)

    plt.xlabel(r'$log(t)$')
    plt.ylabel(r'$pwf$')
    plt.title(r'$Sensibilidade$ $Variação$ $da$ $Compressibilidade$ $Total$')
    plt.show()


def VariacaoRaioExterno(p_i,q_w,mi,k,h,r_w,phi,c_t,re_inicial, re_final, passo_re):
    Re= np.arange(re_inicial,re_final,passo_re)
    for i in range(len(Re)):
        a= Calcula(p_i,q_w,mi,k,h,r_w,phi,c_t,Re[i])
        
        plt.xscale('log')
        
        plt.plot(a[0],a[1], label=str(Re[i]))
        plt.legend(title = r'$r_e$', loc=0)

    plt.xlabel(r'$log(t)$')
    plt.ylabel(r'$pwf$')
    plt.title(r'$Sensibilidade$ $Variação$ $do$ $Raio$ $Externo$')
    plt.show()

# Calcula(p_i,q_w,mi,k,h,r_w,phi,c_t,r_e)
# Calcula(30*10**(6),5*10**(-5),10**(-3),2*10**(-17),100,0.15,0.2,10**(-9),1000)

# pwf(p_i,q_w,mi,k,h,r_w,phi,c_t,r_e)
# pwf(30*10**(6),5*10**(-5),10**(-3),2*10**(-13),100,0.15,0.2,10**(-9),1000)
#se colocar o re de 1000, usar 10000 no numero de passos e trocar a porosidade para -14

# CalculaDerivada(30*10**(6),5*10**(-5),10**(-3),2*10**(-13),100,0.15,0.2,10**(-9),1000)


# VariacaoPi(pi_inicial, pi_final, passoP_i,q_w,mi,k,h,r_w,phi,c_t,r_e)
# VariacaoPi(10*10**(6),100*10**(6), 10*10**(6),5*10**(-5),10**(-3),2*10**(-13),100,0.15,0.2,10**(-9),1000)

# VariacaoQw(p_i,qw_inicial, qw_final, passo_qw,mi,k,h,r_w,phi,c_t,r_e)
VariacaoQw(30*10**(6),1*10**(-5), 8*10**(-5), 2*10**(-5),10**(-3),2*10**(-13),100,0.15,0.2,10**(-9),1000)

# VariacaoMi(p_i,q_w,mi_inicial, mi_final, passo_mi ,k,h,r_w,phi,c_t,r_e)
# VariacaoMi(30*10**(6),5*10**(-5),10**(-3), 5*10**(-3), 10**(-3) ,2*10**(-13),100,0.15,0.2,10**(-9),1000)

# VariacaoPermeabilidade(p_i,q_w,mi,k_inicial, k_final, passo_k,h,r_w,phi,c_t,r_e)
# VariacaoPermeabilidade(30*10**(6),5*10**(-5),10**(-3),1*10**(-13), 8*10**(-13), 1*10**(-13),100,0.15,0.2,10**(-9),1000)

# VariacaoEspessura(p_i,q_w,mi,k,h_inicial, h_final, passo_h,r_w,phi,c_t,r_e)
# VariacaoEspessura(30*10**(6),5*10**(-5),10**(-3),2*10**(-13),50, 200, 20,0.15,0.2,10**(-9),1000)

# VariacaoRaioPoco(p_i,q_w,mi,k,h,rw_inicial, rw_final, passo_rw,phi,c_t,r_e)
# VariacaoRaioPoco(30*10**(6),5*10**(-5),10**(-3),2*10**(-13),100,0.05, 0.20, 0.04,0.2,10**(-9),1000)

# VariacaoPorosidade(p_i,q_w,mi,k,h,r_w,phi_inicial, phi_final, passo_phi,c_t,r_e)
# VariacaoPorosidade(30*10**(6),5*10**(-5),10**(-3),2*10**(-13),100,0.15,0.1, 0.7, 0.1,10**(-9),1000)

# VariacaoCompressibilidadeTotal(p_i,q_w,mi,k,h,r_w,phi,ct_inicial,ct_final,passo_ct,r_e)
# VariacaoCompressibilidadeTotal(30*10**(6),5*10**(-5),10**(-3),2*10**(-13),100,0.15,0.2,10**(-9),8*10**(-9),10**(-9),1000)

# VariacaoRaioExterno(p_i,q_w,mi,k,h,r_w,phi,c_t,re_inicial, re_final, passo_re)
# VariacaoRaioExterno(30*10**(6),5*10**(-5),10**(-3),2*10**(-13),100,0.15,0.2,10**(-9),1000, 100000, 5000)
