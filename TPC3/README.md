# TPC3 - "Conversor de MarkDown para HTML" (21/02/2025)

## Resumo

**Objetivo:** Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na ["Basic
Syntax"](https://www.markdownguide.org/basic-syntax/) da Cheat Sheet.

---

**Resolução**

Foram desenvolvidos as seguintes expressões regulares:

Reconhecer todos os possíveis headings (1 a 6), exceto os alternativos (--- e ====):

> r_headings = r"^(?P\<heading\>#{1,6})(?P\<h_cont\>.\*)$"

Reconhecer uma linha de uma lista ordenada, independentemente da sua identação (usada para aninhar as listas):

> r_list_ord = r"^(?P\<ident\>\s\*)\d+\\.(?P\<list_ord_cont\>.\*)$"

Igual ao anterior, mas para as listas não ordenadas. Reconhece como uma lista caso esta comece com **\*, - ou +**:

> r_list_unord = r"^(?P\<ident_un\>\s\*)\[-+\*\](?P\<list_un_cont\>.\*)$"

Reconhecer imagens:

> r_image = r"^!\\[(?P\<image_name\>.\*)\\]\\((?P\<image_link\>.\*)\\)$"

Reconhecer links:

> r_link = r"\\[(?P\<link_name\>.\*?)\\]\\((?P\<link\>.\*?)\\)"

Reconhecer porções da linha que estejam a negrito, itálico ou ambas:

> r_b_it_imp = r"([\_\*])([\_\*])?([\_\*])?(?P\<b_it_cont\>.\*?)(?P\<em_c\>\3?\2?\1)"

Estas expressões foram posteriormente agrupadas segundo a sua prioridade (das mais específicas para as menos):

1. **Headings e Listas:** estas foram agrupadas pela sua especificidade, uma vez que ocupam uma linha inteira. Podendo uma linha apenas ser uma dessas 3 opções;

2. **Imagens e Links:** Embora as imagens também ocupem uma linha inteira faz mais sentido agrupá-las com os links porque só têm um caractér de diferença ('!'). Fazendo o grupo como **(imagem | link)**, damos prioridade ao _match_ da imagem, devido à sua especificidade. Ao contrário das imagens, os _links_ podem aparecer várias vezes na mesma linha.

3. **Ênfase:** Finalmente temos o regex menos específico, que pode aparecer a qualquer ponto de uma linha várias vezes.

Quando vamos a imprimir a linha para o ficheiro HTML, fazemos a substituição dos elementos que deram _match_ ao contrário da ordem acima, começando no _Ênfase_ e acabando nos _Headings_. Isto porque o grupo dos _Headings_ e das Listas podem conter qualquer um dos outros elementos (Imagens, _Links_ e Ênfase).

**Problemas com a Implementação:**

- Está a ser inserido um **"\n"** extra após as _tags_ **\</li\>**;
- No caso de haver duas listas seguidas no ficheiro, estas têm de ter pelo menos uma linha vazia entre elas. Caso contrário o programa pensa que fazem parte da mesma lista, mesmo que uma seja ordenada e a outra não ordenada;
- O programa não consegue fechar as listas corretamente se estas acabarem numa lista aninhada, a menos que todas sejam do mesmo tipo;

## Resultados

- **Programa:** [conversor.py](conversor.py)
- **Ficheiro HTML Resultante:** [mark_res.html](mark_res.html)
- **Ficheiro de teste Markdown:** [mark.md](mark.md)

## Como correr o programa

O programa pode ser iniciado usando o comando:

> python3 conversor.py \<ficheiro markdown\>

## Autor

<img alt="Author Photo" src="../.assets/A93210.jpg" width="50" height="50"> &nbsp;&nbsp;&nbsp;&nbsp; Beatriz Ribeiro Terra Almeida (A93210)
