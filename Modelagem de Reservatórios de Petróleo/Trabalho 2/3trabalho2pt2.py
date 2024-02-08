import numpy as np
import matplotlib.pyplot as plt

s_inicial = 0.008
s_final = 0.9
s_w = np.arange(s_inicial, s_final, 0.008)

m_w = 0.8*10**(-3)
m_o = 1*10**(-3)
k_o = []
k_w = []
derivada = []
swf = 0.6
x=[]
SW =[]
tempo= 1000000000000
phi =0.2
q_t = 5*10**(-3)
A = 1

def calculaX():
    for i in range(len(s_w)):
        
        k_o.append(0.7*((1-s_w[i])**2))
        k_w.append(0.5*s_w[i]**2)

        if s_w[i]>=swf:
            derivada.append((-1400*s_w[i]**2+1400*s_w[i])/(2809*s_w[i]**4-5936*s_w[i]**3+6104*s_w[i]**2-3136*s_w[i]+784)) 
            SW.append(s_w[i])
    ##insere no 0 prq o maior sw deve estar com o menor x
    SW.insert(0, s_inicial)
    SW.insert(0, s_inicial)
    print(SW)
        
    for j in range(len(derivada)):
        x.append((q_t*tempo/ A*phi)*derivada[j])
    x.insert(0, x[0]) 
    x.insert(0,x[0]+ 0.5*x[0])
  
    
    print(x)
    plt.plot(x,SW)
    plt.show()
    # print('derivada',x)
    

calculaX()
