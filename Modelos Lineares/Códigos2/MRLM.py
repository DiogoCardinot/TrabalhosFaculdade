import numpy as np

x_1 = [31,16,29,19,27,21,24,11,26,18,12,3]
x_2 = [4,5,3,0,2,6,2,3,6,6,1,5]
y= [12,13,3,3,11,19,1,14,15,17,2,15]

linhas = len(x_1)

vec_X = np.array([np.array(x_1), np.array(x_2)]) #vetor com os x_n (adicionar vetores aqui quando precisar)

colunas = (len(vec_X) + 1)

X = np.ones((linhas, colunas)) #cria uma matriz com 1
# print("Matriz de um:", matriz)

for i in range(linhas):
    for j in range(colunas):  
        if j!=0 : #j=0 é a primeira coluna que deve ser de 1  
            X[i][j] = vec_X[j-1][i] #adiciona os valores na matriz
            
print(X)            
x_t = X.T #X Transposta
print("Matriz X Transposta:\n",x_t);
print("\n");
x_tx = np.dot(x_t,X) #multiplicação X Transposta * X
print("X_transposta * X:\n", x_tx)
print("\n");
x_txI = np.linalg.inv(x_tx) #inversa da multiplicação X Transposta * X
print("Inversa de (X_transposta * X):\n", x_txI)
print("\n");
A = np.dot(x_txI, x_t) # multiplicação da inversa com X transposta
print("Inversa de (X_transposta * X) * X_transposta:\n", A)
print("\n");
B = np.dot(A,y) #matriz resultante beta
print("beta: ", B)


for i in range(len(B)):
    print("Beta",i, ":", B[i])





