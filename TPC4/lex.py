import sys
import re
import ply.lex as lex

def main():

    # criar a lista dos tokens
    tokens = (  "COMMENT",
                "LIMIT",
                "QUERY_SELECT",
                "LINE_TERM", 
                "CLAUSE_WHERE",
                "CLAUSE_START", 
                "CLAUSE_END", 
                "PREFIX_A",
                "LANG_SPEC",
                "NUM", 
                "STRING_LITERAL",
                "PREFIX",
                "PREFIX_TYPE",
                "VARS"
            )

    # criar os matchs, funções para tokens com valores variáveis ou que precisem de conversão
    def t_COMMENT(t): 
        r'^\#(.*)$'
        return t
    
    t_QUERY_SELECT = r'^select\b'
    t_LINE_TERM = r'\.'
    t_CLAUSE_WHERE = r'\bwhere\b'
    t_CLAUSE_START = r'{'
    t_CLAUSE_END = r'}'
    t_PREFIX_A = r'\ba\b'
    t_NUM = r'\d+'

    def t_LANG_SPEC(t): 
        r'@(.+)\b'
        var = re.match(r'@(.+)\b', t.value)
        t.value = var.group(1)        
        return t

    t_STRING_LITERAL = r'".*"'

    t_PREFIX = r'([a-zA-Z]+)(?=:)'

    t_PREFIX_TYPE = r'(?<=:)([a-zA-Z]+)'
    
    def t_VARS(t): 
        r'\?(\w+)'
        var = re.match(r'\?(\w+)', t.value)
        t.value = var.group(1)
        return t
    
    t_LIMIT = r'\bLIMIT\b'

    def t_newline(t): # for tracking line numbers
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = ':\t '

    def t_error(t):
        print(f'Illegal character: {t.value[0]}')
        t.lexer.skip(1)

    #Initializaing lexer
    lexer = lex.lex()

    #Feeding it the data
    with open("testfile.txt",'r') as file:    
        for line in file:
            lexer.input(line)
            for tok in lexer:
                print(tok.type, tok.value, tok.lineno, tok.lexpos)

if __name__ == "__main__":
    main()