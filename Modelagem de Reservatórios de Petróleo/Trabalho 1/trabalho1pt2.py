import math 
import matplotlib.pyplot as plt
import numpy as np

import mpmath

V=[0.08333,-32.08333,1279,-15623.666,84244.1666,-236957.5,375911.666,-340071.666,164062.5,-32812.5]


passo_tempo=0.001
numero_passos=1000
n=10
a=1
tempo=[]
F=[]
for j in range(1,numero_passos+1):
    tempo.append(j*passo_tempo)
    
    soma=0.0

    for i in range(1,n+1):
        s=(np.log(2)/tempo[j-1])*i
       
        F_Laplace=(a)/((s**2)+(a**2)) 
     
        soma=soma+(V[i-1]*F_Laplace)
       
    F.append((np.log(2)/tempo[j-1])*soma)

plt.plot(tempo,F)
plt.ylim(0,0.9)
plt.xlim(0,1)
plt.show()
