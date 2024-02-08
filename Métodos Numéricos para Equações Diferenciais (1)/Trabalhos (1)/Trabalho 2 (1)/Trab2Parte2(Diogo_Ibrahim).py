import numpy as np
import matplotlib.pyplot as plt

def ResolveSistema(comprimentoTubo,NumeroNosInternos,tempo, Ci, Ce, u):

    deltaX=comprimentoTubo/NumeroNosInternos  
    deltaT=tempo/NumeroNosInternos
    comprimentoTubo=np.arange(0,comprimentoTubo,deltaX)
    t=np.arange(0,tempo,deltaT)
    Courant = u*(deltaT/deltaX)
    
    C =[Ci for i in range(NumeroNosInternos)]

    for i in range(len(C)):
        if (i==0):
            C[i] = [Ci for i in range(NumeroNosInternos)]     
        else:
            C[i] = [Ce for i in range(NumeroNosInternos)]

    for c in range(len(C)-1):
        for d in range(len(C[i])-1):
            C[c+1][d+1] = C[c][d+1]-Courant*C[c][d+1]+Courant*C[c][d]
    
    return C,comprimentoTubo

def GraficoTodasSolucoes(comprimentoTubo,NumeroNosInternos,tf, Ci, Ce, u):
    C,comprimentotubo = ResolveSistema(comprimentoTubo,NumeroNosInternos,tf, Ci, Ce, u)
    for i in range(len(C)):
        plt.plot(comprimentotubo,C[i])
        plt.title("Concentração x L")
        plt.xlabel("L(m)")
        plt.ylabel("Concentração(U.C)")
    plt.show()

def refinamentoDeltaX(comprimentoTubo,NumeroNosInternosInicial,NumeroNosInternosFinal,passoNumeroNosInternos,tf, Ci, Ce, u):
    VariacaoNos=np.arange(NumeroNosInternosInicial,NumeroNosInternosFinal,passoNumeroNosInternos)

    for i in range(len(VariacaoNos)):
        C,comprimentotubo = ResolveSistema(comprimentoTubo,VariacaoNos[i],tf, Ci, Ce, u)
        
        plt.plot(comprimentotubo,C[len(C)-1],label="Nos Iternos="+str(VariacaoNos[i]))
        plt.title("Refinamento DeltaX")
        plt.xlabel("L(m)")
        plt.ylabel("Concentração(U.C)")
        plt.legend(title="Numero de Nos Internos",loc=0)
    plt.show()


def RefinamentoDeltaT(comprimentoTubo,NumeroNosInternos,tInicial,tFinal, passoT,Ci,Ce,u):
    TF=np.arange(tInicial,tFinal,passoT)

    for i in range(len(TF)):
        C,x_tubo = ResolveSistema(comprimentoTubo,NumeroNosInternos,TF[i], Ci, Ce, u)
        plt.plot(x_tubo,C[len(C)-1],label="tf="+str('{:.2f}'.format(TF[i])))
        plt.title("Variação do passo de tempo")
        plt.xlabel("L(m)")
        plt.ylabel("Concentração(U.C)")
        plt.legend(title="Tempo",loc=0)

    plt.show() 

def SensibilidadeU(comprimentoTubo,NumeroNosInternos,tf, Ci, Ce,uInicial,uFinal,passoU):
   
    U=np.arange(uInicial,uFinal,passoU)

    for i in range(len(U)):
        C,comprimentotubo = ResolveSistema(comprimentoTubo,NumeroNosInternos,tf, Ci, Ce, U[i])
        
        plt.plot(comprimentotubo,C[len(C)-1],label="U="+str('{:.2f}'.format(U[i])))
        plt.title("Sensibilidade Variação U")
        plt.xlabel("L(m)")
        plt.ylabel("Concentração(U.C)")
        plt.legend(title="U",loc=0)
    plt.show()

def SensibilidadeCe(comprimentoTubo,NumeroNosInternos,tf, Ci, CeInicial, CeFinal, passoCe,u):
   
    CE=np.arange(CeInicial,CeFinal, passoCe)

    for i in range(len(CE)):
        C,comprimentotubo = ResolveSistema(comprimentoTubo,NumeroNosInternos,tf, Ci, CE[i], u)
        
        plt.plot(comprimentotubo,C[len(C)-1],label="Ce="+str(CE[i]))
        plt.title("Sensibilidade Variação Ce")
        plt.xlabel("L(m)")
        plt.ylabel("Concentração(U.C)")
        plt.legend(title="Ce",loc=0)
    plt.show()

def SensibilidadeCi(comprimentoTubo,NumeroNosInternos,tf, CiInicial, CiFinal, passoCi, Ce,u):
   
    CI=np.arange(CiInicial,CiFinal,passoCi)

    for i in range(len(CI)):
        C,comprimentotubo = ResolveSistema(comprimentoTubo,NumeroNosInternos,tf, CI[i], Ce, u)
        
        plt.plot(comprimentotubo,C[len(C)-1],label="Ci="+str('{:.2f}'.format(CI[i])))
        plt.title("Sensibilidade Variação Ci")
        plt.xlabel("L(m)")
        plt.ylabel("Concentração(U.C)")
        plt.legend(title="Ci",loc=0)
    plt.show()


#GraficoTodasSolucoes(comprimentoTubo,NumeroNosInternos,tf, Ci, Ce, u)
GraficoTodasSolucoes(60,100,16,1,4,2.5)

#refinamentoDeltaX(comprimentoTubo,NumeroNosInternosInicial,NumeroNosInternosFinal,passoNumeroNosInternos,tf, Ci, Ce, u)
refinamentoDeltaX(60,50,90,3,16,1,4,2.5)

# RefinamentoDeltaT(comprimentoTubo,NumeroNosInternos,tInicial,tFinal, passoT,Ci,Ce,u)
RefinamentoDeltaT(60,100,10,20,1,1,4,2.5)

#SensibilidadeU(comprimentoTubo,NumeroNosInternos,tf, Ci, Ce,uInicial,uFinal,passoU)
SensibilidadeU(60,70,16,1,4,1,3,0.5)

#SensibilidadeCe(comprimentoTubo,NumeroNosInternos,tf, Ci, CeInicial, CeFinal, passoCe,u)
SensibilidadeCe(60,70,16,1,1,7,1,2.5)

#SensibilidadeCi(comprimentoTubo,NumeroNosInternos,tf, CiInicial, CiFinal, passoCi, Ce,u)
SensibilidadeCi(60,70,16,1,2,0.1,4,2.5)
