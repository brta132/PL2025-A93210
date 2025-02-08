# TPC1 - Somador ON/Off (Data: 2025-02-07)

## Resumo

**Objetivo:** Criar, em Python, um programa 'somador' que deve somar todos os números que estejam presentes no texto recebido por input.

**Explicação das Funcionalidades:**

1. Quando encontra a palavra **'Off'** (case-insensitive), a função de somar é desligada / posta em pausa.
2. Quando encontra a palavra **'On'** (case-insensitive), a função de somar é ligada / retomada.
3. Sempre que encontrar o sinal **'='** deve ser efetuado um print do total atual da soma para o stdout. A nenhum ponto do programa deve-se dar reset ao total da soma. Após o print o somador continua a somar como se nada tivesse acontecido.

**Tokens Existentes:** int, 'On', 'Off', '='.

## Restrições da Implementação

O programa verifica cada caracter individualmente, dando _match_ caso aconteça algum dos casos acima. Logo, palavras que contenham as substrings **'on'** ou **'off'** (e.g. 'offer', 'common', etc...) vão ativar as respetivas funcionalidades.

Isto também significa que nenhum dos _tokens_ tem de estar separado por espaços, desde que não dê match com outro _token_.

Por exemplo **'2025-02-07'** é interpretado como **\['2025','2','7'\]**, porque cada _token_ está separado por um caracter sem significado ('-').

Não há reconhecimento de números negativos, uma vez que números como **'-2'** são reconhecidos como **'2'**. Então, o somador não faz operações de subtração.

## Resultados

1. [Somador (Python)](somador.py)
2. [Ficheiro de Teste](Teste-Somador.txt)

## Como Correr o Programa

Para o programa receber um ficheiro de texto como input (maneira recomendada de interagir com o somador), sugere-se usar o seguinte comando:

> cat ficheiro-de-teste.txt | python3 somador.py

Caso queira correr o programa em modo _debug_ (indo ao ficheiro **somador.py**, na linha 89, substituir **"debug=False"** por **"debug=True"**), recomenda-se guardar o _output_ num ficheiro de texto para facilitar a análise:

> cat ficheiro-de-teste.txt | python3 somador.py > output.txt

## Autor

<img alt="Author Photo" src="../.assets/A93210.jpg" width="50" height="50"> &nbsp;&nbsp;&nbsp;&nbsp; Beatriz Ribeiro Terra Almeida (A93210)
