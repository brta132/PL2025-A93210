from lexer import lexer

prox_simb = ('Erro', '', 0, 0)

def parserError(simb):
    print("Erro sintático, token inesperado: ", simb)

def rec_term(simb):
    global prox_simb
    if prox_simb.type == simb:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)

# P3: cont --> Arit Expr
# P4       > | 

def rec_Cont():
    global expr_atual
    if prox_simb == None:
        print("P4:       > | ")
        pass

    elif prox_simb.type == 'PF':
        print("[Start] P3: cont --> Arit Expr, PF")
        print("[End] P3: cont --> Arit Expr, PF")
        pass

    elif prox_simb.type == 'ARIT':
        print("[Start] P3: cont --> Arit Expr")
        rec_term('ARIT')
        rec_expr()
        print("[End] P3: cont --> Arit Expr")

    else:
        parserError(prox_simb)


# P1: Expr --> '(' Expr ')' Cont
# P2:       > | Num Cont
def rec_expr():
    global prox_simb
    if prox_simb.type == 'PA':
        print("[Start] P1: Expr --> '(' Expr ')' Cont")

        rec_term('PA')
        rec_expr()
        rec_term('PF')            

        rec_Cont()
        print("[End] P1: Expr --> '(' Expr ')' Cont")


    elif prox_simb.type == 'NUM':
        print("[Start] P2:       > | Num Cont")
        rec_term('NUM')
        rec_Cont()
        print("[End] P2:       > | Num Cont")

    else:
        parserError(prox_simb)


def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    rec_expr() 
    print("That's all folks!")