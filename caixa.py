from formatacao import *
import sqlite3
import time
import sys
from funcoes import *


def registrar_vendas_vendasepagamentos():
    cliente_cpfvenda = ''
    while cliente_cpfvenda == '':
        try:
            cliente_cpfvenda = str(input('[{:-^100}]\n\n'
                                         'DIGITE O CPF DO CLIENTE: '.format(
                'REGISTRAR VENDA DE PRODUTO')).strip())
            v = cliente_cpfvenda.isnumeric()
            if v == True:
                if len(cliente_cpfvenda) != 11:
                    print('ERRO: UM CPF TEM 11 NÚMEROS. VAMOS TENTAR NOVAMENTE:')
                    cliente_cpfvenda = ''
            else:
                print('DIGITE O CPF USANDO APENAS NÚMEROS. VAMOS TENTAR NOVAMENTE:')
                cliente_cpfvenda = ''
        except:
            if len(cliente_cpfvenda) == 0:
                print('ERRO: POR FAVOR, DIGITE O CPF DO CLIENTE. VAMOS TENTAR NOVAMENTE:')

    separar_input()
    cliente_cpf_dados(cliente_cpfvenda)
    produtoclientevenda = cliente_cpf_dados_nome(cliente_cpfvenda)
    separar_input()
    produto_idvenda = ''
    while produto_idvenda == '':
        try:
            produto_idvenda = str(input('DIGITE O ID DO PRODUTO: ').strip())
        except:
            if len(produto_idvenda) == 0:
                print('ERRO: POR FAVOR, DIGITE O ID DO PRODUTO. VAMOS TENTAR NOVAMENTE: ')

    info_produto(produto_idvenda)

    produto_nomevenda = info_produto_nome(produto_idvenda)
    produtopreco1 = info_produto_valor(produto_idvenda)
    separar_input()
    quantidade = ''
    while quantidade == '':
        try:
            quantidade = int(input('DIGITE A QUANTIDADE DO PRODUTO COMPRADO (EXEMPLO: 2): ').strip())
            if quantidade <= 0:
                print('ERRO: A QUANTIDADE NÃO PODE SER 0 OU MENOR. VAMOS TENTAR NOVAMENTE:')
                quantidade = ''
        except:
            if len(quantidade) == 0:
                print(
                    'ERRO: POR FAVOR, DIGITE A QUANTIDADE DE PRODUTO COMPRADO. VAMOS TENTAR NOVAMENTE:')

    produto_valor_final = produtopreco1 * quantidade
    separar_input()
    produtoparcelas = ''
    while produtoparcelas == '':
        try:
            produtoparcelas = int(input('DIGITE A QUANTIDADE DE PARCELAS: ').strip())
            if produtoparcelas <= -1:
                print(
                    'ERRO: A QUANTIDADE DE PARCELAS NÃO PODE SER MENOR QUE ZERO. VAMOS TENTAR NOVAMENTE:')
                produtoparcelas = ''
        except:
            if len(produtoparcelas) == 0:
                print('ERRO: POR FAVOR, DIGITE A QUANTIDADE DE PARCELAS. VAMOS TENTAR NOVAMENTE:')

    separar_input()
    produtovendas_valor_entrada = ''
    while produtovendas_valor_entrada == '':
        try:
            produtovendas_valor_entrada = float(
                input('DIGITE O VALOR DA ENTRADA ( DIGITE 0 CASO SEJA NULO): R$'))
            if produtovendas_valor_entrada <= -1:
                print(
                    'ERRO: O VALOR DA ENTRADA NÃO PODE SER MENOR QUE 0 REAL. VAMOS TENTAR NOVAMENTE:')
                produtovendas_valor_entrada = ''
        except:
            if len(produtovendas_valor_entrada) == 0:
                print(
                    'ERRO: POR FAVOR, DIGITE O VALOR DA ENTRADA USANDO 0 CASO ELA NÃO EXISTA. VAMOS TENTAR NOVAMENTE:')

    q = quantidade
    v = produtopreco1 * q
    e = produtovendas_valor_entrada
    if produtoparcelas == 0:
        produtoparcelas = 1
    p = produtoparcelas

    vf = (v - e) / p
    separar_input()
    confirma = 'k'
    while confirma[0] not in 'SN':
        confirma = str(input(f"""VOCÊ CONFIRMA A VENDA DO PRODUTO {produto_nomevenda} PARA O CLIENTE DE CPF {formatar_cpf(cliente_cpfvenda)} NOME {produtoclientevenda}
EM QUANTIDADE {quantidade} NO VALOR DE R${produtopreco1 * q:.2f} COM ENTRADA DE R${produtovendas_valor_entrada:.2f} E O RESTANTE R${(v - e):.2f} EM {produtoparcelas} PARCELAS DE R${vf:.2f}? [S/n] """)).upper().strip()

    if confirma[0] == 'S':
        # inserindo dados na tabela //
        conn = sqlite3.connect('bancodedados.db')
        cursor = conn.cursor()
        cursor.execute("""
                    INSERT INTO vendas (vendas_quantidade, vendas_nome_produto, vendas_valor, vendas_parcelas, vendas_valor_entrada, cliente_cpf, vendas_produto_id, vendas_cliente_nome, vendas_valor_total)
                    VALUES (?,?,?,?,?,?,?,?,?)
                    """, (
            quantidade, produto_nomevenda, produtopreco1, produtoparcelas, produtovendas_valor_entrada,
            cliente_cpfvenda,
            produto_idvenda,
            produtoclientevenda, produto_valor_final))

        conn.commit()

        conn.close()
        separar_input()
        print('Registrado com sucesso!')
        time.sleep(3)
