import numpy as np
from sympy import *

x= symbols('x')

#intervalo de restrição
x0 =0.0 #valor inicial
erro= 0.01 #erro desejado

def funcao(x):
    return ((44*x-2)**4 + (92*x-6)**2)

iteracoes=1
numerodeiteracoes=10

while True or (iteracoes<(numerodeiteracoes)):
    derivada1 = diff(funcao(x),x).subs(x,x0)
    derivada2 = diff(funcao(x), x, 2).subs(x,x0)

    x1= (x0-(derivada1/derivada2))
    if(abs(x1-x0) > erro or abs(derivada1) > erro):
        x0= x1
        print("lambda na iteração" , iteracoes , ":" , x0)
    else: 
        break
    iteracoes +=1   
        
print('Converge para o ponto λ=', x0)
print('Número de iterações:', iteracoes)