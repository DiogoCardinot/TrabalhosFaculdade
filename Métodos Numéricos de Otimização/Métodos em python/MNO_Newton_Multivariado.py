import numpy as np
import math as math
from sympy import *

x1 =symbols('x1')
x2= symbols('x2')


def funcao():
    return (x1-2)**4 + (x1-2*x2)**2 # função a ser minimizada (MUDAR AQUI)


def Gradiente(a, b):
    func = funcao()
    diff_x1 = diff(func, x1).subs(x1, a).subs(x2, b)
    diff_x2 = diff(func, x2).subs(x1, a).subs(x2, b)
    gradiente = [[float(diff_x1)], [float(diff_x2)]]
    return gradiente


def Hessiana(a, b):
    func = funcao()
    a_11 = diff(diff(func, x1), x1).subs(x1, a).subs(x2, b)
    a_12 = diff(diff(func, x1), x2).subs(x1, a).subs(x2, b)
    a_22 = diff(diff(func, x2), x2).subs(x1, a).subs(x2, b)
    a_21 = diff(diff(func, x2), x1).subs(x1, a).subs(x2, b)
    matrizhessiana = np.array([[float(a_11), float(a_12)], [float(a_21), float(a_22)]])
    inversa = np.linalg.inv(matrizhessiana)
    
    return inversa

def Newton():
    x0 = [0, 3] # ponto inicial
    x1 = [0, 0] #inicialização de variáveis
    erro = 0.1 # erro estipulado para newton (MUDAR AQUI)
    it = 0
    numerodeiteracoes = 10
    
    
    while True:
        hessgrad = np.matmul(Hessiana(x0[0], x0[1]), Gradiente(x0[0], x0[1])) #matriz Hessiana* vetor gradiente

        for i in range(0, len(x0)):
            x1[i] = x0[i] - hessgrad[i][0]

        it += 1

        print("Novo Intervalo:", x1, "na iteração:", it)  
        print("---------------------------------------------------------------------------")

        if math.sqrt((x1[0]-x0[0])**2+(x1[1]-x0[1])**2) < erro or it > numerodeiteracoes:
            print('Ponto de Mínimo da função:', x1)
            print('Número de iterações:', it)
            break
        else: 
            for i in range(0, len(x0)):
                x0[i] = x1[i]
Newton()