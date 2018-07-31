import sqlite3
from formatacao import *
import sys
import time


def estoque_cadastro():
    produto_nome = ''
    while produto_nome == '':
        try:
            produto_nome = str(input('\n[{:-^100}]\n'
                                     '\nDIGITE O NOME DO PRODUTO: '.format(
                'CADASTRO PRODUTOS')).strip().upper())
        except:
            if len(produto_nome) == 0:
                print('ERRO: POR FAVOR, DIGITE O NOME DO PRODUTO. VAMOS TENTAR NOVAMENTE:')

    produto_tipo = ''
    while produto_tipo == '':
        try:
            produto_tipo = str(
                input('QUAL O TIPO DO PRODUTO? (BEBIDAS, ROUPAS, ALIMENTOS ETC): ').strip().upper())
        except:
            if len(produto_tipo) == 0:
                print('ERRO: POR FAVOR, DIGITE O TIPO DO PRODUTO. VAMOS TENTAR NOVAMENTE:')

    produto_cor = ''
    while produto_cor == '':
        try:
            produto_cor = str(input('DIGITE A COR DO PRODUTO: ').strip().upper())
        except:
            if len(produto_cor) == 0:
                print('ERRO: POR FAVOR, DIGITE A COR DO PRODUTO. VAMOS TENTAR NOVAMENTE:')

    produto_valor = ''
    while produto_valor == '':
        try:
            produto_valor = float(input('DIGITE O VALOR UNITÁRIO DO PRODUTO: R$').strip())
        except:
            if len(produto_valor) == 0:
                print(
                    'ERRO: POR FAVOR, DIGITE O VALOR UNITÁRIO DO PRODUTO. VAMOS TENTAR NOVAMENTE:')

    produto_quantidade = ''
    while produto_quantidade == '':
        try:
            produto_quantidade = int(input('DIGITE A QUANTIDADE DO PRODUTO EM ESTOQUE: ').strip())
        except:
            if len(produto_quantidade) == 0:
                print(
                    'ERRO: POR FAVOR, DIGITE A QUANTIDADE DO PRODUTO EM ESTOQUE. VAMOS TENTAR NOVAMENTE:')

    confirma = 'k'
    while confirma[0] not in 'SN':
        confirma = str(input(f"""VOCÊ CONFIRMA O REGISTRO DO PRODUTO {produto_nome} EM QUANTIDADE {produto_quantidade}
DO TIPO {produto_tipo} COM VALOR UNITÁRIO DE R${produto_valor:.2f} NA COR {produto_cor}? [S/n] """).upper())
    if confirma[0] == 'S':
        conn = sqlite3.connect('bancodedados.db')
        cursor = conn.cursor()
        # inserindo dados na tabela //

        cursor.execute("""
                    INSERT INTO produtos (produto_nome, produto_tipo, produto_cor, produto_valor, produto_quantidade)
                    VALUES (?,?,?,?,?)
                    """, (produto_nome, produto_tipo, produto_cor, produto_valor, produto_quantidade))

        conn.commit()

        conn.close()

        # FINAL CADASTRO PRODUTO //

        print('Produto registrado com sucesso!')
        time.sleep(3)


def lista_estoque():
    print('\n[{:-^100}]\n'.format(
        'LISTA DE PRODUTOS'))
    conn = sqlite3.connect('bancodedados.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
                SELECT * FROM produtos ORDER BY produto_nome;
                """)

    for linha in cursor.fetchall():
        print(f"""PRODUTO: {linha[0]} - PRODUTO ID: {linha[1]} - TIPO DO PRODUTO: {linha[2]} - COR DO PRODUTO: {linha[3]}\nVALOR DO PRODUTO: R${linha[4]:.2f}'
QUANTIDADE EM ESTOQUE: {linha[5]} - DATA DO REGISTRO: {formatar_data(linha[6])}""")
        print('-' * 102)
    conn.close()

    confirma = 'k'
    while confirma[0] not in 'SN':
        confirma = str(input('Deseja voltar ao menu inicial? [S/n] ')).upper().strip()
    if confirma[0] == 'S':
        pass
    elif confirma[0] == 'N':
        sys.exit()


def buscar_estoque():
    conn = sqlite3.connect('bancodedados.db')
    cursor = conn.cursor()

    produtobuscar = input(
        "\n[{:-^100}]\n"
        "\nBUSCAREMOS TODAS AS INFORMAÇÕES DO PRODUTO, DIGITE O ID: ".format('BUSCAR PRODUTO'))

    # Buscando clientes

    cursor.execute("""
                       SELECT * FROM produtos
                       WHERE produto_id = ?
                       """, (produtobuscar,))

    for linha in cursor.fetchall():
        print(
            f'PRODUTO: {linha[0]} - ID: {linha[1]} - TIPO: {linha[2]} - COR: {linha[3]} - VALOR: R${linha[4]:.2F} - QUANTIDADE EM ESTOQUE: {linha[5]}.')
    conn.commit()

    conn.close()
    confirma = 'k'
    while confirma[0] not in 'SN':
        confirma = str(input('Deseja voltar ao menu inicial? [S/n] ')).upper().strip()
    if confirma[0] == 'S':
        pass
    elif confirma[0] == 'N':
        sys.exit()
    # EXIBIR INFO PRODUTO


def deletar_estoque():
    conn = sqlite3.connect('bancodedados.db')
    cursor = conn.cursor()

    produto_id1 = input(
        "\n[{:-^100}]\n\n"
        "DIGITE O ID DO PRODUTO: ".format(
            'DELETAR PRODUTO'))
    # lendo os dados
    cursor.execute("""
                           SELECT * FROM produtos WHERE produto_id = ? LIMIT 1;
                           """, (produto_id1,))

    for linha in cursor.fetchall():
        print('')

    confirma = 'k'
    while confirma[0] not in 'SN':
        confirma = str(input(f"""VOCÊ CONFIRMA A REMOÇÃO DO PRODUTO {linha[0]} NA COR {linha[3]} TIPO {linha[2]} ADICIONADO EM {formatar_data(linha[6])}
DO ESTOQUE? [S/n] """)).upper().strip()
    if confirma[0] == 'S':
        # excluindo um registro da tabela

        cursor.execute("""
                    DELETE FROM produtos
                    WHERE produto_id = ?
                    """, (produto_id1,))

        conn.commit()

        conn.close()
        confirma = 'k'
        while confirma[0] not in 'SN':
            confirma = str(input('Deseja voltar ao menu inicial? [S/n] ')).upper().strip()
        if confirma[0] == 'S':
            pass
        elif confirma[0] == 'N':
            sys.exit()
