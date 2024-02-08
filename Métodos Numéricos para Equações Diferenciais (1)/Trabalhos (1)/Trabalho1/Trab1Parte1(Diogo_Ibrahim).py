from itertools import cycle

from turtle import color
import numpy as np
import matplotlib.pyplot as plt

cycol = cycle('bgrcmk')


#função que calcula o runge kutta de terceira ordem
def RK3(t_inicial, t_final, alfa,beta, gamma, c_a,c_b,c_c,deltaT):

    t=np.arange(t_inicial, t_final, deltaT)
    ca=[len(t)]
    cb=[len(t)]
    cc=[len(t)]
    #condições iniciais
    ca[0]= c_a
    cb[0]= c_b
    cc[0]= c_c

    def dcadt(t,ca,cb,cc):
        return (-alfa*ca*cc+cb)

    def dcbdt(t,ca,cb,cc):
        return (beta*ca*cc-cb)

    def dccdt(t,ca,cb,cc):
        return (-gamma*ca*cc+cb-2*cc)

    for i in range(t_inicial, len(t)-1): 
        #k1
        k1_ca= dcadt(t[i], ca[i], cb[i], cc[i])
        k1_cb= dcbdt(t[i], ca[i], cb[i], cc[i])
        k1_cc= dccdt(t[i], ca[i], cb[i], cc[i])

        #k2
        k2_ca= dcadt(t[i]+ deltaT/2, ca[i] + k1_ca*deltaT/2, cb[i] + k1_cb*deltaT/2, cc[i] + k1_cc*deltaT/2 )
        k2_cb= dcbdt(t[i]+ deltaT/2, ca[i] + k1_ca*deltaT/2, cb[i] + k1_cb*deltaT/2, cc[i] + k1_cc*deltaT/2)
        k2_cc= dccdt(t[i]+ deltaT/2, ca[i] + k1_ca*deltaT/2, cb[i] + k1_cb*deltaT/2, cc[i] + k1_cc*deltaT/2 )

        #k3
        k3_ca= dcadt(t[i]+ deltaT, ca[i]-k1_ca*deltaT + 2*k2_ca*deltaT, cb[i]-k1_cb*deltaT + 2*k2_cb*deltaT, cc[i]-k1_cc*deltaT + 2*k2_cc*deltaT)
        k3_cb= dcbdt(t[i]+ deltaT, ca[i]-k1_ca*deltaT + 2*k2_ca*deltaT, cb[i]-k1_cb*deltaT + 2*k2_cb*deltaT, cc[i]-k1_cc*deltaT + 2*k2_cc*deltaT)
        k3_cc= dccdt(t[i]+ deltaT, ca[i]-k1_ca*deltaT + 2*k2_ca*deltaT, cb[i]-k1_cb*deltaT + 2*k2_cb*deltaT, cc[i]-k1_cc*deltaT + 2*k2_cc*deltaT)

        ca.append(ca[i] + (1/6)*(k1_ca+4*k2_ca+k3_ca)*deltaT)
        cb.append(cb[i] + (1/6)*(k1_cb+4*k2_cb+k3_cb)*deltaT)
        cc.append(cc[i] + (1/6)*(k1_cc+4*k2_cc+k3_cc)*deltaT)

    return ca,cb,cc,t


#função para criar os gráficos de c_x por t para um passo de tempo
def RungeKutta3(t_inicial, t_final, alfa,beta, gamma, c_a,c_b,c_c,deltaT):
    Rk3 = RK3(t_inicial, t_final, alfa,beta, gamma, c_a,c_b,c_c,deltaT)

    plt.plot(Rk3[3],Rk3[0],color='purple', label='Ca')
    plt.legend(title="CA",loc=0)
    plt.plot(Rk3[3],Rk3[1],color='black', label='Cb')
    plt.legend(title="CB",loc=0)

    plt.plot(Rk3[3],Rk3[2],color='blue', label='Cc')
    plt.legend(title="Concentração",loc=0)
    plt.title("Concentração x Tempo")
    plt.xlabel("t(s)")
    plt.ylabel("Concentração(U.C)")
    plt.show()
    # print("KKKKKK", Rk3[0])
    print("Ca=", Rk3[0][len(Rk3[0])-1])
    print("Cb=", Rk3[1][len(Rk3[1])-1])
    print("Cc=", Rk3[2][len(Rk3[2])-1])

