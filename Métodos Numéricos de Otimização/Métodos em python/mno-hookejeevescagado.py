import numpy as np
import sympy as sp
from sympy import *
init_printing(use_unicode=True)

λ = sp.symbols('λ')
x = sp.symbols('x')
y = sp.symbols('y')
x1x = sp.symbols('x1x')
x1y = sp.symbols('x1y')

def funcao(x,y):
    return ((x-2)**4 +(x-2*y)**2)
x0=0
y0=3
erro=0.005
erro1=0.05
d1x=1
d1y=0
d2x=0
d2y=1

j=0
niteracoes=5

while(1>0):
    if(j==0):
        erro1==1
        x1x=0
        x1y=0
        x=10
        y=10
    else:
        x1x=x1x
        x1y=x1y
        x=x
        y=y
    
    while(sqrt((x-x1x)**2+(y-x1y)**2) >erro1 or j<niteracoes):
        #PRIMEIRA PARTE(BUSCA EXPLORATÓRIA)
    
        if(j==0):
            y1x=x0
            y1y=y0
            d=y1x+λ*d1x
            d1=y1y+λ*d1y
            print("x0=""%.2f" % y1x)
            print("y0=""%.2f" % y1y)
        else:
            y1x=x
            y1y=y
            print("x0=""%.2f" % y1x)
            print("y0=""%.2f" % y1y)
            d=x1x+λ*d1x
            d1=x1y+λ*d1y
            print("DDDDDDDDDDDDDDDDDDDDD",d)
            print("DDDDDDDDDDDDDDDDDDDDD",d1)
        #f(y1+λd1)
        funcao1= funcao(d, d1)
        print(funcao1)

        #Método de Newton
        #intervalo de restrição
        λ0 =0.0

        i=0
        numerodeiteracoes=10

        while(i<(numerodeiteracoes)):
            derivada1 = diff(funcao1,λ).subs(λ,λ0)
            derivada2 = diff(funcao1, λ, 2).subs(λ,λ0)

            λ1=(λ0-(derivada1/derivada2))
            if(abs(λ1-λ0) > erro or abs(derivada1) > erro):
                λ0=λ1
                #print(λ0)
            else: 
                break
            i=i+1         
        print('Converge para o ponto λ1='"%.2f" % λ0)
        if(j==0):
        #Componente x e y de y2=y1+λ0d1
            y2x=y1x+ λ0*d1x
            y2y=y1y+ λ0*d1y
            print("y2x=""%.2f" % y2x)
            print("y2y=""%.2f" % y2y)
        if(j>0):
            y2x=x1x+ λ0*d1x
            y2y=x1y+ λ0*d1y
    
        #a2x=y2+λd2(componente x)
        a2x=y2x+λ*d2x
        #a2y=y2+λd2(componente y)
        a2y=y2y+λ*d2y

        #f(y2+λd2)
        funcao2=funcao(a2x,a2y)

        print("Funcao(y2+λ*d2):", funcao2)

        #Método de Newton novamente
        i=0
        numerodeiteracoes=10

        while (i<(numerodeiteracoes)):
            derivada1 = diff(funcao2,λ).subs(λ,λ0)
            derivada2 = diff(funcao2, λ, 2).subs(λ,λ0)

            λ1=(λ0-(derivada1/derivada2))
            if((abs(λ1-λ0) > erro or abs(derivada1) > erro)):
                λ0=λ1
                #print(λ0)
            else: 
                break
            i=i+1         
        print('Converge para o ponto λ2='"%.2f" % λ0)


        #Componente x e y de y3
        y3x=y2x+ λ0*d2x
        y3y=y2y+ λ0*d2y

        x=y3x
        y=y3y

        #print("xxxxxxxxxx", x)
        #print("xxxxxxxxxx", y)


        print("Componente x de y3=""%.2f" % y3x)
        print("Componente y de y3=""%.2f" % y3y)

        #SEGUNDAPARTE(BUSCA PADRÃO)
    
        Dx=y3x-y1x
        Dy=y3y-y1y
        #print("Dx=", Dx)
        #print("Dy=", Dy)
        print("Comp x de d=""%.2f" % Dx)
        print("Comp y de d=""%.2f" % Dy)
    
        #a3x=y3+λd(componente x)
        a3x=y3x+λ*Dx
        #a3y=y3+λd(componente y)
        a3y=y3y+λ*Dy

        print("a3x=", a3x)
        print("a3y=",  a3y)

        funcao3=funcao(a3x,a3y)
        print("funcao3=" ,funcao3)
        #Método de Newton novamente
        i=0
        numerodeiteracoes=10

        while (i<(numerodeiteracoes)):
            derivada1 = diff(funcao3,λ).subs(λ,λ0)
            derivada2 = diff(funcao3, λ, 2).subs(λ,λ0)

            λ1=(λ0-(derivada1/derivada2))
            if(abs(λ1-λ0) > erro or abs(derivada1) > erro):
                λ0=λ1
                #print(λ0)
            else: 
                break
            i=i+1         
        print('Converge para o ponto λchapeu='"%.2f" % λ0)

        x1x=y3x+λ0*Dx
        x1y=y3y+λ0*Dy
    
        j=j+1
        print('-----------------------------------------------------------------------------')
        print("Novo intervalo:""%.2f" % x1x,"%.2f" %x1y)

