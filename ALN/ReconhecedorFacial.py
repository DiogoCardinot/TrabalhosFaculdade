from os import listdir
from random import sample

import cv2
import numpy as np
import pandas as pd
import sklearn.decomposition as decomp
from numpy import linalg


def CarregarImagens(caminho, formatoImagens):
    imagens = listdir(caminho)
    baseDados = {}

    for imagem in imagens:
        if formatoImagens in imagem:
            pessoa_id, imagemId = imagem.removesuffix(formatoImagens).split('-')
           
            if pessoa_id not in baseDados.keys():
                baseDados[pessoa_id] = []

            baseDados[pessoa_id].append(
                cv2.cvtColor(cv2.imread(f'{caminho}/{imagem}'),
                             cv2.COLOR_BGR2GRAY).reshape(1, -1))

    return baseDados


def SepararTreinoTeste(baseDados):
    baseDadosTreino = {}
    baseDadosTeste = {}

    for pessoa_id, imagens in baseDados.items():
        indicesTreino = sample(range(len(imagens)), len(imagens) - 1)
        baseDadosTreino[pessoa_id] = [imagens[i] for i in indicesTreino]

        indicesTeste = [i for i in range(
            len(imagens)) if i not in indicesTreino]
        baseDadosTeste[pessoa_id] = [imagens[i] for i in indicesTeste]

    return baseDadosTreino, baseDadosTeste

def SepararTreinoTesteBonus(baseDados):
    baseDadosTreino = dict() #cria o dicionário que irá conter as imagens de treino
    baseDadosTeste = dict() # cria o dicionário que irá conter as imagens de teste

    for pessoaId, imagens in baseDados.items(): #para cada pessoa no dicionario de imagens
        indicesTreino = sample(range(1,len(imagens)), len(imagens)-1)#supondo que temos n imagens de cada pessoa, ele seleciona n-1 imagens para treino, partindo da imagem 1, e deixa uma de fora para teste
        baseDadosTreino[pessoaId] = [imagens[i] for i in indicesTreino]#define o vetor de treino usando todas as imagens que foram escolhidas para treino na linha acima

        indicesTeste = [0]#pega a primeira imagem de cada pessoa para teste
        baseDadosTeste[pessoaId] = [imagens[i] for i in indicesTeste]# adiciona cada imagem de teste no vetor de testes

    return baseDadosTreino, baseDadosTeste


def definePCA(baseDadosTreino, n_components):
    pca = decomp.PCA(n_components=n_components)

    arrayBaseDadosTreino = []
    for imagens in baseDadosTreino.values():
        for imagem in imagens:
            arrayBaseDadosTreino.append(pd.DataFrame(imagem))
    matriz = pd.concat(arrayBaseDadosTreino)
    pca.fit(matriz)

    return pca


def PCA(pca, imagem):
    return pca.transform(imagem)


def CalculaDistancia(baseDadosTreino, usar_PCA, PCA, test_img):
    imagem_identificada = []
    distancia = np.inf
    pessoa = ''

    for pessoa_id, imagens in baseDadosTreino.items():
        for imagem in imagens:
            if usar_PCA:
                normaDistancia = linalg.norm(PCA(imagem) - PCA(test_img))
            else:
                normaDistancia = linalg.norm(imagem - test_img)
            if normaDistancia < distancia:
                distancia = normaDistancia
                imagem_identificada = imagem
                pessoa = pessoa_id

    return distancia, imagem_identificada, pessoa


def TaxaAcerto(baseDadosTreino, baseDadosTeste, usar_PCA, PCA, CalculaDistancia):
    acertos = 0
    falhas = 0

    for pessoa_id, imagens in baseDadosTeste.items():
        for imagem in imagens:
            distancia, imagem_identificada, pessoa = CalculaDistancia(baseDadosTreino, usar_PCA, PCA, imagem)
            if pessoa == pessoa_id:
                acertos += 1
            else:
                falhas += 1

    return acertos / (acertos + falhas) * 100


def Teste(caminho, usar_PCA, repeticoes):
    media = 0
    for i in range(repeticoes):
        baseDados = CarregarImagens(caminho, '.jpg')
        baseDadosTreino, baseDadosTeste = SepararTreinoTeste(baseDados)

        if usar_PCA:
            pca = definePCA(baseDadosTreino, n_components=5)
            media += TaxaAcerto(baseDadosTreino, baseDadosTeste, usar_PCA, lambda x: PCA(pca, x), CalculaDistancia)
        else:
            media += TaxaAcerto(baseDadosTreino, baseDadosTeste, usar_PCA, None, CalculaDistancia)

    media = round(media / repeticoes, 2)
    print('Reconhecimento utilizando: ',caminho)
    if usar_PCA:
        print(f'PCA com ', repeticoes, ' repeticoes')
    else:
        print(f'Forca Bruta com ', repeticoes, ' repeticoes')
    print('Taxa de acerto: ', media, "%", '\n')

def TesteBonus(caminho, usar_PCA, repeticoes):
    media = 0
    for i in range(repeticoes):
        baseDados = CarregarImagens(caminho, '.jpg')
        baseDadosTreino, baseDadosTeste = SepararTreinoTesteBonus(baseDados)

        if usar_PCA:
            pca = definePCA(baseDadosTreino, n_components=5)
            media += TaxaAcerto(baseDadosTreino, baseDadosTeste, usar_PCA, lambda x: PCA(pca, x), CalculaDistancia)
        else:
            media += TaxaAcerto(baseDadosTreino, baseDadosTeste, usar_PCA, None, CalculaDistancia)

    media = round(media / repeticoes, 2)
    print('Reconhecimento utilizando: ',caminho, "para Teste Bonus")
    if usar_PCA:
        print(f'PCA com ', repeticoes, ' repeticoes')
    else:
        print(f'Forca Bruta com ', repeticoes, ' repeticoes')
    print('Taxa de acerto: ', media, "%", '\n')



repeticoes = 10
print('\tIniciando reconhecimento\n')

paths = ['./recdev-master/very-easy', './recdev-master/easy',
'./recdev-master/medium', './recdev-master/hard', './recdev-master/extras/facebookfaces2/crop-outer']

Teste(paths[3], usar_PCA=False, repeticoes=repeticoes)
Teste(paths[3], usar_PCA=True, repeticoes=repeticoes)

caminhoBonus = './recdev-master/hardBonus'
TesteBonus(caminhoBonus, usar_PCA=False, repeticoes=repeticoes)
TesteBonus(caminhoBonus, usar_PCA=True, repeticoes=repeticoes)