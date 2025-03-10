# TPC5 - "Máquina de Vending" (08/03/2025)

## Resumo

### Objetivo

Criar uma máquina de vending.

Esta tem um stock de produtos: uma lista de triplos, nome do produto, quantidade e preço.

```
stock = [
    {"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.7},
    ...
]
```

Na secção abaixo estão descritos os comandos implementados.

### Implementação

O estado do programa é guardado num ficheiro _json_.

Comandos implementados:

- **SAIR:** grava o estado do programa e sai.

> SAIR

- **LISTAR:** lista todos os produtos existentes, assim como as suas propriedades.

> LISTAR

- **MOEDAS:** Adiciona moedas ao saldo da máquina.

> MOEDAS <lista_de_moedas> .

A lista de moedas tem de ser separada por ",". Moedas aceites são: 2e, 1e, 50c, 20c, 10c, 5c, 2c e 1c.

O comando tem obrigatoriamente de terminar com "."

- **ADICIONAR:** Adiciona um produto novo à máquina. Se já existir um produto com o código dado, este não é adicionado.

> ADICIONAR <código do produto> <nome> <preço> <quantidade>

Todos os códigos são compostos por uma letra Maiúscula seguida de 2 números (ex. A01)

- **SELECIONAR:** Seleciona o produto com o código passado, caso este não exista, não esteja em stock ou não tenha saldo o suficiente, dá erro.

> SELECIONAR <código do produto>

Todos os códigos são compostos por uma letra Maiúscula seguida de 2 números (ex. A01)

- **RESTOCK:** Adiciona a quantidade desejada ao produto com o código passado. Se não existir um produto com o código dado nada é alterado.

> RESTOCK <código do produto> <quantidade>

Todos os códigos são compostos por uma letra Maiúscula seguida de 2 números (ex. A01)"

## Resultados

- **Programa:** [vending.py](vending.py)
- **Ficheiro do Stock:** [stock.json](stock.json)

## Como correr o programa

Pode correr o programa usando o comando:

> python3 vending.py

Caso haja alguma dúvida acerca dos comandos disponíveis, pode escrever qualquer coisa no terminal, o que vai imprimir uma mensagem de ajuda com os comandos disponíveis para o terminal.

## Autor

<img alt="Author Photo" src="../.assets/A93210.jpg" width="50" height="50"> &nbsp;&nbsp;&nbsp;&nbsp; Beatriz Ribeiro Terra Almeida (A93210)
