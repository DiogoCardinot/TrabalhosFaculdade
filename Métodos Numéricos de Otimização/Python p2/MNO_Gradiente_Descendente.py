import math as math
from sympy import *

x = symbols('x')
x1  = symbols('x1')
x2 = symbols('x2')
#x1=x
#x2=y

def funcao(x1,x2):
    return (x1-x2**3)**2 + 3*(x1-x2)**4  # função a ser minimizada (MUDAR AQUI)

def Newton(x1, x2):
    func = funcao(x1,x2) 
    a = 0.0 # ponto inicial
    iteracoes = 1
    b = 0.0 # b do metodo
    erro = 0.01 # erro para o método de newton

    while True:
        derivada1= diff(func).subs(x, a)
        derivada2 = diff(diff(func)).subs(x, a)
        b = a - (derivada1/derivada2) # primeira iteração

        # critério de parada
        if abs(b-a) > erro:
            a = b
            iteracoes += 1

        else:
            return b


def Gradiente(a, b):
    
    func = funcao(x1,x2)  
    grad_x1 = diff(func, x1).subs(x1, a).subs(x2, b)
    grad_x2 = diff(func, x2).subs(x1, a).subs(x2, b)
    gradiente = [-grad_x1, -grad_x2] #gradiente já negativo para o método
    
    return gradiente
    
    
def GradienteDescendente():
    x_0 = [2, 1] # ponto inicial
    it = 1
    numerodeiteracoes = 100
    erro = 0.01 # erro estipulado para gradiente descendente (MUDAR AQUI)

    while True:
        y_1 = x_0.copy() # y1=x0
        y_2 = [0, 0] # y2 que recebe o valor de y_1+λ1*d_1
        y1 = [0,0] # y1 que recebe  y_1+ λ*d1
        d = [0, 0] #inicialização de variáveis
        x_1 = [0, 0] #inicialização de variáveis (x1=y_2)

        d = Gradiente(y_1[0], y_1[1])

        for i in range(0, len(y_1)): 
            y1[i] = y_1[i] + x*d[i]

        # minimizaçao para obter λ 1
        lambda1 = Newton(y1[0], y1[1])
        print('λ:', lambda1)

        for i in range(0, len(y_1)):
            y_2[i] =  y_1[i] + lambda1*d[i] 

        for i in range(0, len(y_1)):
            x_1[i] = y_2[i]

       
        print("Novo Intervalo:", x_1, "na iteração:", it)  
        print("---------------------------------------------------------------------------")

        # criterio de parada
        criterio_parada = Gradiente(x_1[0], x_1[1])

        if math.sqrt(criterio_parada[0]**2 + criterio_parada[1]**2) < erro or it > numerodeiteracoes or abs(lambda1) < 0.00000001:
            print('Ponto de Mínimo da função:', x_1)
            print('Número de iterações:', it)
            break

        else:
            for i in range(0, len(y_1)):
                x_0[i] = x_1[i]

        it += 1


GradienteDescendente()
