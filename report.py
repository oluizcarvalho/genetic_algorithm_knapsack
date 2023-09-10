import threading
import time
import matplotlib.pyplot as plt
import numpy as np
import grasp
import ag_chromosome
import dynamic


# Função que implementa o Cromossomo
def chromosomes_fn():
    start_time = time.time()
    ag_chromosome.main()
    end_time = time.time()
    return end_time - start_time


# Função que implementa o GRASP
def grasp_fn():
    start_time = time.time()
    grasp.main()
    end_time = time.time()
    return end_time - start_time


# Função que implementa programação dinamica
def dynamic_fn():
    start_time = time.time()
    dynamic.main()
    end_time = time.time()
    return end_time - start_time


def performace():
    tempos_algoritmo1 = []
    tempos_algoritmo2 = []
    tempos_algoritmo3 = []

    for _ in range(num_execucoes):
        tempos_algoritmo1.append(chromosomes_fn())
        tempos_algoritmo2.append(grasp_fn())
        tempos_algoritmo3.append(dynamic_fn())

    # Calcular o valor médio e o desvio padrão dos tempos de execução
    media_algoritmo1 = np.mean(tempos_algoritmo1)
    media_algoritmo2 = np.mean(tempos_algoritmo2)
    media_algoritmo3 = np.mean(tempos_algoritmo3)

    desvio_padrao_algoritmo1 = np.std(tempos_algoritmo1)
    desvio_padrao_algoritmo2 = np.std(tempos_algoritmo2)
    desvio_padrao_algoritmo3 = np.std(tempos_algoritmo3)

    print('médias: ', media_algoritmo1, media_algoritmo2, media_algoritmo3)
    print('desvios padrao: ', desvio_padrao_algoritmo1, desvio_padrao_algoritmo2, desvio_padrao_algoritmo3)

    # Gere o gráfico de barras comparando os tempos de execução, incluindo média e desvio padrão
    algoritmos = ['AG Cromossomos', 'GRASP', 'Dinâmico']
    tempos_medios = [media_algoritmo1, media_algoritmo2, media_algoritmo3]
    desvios_padrao = [desvio_padrao_algoritmo1, desvio_padrao_algoritmo2, desvio_padrao_algoritmo3]

    plt.bar(algoritmos, tempos_medios, yerr=desvios_padrao, capsize=10)
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title('Comparação de Tempo de Execução de Três Algoritmos')
    plt.show()


def results():
    num_arquivos = 4

    resultados_algoritmo1 = []
    resultados_algoritmo2 = []
    resultados_algoritmo3 = []
    media_algoritmo1 = 0
    media_algoritmo2 = 0
    media_algoritmo3 = 0
    desvio_padrao_algoritmo1 = 0
    desvio_padrao_algoritmo2 = 0
    desvio_padrao_algoritmo3 = 0

    for _ in range(num_execucoes):
        resultados_algoritmo1.append(ag_chromosome.main())
        resultados_algoritmo2.append(grasp.main())

    resultados_algoritmo3.append(dynamic.main())  # Algoritmo dinamico nao tem alteracao nos resultados

    for i in range(len(resultados_algoritmo1)):
        media_algoritmo1 = np.mean(resultados_algoritmo1, axis=0)
        media_algoritmo2 = np.mean(resultados_algoritmo2, axis=0)
        media_algoritmo3 = np.mean(resultados_algoritmo3, axis=0)

        desvio_padrao_algoritmo1 = np.std(resultados_algoritmo1, axis=0)
        desvio_padrao_algoritmo2 = np.std(resultados_algoritmo2, axis=0)
        desvio_padrao_algoritmo3 = np.std(resultados_algoritmo3, axis=0)

    print('médias: ', media_algoritmo1, media_algoritmo2, media_algoritmo3)
    print('desvios padrao: ', desvio_padrao_algoritmo1, desvio_padrao_algoritmo2, desvio_padrao_algoritmo3)

    posicoes = np.arange(num_arquivos)
    largura_barra = 0.25
    algoritmos = ['AG Cromossomos', 'GRASP', 'Dinâmico']

    plt.bar(posicoes - largura_barra, media_algoritmo1, largura_barra, yerr=desvio_padrao_algoritmo1,
            label=algoritmos[0])
    plt.bar(posicoes, media_algoritmo2, largura_barra, yerr=desvio_padrao_algoritmo2, label=algoritmos[1])
    plt.bar(posicoes + largura_barra, media_algoritmo3, largura_barra, yerr=desvio_padrao_algoritmo3,
            label=algoritmos[2])

    plt.xlabel('Posição no Array de Resultados')
    plt.ylabel('Resultados')
    plt.title('Comparação dos Resultados de Três Algoritmos por Posição')
    plt.xticks(posicoes, ['Instacia 1', 'Instancia 2', 'Instancia 3', 'Instancia 4'])
    plt.legend()

    plt.show()


if __name__ == "__main__":
    # Número de vezes que cada algoritmo será executado
    num_execucoes = 15
    minha_thread = threading.Thread(target=performace)
    minha_thread.start()  # Inicie a thread que compara performace
    # performace()  # Gera o gráfico de comparação de performace
    results()  # Gera o gráfico de comparação de resultados
