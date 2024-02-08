import numpy as np

y=[]
x_1 = [31,16,29,19,27,21,24,11,26,18,12,3]
x = [4,5,3,0,2,6,2,3,6,6,1,5]
y= [12,13,3,3,11,19,1,14,15,17,2,15] #y Transposta

N = len(x)

# for i in range(N):
#     y.append(x[i]**3)
    
print("y: ", y)  
somatorioX = 0.0
somatorioY = 0.0
somatorioXiXmedioYiYmedio = 0.0
somatorioXiXmedio2 = 0.0
somatorioYiYmedio2 = 0.0

for i in range(N):
    somatorioX += x[i]
    somatorioY += y[i]
    
x_medio = somatorioX/N 
y_medio = somatorioY/N 
    
for i in range(N):
    somatorioXiXmedioYiYmedio += (x[i]-x_medio)*(y[i]-y_medio)
    somatorioXiXmedio2 += (x[i]-x_medio)**2
    somatorioYiYmedio2 += (y[i]-y_medio)**2
    
coefCor = (somatorioXiXmedioYiYmedio)/np.sqrt(somatorioXiXmedio2*somatorioYiYmedio2)
T = coefCor*np.sqrt(N-2) / (np.sqrt(1-(coefCor)**2))


print("X_medio: ", x_medio)
print("Y_medio: ", y_medio)
print('Somatorio (xi-x_medio)(yi-y_medio): ', somatorioXiXmedioYiYmedio)
print("Somatorio (xi-x_medio)^2: ", somatorioXiXmedio2)
print("Somatorio (yi-y_medio)^2: ", somatorioYiYmedio2)
print("coeficienteCorrelacao Chapeu:", coefCor)
print("T: ", T)