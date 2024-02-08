import random

    
import matplotlib.pyplot as plt
 
import  numpy as np
import string

def solucaoAleatoria(tsp):
    cidades = list(range(len(tsp)))
    solucao = []

    for i in range(len(tsp)):
        cidadeAleatoria = cidades[random.randint(0, len(cidades) - 1)]
        solucao.append(cidadeAleatoria)
        cidades.remove(cidadeAleatoria)

    return solucao

def comprimentoRota(tsp, solucao):
    comprimentoRota = 0
    for i in range(len(solucao)):
        comprimentoRota += tsp[solucao[i - 1]][solucao[i]]
    return comprimentoRota

def pegaVizinhos(solucao):
    vizinhos = []
    for i in range(len(solucao)):
        for j in range(i + 1, len(solucao)):
            vizinho = solucao.copy()
            vizinho[i] = solucao[j]
            vizinho[j] = solucao[i]
            vizinhos.append(vizinho)
    return vizinhos

def pegaMelhorVizinho(tsp, vizinhos):
    melhorComprimentoRota = comprimentoRota(tsp, vizinhos[0])
    melhorVizinho = vizinhos[0]
    for viz in vizinhos:
        comprimentoRotaAtual = comprimentoRota(tsp, viz)
        if comprimentoRotaAtual < melhorComprimentoRota:
            melhorComprimentoRota = comprimentoRotaAtual
            melhorVizinho = viz
    return melhorVizinho, melhorComprimentoRota

def hillClimbing(tsp):
    solucaoAtual = solucaoAleatoria(tsp)
    comprimentoRotaAtual = comprimentoRota(tsp, solucaoAtual)
    vizinhos = pegaVizinhos(solucaoAtual)
    melhorVizinho, melhorVizinhoComprimentoRota = pegaMelhorVizinho(tsp, vizinhos)

    while melhorVizinhoComprimentoRota < comprimentoRotaAtual:
        solucaoAtual = melhorVizinho
        comprimentoRotaAtual = melhorVizinhoComprimentoRota
        vizinhos = pegaVizinhos(solucaoAtual)
        melhorVizinho, melhorVizinhoComprimentoRota = pegaMelhorVizinho(tsp, vizinhos)
    print(f"A menor distancia e {comprimentoRotaAtual} para a melhor solucao encontrada: ({solucaoAtual})")
    return solucaoAtual, comprimentoRotaAtual

def GeradorDeProblema(nCidades):
    tsp = []
    for i in range(nCidades):
        distancias = []
        for j in range(nCidades):
            if j == i:
                distancias.append(0)
            elif j < i:
                distancias.append(tsp[j][i])
            else:
                distancias.append(random.randint(10, 1000))
        tsp.append(distancias)
    return tsp

def main():
    tsp = [
        [0.0, 3.0, 4.0, 2.0, 7.0],
        [3.0, 0.0, 4.0, 6.0, 3.0],
        [4.0, 4.0, 0.0, 5.0, 8.0],
        [2.0, 6.0, 5.0, 0.0, 6.0],
        [7.0, 3.0, 8.0, 6.0, 0.0]
    ]

    hillClimbing(tsp)




if __name__ == "__main__":
    main()