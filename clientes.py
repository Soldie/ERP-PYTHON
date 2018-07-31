import sqlite3
import time
import sys
from funcoes import *
from formatacao import *


def cliente_cadastro():
    cliente_nome = ''
    while cliente_nome == '':
        try:
            cliente_nome = str(input('\n[{:-^100}]\n'
                                     '\nDIGITE O NOME COMPLETO DO CLIENTE: '.format(
                'CADASTRO CLIENTE')).strip().upper())
        except:
            if len(cliente_nome) == 0:
                print('ERRO: POR FAVOR, DIGITE O NOME COMPLETO DO CLIENTE. VAMOS TENTAR NOVAMENTE: ')

    cliente_telefone = ''
    while cliente_telefone == '':
        try:
            cliente_telefone = str(input('DIGITE O TELEFONE DO CLIENTE: '))
            x = cliente_telefone.isnumeric()
            if x == True:
                if len(cliente_telefone) == 10 or len(cliente_telefone) == 11:
                    cliente_telefone = cliente_telefone
                else:
                    print(
                        'ERRO: O NÚMERO NÃO FOI ACEITO PELO SISTEMA.'
                        '\nDIGITE O NÚMERO COM FORMATO 33988002222 OU 3388002222.\n'
                        'VAMOS TENTAR NOVAMENTE: ')
                    cliente_telefone = ''
            else:
                print('ERRO: DIGITE APENAS NÚMEROS! VAMOS TENTAR NOVAMENTE: ')
                cliente_telefone = ''
        except:
            if len(cliente_telefone) == 0:
                print(
                    'ERRO: POR FAVOR, DIGITE O TELEFONE DO CLIENTE. VAMOS TENTAR NOVAMENTE: ')
                cliente_telefone == ''

    cliente_cpf = ''
    while cliente_cpf == '':
        try:
            cliente_cpf = str(input('DIGITE O CPF DO CLIENTE: ').strip())
            v = cliente_cpf.isnumeric()
            if v == True:
                if len(cliente_cpf) != 11:
                    print('ERRO: UM CPF TEM 11 NÚMEROS. VAMOS TENTAR NOVAMENTE: ')
                    cliente_cpf = ''
            else:
                print('ERRO: DIGITE O CPF USANDO APENAS NÚMEROS. VAMOS TENTAR NOVAMENTE: ')
                cliente_cpf = ''
        except:
            if len(cliente_cpf) == 0:
                print('ERRO: POR FAVOR, DIGITE O CPF DO CLIENTE. VAMOS TENTAR NOVAMENTE: ')

    cliente_rg = ''
    while cliente_rg == '':
        try:
            cliente_rg = str(input('DIGITE O RG DO CLIENTE: '))
            x = len(cliente_rg)
            if x != 10:
                print('NÃO PARECE SER UM RG, USE O FORMATO MG15232323. VAMOS TENTAR NOVAMENTE: ')
                cliente_rg = ''
        except:
            print('ERRO: DIGITE O RG. VAMOS TENTAR NOVAMENTE: ')

    estados = {'MG' == 'MINAS GERAIS', 'SC' == 'SANTA CATARINA', 'SP' == 'SÃO PAULO',
               'TESTE' == 'VERSÃO DE TESTE'}

    cliente_endereco_estado = ''
    while cliente_endereco_estado == '':
        try:
            cliente_endereco_estado = str(input('ENDEREÇO - ESTADO UF: ').strip().upper())
            x = cliente_endereco_estado.isalpha()
            if len(cliente_endereco_estado) != 2 or x != True:
                print('DIGITE APENAS O UF DO ESTADO, EXEMPLO: MG. VAMOS TENTAR NOVAMENTE: ')
                ufprint = ''
                while ufprint == '':
                    try:
                        ufprint = str(input('DESEJA VISUALIZAR A LISTA DE UF?\n'
                                            'RESPONDA SIM COM [S] E NÃO COM [N] *APENAS LETRAS! ').upper().strip())

                        if ufprint == 'S' or ufprint == 'N':
                            if ufprint == 'S':
                                print('LISTA EM BREVE')
                        else:
                            print('ERRO: DIGITE APENAS S OU N. VAMOS TENTAR NOVAMENTE: ')
                            ufprint = ''
                    except:
                        print('ERRO: DIGITE UMA RESPOSTA. VAMOS TENTAR NOVAMENTE: ')
                cliente_endereco_estado = ''
        except:
            if len(cliente_endereco_estado) == 0:
                print('ERRO: POR FAVOR, DIGITE O ENDEREÇO - ESTADO. VAMOS TENTAR NOVAMENTE: ')

    cliente_endereco_cep = ''
    while cliente_endereco_cep == '':
        try:
            cliente_endereco_cep = str(input('ENDEREÇO - CEP: '))
        except:
            if len(cliente_endereco_cep) == 0:
                print('ERRO: DIGITE O CEP: VAMOS TENTAR NOVAMENTE: ')

    cliente_endereco_cidade = ''
    while cliente_endereco_cidade == '':
        try:
            cliente_endereco_cidade = str(input('ENDEREÇO - CIDADE: ').strip().upper())
        except:
            if len(cliente_endereco_cidade) == 0:
                print('ERRO: POR FAVOR, DIGITE O ENDEREÇO - CIDADE. VAMOS TENTAR NOVAMENTE: ')

    cliente_endereco_bairro = ''

    while cliente_endereco_bairro == '':
        try:
            cliente_endereco_bairro = str(input('ENDEREÇO - BAIRRO: ').strip().upper())
        except:
            if len(cliente_endereco_bairro) == 0:
                print('ERRO: POR FAVOR, DIGITE O ENDEREÇO - BAIRRO. VAMOS TENTAR NOVAMENTE: ')

    cliente_endereco_rua = ''
    while cliente_endereco_rua == '':
        try:
            cliente_endereco_rua = str(input('ENDEREÇO - RUA: ').strip().upper())
        except:
            if len(cliente_endereco_rua) == 0:
                print('POR FAVOR, DIGITE O ENDEREÇO - RUA. VAMOS TENTAR NOVAMENTE: ')

    cliente_endereco_numero = ''
    while cliente_endereco_numero == '':
        try:
            cliente_endereco_numero = int(input('ENDEREÇO - NÚMERO: ').strip())
        except:
            if len(cliente_endereco_numero) == 0:
                print('ERRO: POR FAVOR, DIGITE O ENDEREÇO - NÚMERO. VAMOS TENTAR NOVAMENTE: ')
    confirma = 'k'
    while confirma[0] not in 'SN':
        confirma = str(
            input(f"""VOCÊ CONFIRMA O CADASTRO DO CLIENTE {cliente_nome} COM CPF {cliente_cpf}, RG {cliente_rg},
TELEFONE {cliente_telefone}, MORADOR DO ESTADO DE {cliente_endereco_estado}, CIDADE {cliente_endereco_cidade}, CEP {cliente_endereco_cep}
BAIRRO {cliente_endereco_bairro}, RUA {cliente_endereco_rua}, NÚMERO {cliente_endereco_numero}?
VOCÊ CONFIRMA? [S/n]: """)).strip().upper()

    if confirma[0] == 'S':
        # inserindo dados na tabela //
        conn = sqlite3.connect('bancodedados.db')

        cursor = conn.cursor()
        cursor.execute("""
                    INSERT INTO clientes (cliente_nome, cliente_cpf, cliente_telefone, cliente_endereco_estado,
                    cliente_endereco_cidade, cliente_endereco_bairro, cliente_endereco_rua, cliente_endereco_numero, cliente_rg,cliente_endereco_cep)
                    VALUES (?,?,?,?,?,?,?,?,?,?)
                    """, (cliente_nome, cliente_cpf, cliente_telefone, cliente_endereco_estado, cliente_endereco_cidade,
                          cliente_endereco_bairro, cliente_endereco_rua, cliente_endereco_numero, cliente_rg,
                          cliente_endereco_cep))

        conn.commit()

        # FECHA A CONEXÃO

        conn.close()
        print('Cliente cadastrado com sucesso.')
        time.sleep(2)
        # FINAL CADASTRO CLIENTE //

