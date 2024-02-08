from turtle import color
import numpy as np
import matplotlib.pyplot as plt

deltaT = 0.5
t_inicial = 0
t_final=20
t=np.arange(t_inicial, t_final, deltaT)


deltaT_inicial=0.1
deltaT_final = 0.5
DeltaT= np.arange(deltaT_inicial, deltaT_final, 0.1)

# print(DeltaT)
eixoY=[]
f=[len(t)]


def dfdt(t,f):
    dfdt= 4*np.e**(0.8*t)-0.5*f
    return dfdt

for i in range(t_inicial, len(t)-1):
    f[0]=2
    k1= dfdt(t[i],f[i])
    k2= dfdt(t[i]+ deltaT/2, f[i] + k1*deltaT/2)
    k3= dfdt(t[i]+ deltaT, f[i]-k1*deltaT + 2*k2*deltaT)
    eixoY.append(f[i] + (1/6)*(k1+4*k2+k3)*deltaT)
    f.append(eixoY[i])

    
    
# print("Fn", f[i])   
print(eixoY)

# plt.plot(t,f)
# plt.xlabel("Tempo(s)")
# plt.ylabel("F(n)")
# plt.plot(f,f, color='black')
# plt.show()

