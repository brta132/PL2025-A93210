# TPC6 - "Recursivo Descendente para expressões aritméticas" (21/03/2025)

## Resumo

### Objetivos

Baseado nos materiais fornecidos na aula, cria um parser LL(1) recursivo descendente que reconheça expressões aritméticas e calcule o respetivo valor.

Exemplos de algumas frases:

2+3
67-(2+3*4)
(9-2)*(13-4)

### Desenvolver a gramática

P1: Expr --> '(' Expr ')' Cont
P2: > | Num Cont
P3: cont --> Arit Expr
P4 > |

simbolos lexer:
PA --> '('
PF ---> ')'
Num --> \d+
Arit --> '+' | '-' | '\*' | '/'

## Resultados

lista com apontadores para os ficheiros resultantes

## Autor

<img alt="Author Photo" src="../.assets/A93210.jpg" width="50" height="50"> &nbsp;&nbsp;&nbsp;&nbsp; Beatriz Ribeiro Terra Almeida (A93210)
