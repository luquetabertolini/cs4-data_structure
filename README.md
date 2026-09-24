# GoodWe Smart Charging Station

Sistema de gerenciamento e simulação de sessões de recarga de veículos elétricos, desenvolvido para o projeto acadêmico da disciplina de Estruturas de Dados e Algoritmos.

O sistema permite cadastrar e gerenciar sessões de recarga, calcular consumo de energia, tempo de carregamento e custo, aplicar tarifação de acordo com o horário, realizar buscas, ordenar registros e apresentar estatísticas gerais.

## Objetivo do projeto

O projeto tem como objetivo desenvolver uma solução para simular e gerenciar sessões de carregamento de veículos elétricos de forma organizada, utilizando estruturas de dados e algoritmos implementados em Python.

A aplicação também demonstra a integração entre uma interface Web e um backend Python responsável pelo processamento dos dados.

## Funcionalidades

O sistema possui as seguintes funcionalidades:

* Cadastro de sessões de recarga;
* Identificação das sessões por ID;
* Seleção do modelo do veículo;
* Seleção do tipo de carregamento;
* Definição da bateria atual e da bateria desejada;
* Definição do horário de início da recarga;
* Cálculo da energia necessária;
* Cálculo do tempo estimado de carregamento;
* Cálculo do custo da sessão;
* Aplicação de tarifação conforme o horário;
* Armazenamento de múltiplas sessões;
* Listagem das sessões cadastradas;
* Busca de sessões por ID;
* Ordenação das sessões;
* Estatísticas gerais das sessões;
* Cálculo de faturamento total;
* Cálculo de ticket médio;
* Identificação do maior e menor consumo.

## Estruturas de Dados

Cada sessão de recarga é representada por um objeto da classe `Sessao`.

```python
class Sessao:
    def __init__(self, id_sessao, modelo, tipo, energia, tempo, custo):
        self.id = id_sessao
        self.modelo = modelo
        self.tipo = tipo
        self.energia = energia
        self.tempo = tempo
        self.custo = custo
```

As sessões são armazenadas em uma lista Python:

```python
sessoes = []
```

Quando uma nova sessão é cadastrada, ela é adicionada à lista:

```python
sessoes.append(nova_sessao)
```

Essa estrutura permite armazenar e manipular múltiplas sessões durante a execução da aplicação.

## Algoritmo de busca

O sistema utiliza uma Busca Sequencial (Busca Linear) para localizar uma sessão pelo seu ID.

```python
def busca_sequencial_id(sessoes, id_procurado):
    for i in range(len(sessoes)):
        if sessoes[i].id == id_procurado:
            return i

    return -1
```

O algoritmo percorre a lista de sessões uma posição por vez até encontra
