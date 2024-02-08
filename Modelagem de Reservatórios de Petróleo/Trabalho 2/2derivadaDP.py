import numpy as np
import matplotlib.pyplot as plt

DeltaP = [2290.353795792637, 2428.2570718477605,3272.329248561229, 3273.7644271932436,3411.1377785823056, 3412.0322774344477,3909.6579843053155, 3910.4536333358765,4000.3693869057383, 4001.165158620252]
tempo = [1000,2000,3000,4000,20000,40000,350000,850000,950000,1000000]

derivada = []

def derivadaDp():
    for j in range(1,len(DeltaP)-1):
        L=j-1
        R =j+1
        B1 = ((DeltaP[j] - DeltaP[L])/(np.log(tempo[j]/tempo[L]))) *((np.log(tempo[R]/tempo[j]))/(np.log(tempo[R]/tempo[L]))) 
        B2 = ((DeltaP[R] - DeltaP[j])/(np.log(tempo[R]/tempo[j]))) *((np.log(tempo[j]/tempo[L]))/(np.log(tempo[R]/tempo[L])))
        # print("posicao:", j, "Valor", B1+B2)
        derivada.append(B1+B2)
    print(derivada)
    derivada.insert(0, DeltaP[0])
    derivada.insert(len(DeltaP)-1, DeltaP[len(DeltaP)-1])
    print(derivada)
    
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(tempo,derivada)
    plt.show()


derivadaDp()
