# -*- coding: utf-8 -*-
import time
import sysconfig
import sqlite3
from formatacao import *


# Use uma lista para o valor de 'a' onde o primeiro termo é sempre o título do menu!!
def menu(a):
    print(f'[{a[0]:-^100}]\n')
    n = 0
    del a[0]
    for opcao in a:
        n += 1
        print(f'[{n}] {str(opcao).title()}')
    selecao = int(input('\nDigite o número da opção desejada: '))
    print()
    return selecao


# Header do programa
def programa_header():
    # NÃO REMOVA ESSES DADOS =================>
    print(f"[{' Augen v0.1.1 Copyright (C) 2018 RAFIK MOREIRA DIAS ':-^100}]")
    tempo = time.localtime()
    print('[{:-^100}]'.format(
        ' SISTEMA OPERACIONAL: {} - DATA: {}/{}/{} {}h {}m '.format(sysconfig.get_platform(), tempo[2], tempo[1],
                                                                    tempo[0], tempo[3], tempo[4])))
    print(
        '[{:-^100}]'.format(

            ' O programa Augen vem ABSOLUTAMENTE SEM NENHUMA GARANTIA; '.upper()))
    print('[{:-^100}]'.format(' SOCIAL: HTTPS://FACEBOOK.COM/RAFIKMOREIRA '))
    print('[{:-^100}]'.format(' GITHUB: HTTPS://GITHUB.COM/RAFIKMOREIRA '))
    print('[{:-^100}]'.format(' CONTATO: RAFIKMOREIRADIAS@OUTLOOK.COM '))
    print()
    # NÃO REMOVA ESSES DADOS =================>


def cliente_cpf_dados(x):
    # Buscando clientes
    conn = sqlite3.connect('bancodedados.db')
    cursor = conn.cursor()
    cursor.execute("""
                                  SELECT * FROM clientes
                                  WHERE cliente_cpf = ?
                                  """, (x,))

    for linha in cursor.fetchall():
        dados = print('CLIENTE: {}'
                      '\nID: {}'
                      '\nCPF: {} - RG: {} - TELEFONE: {}'
                      '\nESTADO: {} - CIDADE: {} - BAIRRO: {}'
                      '\nRUA: {} - NÚMERO: {}'
                      '\nDATA DO REGISTRO: {}'
                      '\nSALDO: R${:.2f}'.format(
            linha[0], linha[1], formatar_cpf(linha[2]), formatar_rg(linha[10]),
            formatar_telefone(linha[3]), linha[4], linha[5], linha[6],
            linha[7], linha[8], formatar_data(linha[11]), linha[9]))
    conn.commit()
    return dados
    conn.close()


def info_produto(x):
    conn = sqlite3.connect('bancodedados.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
                SELECT * FROM produtos
                               WHERE produto_id = ?
                               """, (x,))

    for linha in cursor.fetchall():
        print(f"""PRODUTO: {linha[0]} - PRODUTO ID: {linha[1]} - TIPO DO PRODUTO: {linha[2]} - COR DO PRODUTO: {linha[3]}
VALOR DO PRODUTO: R${linha[4]:.2f}'
QUANTIDADE EM ESTOQUE: {linha[5]} - DATA DO REGISTRO: {formatar_data(linha[6])}""")
    conn.close()


def info_produto_nome(x):
    conn = sqlite3.connect('bancodedados.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
                SELECT produto_nome FROM produtos
                               WHERE produto_id = ?
                               """, (x,))

    for linha in cursor.fetchall():
        p_nome = linha[0]
        return p_nome
    conn.close()


def info_produto_valor(x):
    conn = sqlite3.connect('bancodedados.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
                SELECT produto_valor FROM produtos
                               WHERE produto_id = ?
                               """, (x,))

    for linha in cursor.fetchall():
        p_valor = linha[0]
        return p_valor
    conn.close()


def venda_id_dados(x):
    conn = sqlite3.connect('bancodedados.db')
    cursor = conn.cursor()
    # Buscando VENDAS
    # Buscando VENDAS

    cursor.execute("""
                               SELECT * FROM vendas
                               WHERE vendas_id = ?
                               """, (x,))

    for linha in cursor.fetchall():
        vv1 = float(linha[11])

        ve2 = float(linha[8])

        vp3 = float(linha[7])
        d5 = print(f"""DATA DA COMPRA: {formatar_data(linha[5])} - CPF USADO: {formatar_cpf(linha[0])} - ID DA VENDA {linha[1]}
PRODUTO: {linha[2]} - ID DO PRODUTO COMPRADO: {linha[3]}
VALOR DO PRODUTO: R${linha[4]:.2f} QUANTIDADE: {linha[10]} VALOR TOTAL DA COMPRA: R${linha[11]:.2f}
Entrada DE R${linha[8]:.2f} RESTANDO R${(vv1 - ve2):.2f}
RESTANTE DO PAGAMENTO EM {linha[7]} PARCELA(S) DE R${((vv1 - ve2) / vp3):.2f}.""")
    return d5
    conn.commit()
    conn.close()
