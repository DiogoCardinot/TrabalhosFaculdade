import numpy as np

# def GaussJacobi(A, B, VetorSolucao, iteracoes):
#     iteracao=0
#     vetorAuxiliar = []
#     for k in range(len(VetorSolucao)):
#         vetorAuxiliar.append(0)

#     while iteracao<iteracoes:
#         for i in range(len(A)):
#             x=B[i]
#             for j in range(len(A)):
#                 if i!=j:
#                     x-=A[i][j]*VetorSolucao[j]
#             x/=A[i][i]
#             vetorAuxiliar[i]=x
#         iteracao+=1
#         for p in range(len(vetorAuxiliar)):
#             VetorSolucao[p]= vetorAuxiliar[p]

#     print(VetorSolucao)


# A = [[1,1,-3,1],[-5,3,-4,1],[1,1,2,-1],[1,2,1,1]]
# B = [2,0,1,12]
# C=[0,0,0,0]
# GaussJacobi(A,B,C, 1000)

# from pprint import pprint
# from numpy import array, zeros, diag, diagflat, dot

# def jacobi(A,b,N=25,x=None):
#     """Solves the equation Ax=b via the Jacobi iterative method."""
#     # Create an initial guess if needed                                                                                                                                                            
#     if x is None:
#         x = zeros(len(A[0]))

#     # Create a vector of the diagonal elements of A                                                                                                                                                
#     # and subtract them from A                                                                                                                                                                     
#     D = diag(A)
#     R = A - diagflat(D)

#     # Iterate for N times                                                                                                                                                                          
#     for i in range(N):
#         x = (b - dot(R,x)) / D
#     return x

# A = array([[1,1,1,-3],[2,3,-4,-2],[2,7,-3,1],[2,1,1,-1]])
# b = array([3,9,7,3])
# guess = array([0,0,0,0])

# sol = jacobi(A,b,N=25,x=guess)

# print("A", A)
# print("b", b)
# print('x', sol)



#------------------------------------------------------------
# Declaração da função que calculará a solução do sistema de equação lineares usadno o método de Gauss-Jacobi

# def Gauss_Jacobi(A, b, x0, N, tolerancia):
#     linha_A, coluna_A = A.shape     #atribuição das dimensões da matriz A à duas variáveis
#     x_novo = np.zeros(b.shape)     #declaração do vetor que armazenará os novos valores das incógnitas
#     erro = np.zeros(b.shape)     #declaração do vetor que armazenará o erro relativo de cada incógnita
#     n = 0     #contador do número de iterações no laço while
#     while n<=N:
#         for l in range(linha_A):     #o contador l percorrerá as linhas da matriz A
#             soma = 0     #variável que armazenará a soma dos termos (A_ij)*(x_j) com i != j
#             for c in range(coluna_A):     #o contador c percorrerá as colunas da matriz A
#                 if (l != c):
#                     soma += A[l,c]*x0[c]     #atualização da variável soma
#             x_novo[l] = (1/A[l,l])*(b[l]-soma)     #atualização dos valores das incógnitas
#             erro[l] = abs((x_novo[l]-x0[l])/(x0[l]))     #cálculo do erro relativo de cada incógnita
#         diferenca = max(erro)     #variável que armazenará o máximo valor do vetor de erro
#         if diferenca < tolerancia:     #critério de parada
#             break
#         else:
#             x0 = x_novo.copy()     #atualização do vetor x0 em caso de falha do critério de parada
#         n += 1     #atualização do contador do laço while
#     return x_novo   


# A = np.array([[10, 2, 1],
#               [1, 5, 1],
#               [2, 3, 10]])

# b = np.array([7, -8, 6])

# x0 = [1, 1, 1]

# N = 100

# tolerancia = 10**(-7)

# solucao = Gauss_Jacobi(A, b, x0, N, tolerancia)

# print(solucao)



#--------------------------------------------------------------------------------------------------------------------
# def jacobi(A, b, tolerance=1e-10, max_iterations=10000):
    
#     x = np.zeros_like(b, dtype=np.double)
    
#     T = A - np.diag(np.diagonal(A))
    
#     for k in range(max_iterations):
        
#         x_old  = x.copy()
        
#         x[:] = (b - np.dot(T, x)) / np.diagonal(A)
        
#         if np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < tolerance:
#             break
            
#     print(x)

# A = np.array([[1,1,1,-3],[2,3,-4,-2],[2,7,-3,1],[2,1,1,-1]])

# b = np.array([3,9,7,3])
# jacobi(A,b,1e-10, 10000)



# Defining our function as seidel which takes 3 arguments
# as A matrix, Solution and B matrix
   
def seidel(a, x ,b):
    #Finding length of a(3)       
    n = len(a)                   
    # for loop for 3 times as to calculate x, y , z
    for j in range(0, n):        
        # temp variable d to store b[j]
        d = b[j]                  
          
        # to calculate respective xi, yi, zi
        for i in range(0, n):     
            if(j != i):
                d-=a[j][i] * x[i]
        # updating the value of our solution        
        x[j] = d / a[j][j]
    # returning our updated solution           
    return x    
   
# int(input())input as number of variable to be solved                
n = 3                              
a = []                            
b = []        
# initial solution depending on n(here n=3)                     
x = [0, 0, 0,0]                        
a = [[1,1,1,-3],[2,3,-4,-2],[2,7,-3,1],[2,1,1,-1]]
b = [3,9,7,3]
print(x)
  
#loop run for m times depending on m the error value
for i in range(0, 25):            
    x = seidel(a, x, b)
    #print each time the updated solution
    print(x)      