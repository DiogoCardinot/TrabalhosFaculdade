import numpy as np
import matplotlib.pyplot as plt

def Matriz(comprimentoTubo,NumeroNosInternos,deltaT,DeltaX,Ci,Ce, alfa):
    s=alfa*deltaT/DeltaX**2
    A = np.zeros((NumeroNosInternos+1, NumeroNosInternos+1))
    b = np.zeros((NumeroNosInternos+1))

    for i in range(NumeroNosInternos+1):
        for j in range(NumeroNosInternos):
            if(i == j==0): 
                A[i,j] =(1 + 2*s)
                A[i,j+1]=-s
                break

            if (i==j):
               A[i,j-1]= -s
               A[i,j]=1+2*s
               A[i,j+1]= -s
               break

            if(i==NumeroNosInternos):
                if(j==NumeroNosInternos-1):
                 A[i,j]=-2*s
                 A[i,j+1]=(1 + 2*s)
                 break

       #Vetor Solucao b
        if j==0:
            b[j]=Ci

        b[i] = Ce

        if(i == 0):
            b[i] = b[i] + s*Ce
   
    return A,b

def GaussJacobi(a, b, solucaoInicial, tolerancia, QuantidadeMaximaIteracoes):
    n = len(b)
    x = solucaoInicial
    for i in range(QuantidadeMaximaIteracoes):
        x_new = np.zeros(n)
        for j in range(n):
            s1 = np.dot(a[j, :j], x[:j])
            s2 = np.dot(a[j, j + 1:], x[j + 1:])
            x_new[j] = (b[j] - s1 - s2) / a[j, j]
        if np.allclose(x, x_new, rtol=tolerancia):
            return x_new
        x = x_new
    return x

def GraficoTodasSolucoes(comprimentoTubo,NumeroNosInternos,tempoInicial,tempoFinal, Ci, Ce, alfa):

    DeltaX=comprimentoTubo/(NumeroNosInternos+1)
    deltaT=DeltaX**2/(2*alfa)

    A,b= Matriz(comprimentoTubo,NumeroNosInternos,deltaT,DeltaX, Ci, Ce, alfa)

    solucaoInicial = np.zeros(len(b))
    precisao = 1e-6
    QuantidadeMaximaIteracoes = 150

    C_N = []

    T=np.arange(tempoInicial,tempoFinal,1)

    for i in range(len(T)):
        vetorSolucaoSistema = GaussJacobi(A, b, solucaoInicial,precisao, QuantidadeMaximaIteracoes)
        C_N.append(vetorSolucaoSistema)
        CN=np.insert(C_N,0,Ce,axis=1)
        b = vetorSolucaoSistema  

    
    comprimentoTubo = float(comprimentoTubo)
    comprimentotubo=[k*comprimentoTubo/tempoFinal for k in range(0,tempoFinal)]

    for i in range(len(CN)):
        plt.plot(comprimentotubo,CN[:,i])     


    plt.title("Concentração x L")
    plt.xlabel("L(m)")
    plt.ylabel("Concentração(U.C)")
    plt.show()
   
def refinamentoNumeroNos(comprimentoTubo,NumeroNosInternosInicial,NumeroNosInternosFinal, variacaoNumeroNos,tempoInicial,tempoFinal,deltaT, Ci, Ce, alfa):
   
    VariacaoNos=np.arange(NumeroNosInternosInicial, NumeroNosInternosFinal, variacaoNumeroNos)
    
    for i in range(len(VariacaoNos)):
        DeltaX=comprimentoTubo/(VariacaoNos[i]+1)

        A,b= Matriz(comprimentoTubo,VariacaoNos[i],deltaT,DeltaX, Ci, Ce, alfa)

        solucaoInicial = np.zeros(len(b))
        precisao = 1e-6
        QuantidadeMaximaIteracoes = 150

        C_N = []

        T=np.arange(tempoInicial,tempoFinal,1)

        for j in range(len(T)):
            vetorSolucaoSistema = GaussJacobi(A, b, solucaoInicial,precisao, QuantidadeMaximaIteracoes)
            C_N.append(vetorSolucaoSistema)
            CN=np.insert(C_N,0,Ce,axis=1)
            b = vetorSolucaoSistema  

        comprimentoTubo = float(comprimentoTubo)
        comprimentotubo=[k*comprimentoTubo/tempoFinal for k in range(0,tempoFinal)]
        CN = list(map(lambda x: x[1], CN))
        plt.plot(comprimentotubo,CN, label = 'Nos Iternos='+str(VariacaoNos[i]))

    plt.title("Refinamento DeltaX")  
    plt.xlabel("L(m)")
    plt.ylabel("Concentração(U.C)")
    plt.legend(title='Numero de Nos Internos', loc=0)
    plt.show()

