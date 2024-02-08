from sympy import *
import math as math
import numpy as np

x = symbols('x')


def metodo_newton(x1, x2):
    funcao = (x1-2)**4+(x1-2*x2)**2 # função a ser minimizada (MUDAR AQUI)
    a = 0.0 # ponto inicial
    iteracoes = 1
    b = 0.0 # b do metodo
    erro = 0.00000000001 # erro para o método de newton

    while True:
        derivada1= diff(funcao).subs(x, a)
        derivada2 = diff(diff(funcao)).subs(x, a)
        b = a - (derivada1/derivada2) # primeira iteração

        # critério de parada
        if abs(b-a) > erro:
            a = b
            iteracoes += 1

        else:
            return a
        
def Rosenbrock():
    x_0 = [0, 3] #intervalo inicial  (MUDAR AQUI)
    it = 1
    numerodeiteracoes = 10
    erro = 0.05 # erro estipulado para rosenbrock (MUDAR AQUI)
    d1 = [1, 0] # d1 inicial
    d2 = [0, 1] # d2 inicial
    a1 = [0,0] #inicialização de variáveis
    b1 = [0,0] #inicialização de variáveis
    a2 = [0,0] #inicialização de variáveis
    b2 = [0,0] #inicialização de variáveis
    
    while True:
        y_1 = x_0.copy() # y1=x0
        y_2 = [0, 0] # y2 que recebe o valor de y_1+λ1*d_1
        y_3 = [0, 0] # y3 que recebe o valor de y_2+λ2*d_2
        y1 = [0,0] # y1 que recebe  y_1+ λ*d1
        y2 = [0,0] # y2 que recebe  y_2+ λ*d2
       
        for i in range(0, len(y_1)): 
            y1[i] = y_1[i] + x*d1[i]
       
        # minimização para obter λ1 com os parâmetros atualizados
        lambda1 = metodo_newton(y1[0], y1[1])
        print('λ1:', lambda1)

        for i in range(0, len(y_1)):
            y_2[i] = y_1[i] + lambda1*d1[i] 
            y2[i] = y_2[i] + x*d2[i]
        
        # minimização para obter λ2 com os parâmetros atualizados
        lambda2 = metodo_newton(y2[0], y2[1])
        print('λ2:', lambda2)
        
        for i in range(0, len(y_1)):
            y_3[i] = y_2[i] + lambda2*d2[i] 

        #cálculo do a1
        for i in range(0, len(y_1)):
            if(lambda1 == 0):
                a1[i]= d1[i]
            
            else:
                a1[i]= lambda1*d1[i] + lambda2*d2[i]
            
        b1=a1.copy()
        
        for i in range(0, len(y_1)):
            d1[i]= b1[i]/(math.sqrt(b1[0]**2 + b1[1]**2)) #cálculo do d1(barra)
            a2[i]= lambda2*d2[i] #cálculo do a2
        
        for i in range(0, len(y_1)): 
            k=((a2[0]* d1[0])+(a2[1]* d1[1]))  #multiplicação do a2 com a transposta de d1(barra)
            b2[i]= a2[i] - (k*d1[i]) #cálculo do b2
        
        for i in range(0, len(y_1)):
            d2[i]= b2[i]/(math.sqrt(b2[0]**2 + b2[1]**2)) #cálculo do d2(barra)

        print("Novo Intervalo:", y_3, "na iteração:", it) 
        print("---------------------------------------------------------------------------")
            
                

        # critério de parada
        if math.sqrt((y_3[0]-x_0[0])**2+(y_3[1]-x_0[1])**2) < erro or it > numerodeiteracoes or abs(lambda1) < 0.00000001 or abs(lambda2) < 0.00000001 :
            print('Ponto de Mínimo da função:', y_3)
            print('Número de iterações:', it)
            break
  
        else:
            for i in range(0, len(y_1)):
                x_0[i] = y_3[i] # atualização para o novo intervalo

        it += 1


Rosenbrock()