def lista_clientes():
    print('[{:-^100}]\n'

          ''.format(
        'LISTA DE CLIENTES'))

    conn = sqlite3.connect('bancodedados.db')

    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
                SELECT * FROM clientes ORDER BY cliente_nome;
                """)

    for linha in cursor.fetchall():
        print(f"""CLIENTE: {linha[0]}
ID: {linha[1]}
CPF: {formatar_cpf(linha[2])} - RG: {formatar_rg(linha[10])} - TELEFONE: {formatar_telefone(linha[3])}
ESTADO: {linha[4]} - CIDADE: {linha[5]} - BAIRRO: {linha[6]} - RUA: {linha[7]}
NÚMERO: {linha[8]}
DATA DO REGISTRO: {formatar_data(linha[11])}
SALDO: R${linha[9]:.2f}
{'-'*102}""")

    conn.close()

    confirma = 'k'
    while confirma[0] not in 'SN':
        confirma = str(input('Deseja voltar ao menu inicial? [S/n] ')).upper().strip()
    if confirma[0] == 'S':
        pass
    elif confirma[0] == 'N':
        sys.exit()

def buscar_cliente():
    conn = sqlite3.connect('bancodedados.db')

    cursor = conn.cursor()

    buscar = ''

    while buscar == '':
        try:
            buscar = input(
                "\n[{:-^100}]\n"
                "\nBUSCAREMOS TODAS AS INFORMAÇÕES DO CLIENTE, DIGITE O CPF: ".format(
                    'EXIBIR DADOS DO CLIENTE')).strip()

            v = buscar.isnumeric()
            if v == True:
                if len(buscar) != 11:
                    print('ERRO: UM CPF TEM 11 NÚMEROS. VAMOS TENTAR NOVAMENTE: ')
                    buscar = ''
            else:
                print('ERRO: DIGITE O CPF USANDO APENAS NÚMEROS. VAMOS TENTAR NOVAMENTE: ')
                buscar = ''
        except:
            if len(buscar) == 0:
                print('ERRO: POR FAVOR, DIGITE O CPF DO CLIENTE. VAMOS TENTAR NOVAMENTE: ')

    print('\n[{:-^100}]\n'.format(
        'INFORMAÇÕES DO CLIENTE'))


    # Buscando clientes
    cursor.execute("""
                       SELECT * FROM clientes
                       WHERE cliente_cpf = ?
                       """, (buscar,))

    for linha in cursor.fetchall():
        print(f"""CLIENTE: {linha[0]}
