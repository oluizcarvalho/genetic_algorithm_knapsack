import random
import time


def gerar_populacao(tamanho, itens):
    populacao = []
    for _ in range(tamanho):
        genes = [0, 1]
        cromossomo = [random.choice(genes) for _ in range(len(itens))]
        populacao.append(cromossomo)
    return populacao


def calcular_fitness(cromossomo, itens, capacidade_mochila):
    peso_total_aux = sum(itens[i][0] for i in range(len(cromossomo)) if cromossomo[i] == 1)
    valor_total_aux = sum(itens[i][1] for i in range(len(cromossomo)) if cromossomo[i] == 1)
    return valor_total_aux if peso_total_aux <= capacidade_mochila else 0


def selecionar_cromossomos(populacao, itens, capacidade_mochila):
    valores_fitness = [calcular_fitness(cromossomo, itens, capacidade_mochila) for cromossomo in populacao]
    soma_fitness = sum(valores_fitness)
    try:
        probabilidades_fitness = [fitness / soma_fitness for fitness in valores_fitness]
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")
        exit()

    pai1 = random.choices(populacao, weights=probabilidades_fitness, k=1)[0]
    pai2 = random.choices(populacao, weights=probabilidades_fitness, k=1)[0]
    return pai1, pai2


def crossover(pai1, pai2, itens):
    ponto_crossover = random.randint(0, len(itens) - 1)
    filho1 = pai1[:ponto_crossover] + pai2[ponto_crossover:]
    filho2 = pai2[:ponto_crossover] + pai1[ponto_crossover:]
    return filho1, filho2


def mutacao(cromossomo, itens):
    ponto_mutacao = random.randint(0, len(itens) - 1)
    cromossomo[ponto_mutacao] = 1 - cromossomo[ponto_mutacao]
    return cromossomo


def obter_melhor(populacao, itens, capacidade_mochila):
    valores_fitness = [calcular_fitness(cromossomo, itens, capacidade_mochila) for cromossomo in populacao]
    indice_maximo = valores_fitness.index(max(valores_fitness))
    return populacao[indice_maximo]


def ler_parametros(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        tamanho_populacao_aux = int(lines[0].strip())
        capacidade_mochila_aux = int(lines[-1].strip())
        itens_aux = []
        for line in lines[1:-1]:
            parts = line.split()
            peso = int(parts[1])
            valor = int(parts[2])
            itens_aux.append([peso, valor])
    return capacidade_mochila_aux, itens_aux, tamanho_populacao_aux


def algoritmo_genetico(populacao, geracoes, probabilidade_mutacao, itens, capacidade_mochila):
    for _ in range(geracoes):
        pai1, pai2 = selecionar_cromossomos(populacao, itens, capacidade_mochila)

        filho1, filho2 = crossover(pai1, pai2, itens)

        if random.uniform(0, 1) < probabilidade_mutacao:
            filho1 = mutacao(filho1, itens)
        if random.uniform(0, 1) < probabilidade_mutacao:
            filho2 = mutacao(filho2, itens)

        populacao = [filho1, filho2] + populacao[2:]

    melhor = obter_melhor(populacao, itens, capacidade_mochila)

    peso_total_result = sum(itens[i][0] for i in range(len(melhor)) if melhor[i] == 1)
    valor_total_result = sum(itens[i][1] for i in range(len(melhor)) if melhor[i] == 1)
    return peso_total_result, valor_total_result


def main():
    output_max_values = []

    for iterator in range(2, 3):
        input_file_path = f"input/input{iterator}.in"
        capacidade_mochila, itens, tamanho_populacao = ler_parametros(input_file_path)
        probabilidade_mutacao = 0.2
        geracoes = 50

        print("Itens disponíveis:\n", itens)
        print("\nParâmetros do algoritmo genético:")
        print("Peso máximo:", capacidade_mochila)
        print("População:", tamanho_populacao)
        print("Probabilidade de mutação:", probabilidade_mutacao)
        print("Gerações:", geracoes, "\n")
        print("Realizando evolução genética:")

        populacao = gerar_populacao(tamanho_populacao * 10, itens)
        peso_total, valor_total = algoritmo_genetico(populacao, geracoes, probabilidade_mutacao, itens,
                                                     capacidade_mochila)

        output_line = f"Instancia {iterator} -> Peso: {peso_total}, Valor {valor_total}\n"

        with open("output/dynamic.out", "a+") as output_file:
            output_file.write(output_line)
        output_max_values.append([peso_total, valor_total])
        print("\nA melhor solução:")
        print("Peso:", peso_total)
        print("Valor:", valor_total)

    return output_max_values


if __name__ == "__main__":
    start_time = time.time()
    main()
    execution_time = time.time() - start_time
    print(f"Tempo de execução: {execution_time} segundos")
