import igraph as ig


def metricasGrafo(matriz_pesos):

    matriz = matriz_pesos.copy()
    matriz[matriz != 0] = 1

    g = ig.Graph.Adjacency(matriz, mode='UNDIRECTED')

    nArestas = g.ecount()

    grauMedio = 2 * g.ecount() / g.vcount()
    grauMaximo = max(g.degree())
    grauMinimo = min(g.degree())

    graus = g.degree()
    verticesIsolados = sum(1 for grau in graus if grau == 0)

    diametro = g.diameter()

    coefClustering = g.transitivity_undirected()

    return nArestas, grauMedio, grauMaximo, grauMinimo, verticesIsolados, diametro, coefClustering
