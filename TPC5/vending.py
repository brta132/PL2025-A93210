import sys
import re
import json
import os
from datetime import datetime

# gloval vars
saldo = 0.0

stock_path = "stock.json"

fd = open(stock_path, "r")
stock = json.load(fd)
fd.close()

exit = False

commandos_usage = {
    "MOEDAS" : "[COMANDO] MOEDAS <lista_de_moedas> .\nAdiciona moedas ao saldo da máquina.\nA lista tem de ser separada por \",\". Moedas aceites são: 2e, 1e, 50c, 20c, 10c, 5c, 2c e 1c.\n O comando tem obrigatoriamente de terminar com \".\".",
    "SAIR": "[COMANDO] SAIR\nGuarda o estado atual e sai do programa.",
    "LISTAR" : "[COMANDO] LISTAR\nLista todos os produtos existentes, assim como as suas propriedades.",
    "ADICIONAR" : "[COMANDO] ADICIONAR <código do produto> <nome> <preço> <quantidade>\nAdiciona um produto novo à máquina.\n Se já existir um produto com o código dado, este não é adicionado.\n Todos os códigos são compostos por uma letra Maiúscula seguida de 2 números (ex. A01)",
    "SELECIONAR" : "[COMANDO] SELECIONAR <código do produto>\nSeleciona o produto com o código passado, caso este não exista, não esteja em stock ou não tenha saldo o suficiente, dá erro.\nTodos os códigos são compostos por uma letra Maiúscula seguida de 2 números (ex. A01)",
    "RESTOCK" : "[COMANDO] RESTOCK <código do produto> <quantidade>\nAdiciona a quantidade desejada ao produto com o código passado.\n Se não existir um produto com o código dado nada é alterado.\n Todos os códigos são compostos por uma letra Maiúscula seguida de 2 números (ex. A01)"
}


def item_exists(cod):
    item_exists = False
    index = -1
    for i in range(len(stock["stock"])):
        if stock["stock"][i]["cod"] == cod:
            item_exists = True
            index = i
            break
    return item_exists, index

# FUNCS
def listar():
    columns = os.get_terminal_size()[0]
    separator = "-" * columns
    print(separator)
    print(f"| código | nome | quantidade | preço |")
    print(separator)
    for s in stock["stock"]:
        line = f"| {s["cod"]} | {s["nome"]} | {s["quant"]} | {s["preco"]} |"
        print(line)
        print(separator)
    return

def sair():
    global exit
    with open(stock_path, "w", encoding='utf8') as stock_file:
        json.dump(stock, stock_file, indent=4)
    exit = True
    return

