from itertools import cycle
import numpy as np
import matplotlib.pyplot as plt

cycol = cycle('bgrcmk')


def MontaMatriz(C_0,C_N, NumeroNosInternos, L, K, D):
    DeltaX = L/(NumeroNosInternos+1)
    s = DeltaX**2 * K/D
    x= np.arange(DeltaX,L-DeltaX,DeltaX)
    X=[0 for i in range(len(x)+3)]

    X[0]=0
    X[(len(X)-1)]=X[len(X)-5]+DeltaX
    for i in range(0,len(x)):
        X[i+1]=(x[i])
    #colocar os iniciais aq tbm
    A=[[0 for x in range(NumeroNosInternos)]for y in range(NumeroNosInternos)]
    for i in range(NumeroNosInternos):
        for j in range(NumeroNosInternos):
            if(i==j and j==0):
                A[i][j] = 2+s
                A[i][j+1]= -1
                continue

            if(i==j and j==(NumeroNosInternos-1)):
                A[i][j] = 2+s
                A[i][j-1]= -1
                continue

            if(i==j):
                A[i][j] = 2+s
                A[i][j+1]= -1
                A[i][j-1]= -1
        

    B=[0 for x in range(NumeroNosInternos)]
    B[0] = C_0
    B[NumeroNosInternos-1] = C_N

    return A,B,X

def GaussSeidel(a, SolucaoInicial ,b):
    n = len(a)                   
    
    for j in range(0, n):        
        temp = b[j]                  
          
        for i in range(0, n):     
            if(j != i):
                temp-=a[j][i] * SolucaoInicial[i]      
        SolucaoInicial[j] = temp / a[j][j]      
    return SolucaoInicial   
   

def Solver(C_0,C_N, NumeroNosInternos, L, K, D):
    Sistema = MontaMatriz(C_0,C_N, NumeroNosInternos, L, K, D)
                        
    solucaoInicial = [0.5 for i in range(len(Sistema[0]))]                        
    a = Sistema[0]
    b = Sistema[1]

    for i in range(0, 2500):            
        C = GaussSeidel(a, solucaoInicial, b)
    # tem que voltar o C inicial e final
    c=[]
    for i in range(NumeroNosInternos+2):
        c.append(0)
    c[0]=C_0
    c[NumeroNosInternos+1]=C_N
    for i in range(0,NumeroNosInternos):
        c[i+1]=(C[i])
       
    for i in range(len(c)):
        print('C'+str(i+1)+" = ",c[i])
    print("\n")
    return Sistema[2], c

def SolveWithGraph(C_0,C_N, NumeroNosInternos, L, K, D):
    C=Solver(C_0,C_N, NumeroNosInternos, L, K, D)
    plt.plot(C[1], C[0])
    plt.xlabel("Delta X")
    plt.ylabel("Concentração")
    plt.show()

def Refinamento(C_0,C_N, L, K, D, iInicial, iFinal):
    for i in range(iInicial, iFinal+1):
        Color = next(cycol)
        Sistema1 = Solver(C_0,C_N, i, L, K, D)
        plt.plot(Sistema1[0], Sistema1[1], color = Color, label = 'Nos Iternos='+str(i))
        plt.legend(title='Numero de Nos Internos', loc=0)
        plt.xlabel("Delta X")
        plt.ylabel("Concentração")

    plt.show()
        
            
def Sensibilidade(C_0,C_N, NumeroNosInternos, L, K, D, passoK, passoD):
    d = [D-2*passoD, D-passoD, D, D+passoD, D+2*passoD]
    k = [K-2*passoK, K-passoK, K, K+passoK, K+2*passoK]
    # Marker = ['','o','*','',"D",'1','','','o','*','',"D",'1','','','o','*','',"D",'1','','','o','*','',"D",'1','']
    for i in range(0, len(d)):
        # print("BBB","\n")
        Color = next(cycol)
        SolverK = Solver(C_0,C_N, NumeroNosInternos, L, k[i], D)
        plt.plot(SolverK[0], SolverK[1], color=Color, label="K="+str(k[i]))
        plt.legend(title="K", loc=0)
    plt.show()
    for i in range(0, len(k)-1):
        # print("AAA","\n")
        Color = next(cycol)
        SolverD = Solver(C_0,C_N, NumeroNosInternos, L, K, d[i])
        plt.plot(SolverD[0], SolverD[1], color=Color, label="D="+str(d[i]))
        plt.legend(title="D", loc=0)
    plt.show()

C_0 = 0.1
C_N = 0
NumeroNosInternos = 20
L= 4
K = 8*10**(-6)
D = 2*10**(-6)
iInicial = 3
iFinal = 6
passoK = 1*10**(-6)
passoD = 0.5*10**(-6) 

SolveWithGraph(C_0,C_N, NumeroNosInternos, L, K, D)
# Refinamento(C_0,C_N, L, K, D,iInicial,iFinal)
# Sensibilidade(C_0,C_N, NumeroNosInternos ,L, K, D, passoK, passoD)