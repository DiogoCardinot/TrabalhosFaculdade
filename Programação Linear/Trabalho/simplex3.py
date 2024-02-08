import numpy as np
from numpy import linalg as LA 
from numpy.linalg import inv

def simplex_iteration(A, b, C, m: int, n: int):
    Iteration=0
    Z=0
    X=np.zeros((n+m))
    XB=np.zeros((m))
    CB=np.zeros((m))
    XN=np.zeros((n))
    CN=np.zeros((n))
    RC = np.zeros((n+m))
    Basis:int=np.zeros((m))
    B = np.zeros((m,m))
    NB = np.zeros((m,n))
    Index_Enter=-1
    Index_Leave=-1
    eps = 0

    for i in range(0,m):
        Basis[i]=n+i  #Quais variáveis estão na base, lembrar que começa de 0
        for j in range(0,m):
         B[i, j]=A[i,n+j]
        for j in range(0,n):
         NB[i, j]=A[i,j]

    for i in range(0,n):
        CN[i]=C[i]
        # print("CN: ", CN[i]) 
        
    # print("C", C)
    # print("CB", NB.transpose())
    # print("Coeficiente das basicas:", CB)
    # print("Basicas:", B)
    # print("Inversa das básicas", inv(B).transpose())

    
    basicasInversa = inv(B)
    basicasInversaTransposta = basicasInversa.transpose()
    naoBasicaTransposta = NB.transpose()
    NbT_basicasInversaT = np.dot(naoBasicaTransposta,basicasInversaTransposta)
    print("nao basicas * basica inversa transposta", NbT_basicasInversaT)
    NbTbasicasInversaB = np.dot(NbT_basicasInversaT,CB)
    print('nao basicas t * basica inversa t * coeficiente das basicas:', NbTbasicasInversaB)
    NbT_basicasInversa_B_T = NbTbasicasInversaB.transpose()
    print("nao basicas t * basica inversa t * coeficiente das basicas certa:", NbT_basicasInversa_B_T)
    RC= CN- NbTbasicasInversaB.transpose(); 
    print("gama:", RC)
    
    MaxRC=0
    for i in range(0,n):
        if(MaxRC<RC[i]):
         MaxRC=RC[i]
         Index_Enter=i
        if(MaxRC<=0):
            break
        
    
    # print(MaxRC)
    # print("Basis", Basis+1)
    
    

C=np.array([[5],[2],[0],[0],[0]])
A=np.array([[1,2,1,0,0],[1,0,0,1,0],[0,1,0,0,1]])
b=np.array([[9],[3],[4]])

Z,X,RC=simplex_iteration(A,b,C,3,2)  #entra as restrições, coluna b, coeficientes, tamanho da base(coluna), tamanho da não base(coluna)

print("Z", Z)
print("X",X)
print("RC",RC)