def tokenizer(linha):

    global saldo
    global stock

    token_specification = [
        ("SAIR", r"SAIR"),
        ("LISTAR", r"LISTAR"),
        ("ADICIONAR", r"(?:ADICIONAR) (?P<codAD>[A-Z]\d{2}), (?P<nomeAD>\".*\"), (?P<precoAD>\d+.\d+), (?P<quantAD>\d+)"),
        ("SELECIONAR", r"(?:SELECIONAR) (?P<codSEL>[A-Z]\d{2})"),
        ("RESTOCK", r"(?:RESTOCK) (?P<codRE>[A-Z]\d{2}) (?P<quantRE>\d+)"),
        ("MOEDAS", r"(?:MOEDAS) (?P<moedas>.*) .")
    ]

    tok_regex = '|'.join([f'(?P<{id}>{expreg})' for (id, expreg) in token_specification])

    mo = re.finditer(tok_regex, linha)
    matched = 0

    for m in mo:
        dic = m.groupdict()
        if dic["LISTAR"]:
            listar()
            matched = 1

        if dic["SAIR"]:
            sair()
            matched = 1

        if dic["MOEDAS"]:
            for moeda in (dic["moedas"]).split(","):
               
                moeda = moeda.strip()
                
                if moeda.__eq__("2e"):
                    saldo += 2.0

                elif moeda.__eq__("1e"):
                    saldo += 1.0
                
                elif moeda.__eq__("50c"):
                    saldo += 0.5

                elif moeda.__eq__("20c"):
                    saldo += 0.2

                elif moeda.__eq__("10c"):
                    saldo += 0.1
                
                elif moeda.__eq__("5c"):
                    saldo += 0.05

                elif moeda.__eq__("2c"):
                    saldo += 0.02

                elif moeda.__eq__("1c"):
                    saldo += 0.01
                
                else:
                    print(f"MOEDA: {moeda} não reconhecida. MOEDAS aceitáveis: 2e, 1e, 50c, 20c, 10c, 5c, 2c, 1c.")
                
           
            saldo_e = str(saldo).split(".")[0]
            saldo_c = str(saldo).split(".")[1]
            
            print(f"SALDO: {saldo_e[:2]}e {saldo_c[:2]}c")
            
            matched = 1

        if dic["ADICIONAR"]:

            # check if item exists
            it_exists, id = item_exists(dic["codAD"])

            if(not it_exists):
                nome = dic["nomeAD"].replace("\"","")
                item = {"cod": dic["codAD"], "nome" : nome, "preco": dic["precoAD"], "quant": dic["quantAD"] }
                stock["stock"].append(item)
                print("Produto adicinado com sucesso.")
            else:
                print(f"[ERROR]: Não foi possível adicionar produto. Código de Produto: {dic["codAD"]} já existe.")

            matched = 1

        if dic["SELECIONAR"]:
            # check if item exists
            it_exists, id = item_exists(dic["codSEL"])

            if(it_exists):
                qt = int(stock["stock"][id]["quant"])
                preco = float(stock["stock"][id]["preco"])

                if qt > 0:
                    if saldo >= preco: 
                        stock["stock"][id]["quant"] = qt - 1
                        saldo -= preco

                        saldo_e = str(saldo).split(".")[0]
                        saldo_c = str(saldo).split(".")[1]

                        print(f"SALDO = {saldo_e}e {saldo_c}c.")

                    else:
                        saldo_e = str(saldo).split(".")[0]
                        saldo_c = str(saldo).split(".")[1]

                        preco_e = str(preco).split(".")[0]
                        preco_c = str(preco).split(".")[1]

                        print(f"[ERROR]: Saldo insuficiente. Saldo = {saldo_e}e {saldo_c[:2]}c. Preço = {preco_e}e {preco_c[:2]}c.")
                else:
                    print("[ERROR]: O produto não está em stock.")
            else:
                print(f"[ERROR]: Produto {dic["codSEL"]} não existe.")

            matched = 1

        if dic["RESTOCK"]:

            it_exists, id = item_exists(dic["codRE"])
            if it_exists:
                if int(dic["quantRE"]) > 0:
                    stock["stock"][id]["quant"] = stock["stock"][id]["quant"] + int(dic["quantRE"])
                else:
                    print(f"[ERROR]: Valor de RESTOCK \"{dic["quantRE"]}\" inválido. Tem de ser MAIOR que 0.")
            else:
                print(f"[ERROR]: Produto {dic["codRE"]} não existe.")

            matched = 1

    #HELP MESSAGE
    if(matched == 0):
        if str(linha).__contains__("MOEDAS"):
            print(commandos_usage["MOEDAS"])
        elif str(linha).__contains__("RESTOCK"):
            print(commandos_usage["RESTOCK"])
        elif str(linha).__contains__("ADICIONAR"):
            print(commandos_usage["ADICIONAR"])
        elif str(linha).__contains__("SELECIONAR"):
            print(commandos_usage["SELECIONAR"])
        else:
            print(f"Comando \"{str(linha).strip()}\" não reconhecido.\nOs comandos reconhecidos pelo programa são:\n")
            for cmd_desc in commandos_usage.values():
                print(cmd_desc + "\n")
            
    return

def main():

    #Message
    print(f"maq: {datetime.today().strftime('%Y-%m-%d')}, Stock carregado, Estado atualizado.\nmaq: Bom dia. Estou disponível para atender o seu pedido.")
    
    # tokenize
    for linha in sys.stdin:
        tokenizer(linha)
        if exit:
            break
    return


if __name__ == "__main__":
    main()