# Projeto de Resolução do Problema da Mochila

## Alunos
- Luiz André da Silva Carvalho
- João Victor Fernandes de Souza Silva

## Sobre
Este projeto implementa algoritmos para resolver o problema da mochila em quatro arquivos de entrada diferentes,
localizados na pasta `input`. Os resultados são exibidos por meio de logs no terminal e também são gerados ou
atualizados arquivos na pasta `output`.

`/ag_chromosome.py` → Algoritmo genético de cromossomos

`/dynamic.py` → Algoritmo de programação dinâmica

`/grasp.py` → Algoritmo meta-heurística GRASP

`/report.py` → Algoritmo que roda os outros algoritmos, gera gráficos com a média e desvio padrão dos resultados e tempo
de execução

P.s: O algoritmo de programação dinâmica e GRASP forem baseados
desse [repositório](https://github.com/neemiasbsilva/knapsack-problem-using-dp-grasp-tabu).

## Pré-requisitos

- Instalar as dependêcias necessárias

## Como Usar

1. Clone este repositório em sua máquina local:

   ```bash
   git clone https://github.com/oluizcarvalho/genetic_algorithm_knapsack.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd genetic_algorithm_knapsack
   ```

3. Execute o algortimo que desejar para resolver o problema da mochila:

   ```bash
   python ag_chromosome.py
   ```
4. Os resultados serão exibidos no terminal e os arquivos de saída serão gerados ou atualizados na pasta `output`.

## Arquivos de Entrada

Os quatro primeiros arquivos de entrada para o problema da mochila estão localizados na pasta `input`. Certifique-se de
que esses arquivos estejam formatados corretamente para a entrada do algoritmo.

## Saída

Os resultados da resolução do problema da mochila serão exibidos no terminal durante a execução do programa e também
serão registrados em arquivos na pasta `output`. Certifique-se de verificar esses arquivos para os resultados finais.

## Relatório

O resultado de comparação entre os três algoritmos se encontra no arquivo de extensão ".pdf" chamado **report**, localizado na pasta "reports".