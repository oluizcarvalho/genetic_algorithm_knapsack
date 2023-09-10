import time
import matplotlib.pyplot as plt
import numpy as np
import grasp
import chromosome


# Função que implementa o Cromossomo
def algoritmo1():
    start_time = time.time()
    end_time = time.time()
    return end_time - start_time


# Função que implementa o Algoritmo 2
def algoritmo2():
    start_time = time.time()
    # Código do Algoritmo 2
    end_time = time.time()
    return end_time - start_time


# Número de vezes que cada algoritmo será executado
num_execucoes = 50

tempos_algoritmo1 = []
tempos_algoritmo2 = []

for _ in range(num_execucoes):
    tempos_algoritmo1.append(algoritmo1())
    tempos_algoritmo2.append(algoritmo2())

# Calcular o valor médio e o desvio padrão dos tempos de execução
media_algoritmo1 = np.mean(tempos_algoritmo1)
media_algoritmo2 = np.mean(tempos_algoritmo2)

desvio_padrao_algoritmo1 = np.std(tempos_algoritmo1)
desvio_padrao_algoritmo2 = np.std(tempos_algoritmo2)

# Gere o gráfico de barras comparando os tempos de execução, incluindo média e desvio padrão
algoritmos = ['Cromossomos Bioinspirada', 'GRASP']
tempos_medios = [media_algoritmo1, media_algoritmo2]
desvios_padrao = [desvio_padrao_algoritmo1, desvio_padrao_algoritmo2]

plt.bar(algoritmos, tempos_medios, yerr=desvios_padrao, capsize=10)
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Comparação de Tempo de Execução de Três Algoritmos')
plt.show()
