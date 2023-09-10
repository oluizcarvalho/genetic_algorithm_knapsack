import random
import re
import time


# Crie a população inicial
def criar_individuo():
    return [random.randint(0, 1) for _ in range(len(pesos))]


def criar_populacao():
    return [criar_individuo() for _ in range(tamanho_populacao)]


# Avalie a aptidão de um indivíduo
def avaliar_fitness(individuo):
    peso_total = sum(p * i for p, i in zip(pesos, individuo))
    valor_total = sum(v * i for v, i in zip(valores, individuo))
    if peso_total > capacidade_mochila:
        return 0.1
    return valor_total


def calculate_fitness(chromosome):
    """Calculate the fitness of a chromosome."""
    total_weight = sum(items[i][0] for i in range(len(chromosome)) if chromosome[i] == 1)
    total_value = sum(items[i][1] for i in range(len(chromosome)) if chromosome[i] == 1)
    return total_value if total_weight <= max_weight else 0


# Selecione indivíduos para reprodução com base na aptidão
def selecao(populacao):
    return random.choices(populacao, weights=[avaliar_fitness(individuo) for individuo in populacao], k=2)


# Cruzamento de dois indivíduos
def cruzamento(individuo1, individuo2):
    ponto_corte = random.randint(1, len(individuo1) - 1)
    filho1 = individuo1[:ponto_corte] + individuo2[ponto_corte:]
    filho2 = individuo2[:ponto_corte] + individuo1[ponto_corte:]
    return filho1, filho2


# Mutação de um indivíduo
def mutacao(individuo):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i]  # Troque 0 por 1 ou 1 por 0


# Algoritmo genético
def algoritmo_genetico():
    populacao = criar_populacao()
    for geracao in range(geracoes):
        nova_populacao = []
        for _ in range(tamanho_populacao // 2):
            individuo1, individuo2 = selecao(populacao)
            filho1, filho2 = cruzamento(individuo1, individuo2)
            mutacao(filho1)
            mutacao(filho2)
            nova_populacao.extend([filho1, filho2])
        populacao = nova_populacao

        melhor_individuo = max(populacao, key=avaliar_fitness)
        melhor_fitness = avaliar_fitness(melhor_individuo)
        print(f"Geração {geracao + 1}: Melhor valor = {melhor_fitness}, Mochila = {melhor_individuo}")

    melhor_individuo = max(populacao, key=avaliar_fitness)
    melhor_fitness = avaliar_fitness(melhor_individuo)
    print(f"Melhor solução encontrada: Valor = {melhor_fitness}, Mochila = {melhor_individuo}")


def solve_knapsack_problem(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    n = int(lines[0].strip())
    capacity = int(lines[-1].strip())

    id, value, weight = [], [], []
    for line in lines[1:-1]:
        numbers = re.findall(r"[0-9]+", line)
        id.append(int(numbers[0]) - 1)
        value.append(int(numbers[1]))
        weight.append(int(numbers[2]))

    return n, value, weight, capacity


def ler_parametros(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        tamanho_populacao = int(lines[0].strip()) * 10
        capacidade_mochila = int(lines[-1].strip())
        pesos = []
        valores = []
        for line in lines[1:-1]:
            parts = line.split()
            peso = int(parts[1])
            valor = int(parts[2])
            pesos.append(peso)
            valores.append(valor)
    return capacidade_mochila, pesos, valores, tamanho_populacao


if __name__ == "__main__":
    start_time = time.time()
    capacidade_mochila, pesos, valores, tamanho_populacao = ler_parametros("input/input1.in")
    taxa_mutacao = 0.1
    geracoes = 100
    algoritmo_genetico()
    execution_time = time.time() - start_time
    print(f"Execution time: {execution_time} seconds")
