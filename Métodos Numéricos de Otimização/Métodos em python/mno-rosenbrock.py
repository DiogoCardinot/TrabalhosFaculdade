import sympy as sympy
import math as math
import numpy as np

x = sympy.Symbol('x')


def metodo_newton(x_1, x_2):
    funcao = (x_1-2)**4+(x_1-2*x_2)**2 # funcao a ser minimizada
    a = 0.0 # ponto inicial
    it = 0
    b = 0.0 # b do metodo
    erro = 0.00000000001 # erro para o método de newton

    while True:
        b = a - (sympy.diff(funcao).subs(x, a)/sympy.diff(sympy.diff(funcao)).subs(x, a)) # primeira iteracao

        # criterio de parada
        if abs(b-a) > erro:
            a = b
            it += 1
            
        else:
            return a
        
      

def Rosenbrock():
    x_0 = [0, 3] # ponto inicial
    it = 1
    erro = 0.05 # erro estipulado para rosenbrock
    d_1 = [1, 0] # d1 inicial
    d_2 = [0, 1] # d2 inicial
    a_1=[0,0] #inicialização de variáveis
    b_1=[0,0] #inicialização de variáveis
    a_2=[0,0] #inicialização de variáveis
    b_2=[0,0] #inicialização de variáveis
    
    while True:
        y_1 = x_0.copy() # y1 do metodo
        y_2 = [0, 0] # y2 do metodo
        y_3 = [0, 0] # y3 do metodo
        y1 = [0,0] # y1 que recebe y_1+ λ1*d1
        y2 = [0,0] # y2 que recebe y_2+ λ2*d2
       
        for i in range(0, len(y_1)): 
            y1[i] = y_1[i] + x*d_1[i]
       
        # minimizaçao para obter λ1 com os parâmetros atualizados
        lambda_1 = metodo_newton(y1[0], y1[1])
        print('λ1:', lambda_1)

        for i in range(0, len(y_1)):
            y_2[i] = y_1[i] + lambda_1*d_1[i] 
            y2[i] = y_2[i] + x*d_2[i]
        
        # minimizaçao para obter λ2 com os parâmetros atualizados
        lambda_2 = metodo_newton(y2[0], y2[1])
        print('λ2:', lambda_2)
        
        for i in range(0, len(y_1)):
            y_3[i] = y_2[i] + lambda_2*d_2[i] 

        #calculo do a1
        for i in range(0, len(y_1)):
            if(lambda_1 == 0):
                a_1[i]= d_1[i]
            
            else:
                a_1[i]= lambda_1*d_1[i] + lambda_2*d_2[i]
            
        b_1=a_1.copy()
        
        for i in range(0, len(y_1)):
            d_1[i]= b_1[i]/(math.sqrt(b_1[0]**2 + b_1[1]**2)) #calculo d1(barra)
            a_2[i]= lambda_2*d_2[i] #calculo do a2
        
        for i in range(0, len(y_1)): 
            k=((a_2[0]* d_1[0])+(a_2[1]* d_1[1]))  #multiplicação do a2 com a transposta de d1(barra)
            b_2[i]= a_2[i] - (k*d_1[i]) #calculo b2
        
        for i in range(0, len(y_1)):
            d_2[i]= b_2[i]/(math.sqrt(b_2[0]**2 + b_2[1]**2)) #calculo d2(barra)

        print("Novo Intervalo: ", y_3) 
        print("-----------------------------------------------------------------")
            
                

        # criterio de parada
        if math.sqrt((y_3[0]-x_0[0])**2+(y_3[1]-x_0[1])**2) < erro or abs(lambda_1) < 0.0000000001 or abs(lambda_2) < 0.0000000001 :
            print('Ponto Mínimo da função:', y_3)
            print('Número de iterações:', it)
            break
  
        else:
            for i in range(0, len(y_1)):
                x_0[i] = y_3[i] # atualização para o novo intervalo

        it += 1


Rosenbrock()
