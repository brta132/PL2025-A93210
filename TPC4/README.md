# TPC4 - "Analisador Léxico" (28/02/2025)

## Resumo

### Objetivo

Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do
género:

```
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

### Implementação

Apenas foi construído um analisador léxico para o excerto dado acima (linguagem SparQL).

A primeira etapa a ser completada é a definição dos _tokens_ e das suas respetivas expressões regulares:

```
COMMENT: r'^\#(.*)$'
QUERY_SELECT: r'^select\b'
VARS: r'\?(\w+)'
CLAUSE_WHERE: r'\bwhere\b'
CLAUSE_START: r'{'
CLAUSE_END: r'}'
PREFIX: r'([a-zA-Z]+)(?=:)'
PREFIX_TYPE: r'(?<=:)([a-zA-Z]+)'
PREFIX_A: r'\ba\b'
STRING_LITERAL: r'".*"'
LANG_SPEC: r'@(.+)\b'
LINE_TERM: r'\.'
LIMIT: r'LIMIT'
NUM: r'\d+'
NEW_LINE: r'\n'
SKIP: r' \t:'
ERROR: r'.'
```

De seguida temos de definir a ordem de prioridade, para que as expressões regulares mais específicas sejam as primeiras:

```
COMMENT
LIMIT
QUERY_SELECT
LINE_TERM
CLAUSE_WHERE
CLAUSE_START
CLAUSE_END
PREFIX_A
LANG_SPEC
NUM
STRING_LITERAL
PREFIX
PREFIX_TYPE
VARS
NEW_LINE
SKIP
ERROR
```

Estas últimas 3 (NEW_LINE, SKIP e ERROR) podem ser defenidas diretamente nas regras do lexer (ply.lex).

Finalmente, inicializamos o _lexer_ e aplicamo-lo a cada linha do ficheiro de teste (testfile.txt).

## Resultados

- **Analisador Léxico:** [lex.py](lex.py)
- **Ficheiro de Teste:** [testfile.txt](testfile.txt)

## Como Correr o Programa

Utilizando o comando:

> python3 lex.py

**Notas:** É necessário ter um ficheiro de teste chamado "testfile.txt" na mesma pasta do ficheiro _lex.py_.

## Autor

<img alt="Author Photo" src="../.assets/A93210.jpg" width="50" height="50"> &nbsp;&nbsp;&nbsp;&nbsp; Beatriz Ribeiro Terra Almeida (A93210)