#função para plotar os graficos c_x por t para mais de um passo de tempo
def RefinamentoMalha(t_inicial, t_final, alfa,beta, gamma, c_a,c_b,c_c,DeltaT_inicial, DeltaT_final):
    deltaT_inicial=DeltaT_inicial
    deltaT_final = DeltaT_final
    DeltaT= np.arange(deltaT_inicial, deltaT_final, deltaT_inicial)
    
    fig, (a1, a2, a3)= plt.subplots(1,3)
    # Marker = ['','o','*','',"D",'1','']
    for i in range(0,len(DeltaT)):
        Rk3 = RK3(t_inicial, t_final, alfa,beta, gamma, c_a,c_b,c_c,DeltaT[i])
        # print(Rk3[0],Rk3[3])
        LineStyle = ['solid', 'dashed', 'dashdot', 'solid', 'dashed', 'dashdot', 'solid', 'dashed', 'dashdot']
        Color = next(cycol)
        a1.plot(Rk3[3],Rk3[0],color=Color,label='%.6f'%(float(DeltaT[i])), linestyle = LineStyle[i])
        a1.legend(title="ΔT",loc=0)
        a1.set_xlabel("t(s)")
        a1.set_ylabel("Ca(U.C)")
        a2.set_title('Refinamento de Malha')
        a2.plot(Rk3[3],Rk3[1],color=Color, label='%.6f'%(float(DeltaT[i])), linestyle = LineStyle[i])
        a2.legend(title="ΔT",loc=0)
        a2.set_xlabel("t(s)")
        a2.set_ylabel("\n"+"Cb(U.C)")
        a3.plot(Rk3[3],Rk3[2],color=Color, label='%.6f'%(float(DeltaT[i])),linestyle = LineStyle[i])
        a3.legend(title="ΔT",loc=0)
        a3.set_xlabel("t(s)")
        a3.set_ylabel("\n"+"Cc(U.C)") 
        
    plt.show()
    

