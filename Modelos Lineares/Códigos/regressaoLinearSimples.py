import numpy as np
import matplotlib.pyplot as plt

beta_0 = -1
beta_1 = 0.5

x = 5
media = 1
variancia = 9

erro = []
y=[]

s = np.random.normal(media, variancia, 1)

print(s)
  
y=beta_0 + beta_1*x + s
print(y)    

    
   
# print("Erro", erro)     
# plt.plot(x,erro)

# plt.figure(figsize=(10, 10))
# plt.plot(x,y, "o", ms = 5)
# plt.title("Y em função de X")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# plt.hist(s,rwidth=0.9)
# plt.title("Histograma do Erro")
# plt.ylabel("Quantidade de Erros")
# plt.xlabel("Grandeza do erro")
# plt.show()
