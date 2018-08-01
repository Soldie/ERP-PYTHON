# -*- Coding: utf-8 -*-
import sqlite3


def cliente_cpf_dados(x):
    # Buscando clientes
    conn = sqlite3.connect('bancodedados.db')
    cursor = conn.cursor()
    cursor.execute("""
                                  SELECT * FROM clientes
                                  WHERE cliente_cpf = ?
                                  """, (x,))

    for linha in cursor.fetchall():
        dados = print(f"""CLIENTE: {linha[0]}
                      ID: {linha[1]}
                      CPF: {formatar_cpf(linha[2])} - RG: {formatar_rg(linha[10])} - TELEFONE: {formatar_telefone(linha[3])}
                      ESTADO: {linha[4]} - CIDADE: {linha[5]} - BAIRRO: {linha[6]}
                      RUA: {linha[7]} - NÚMERO: {linha[8]}
                      DATA DO REGISTRO: {formatar_data(linha[11])}
                      SALDO: R${linha[9]:.2f}""")
    conn.commit()
    return dados
    conn.close()


def cliente_cpf_dados_nome(x):
    conn = sqlite3.connect('bancodedados.db')
    cursor = conn.cursor()
    cursor.execute("""
                                              SELECT cliente_nome FROM clientes
                                              WHERE cliente_cpf = ?
                                              """, (x,))

    for linha in cursor.fetchall():
        dadoscliente2 = linha[0]
        return dadoscliente2
    conn.commit()
    conn.close()


def valor_compra(x):
    conn = sqlite3.connect('bancodedados.db')
    # Buscando VENDAS
    cursor = conn.cursor()
    cursor.execute("""
                                   SELECT * FROM vendas
                                   WHERE vendas_id = ?
                                   """, (x,))

    for linha in cursor.fetchall():
        d5 = linha[11] - linha[8]

        return d5
    conn.commit()
    conn.close()


def formatar_data(x):
    d = str(x).split('-')
    c = '{}-{}-{}'.format(d[2], d[1], d[0])
    return c


def formatar_telefone(c):
    if len(c) == 10:
        b = '({}) {}-{}'.format(c[0:2], c[2:6], c[6:10])
        return b
    if len(c) == 11:
        b = '({}) {}-{}'.format(c[0:2], c[2:7], c[7:11])
        return b


def formatar_cpf(c):
    d = '{}.{}.{}-{} '.format(c[0:3], c[3:6], c[6:9], c[9:11])
    return d


def formatar_rg(c):
    b = c[0:2], c[2:4], c[4:7], c[7:10]
    c = '{}-{}.{}.{}'.format(b[0].upper(), b[1], b[2], b[3])
    return c

def separar_input():
    print('-'*102)