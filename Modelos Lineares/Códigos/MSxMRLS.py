import numpy as np
import matplotlib.pyplot as plt

x = [720,720,720,730,730,740,740,740,750,750,750,750,760,760,760,770,770,780,780,780,780,790,790,790]
y = [257,263,266,269,271,275,274,278,278,275,280,284,281,286,289,293,297,295,299,299,301,296,303,308]

N = len(x)

somatorioX = 0.0 #somatorio de xi
somatorioXX=0.0 #somatorio de xi^2
somatorioY = 0.0 #somatorio de yi
somatorioXY= 0.0 #somatorio de xi*yi
somatorioYiYchapeu2 = 0.0 #(yi-y_chapeu)**2
somatorioXiXmedio2= 0.0 #(xi-x_medio)**2
somatorioYiYmedio2 = 0.0 #(yi-y_medio)**2
var2 = 0.0 #variancia do MSxMRLS
SQReg= 0.0 
SQT  = 0.0


for i in range(N):
    somatorioX += x[i]
    somatorioXX += x[i]**2
    somatorioY += y[i]
    somatorioXY += x[i] * y[i]


b_chapeu = (somatorioXY -  somatorioY*somatorioX/N)/(somatorioXX - (somatorioX)**2/N)
a_chapeu = ((somatorioY/N) ) - (b_chapeu/N) * somatorioX
beta_0 = a_chapeu
beta_1 = b_chapeu
y_medio = somatorioY/N
x_medio = somatorioX/N


print("Somatorio de x:",somatorioX)
print("Somatorio de x^2:",somatorioXX)
print("Somatorio de y: ",somatorioY)
print("Somatorio de x*y:",somatorioXY)
print("beta0:", beta_0)
print("beta1:", beta_1)

for i in range(N):
    y_chapeu = (beta_0 + beta_1*x[i]) 
    somatorioYiYchapeu2 += (y[i]-y_chapeu)**2
    somatorioXiXmedio2 += (x[i]-x_medio)**2
    somatorioYiYmedio2 += (y[i]- y_medio)**2
    # print("y_chapeu=",y_chapeu)
    
 
var2 = (somatorioYiYchapeu2)/(N-2)    
SQReg = (beta_1**2)*somatorioXiXmedio2
SQT = somatorioYiYmedio2
SQE = SQT - SQReg
F_0 = SQReg/(SQE/(N-2))



print("variancia quadrada: ", var2)
print("x_medio:", x_medio)
print("(x_i - x_medio)^2:", somatorioXiXmedio2)
print("SQReg: ", SQReg)
print("Y_medio:", y_medio)
print("(y_i - y_medio)^2:", somatorioYiYmedio2)
print("SQT: ", SQT)
print("SQE: ", SQE)
print("F_0: ", F_0)