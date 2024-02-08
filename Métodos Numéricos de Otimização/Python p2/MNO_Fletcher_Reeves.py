import math as math
from sympy import *

x = symbols("x")
x1  = symbols('x1')
x2 = symbols('x2')

def funcao(x1,x2):
    return (x1-2)**4 + (x1-2*x2)**2 # função a ser minimizada (MUDAR AQUI)

def Newton(x1, x2):
    func = funcao(x1,x2) 
    a = 0.0 # ponto inicial
    it = 0
    b = 0.0 # b do metodo
    erro = 0.01 # erro

    while True:
        derivada1= diff(func).subs(x, a)
        derivada2 = diff(diff(func)).subs(x, a)
        b = a - (derivada1/derivada2) # primeira iteração
        # criterio de parada
        if abs(b-a) > erro:
            a = b
            it += 1

        else:
            return b 


def Gradiente(a, b):
    
    func = funcao(x1,x2)
    grad_x1 = diff(func, x1).subs(x1, a).subs(x2, b)
    grad_x2 = diff(func, x2).subs(x1, a).subs(x2, b)
    gradiente = [-grad_x1, -grad_x2]
    
    return gradiente


def FletcherReeves():
    x_0 = [0, 3] # ponto inicial
    it = 1 
    numerodeiteracoes = 10
    j = 1
    erro = 0.0001 # erro estipulado para fletcher reeves (MUDAR AQUI)
    d_1=[0, 0]

    while True:
        y_1 = x_0.copy() # y1=x0
        y_2 = [0, 0] # y2 que recebe o valor de y_1+λ1*d_1
        y1 = [0,0] # y1 que recebe  y_1+ λ*d1   
        d = [0, 0] # d do metodo
        x1 = [0, 0] # x1 do metodo
        
        
        if j % 2 == 0: 
            #d para a segunda parte de cada iteração
            d = Gradiente(y_1[0],y_1[1]) 
            
            alfa = ((math.sqrt(d[0]**2 + d[1]**2))**2)/ ((math.sqrt(d_1[0]**2 + d_1[1]**2))**2)
           
            for i in range(0, len(y_1)):
                d[i]= d[i] + alfa*d_1[i]
            
        else:
            #d para a primeira parte de cada iteração
            d = Gradiente(y_1[0],y_1[1])
        
        for i in range(0, len(y_1)): 
                y1[i] =  y_1[i] + x*d[i] 

        # minimizaçao para obter λ 
        lambda1 = Newton(y1[0], y1[1])
        print('λ: ', lambda1)

        for i in range(0, len(y_1)):
            y_2[i] = y_1[i] + lambda1*d[i] 
                
        for i in range(0, len(y_1)):
            x1[i] = y_2[i]
        
             
        
        print("Novo Intervalo:", x1, "na iteração:", it)  
        print("---------------------------------------------------------------------------")
        
        # criterio de parada
        criterio_parada = Gradiente(x1[0], x1[1])

        if math.sqrt(criterio_parada[0]**2 + criterio_parada[1]**2) < erro or abs(lambda1) < 0.0001 or it > numerodeiteracoes:
            print('Ponto de Mínimo da função:', x1)
            print('Número de iterações:', it)
            return False

        else:
            d_1 = d.copy()
            for i in range(0, len(y_1)):
                x_0[i] = x1[i]
                
        j+=1
        it += 1   

FletcherReeves()