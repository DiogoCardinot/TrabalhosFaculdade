

# Esperança = sum(x_i*p_i)
# Variância = E[x^2] - (E[x])^2

import numpy as np
import random as rd

tamAmostra = 5;

aleatoryVar= []
probabilidade = []

#gera as variáveis aleatórias, com quantidade pré estipulada
for j in range(0, tamAmostra):
     aleatoryVar.append(rd.random()) # gera valor entre 0 e 1
    #  aleatoryVar.append(rd.randrange(0,100))

sumAleatoryVar = sum(aleatoryVar)

# Pega o numero aleatorio da posicao j e divide pela soma, no final, a soma dessa divisao vai dar 1 prq o somatorio de aleatoryVar[j] = sumAleatoryVar
for j in range(0, tamAmostra):
    probabilidade.append(aleatoryVar[j] / sumAleatoryVar)
    
esperanca = 0   

for j in range(0, tamAmostra):
    esperanca += aleatoryVar[j] * probabilidade[j]
    
 
esperancaXQuad=0 
for j in range(0, tamAmostra):
    esperancaXQuad += ((aleatoryVar[j]**2) * probabilidade[j]) 
    
variancia = esperancaXQuad - (esperanca**2)   
    
        
print("Numero de Amostras: ", tamAmostra)
print("Variavel Aleatoria: ", aleatoryVar)
print("Probabilidade: ", probabilidade)
print("Esperanca: ", esperanca)
print("Variancia: ", variancia)
# print(sum(probabilidade))
