import numpy as np
import matplotlib.pyplot as plt

x = [0.05,0.1,0.15,0.2,0.25,0.3,0.4,0.5,0.55,0.60,0.70,0.80,0.85,0.90,0.95]
y = [12.3,15,15.7,16.2,17.1,18,19.2,20.4,21.2,21.9,22.6,23.8,24.2,25.3,26.0]

N = len(x)

somatorioX = 0.0
somatorioXX=0.0
somatorioY = 0.0
somatorioXY= 0.0
somatorioResiduos= 0.0
somatorioYChapeu= 0.0

for i in range(N):
    somatorioX += x[i]
    somatorioXX += x[i]**2
    somatorioY += y[i]
    somatorioXY += x[i] * y[i]


b_chapeu = (somatorioXY -  somatorioY*somatorioX/N)/(somatorioXX - (somatorioX)**2/N)
a_chapeu = ((somatorioY/N) ) - (b_chapeu/N) * somatorioX


print("Somatorio de X:",somatorioX)
print("Somatorio de x^2:",somatorioXX)
print("Somatorio de y: ",somatorioY)
print("Somatorio de x*y:",somatorioXY)
print("a_chapeu:", a_chapeu)
print("b_chapeu:", b_chapeu)
print("A reta do mmq que melhor se ajusta aos dados e y=", a_chapeu, "+" , b_chapeu,"*x")

#Residuos
for i in range(N):
    y_chapeu = (a_chapeu + b_chapeu*x[i]) 
    e = y[i] - y_chapeu
    somatorioResiduos += e
    somatorioYChapeu += y_chapeu
    print("y^=",y_chapeu,"||","e= ",e)
    

print("Somatorio dos Residuos:", somatorioResiduos)
print("Somatorio de Y:", somatorioY)
print("Somatorio de Y chapeu:", somatorioYChapeu)



#Plotando a reta do mmq que melhor se ajusta aos dados fornecidos
X = np.arange(0,100,0.1)
Y = []

for i in range(len(X)):
    Y.append(a_chapeu + b_chapeu*X[i]) 


# plt.plot(X,Y)
# plt.axis([0,100,0,100])
# plt.title("Reta do mmq que melhor se ajusta aos dados")
# plt.xlabel("X")
# plt.ylabel("Y")
# # plt.ylim(0,3)
# plt.show()