def refinamentoNumeroNosDeltaT(comprimentoTubo,NumeroNosInternos,tempoInicial,tempoFinal,deltaInicial, deltaTFinal,passoDeltaT, Ci, Ce, alfa):
   
    DeltaT=np.arange(deltaInicial,deltaTFinal, passoDeltaT)
    
    for i in range(len(DeltaT)):
        DeltaX=comprimentoTubo/(DeltaT[i]+1)

        A,b= Matriz(comprimentoTubo,NumeroNosInternos,DeltaT[i],DeltaX, Ci, Ce, alfa)

        solucaoInicial = np.zeros(len(b))
        precisao = 1e-6
        QuantidadeMaximaIteracoes = 150

        C_N = []

        T=np.arange(tempoInicial,tempoFinal,1)

        for j in range(len(T)):
            vetorSolucaoSistema = GaussJacobi(A, b, solucaoInicial,precisao, QuantidadeMaximaIteracoes)
            C_N.append(vetorSolucaoSistema)
            CN=np.insert(C_N,0,Ce,axis=1)
            b = vetorSolucaoSistema  

    
        comprimentoTubo = float(comprimentoTubo)
        comprimentotubo=[k*comprimentoTubo/tempoFinal for k in range(0,tempoFinal)]
        CN = list(map(lambda z: z[1], CN))
        plt.plot(comprimentotubo,CN, label = 'DeltaT='+str(DeltaT[i]))

    plt.title("Refinamento DeltaT")  
    plt.xlabel("L(m)")
    plt.ylabel("Concentração(U.C)")
    plt.legend(title='Variação DeltaT', loc=0)
    plt.show()

def SensibilidadeAlfa(comprimentoTubo,NumeroNosInternos,tempoInicial,tempoFinal,deltaT,DeltaX, Ci, Ce, alfaInicial, alfaFinal, passoAlfa):
    Alfas=np.arange(alfaInicial, alfaFinal, passoAlfa)

    for i in range(len(Alfas)):

        A,b= Matriz(comprimentoTubo,NumeroNosInternos,deltaT,DeltaX, Ci, Ce, Alfas[i])

        solucaoInicial = np.zeros(len(b))
        precisao = 1e-6
        QuantidadeMaximaIteracoes = 150

        C_N = []

        T=np.arange(tempoInicial,tempoFinal,1)

        for j in range(len(T)):
            vetorSolucaoSistema = GaussJacobi(A, b, solucaoInicial,precisao, QuantidadeMaximaIteracoes)
            C_N.append(vetorSolucaoSistema)
            CN=np.insert(C_N,0,Ce,axis=1)
            b = vetorSolucaoSistema  

    
        comprimentoTubo = float(comprimentoTubo)
        comprimentotubo=[k*comprimentoTubo/tempoFinal for k in range(0,tempoFinal)]

        CN = list(map(lambda z: z[1], CN))
        plt.plot(comprimentotubo,CN, label = 'Alfa='+str(Alfas[i]))

    plt.title("Sensibilidade Variação Alfa")   
    plt.xlabel("L(m)")
    plt.ylabel("Concentração(U.C)")
    plt.legend(title='Alfa', loc=0)
    plt.show()
  
def SensibilidadeCe(comprimentoTubo,NumeroNosInternos,tempoInicial,tempoFinal,deltaT,DeltaX, Ci,CeInicial, CeFinal,passoCe, alfa):
    
    CE=np.arange(CeInicial,CeFinal,passoCe)

    for i in range(len(CE)):
        A,b= Matriz(comprimentoTubo,NumeroNosInternos,deltaT,DeltaX, Ci, CE[i], alfa)

        solucaoInicial = np.zeros(len(b))
        precisao = 1e-6
        QuantidadeMaximaIteracoes = 150

        C_N = []

        T=np.arange(tempoInicial,tempoFinal,1)

        for j in range(len(T)):
            vetorSolucaoSistema = GaussJacobi(A, b, solucaoInicial,precisao, QuantidadeMaximaIteracoes)
            C_N.append(vetorSolucaoSistema)
            CN=np.insert(C_N,0,CE[i],axis=1)
            b = vetorSolucaoSistema  

    
        comprimentoTubo = float(comprimentoTubo)
        comprimentotubo=[k*comprimentoTubo/tempoFinal for k in range(0,tempoFinal)]
        CN = list(map(lambda x: x[1], CN))
        plt.plot(comprimentotubo,CN, label = 'Ce='+str('{:.2f}'.format(CE[i])))
    
    plt.title("Sensibilidade Variação Ce")   
    plt.xlabel("L(m)")
    plt.ylabel("Concentração(U.C)")
    plt.legend(title='Ce', loc=0)
    plt.show()
   


# GraficoTodasSolucoes(comprimentoTubo,NumeroNosInternos,tempoInicial,tempoFinal, Ci, Ce, alfa)
GraficoTodasSolucoes(20,115,0,30,2,0.5,2*10**(-3))

#refinamentoNumeroNos(comprimentoTubo,NumeroNosInternosInicial,NumeroNosInternosFinal, variacaoNumeroNos,tempoInicial,tempoFinal,deltaT, Ci, Ce, alfa)
refinamentoNumeroNos(20,100,130,5,0,30,5,2,0.5,2*10**(-3))

#refinamentoNumeroNosDeltaT(comprimentoTubo,NumeroNosInternos,tempoInicial,tempoFinal,deltaInicial, deltaTFinal,passoDeltaT, Ci, Ce, alfa)
refinamentoNumeroNosDeltaT(20,115,0,30,0,50,5,2,0.5,2*10**(-3))

#SensibilidadeAlfa(comprimentoTubo,NumeroNosInternos,tempoInicial,tempoFinal,deltaT,DeltaX, Ci, Ce, alfaInicial, alfaFinal, passoAlfa)
SensibilidadeAlfa(20,115,0,30,5,0.1,2,0.5,2*10**-3,7*10**-3,1*10**-3)

#SensibilidadeCe(comprimentoTubo,NumeroNosInternos,tempoInicial,tempoFinal,deltaT,DeltaX, Ci,CeInicial, CeFinal,passoCe, alfa)
SensibilidadeCe(20,115,0,30,5,0.1,2,0.1,0.5,0.1,2*10**(-3))

