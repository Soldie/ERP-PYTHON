# -*- coding: utf-8 -*-
import sqlite3


def criar_tabelas():
    # Banco de Dados //
    conn = sqlite3.connect('bancodedados.db')
    cursor = conn.cursor()

    # Criando estruturas da tabelas caso não exista //

    # CONTA
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contas (
            conta_nome VARCHAR (30) NOT NULL,
            conta_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            conta_login VARCHAR (30) UNIQUE NOT NULL,
            conta_senha_adm VARCHAR (40) NOT NULL,
            conta_senha_padrao VARCHAR (40) NOT NULL
        );
        """)
    # CLIENTES
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        cliente_nome VARCHAR (30) NOT NULL,
        cliente_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        cliente_cpf VARCHAR (30) UNIQUE NOT NULL,
        cliente_telefone VARCHAR (20) NOT NULL,
        cliente_endereco_estado VARCHAR (30) NOT NULL,
        cliente_endereco_cidade VARCHAR (30) NOT NULL,
        cliente_endereco_bairro VARCHAR (30) NOT NULL,
        cliente_endereco_rua    VARCHAR (30) NOT NULL,
        cliente_endereco_numero INT (11) NOT NULL,
        cliente_saldo [INT DECIMAL] (6,2) DEFAULT (0),
        cliente_rg VARCHAR (20) NOT NULL UNIQUE,
        data_registro DATE DEFAULT CURRENT_DATE,
        horario_registro TIME DEFAULT CURRENT_TIME,
        cliente_endereco_cep VARCHAR (30) NOT NULL
    );
    """)

    # EMPRESA
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS empresas (
        empresa_nome VARCHAR (30) NOT NULL,
        empresa_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        empresa_telefone VARCHAR (20) NOT NULL,
        empresa_endereco_estado VARCHAR (30) NOT NULL,
        empresa_endereco_cidade VARCHAR (30) NOT NULL,
        empresa_endereco_bairro VARCHAR (30) NOT NULL,
        empresa_endereco_rua    VARCHAR (30) NOT NULL,
        empresa_endereco_numero INT (11) NOT NULL,
        empresa_cnpj VARCHAR (30) NOT NULL UNIQUE,
        data_registro DATE DEFAULT CURRENT_DATE,
        horario_registro TIME DEFAULT CURRENT_TIME
    );
    """)

    # PRODUTOS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        produto_nome VARCHAR (30) NOT NULL,
        produto_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        produto_tipo VARCHAR (30) NOT NULL,
        produto_cor VARCHAR (30) NOT NULL,
        produto_valor [INT DECIMAL] (6,2) NOT NULL,
        produto_quantidade INTEGER (30) NOT NULL,
        data_registro DATE DEFAULT CURRENT_DATE,
        horario_registro TIME DEFAULT CURRENT_TIME
    );
    """)

    # VENDAS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas (
        cliente_cpf VARCHAR (30) NOT NULL,
        vendas_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        vendas_nome_produto   VARCHAR (30)   NOT NULL,
        vendas_produto_id       VARCHAR (30)   NOT NULL,
        vendas_valor    [INT DECIMAL] (6,2) NOT NULL,
        vendas_data      DATE           DEFAULT CURRENT_DATE,
        vendas_horario  TIME           DEFAULT CURRENT_TIME,
        vendas_parcelas INT            DEFAULT (0),
        vendas_valor_entrada         DECIMAL (6, 2),
        vendas_cliente_nome   VARCHAR (50),
        vendas_quantidade INT            DEFAULT (1),
        vendas_valor_total    [INT DECIMAL] (6,2) NOT NULL
    );
    """)

    # PAGAMENTOS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pagamentos (
        pagamentos_cliente_cpf VARCHAR (30) NOT NULL,
        pagamentos_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        pagamentos_venda_id   VARCHAR (30)   NOT NULL,
        pagamentos_valor    [INT DECIMAL] (6,2) NOT NULL,
        pagamentos_data      DATE           DEFAULT CURRENT_DATE,
        pagamentos_horario  TIME           DEFAULT CURRENT_TIME,
        pagamentos_cliente VARCHAR (30) NOT NULL
    );
    """)

    # FECHA A CONEXÃO
    conn.close()
