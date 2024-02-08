import numpy as np

α=0.618
a=0
b=3
erro= 0.005

it=0
numerodeiteracoes = 100
def funcao(x):
    return (x**3 - 3*x - 3)
      

while(it > numerodeiteracoes or (abs(b-a))>erro):
    
    f_a=funcao(a)
    f_b=funcao(b)
    x=(a+(1-α)*(b-a))
    μ=(a+α*(b-a))
    f_x=funcao(x)
    f_μ=funcao(μ)
   
    if(f_x > f_μ):
        a=x
        f_a=f_x 
         
    else:
        b=μ
        f_b=f_μ
              
    it += 1
    
    
    print('O intervalo é a:', a, 'e b:', b, "na iteração: ", it) 
    print("-------------------------------------------------------------------------------------------------------")   

print('O intervalo desejado é a:', a, 'e b:', b)
print('O ponto desejado é:', (a+b)/2)




