import numpy as np

x_1 = [1,2,3,4,5,6,7,8,9,10]
x_2 = [4,5,3,0,2,6,2,3,6,6,1,5]
Y= [0.08,0.18,0.32,0.53,0.88,1.30,1.95,2.8,3.9,4.6] #y Transposta

# x_2= []#UTILIZAR APENAS QUANDO X2 depender de X1
tamanhoY = len(Y)
linhas = len(x_1)

#UTILIZAR APENAS QUANDO X2 depender de X1
# for i in range(tamanhoY):
#     x_2.append(x_1[i]**2)


vec_X = np.array([np.array(x_1), np.array(x_2)]) #vetor com os x_n (adicionar vetores aqui quando precisar)

colunas = (len(vec_X) + 1)

X = np.ones((linhas, colunas)) #cria uma matriz com 1

for i in range(linhas):
    for j in range(colunas):  
        if j!=0 : #j=0 é a primeira coluna que deve ser de 1  
            X[i][j] = vec_X[j-1][i] #adiciona os valores na matriz
 
        
y = np.array([Y]).T  #y normal    
x_t = X.T #X Transposta
x_tx = np.dot(x_t,X) #multiplicação X Transposta * X
x_txI = np.linalg.inv(x_tx) #inversa da multiplicação X Transposta * X
A = np.dot(x_txI, x_t) # multiplicação da inversa com X transposta
B = np.dot(A,y) #matriz resultante beta
print("beta: ", B)

for i in range(len(B)):
    print("Beta",i, ":", B[i])
print("---------------------------------------------------")
#-----------------------------------------ANOVA---------------------------------------

somatorioY = 0.0

for i in range(tamanhoY):
    somatorioY += y[i]
    
y_medio = somatorioY/tamanhoY

print("y_medio: ", y_medio)
print("---------------------------------------------------")

Ny = tamanhoY*y #N*y

betaT = np.array(B).T  #betaTransposto
Ny2 = tamanhoY*y_medio**2 #N*y_medio**2
yt_y = np.dot(np.array([Y]), y) #y transposta * y (a ordem tá trocada prq y original é a transposta e a transposta é a original)

print("yt * y\n", yt_y)
print("---------------------------------------------------")
yt_X = np.dot(y.T,X)
print("yT * X\n", yt_X)
print("---------------------------------------------------")
yt_X_B = np.dot(yt_X, B)
print("yT * X * Beta\n", yt_X_B)
print("---------------------------------------------------")

SQE = yt_y - yt_X_B
print("SQE:", SQE)
print("---------------------------------------------------")

betaTXT = np.dot(betaT,x_t) #multiplicacao BT*XT
print("Beta T * XT\n", betaTXT)
betaTXTy = np.dot(betaTXT, y) #multiplicacao BT*XT*y
print("Beta T * XT * y\n", betaTXTy)

print("N * y_medio**2: ", tamanhoY* y_medio**2)
SQREG = betaTXTy - tamanhoY* y_medio**2
print("SQREG:", SQREG)
print("---------------------------------------------------")
# SQRT = yt_y - Ny
# print("SQrT:",SQRT)

SQT = SQE+SQREG
print("SQT: ", SQT)
print("---------------------------------------------------")
p = len(B) - 1 #B_0 não entra, por isso -1

F_0 = (SQREG/p)/(SQE/(tamanhoY-2))

print("F_0:", F_0)