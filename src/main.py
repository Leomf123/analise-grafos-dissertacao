import sys
from teste import teste


def main(indice_inicio, indice_fim):
    
    datasets = [
        "armstrong2002v1.data",
        "chowdary2006.data",
        "ace_ECFP_4.data",
        "ace_ECFP_6.data",
        "cox2_ECFP_6.data",
        "dhfr_ECFP_4.data",
        "dhfr_ECFP_6.data",
        "fontaine_ECFP_4.data",
        "fontaine_ECFP_6.data",
        "m1_ECFP_4.data",
        "m1_ECFP_6.data",
        "transplant.data",
        "autoPrice.data",
        "seeds.data",
        "chscase_geyser1.data",
        "diggle_table.data",
        "gordon2002.data",
        "articles_1442_5.data",
        "articles_1442_80.data",
        "iris.data",
        "analcatdata_authorship-458.data",
        "wine-187.data",
        "banknote-authentication.data",
        "yeast_Galactose.data",
        "mfeat-karhunen.data",
        "mfeat-factors.data",
        "semeion.data",
        "wdbc.data",
        "stock.data",
        "segmentation-normcols.data",
        "cardiotocography.data",
    ]

    K = [4, 6, 8, 10, 12, 14, 16]

    Adjacencia = ["MST", "mutKNN", "symKNN", "symFKNN", "SKNN", "MKNN", "Completa"]

    Ponderacao = ["RBF", "BB-0.01", "BB-0.05", "BB-0.1"]

    Quantidade_rotulos = [0.02, 0.05, 0.08, 0.1]

    Quantidade_experimentos = 20
    
    teste(indice_inicio, indice_fim, datasets, K, Adjacencia, Ponderacao, Quantidade_rotulos, Quantidade_experimentos)


if __name__ == "__main__":

    indice_inicio = int(sys.argv[1])
    indice_fim = int(sys.argv[2])

    if indice_inicio < 0 or indice_fim > 31 or indice_inicio >= indice_fim:
        print("Forneça valores válidos para o inicio e fim!!!!")
    else:
        main(indice_inicio, indice_fim)
