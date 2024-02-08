
def funcao(x):
    return x**2 - 6*x + 15


def lbd(a, b):
    return a + 0.382*(b -a)

def mi(a, b):
    return a + 0.618*(b-a)

def metodo_aurea():
    a = 0
    b = 10
    erro = 0.2
    it = 0
    while abs(b-a) > erro:
        valor_lbd = lbd(a, b)
        valor_mi = mi(a, b)
        if funcao(valor_lbd) > funcao(valor_mi):
            a = valor_lbd
        else:
            b = valor_mi
        it += 1
    print ("valor de a:", a)
    print ("valor de b:", b)
    print(it)


metodo_aurea()