def Sensibilidade(t_inicial, t_final, alfa, beta, gamma, c_a, c_b, c_c, deltaT, passoAlfa, passoBeta, passoGamma):
    alfas= [alfa-2*passoAlfa,alfa-passoAlfa, alfa, alfa+passoAlfa, alfa+2*passoAlfa]
    betas= [beta-2*passoBeta,beta-passoBeta, beta, beta+passoBeta, beta+2*passoBeta]
    gammas= [gamma-2*passoGamma,gamma-passoGamma, gamma, gamma+passoGamma, gamma+2*passoGamma]
    Color= ['blue', 'green', 'red', 'purple', 'yellow']
    fig, (Alfa1, Alfa2,Alfa3)= plt.subplots(1,3)
    fig, (Beta1, Beta2, Beta3)= plt.subplots(1,3)
    fig, (Gamma1, Gamma2,Gamma3)= plt.subplots(1,3)

    for i in range(0, len(alfas)):
        Rk3Alfa = RK3(t_inicial, t_final, alfas[i], beta, gamma, c_a, c_b, c_c, deltaT)
        Rk3Beta = RK3(t_inicial, t_final, alfa, betas[i], gamma, c_a, c_b, c_c, deltaT)
        Rk3Gamma = RK3(t_inicial, t_final, alfa, beta, gammas[i], c_a, c_b, c_c, deltaT)

        Alfa1.plot(Rk3Alfa[3],Rk3Alfa[0],color=Color[i], label='%.2f'%(float(alfas[i])))
        Alfa1.legend(title="alfa",loc=0)
        Alfa1.set_xlabel("t(s)")
        Alfa1.set_ylabel("Ca(U.C)")
        Alfa2.set_title('Sensibilidade Alfa')
        Alfa2.plot(Rk3Alfa[3],Rk3Alfa[1],color=Color[i], label='%.2f'%(float(alfas[i])))
        Alfa2.legend(title="alfa",loc=0)
        Alfa2.set_xlabel("t(s)")
        Alfa2.set_ylabel("Cb(U.C)")
        Alfa3.plot(Rk3Alfa[3],Rk3Alfa[2],color=Color[i], label='%.2f'%(float(alfas[i])))
        Alfa3.legend(title="alfa",loc=0)
        Alfa3.set_xlabel("t(s)")
        Alfa3.set_ylabel("Cc(U.C)")

        Beta1.plot(Rk3Beta[3],Rk3Beta[0],color=Color[i], label='%.2f'%(float(betas[i])))
        Beta1.legend(title="beta",loc=0)
        Beta1.set_xlabel("t(s)")
        Beta1.set_ylabel("\n"+"Ca(U.C)")
        Beta2.set_title('Sensibilidade Beta')
        Beta2.plot(Rk3Beta[3],Rk3Beta[1],color=Color[i], label='%.2f'%(float(betas[i])))
        Beta2.legend(title="beta",loc=0)
        Beta2.set_xlabel("t(s)")
        Beta2.set_ylabel("\n"+"Cb(U.C)")

        Beta3.plot(Rk3Beta[3],Rk3Beta[2],color=Color[i], label='%.2f'%(float(betas[i])))
        Beta3.legend(title="beta",loc=0)
        Beta3.set_xlabel("t(s)")
        Beta3.set_ylabel("\n"+"Cc(U.C)")

        Gamma1.plot(Rk3Gamma[3],Rk3Gamma[0],color=Color[i], label='%.2f'%(float(gammas[i])))
        Gamma1.legend(title="gamma",loc=0)
        Gamma1.set_xlabel("t(s)")
        Gamma1.set_ylabel("\n"+"Ca(U.C)") 
        Gamma2.set_title('Sensibilidade Gamma')
        Gamma2.plot(Rk3Gamma[3],Rk3Gamma[1],color=Color[i], label='%.2f'%(float(gammas[i])))
        Gamma2.legend(title="gamma",loc=0)
        Gamma2.set_xlabel("t(s)")
        Gamma2.set_ylabel("\n"+"Cb(U.C)") 
        Gamma3.plot(Rk3Gamma[3],Rk3Gamma[2],color=Color[i], label='%.2f'%(float(gammas[i])))
        Gamma3.legend(title="gamma",loc=0)
        Gamma3.set_xlabel("t(s)")
        Gamma3.set_ylabel("\n"+"Cc(U.C)") 
    plt.show()

t_inicial= 0 
t_final= 9.5
c_a = 11  #condicao inicial ca
c_b= 0   #condicao inicial cb
c_c = 8 #condicao inicial cc
alfa= 37
beta= 55
gamma= 80
deltaT = 0.0001
DeltaT_inicial= 0.0005  #refinamento
DeltaT_final= 0.0020 #refinamento
passoAlfa = 6 #sensibilidade
passoBeta = 6 #sensibilidade
passoGamma = 6 #sensibilidade

RK3(t_inicial, t_final, alfa,beta, gamma, c_a,c_b,c_c,deltaT)
RungeKutta3(t_inicial, t_final, alfa,beta, gamma, c_a,c_b,c_c,deltaT)
# RefinamentoMalha(t_inicial, t_final, alfa,beta, gamma, c_a,c_b,c_c,DeltaT_inicial, DeltaT_final)
# Sensibilidade(t_inicial, t_final, alfa, beta, gamma, c_a, c_b, c_c, deltaT, passoAlfa, passoBeta, passoGamma)
