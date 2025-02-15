# TPC2 - "Análise de um Dataset de Obras Musicais" (14/02/2025)

## Resumo

**Objetivos:** Ler e processar o dataset "obras.csv", respondendo aos seguintes pontos:

- Lista ordenada alfabeticamente dos compositores musicais;
- Distribuição das obras por período: quantas obras foram catalogadas em cada período;
- Dicionário em que a cada período está associada uma lista alfabética dos títulos das obras
  desse período.

---

**Resolução:**

Primeiro foi gerada a expressão regular para dar _match_ com uma linha do ficheiro csv, chegando ao seguinte resultado:

> (.+?);.+?;\d+;(.+?);(.+?);\d\d:\d\d:\d\d;O\d+

Por partes:

- **(.+?); ->** Grupo de captura que dá _match_ com qualquer caractér até encontrar o primeiro ';'. Captura o título da obra.
- **.+?; ->** _match_ até ao próximo ';'. Não captura nada.
- **\d+; ->** faz _match_ com o ano;
- **(.+?); ->** Grupo de captura que dá _match_ com qualquer caractér até encontrar o próximo ';'. Captura o Período.
- **(.+?); ->** Grupo de captura que dá _match_ com qualquer caractér até encontrar o próximo ';'. Captura o nome do Compositor.
- **\d\d:\d\d:\d\d; ->** duração da obra sob o formato de tempo xx:xx:xx;
- **O\d+** -> id da obra

De seguida, devido à formatação do ficheiro, foi criado uma segunda expressão regular para fazer _match_ com as linhas identadas (para quando as descrições são multi-linha):

> ^\W+

Esta expressão regular limita-se a verificar se o início da linha contém 1 ou mais caractéres em branco (espaços, _tabs_, _new lines_, etc...)

Com as expressões criadas, o desenvolvimento do código foi feito por etapas:

1. abrir e ler o ficheiro _.csv_ linha a linha
2. usar o regex criado para dar _match_ com a linha inteira para tentar retirar a informação pretendida da linha.
   - Caso não seja possível (uma linha do _.csv_ equivaler a mais linhas no ficheiro), usar o regex de linhas identadas para dar _match_ até não haver mais linhas identadas consecutivas;
   - Concatenar todas as partes numa única string;
   - voltar a repetir o passo 2.
3. Guardar a _match_ numa lista para poder aceder depois;
4. Manipular os dados para responder aos objetivos acima. Foram criados métodos separados para cada objetivo.

## Resultados

1. [Programa Principal](main.py)
2. [Dataset](obras.csv)
3. Ficheiros de _debug_ de resultados:
   1. [Lista de Compositores por Ordem Alfabética](obras__CompositoresPorOrdemAlfabetica.txt)
   2. [Distribuição das Obras por Período](obras__NumObrasPorPeriodo.txt)
   3. [Dicionário{Período, Lista das Obras por Ordem Alfabética}](obras__ObrasPorPeriodoListaOrd.txt)

## Como Correr o Programa

Para correr o programa em modo _default_ (resultados impressos para o _STDOUT_):

> python3 main.py

Caso queira correr o programa em modo _debug_ deve ir ao ficheiro **main.py**, na linha 143, substituir **"writeOutputToFile=False"** por **"writeOutputToFile=True"**. Isto vai fazer com que os resultados dos 3 pontos dos objetivos sejam impressos para ficheiros separados, sendo mais fácil de ler.

## Autor

<img alt="Author Photo" src="../.assets/A93210.jpg" width="50" height="50"> &nbsp;&nbsp;&nbsp;&nbsp; Beatriz Ribeiro Terra Almeida (A93210)
