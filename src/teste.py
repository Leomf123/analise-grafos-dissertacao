import numpy as np
import pandas as pd

from utils import gerar_matriz_distancias
from algoritmos_adjacencias import gerar_matriz_adjacencias
from algoritmos_peso import gerar_matriz_pesos
from utils import definir_medida_distancia
from utils import normalizar_dados, retornar_sigma, checar_matrix_adjacencias
from gravar import gravar_resultados
from analiseGrafos import metricasGrafo


def teste(indice_inicio, indice_fim, datasets, K, Adjacencia, Ponderacao, Quantidade_rotulos, Quantidade_experimentos):
    
    dataset = datasets[indice_inicio:indice_fim]
    print(dataset)

    test_ID = 0
    # 1 - Para cada dataset
    for nome_dataset in dataset:

        print("Dataset: ", nome_dataset)
        # Lendo dados
        df = pd.read_csv('data/' + nome_dataset, header=None)

        # Conversão para numpy
        dados = df.to_numpy()
        # Separando rótulos dos dados
        ultima_coluna = dados.shape[1] - 1
        rotulos = np.array(dados[:,ultima_coluna], dtype='int64')
        dados = np.array(dados[:,:ultima_coluna])
        # Pegar classes
        classes = np.unique(rotulos)

        # Normalizar dados
        dados = normalizar_dados(nome_dataset, dados)

        # medida_distancia = 'euclidean'
        medida_distancia = definir_medida_distancia(nome_dataset)
        matriz_distancias = gerar_matriz_distancias(dados, dados, medida_distancia)
        
        del df
        # 2 - Para cada valor de K
        for k in K:

            # 3 - Para cada algoritmo de adjacencia
            for adjacencia in Adjacencia:
                # Gerar matriz de adjacencia
                matriz_adjacencias = gerar_matriz_adjacencias(dados, matriz_distancias, medida_distancia, k, adjacencia)

                # Usado no RBF
                sigma = retornar_sigma(matriz_distancias, k)

                # 4 - Para cada ponderação
                for ponderacao in Ponderacao:

                    if adjacencia in ["MST", "mutKNN", "symKNN", "symFKNN", "SKNN", "MKNN"] and ponderacao in ["BB-0.01", "BB-0.05", "BB-0.1"]:
                        break

                    # Gerar matriz pesos
                    if ponderacao == "BB-0.01":
                        alpha = 0.01
                    elif ponderacao == "BB-0.05":
                        alpha = 0.05
                    else:
                        alpha = 0.1
                    matriz_pesos = gerar_matriz_pesos(dados, matriz_adjacencias, matriz_distancias, sigma, k, alpha, ponderacao)

                    simetrica, conectado, positivo = checar_matrix_adjacencias(matriz_pesos)

                    nArestas, grauMedio, grauMaximo, grauMinimo, verticesIsolados, diametro, coefClustering = metricasGrafo(matriz_pesos)

                    # gravar resultado em uma linha usando pandas
                    gravar_resultados(indice_fim, test_ID, nome_dataset, k, adjacencia, ponderacao, nArestas, grauMedio, grauMaximo, grauMinimo, verticesIsolados, diametro, coefClustering)

                    #print("test_ID: ", test_ID)

                    test_ID += 1
    print('Fim Testes: ', test_ID)
