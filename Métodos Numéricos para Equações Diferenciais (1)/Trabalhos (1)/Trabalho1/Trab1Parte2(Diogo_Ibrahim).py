import numpy as np
import matplotlib.pyplot as plt
import random




def MontaMatriz(C_0,C_N, NumeroNosInternos, L, K, D):
    DeltaX = L/(NumeroNosInternos+1)
    s = DeltaX**2 * K/D
    X= np.arange(DeltaX,L,DeltaX)   
    #colocar os iniciais aq tbm
    x = [0 for i in range(NumeroNosInternos+2)] 
    x[0] = 0
    x[NumeroNosInternos+1] = L
    for i in range(0,len(X)):
        x[i+1] = X[i]
    # print("x", x)
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
    # print("A",'\n',A,'\n')
    # print("B",'\n', B,'\n')

    return A,B,X, x

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
    i=0
     
    while i<=2500:
        C = GaussSeidel(a, solucaoInicial, b)
        i=i+1
    c = [0 for i in range(NumeroNosInternos+2)] 
    c[0] = C_0
    c[NumeroNosInternos] = C_N
    for i in range(0,len(C)):
        c[i+1] = C[i]

    # print('c',c)
   
    # print("Sistema", Sistema)
    # plt.plot(Sistema[2], C)
    # plt.xlabel("Delta X")
    # plt.ylabel("Concentração")
    # plt.show()

    return Sistema[3], C,c


def Results(C_0,C_N, NumeroNosInternos, L, K, D):
    Results = Solver(C_0,C_N, NumeroNosInternos, L, K, D)
    print("Concentracoes:",'\n')
    for i in range(len(Results[0])):
        print('C'+str(i+1)+" = ",Results[2][i])
    print("\n")

    plt.plot(Results[0], Results[2], color='#8a2be2')
    plt.xlabel("L(m)")
    plt.ylabel("Concentração(U.C)")
    plt.title("Concentração x Comprimento")
    plt.show()

def Refinamento(C_0,C_N, L, K, D, NumeroNosInternosInicio, NumeroNosInternosFinal):
    for i in range(NumeroNosInternosInicio, NumeroNosInternosFinal+1):
        Color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])

        Sistema1 = Solver(C_0,C_N, i, L, K, D)
        plt.plot(Sistema1[0], Sistema1[2], color = Color, label = 'Nos Iternos='+str(i))
        plt.legend(title='Numero de Nos Internos', loc=0)
        plt.title('Refinamento de Malha')
        plt.xlabel("L(m)")
        plt.ylabel("Concentração(U.C)")
    plt.show()
        
            
def Sensibilidade(C_0,C_N, NumeroNosInternos, L, K, D, passoK, passoD):
    d = [D-2*passoD, D-passoD, D, D+passoD, D+2*passoD]
    k = [K-2*passoK, K-passoK, K, K+passoK, K+2*passoK]
    # Marker = ['','o','*','',"D",'1','','','o','*','',"D",'1','','','o','*','',"D",'1','','','o','*','',"D",'1','']
    for i in range(0, len(k)):
        # print("BBB","\n")
        Color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        SolverK = Solver(C_0,C_N, NumeroNosInternos, L, k[i], D)
        plt.plot(SolverK[0], SolverK[2], color=Color, label="K="+str(k[i]))
        plt.xlabel("L(m)")
        plt.ylabel("Concentração(U.C)")
        plt.title("Sensibilidade Variação de K")
        plt.legend(title="K", loc=0)
    plt.show()
    for i in range(0, len(d)):
        # print("AAA","\n")
        Color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        SolverD = Solver(C_0,C_N, NumeroNosInternos, L, K, d[i])
        plt.plot(SolverD[0], SolverD[2], color=Color, label="D="+str(d[i]))
        plt.xlabel("L(m)")
        plt.ylabel("Concentração(U.C)")
        plt.title("Sensibilidade Variação de D")
        plt.legend(title="D", loc=0)
    plt.show()

C_0 = 0.1  #condiçao de contorno em x=0
C_N = 0  #condição de contorno em x=L
NumeroNosInternos = 30
L= 4  #comprimento total do tubo
K = 4*10**(-6) 
D = 2*10**(-6)
NumeroNosInternosInicio = 25   #refinamento de malha
NumeroNosInternosFinal = 35   #refinamento de malha
passoK = 0.9*10**(-6)  #analise de sensibilidade
passoD = 0.9*10**(-6) #analise de sensibilidade

# Solver(C_0,C_N, NumeroNosInternos, L, K, D)
# Results(C_0,C_N, NumeroNosInternos, L, K, D)
# Refinamento(C_0,C_N, L, K, D,NumeroNosInternosInicio,NumeroNosInternosFinal)
Sensibilidade(C_0,C_N, NumeroNosInternos ,L, K, D, passoK, passoD)