ID: {linha[1]}
CPF: {formatar_cpf(linha[2])} - RG: {formatar_rg(linha[10])} - TELEFONE: {formatar_telefone(linha[3])}
ESTADO: {linha[4]} - CIDADE: {linha[5]} - BAIRRO: {linha[6]}
RUA: {linha[7]} - NÚMERO: {linha[8]}
DATA DO REGISTRO: {formatar_data(linha[11])}
SALDO: R${linha[9]:.2f}
""")

    conn.commit()

    print('[{:-^100}]\n'.format(
        'INFORMAÇÕES DE COMPRAS'))


    # Buscando VENDAS

    cursor.execute("""
                               SELECT * FROM vendas
                               WHERE cliente_cpf = ? Order by vendas_data
                               """, (buscar,))

    for linha in cursor.fetchall():
        vv1 = float(linha[11])

        ve2 = float(linha[8])

        vp3 = float(linha[7])
        print(f"""DATA DA COMPRA: {formatar_data(linha[5])} - CPF USADO: {formatar_cpf(linha[0])} - ID DA VENDA { linha[1]}
PRODUTO: {linha[2]} - ID DO PRODUTO COMPRADO: {linha[3]}
VALOR DO PRODUTO: R${linha[4]:.2f} QUANTIDADE: {linha[10]} VALOR TOTAL DA COMPRA: R${linha[11]}
ENTRADA DE R${linha[8]:.2f} RESTANDO R${vv1 - ve2:.2f}
RESTANTE DO PAGAMENTO EM {linha[7]} PARCELA(S) DE R${(vv1 - ve2) / vp3:.2f}.""")
        print('-'*102)

    conn.commit()

    # EXIBIR COMPRAS DO CLIENTE

    print('[{:-^100}]\n'.format(
        'INFORMAÇÕES DE PAGAMENTOS'))
    # BUSCANDO PAGAMENTOS

    cursor.execute("""
                               SELECT * FROM pagamentos
                               WHERE pagamentos_cliente_cpf = ? Order by pagamentos_data
                               """, (buscar,))

    for linha in cursor.fetchall():
        print(f"""DATA DO PAGAMENTO: {formatar_data(linha[4])} - CPF USADO: {formatar_cpf(linha[0])} - ID DO PAGAMENTO {linha[1]}
ID DA OPERAÇÃO DE VENDA: {linha[2]} - VALOR DO PAGAMENTO: R${linha[3]:.2F}.""")
        print('-' * 102)
    conn.commit()



    conn.close()
    confirma = 'k'
    while confirma[0] not in 'SN':
        confirma = str(input('Deseja voltar ao menu inicial? [S/n] ')).upper().strip()
    if confirma[0] == 'S':
        pass
    elif confirma[0] == 'N':
        sys.exit()
    # EXIBIR PAGAMENTOS DO CLIENTE

def deletar_cliente():
    conn = sqlite3.connect('bancodedados.db')
    cursor = conn.cursor()
    buscar = ''

    while buscar == '':
        try:
            buscar = str(input(
                "\n[{:-^100}]\n\n"
                "Digite o CPF DO CLIENTE: ".upper().format(
                    'DELETAR CLIENTE')).strip().upper())
            v = buscar.isnumeric()
            if v == True:
                if len(buscar) != 11:
                    print('ERRO: UM CPF TEM 11 NÚMEROS. VAMOS TENTAR NOVAMENTE: ')
                    buscar = ''
            else:
                print('ERRO: DIGITE O CPF USANDO APENAS NÚMEROS. VAMOS TENTAR NOVAMENTE: ')
                buscar = ''
        except:
            if len(buscar) == 0:
                print('ERRO: POR FAVOR, DIGITE O CPF DO CLIENTE. VAMOS TENTAR NOVAMENTE: ')


    cliente_cpf_dados(buscar)
    confirma = 'k'
    while confirma[0] not in 'SN':
        confirma = str(input('Você confirma? [S/n] ')).upper().strip()
    if confirma[0] == 'S':
        # excluindo um registro da tabela
        cursor.execute("""
                    DELETE FROM clientes
                    WHERE cliente_cpf = ?
                    """, (buscar,))

        conn.commit()



        conn.close()
        print('Cliente deletado com sucesso!')
        time.sleep(2)