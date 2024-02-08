
import numpy as np
import matplotlib.pyplot as plt
# from sympy import symbols, Eq, solve

# def MontaConcentracao(C_0,C_N, NumeroNosInternos, DeltaX, K, D):
#     C=[0 for i in range(NumeroNosInternos)]
#     C[0]= C_0
#     C[NumeroNosInternos-1] = C_N

#     print(C)
#     s = DeltaX**2 * K/D

#     for i in range(1,NumeroNosInternos-1):
#        C[i]= 'C'+str(i)

#     print(C)
#     for i in range(NumeroNosInternos):
#         X = '-'+str(C[i])+'+'+str(C[i-1])+'-'+str(C[i-2])
#         print(X)


# MontaConcentracao(0.1,0,10,0.2,2,1)


def MontaMatriz(C_0,C_N, NumeroNosInternos, L, K, D):
    DeltaX = L/NumeroNosInternos
    s = DeltaX**2 * K/D
    X= np.arange(0,L,DeltaX)    
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
    print("A",'\n',A,'\n')
    print("B",'\n', B,'\n')

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
   

# Sistema= MontaMatriz(0.1,0,20,4,2,1)  
C_0 = 0.1
C_N = 0
NumeroNosInternos = 20
L= 4
K = 8*10**(-6)
D = 2*10**(-6)



Sistema = MontaMatriz(C_0,C_N, NumeroNosInternos, L, K, D)
                       
solucaoInicial = [0.5 for i in range(len(Sistema[0]))]                        
a = Sistema[0]
b = Sistema[1]

  
for i in range(0, 2500):            
    C = GaussSeidel(a, solucaoInicial, b)

    
for i in range(len(C)):
    print('C'+str(i+2)+" = ",C[i])


# MontaConcentracao(C_0,C_N, NumeroNosInternos, DeltaX, K, D)
# MontaMatriz(0.1,0,10,0.2,2,1)

plt.plot(Sistema[2], C)
plt.show()