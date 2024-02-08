from sympy import *

x = symbols('x')


def funcao(x1, x2):
    return (x1-2)**2 + (x1 - (2*x2))**2 # função a ser minimizada (MUDAR AQUI)

def SimplexNelderMead():
    x1 = [0,3] #ponto inicial
    x2 = [0.00025, 3] #ponto inicial
    x3 = [0, 3.05] #ponto inicial
    it = 1
    numerodeiteracoes = 9
    erro = 0.01  # erro estipulado para o método de simplex de nelder mead

    while True:
        fx1 = funcao(x1[0], x1[1])
        fx2 = funcao(x2[0], x2[1])
        fx3 = funcao(x3[0], x3[1])
        centroide = [0, 0] 
        Xr = [0, 0]
        NovoXb = [0, 0]
        Xc = [0, 0]

        
        
        if (fx1 > fx2 > fx3):
            Xw = x1
            Xl = x2
            Xb = x3
        
        if (fx3 > fx2 > fx1):
            Xw = x3
            Xl = x2
            Xb = x1
        
        if (fx1 > fx3 > fx2):
            Xw = x1
            Xl = x3
            Xb = x2
        
        if (fx3 > fx1 > fx2):
            Xw = x3
            Xl = x1
            Xb = x2

        if (fx2 > fx3 > fx1):
            Xw = x2
            Xl = x3
            Xb = x1

        if (fx2 > fx1 > fx3):
            Xw = x2
            Xl = x1
            Xb = x3  

        for i in range(0, len(centroide)):
            centroide[i] = (1/2)*(Xb[i]+Xl[i])

        for i in range(0, len(centroide)):
            Xr[i] = centroide[i] + 1*(centroide[i]-Xw[i])

        if (funcao(Xw[0], Xw[1]) > funcao(Xr[0], Xr[1]) > funcao(Xb[0], Xb[1])):
            Xw = Xr

        if (funcao(Xr[0], Xr[1]) < funcao(Xb[0], Xb[1])):
            for i in range(0, len(centroide)):
                NovoXb[i] = centroide[i] + 2*(Xr[i] - centroide[i])
            Fxr = funcao(Xr[0], Xr[1])
            FNovoXb = funcao(NovoXb[0], NovoXb[1])

            if Fxr > FNovoXb:
                Xw = NovoXb
            if FNovoXb > Fxr:
                Xw = Xr

        if (funcao(Xr[0], Xr[1]) > funcao(Xw[0], Xw[1])):
            for i in range(0, len(centroide)):
                Xc[i] = centroide[i] + 0.5*(Xw[i] - centroide[i])
            Fxc = funcao(Xc[0], Xc[1])
            Fxw = funcao(Xw[0], Xw[1])

            if Fxc < Fxw:
                Xw = Xc
            if Fxc > Fxw:
                Xw = Xw


        x1 = Xw
        x2 = Xl
        x3 = Xb
        print("Novos pontos na iteração", it)
        print("X1: ", Xw)
        print("X2: ", Xl)
        print("X3: ", Xb)
        print("----------------------------------------------------------------")

        if (it > numerodeiteracoes):
            return False

        else:
            it += 1


SimplexNelderMead()
