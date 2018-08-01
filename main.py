# -*- coding: utf-8 -*-
from funcoes import *
from tabelas import *
from clientes import *
from estoque import *
from caixa import *
import sys
import time
import webbrowser

# Chamando a função que cria as tabelas e o banco
criar_tabelas()


class Augen:
    def iniciar(self):
        # Exibe informações do programa
        programa_header()
        # Explicação Menu
        # Primeiro você define uma lista onde o primeiro termo é o título do menu e os demais são opções
        c = ['Menu Principal', 'Clientes', 'Estoque', 'Vendas e Pagamentos', 'Sistema de reputação *EM BREVE',
             'Sistema de juros *EM BREVE', 'GitHub', 'Licença', 'Sair']
        # Depois você define uma variável com a função menu usando a lista
        d = menu(c)
        # Pronto!
        if d == 1:
            app.menu_clientes()
        if d == 2:
            app.menu_estoque()
        if d == 3:
            app.menu_vendas_pagamentos()
        if d == int(len(c)-2):
            webbrowser.open('https://www.github.com/rafikmoreira/augen')
            app.iniciar()
        if d == int(len(c)-1):
            webbrowser.open('https://www.gnu.org/licenses/gpl-3.0.html')
            app.iniciar()
        elif d == int(len(c)):
            separar_input()
            print('Obrigado por utilizar o Augen!')
            time.sleep(2)
            print('Tenha um bom dia!')
            time.sleep(3)
            app.sair()

    def sair(self):
        sys.exit()

    def menu_clientes(self):
        m_clientes = ['Menu Clientes', 'Cadastrar Cliente', 'Listar Clientes', 'Pesquisar Cpf', 'Deletar Cliente', 'Menu Principal']
        f = menu(m_clientes)
        if f == 1:
            cliente_cadastro()
        if f == 2:
            lista_clientes()
        if f == 3:
            buscar_cliente()
        if f == 4:
            deletar_cliente()
        if f == int(len(m_clientes)):
            app.iniciar()
        pass

    def menu_estoque(self):
        m_estoque = ['Menu Estoque', 'Cadastrar Produto/Serviço', 'Listar Produtos/Serviços', 'Pesquisar Registro', 'Deletar Registro',
                      'Menu Principal']
        f = menu(m_estoque)
        if f == 1:
            estoque_cadastro()
        if f == 2:
            lista_estoque()
        if f == 3:
            buscar_estoque()
        if f == 4:
            deletar_estoque()
        if f == int(len(m_estoque)):
            app.iniciar()
        pass

    def menu_vendas_pagamentos(self):
        m_vendas_e_pagamentos = ['Vendas E Pagamentos', 'Registrar Venda', 'Vendas Do Dia', 'Registrar Pagamento', 'Listar Pagamentos Do Dia',
                     'Deletar Registro',
                     'Menu Principal']
        f = menu(m_vendas_e_pagamentos)
        if f == 1:
            registrar_vendas_vendasepagamentos()
        if f == 2:
            vendasdodia_vendasepagamentos()
        if f == 3:
            registrar_pagamentos_vendasepagamentos()
        if f == 4:
            pagamentosdodia_vendasepagamentos()
        if f == 5:
            deletar_registro_vendasepagamentos()
        if f == int(len(m_vendas_e_pagamentos)):
            app.iniciar()
        pass
        pass

    def sistema_de_reputacao(self):
        pass

    def sistema_de_juros(self):
        pass


while True:
    app = Augen()
    app.iniciar()
