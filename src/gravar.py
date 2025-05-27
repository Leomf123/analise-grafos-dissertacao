import pandas as pd

def gravar_resultados(indice_dataset, test_ID, nome_dataset, k, adjacencia, ponderacao, nArestas, grauMedio, grauMaximo, grauMinimo, verticesIsolados, diametro, coefClustering, densidade):
    
    if test_ID == 0: 

        # Criando um dataframe
        dados = [{'test_ID': test_ID, 'Dataset': nome_dataset, 'Adjacencia': adjacencia, 'k': k, 'Ponderacao': ponderacao, 'nArestas': nArestas, 'grauMedio': grauMedio, 'grauMaximo': grauMaximo, 'grauMinimo': grauMinimo, 'verticesIsolados': verticesIsolados, 'diametro': diametro, 'coefClustering': coefClustering, 'densidade': densidade}]

        df = pd.DataFrame(dados)
        # salvo arquivo csv
        df.to_csv('ResultadosGrafos' + str(indice_dataset) + '.csv', index=False)

    else:
        
        # leio arquivo csv existente e salvo df
        df = pd.read_csv('ResultadosGrafos' + str(indice_dataset) + '.csv')
  
        # Adicionando dados
        dados = [{'test_ID': test_ID, 'Dataset': nome_dataset, 'Adjacencia': adjacencia, 'k': k, 'Ponderacao': ponderacao, 'nArestas': nArestas, 'grauMedio': grauMedio, 'grauMaximo': grauMaximo, 'grauMinimo': grauMinimo, 'verticesIsolados': verticesIsolados, 'diametro': diametro, 'coefClustering': coefClustering, 'densidade': densidade}]

        dados = pd.DataFrame(dados)
        df = pd.concat([df, dados], ignore_index=True)

        # salvo arquivo csv mesmo lugar do outro
        df.to_csv('ResultadosGrafos' + str(indice_dataset) + '.csv', index=False)