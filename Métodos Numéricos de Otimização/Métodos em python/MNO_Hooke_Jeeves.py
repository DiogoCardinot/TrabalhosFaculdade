from sympy import *
import math as math

x = symbols('x')


def metodo_newton(x1, x2):
    funcao = (x1-2)**4+(x1-2*x2)**2 # função a ser minimizada
    a = 0.0 # ponto inicial
    iteracoes = 1
    b = 0.0 # b do metodo
    erro = 0.0001 # erro para o método de newton

    while True:
        b = a - (diff(funcao).subs(x, a)/diff(diff(funcao)).subs(x, a)) # primeira iteracao

        # critério de parada
        if abs(b-a) > erro:
            a = b
            iteracoes += 1

        else:
            break

    return a 


def HookeJevees():
    x_0 = [0, 3] # ponto inicial
    it = 1
    numerodeiteracoes=10
    erro = 0.05 # erro estipulado para hooke jeeves

    while True:
        d1 = [1, 0] # d1 do metodo
        d2 = [0, 1] # d2 do metodo
        y_1 = x_0.copy() # y1 do metodo(y1=x0)
        y_2 = [0, 0] # y2 que recebe y_1+ λ1*d1
        y_3 = [0, 0] # y3 recebe y_2+ λ2*d2
        y1 = [0,0] #inicialização de variáveis
        y2 = [0,0] #inicialização de variáveis
        y3 = [0, 0] #inicialização de variáveis
        d = [0, 0] # d que recebe y3-y1
        x1 = [0, 0] # novo intervalo
        for i in range(0, len(y_1)): 
            y1[i] = y_1[i] + x*d1[i] 

        # minimização para obter λ1 com os parâmetros atualizados
        lambda1 = metodo_newton(y1[0], y1[1])
        print('λ1:', lambda1)

        for i in range(0, len(y_1)):
            y_2[i] = y_1[i] + lambda1*d1[i] 
            y2[i] =  y_2[i] + x*d2[i] 
        
        # minimização para obter λ2 com os parâmetros atualizados
        lambda2 = metodo_newton(y2[0], y2[1])
        print('λ2:', lambda2)
        
        #cálculo do y3(y3 = y2+λ2*d2)
        for i in range(0, len(y_1)):
            y_3[i] =  y_2[i] + lambda2*d2[i] 

        for i in range(0, len(y_1)):
            d[i] = y_3[i] - y_1[i]
        
        for i in range(0, len(y_1)):
            y3[i] = y_3[i] + x*d[i] 
            
        # minimização para obter λchapéu com os parâmetros atualizados
        lambda_chapeu = metodo_newton(y3[0], y3[1])
        print('λ_chapeu:', lambda_chapeu)

        
        for i in range(0, len(y_1)):
            y_3[i] =  y_3[i] + lambda_chapeu*d[i] #cálculo do novo intervalo
            x1[i] = y_3[i] 

        print("Novo intervalo:", x1)
        print('-----------------------------------------------------------------')

        # critério de parada
        if math.sqrt((x1[0]-x_0[0])**2+(x1[1]-x_0[1])**2) < erro or it > numerodeiteracoes or abs(lambda1) < 0.0000000001 or abs(lambda2) < 0.0000000001:
            print('Ponto de Mínimo da função:', x1)
            print('Número de iterações:', it)
            break

        else:
            for i in range(0, len(y_1)):
                x_0[i] = x1[i]  # atualização para o novo intervalo

        it += 1


HookeJevees()
