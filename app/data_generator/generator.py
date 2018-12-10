import random
import string
import re
import time

import numpy as np
import pandas as pd
from faker import Faker
from faker.providers import BaseProvider
from datetime import datetime
from datetime import timedelta

faker = Faker('pt_BR')


class Provider(BaseProvider):

    def numeric_code(self, lenght):
        import random
        numbers = [str(random.randint(0, 9)) for _ in range(lenght)]
        return "".join(numbers)

    def cpf(self):
        return "{}.{}.{}-{}".format(self.numeric_code(3), self.numeric_code(3), self.numeric_code(3),
                                    self.numeric_code(2))

    def random_int(self):
        return random.randint(5, 1000)

    def monetary(self):
        value = random.randint(10, 1000) / 100 + random.randint(1, 100) / 100
        return value


faker.add_provider(Provider)


class BASECOMPRASPDV_DDL:
    """
    Cada tabela se transforma em uma classe, isso facilita organizar metodos caso sejam necessarios
    Os atributos de cada tabela estão organizdos em um dicionario para facilitar a manipulação.
    O construtor da classe ja atribui valores faker para cada campo

    """

    def __init__(self):
        self.info = {
            'CPF': faker.cpf(),
            'COD_GRUPO_FRANQUIA': random.choice(lista_franquia),
            'CD_LOJA': random.choice(lista_lojas),
            'Z_CD_LOJA': random.choice(lista_lojas),
            'NR_PDV': random.randint(1, 100000),
            'NR_CUPOM': random.randint(1, 100000),
            'DT_VENDA': random_dates('fim'),
            'CD_PRODUTO': random.choice(lista_produtos),
            'CD_STATUS_CUPOM': random.randint(1, 100),
            'DH_TIMESTAMP': random_dates('fim'),
            'DH_TIMESTAMP_DEC': random_dates('fim'),
            'NR_ATENDIMENTO': round(random.uniform(1, 1000), 2),
            'DS_ORIGEM_BOLETO': faker.text(5),
            'CD_CONSULTOR': ''.join(random.choices(string.ascii_uppercase + string.digits, k=20)),
            'COD_GRUPO_CONTAS': random.choice(lista_grupo_contas),
            'DES_MATERIAL': faker.text(40),
            'COD_MARCA': random.choice(lista_marca),
            'DES_MARCA': faker.text(40),
            'COD_LINHA': random.choice(lista_linha),
            'COD_CATEGORIA': random.choice(lista_categoria),
            'DES_CATEGORIA': faker.text(40),
            'COD_SUBCATEGORIA': random.choice(lista_grupo_contas),
            'DES_SUBCATEGORIA': faker.text(40),
            'DES_SUBMODELO': faker.text(40),
            'QT_VENDA': random.randint(1, 1000),
            'VL_VENDA': round(random.uniform(1, 1000), 2),
            'VL_VENDA_LIQ': round(random.uniform(1, 1000), 2),
            'VL_DSCT_TOTAL': round(random.uniform(1, 10), 2),
            'VL_DSCT_FIDELI': round(random.uniform(1, 10), 2),
            'VL_COMISSAO': round(random.uniform(1, 10), 2),
            'FIDELIDADE': ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
            'QT_PONTOS_UTILIZADOS': round(random.uniform(1, 100), 2),
            'DT_ATUALIZACAO': random_dates('fim')
        }


class BASECONSUMIDOR_BOT_DDL:
    def __init__(self):
        first_name = faker.first_name()
        last_name = faker.last_name()
        self.info = {
            'CPF': faker.cpf(),
            'BUSINESS_PARTNER': faker.text(10),
            'NOME_PRIMEIRO': first_name,
            'NOME_ULTIMO': last_name,
            'NOME_COMPLETO': first_name + ' ' + last_name,
            'SEXO': random.choice(lista_sexo),
            'DT_NASCIMENTO': faker.date_of_birth().strftime('%Y-%m-%d %H:%M:%S'),
            'IDADE': random.randint(18, 100),
            'NACIONALIDADE': faker.bank_country(),
            'COD_ORIGEM_CADASTRO': faker.text(18),
            'DES_ORIGEM_CADASTRO': faker.text(21),
            'COD_LOJA_CADASTRO': random.choice(lista_lojas),
            'COD_LOJA_ALTERACAO': random.choice(lista_lojas),
            'COD_CANAL_ALTERACAO': random.choice(lista_canal),
            'DT_CADASTRO': faker.date(),
            'DT_ALTERACAO': faker.date(),
            'COD_CONSULTOR_CADASTRO': faker.first_name(),
            'COD_TIPO_CLIENTE': ''.join(random.choices(string.ascii_uppercase + string.digits, k=1)),
            'DES_TIPO_CLIENTE': faker.text(11),
            'ENDER_RUA': faker.street_name(),
            'ENDER_NUMERO': random.randint(1, 1000),
            'ENDER_COMPLEMENTO': faker.text(10),
            'BAIRRO': faker.text(50),
            'CIDADE': faker.city(),
            'CEP': ''.join(random.choices(string.digits, k=10)),
            'ESTADO': faker.state(),
            'PAIS': faker.country(),
            'TEL_RESIDENCIAL': faker.phone_number(),
            'TEL_COMERCIAL': faker.phone_number(),
            'TEL_CELULAR': faker.phone_number(),
            'EMAIL': faker.email(),
            'EMAIL_2': faker.email(),
            'IN_EMAIL_VALIDO_2': faker.email(),
            'EMAIL_3': faker.email(),
            'IN_EMAIL_VALIDO_3': faker.email(),
            'COD_LOJA_PREF': random.choice(lista_lojas),
            'CIDADE_PREF': faker.city(),
            'ESTADO_PREF': faker.state(),
            'DT_ULTIMO_RESGATE_DESCONTO': random_dates('ini'),
            'IN_RESGATE_ANO_ATUAL': ''.join(random.choices(string.ascii_uppercase + string.digits, k=1)),
            'IN_RESGATE_ANO_ANTERIOR': ''.join(random.choices(string.ascii_uppercase + string.digits, k=1)),
            'COD_LOJA_PRIMEIRA_COMPRA_FIDELIDADE': random.choice(lista_lojas),
            'DT_PRI_COMPRA_FIDELIDADE': random_dates('ini'),
            'DT_ULT_COMPRA_FIDELIDADE': random_dates('fim'),
            'DT_PRI_COMPRA_MV': random_dates('ini'),
            'DT_ULT_COMPRA_MV': random_dates('fim'),
            'DT_PRI_COMPRA_PDV': random_dates('ini'),
            'DT_ULT_COMPRA_PDV': random_dates('fim'),
            'COD_FRANQ_PREF': faker.text(10),
            'DES_SEGMENTACAO': faker.text(50),
            'QTD_PONTOS_FID_ATUAL': random.randint(1, 100),
            'QTD_PONTOS_FID_VENCER_MES_ATUAL': random.randint(1, 100),
            'QTD_PONTOS_FID_VENCER_30': random.randint(1, 100),
            'QTD_PONTOS_FID_VENCER_60': random.randint(1, 100),
            'QTD_PONTOS_FID_VENCER_90': random.randint(1, 100),
            'QTD_PONTOS_FID_VENCER_90_MAIS': random.randint(1, 100),
            'QTD_DIAS_PRI_COMPRA': random.randint(1, 100),
            'QTD_DIAS_ULT_COMPRA': random.randint(1, 100),
            'QTD_BOLETOS_12MESES': random.randint(1, 100),
            'VLR_BOLETOS_12MESES': round(random.uniform(1, 1000), 2),
            'DT_ATUALIZACAO': random_dates('fim')
        }


class SELLOUT_TB_LOJA_VENDA_SO_DDL:
    def __init__(self):
        self.info = {
            'CD_PRODUTO': ''.join(random.choices(string.ascii_uppercase + string.digits, k=18)),
            'CD_LOJA': random.choice(lista_lojas),
            'DT_VENDA': random_dates('ini'),
            'NR_HORA': random.randint(8, 22),
            'NR_CUPOM': random.randint(1, 10000000),
            'NR_PDV': random.randint(1, 100000),
            'ID_VENDEDOR': random.choice(lista_vendedor),
            'CD_STATUS_CUPOM': random.randint(1, 100000),
            'NR_SEQ': random.randint(1, 100000),
            'NR_QTD_VENDA': random.randint(1, 100),
            'VL_VENDA': round(random.uniform(1, 1000), 2),
            'VL_DSCT_TOTAL': round(random.uniform(1, 10), 2),
            'VL_DSCT_FIDELI': round(random.uniform(1, 10), 2),
            'VL_COMISSAO': round(random.uniform(1, 10), 2),
            'CD_TIPO_DOC': faker.text(50),
            'Z_CD_LOJA': random.choice(lista_lojas),
            'DH_TIMESTAMP': random_dates('ini'),
            'DH_TIMESTAMP_DEC': round(random.uniform(1, 1000), 2),
            'ID_RECORDO': random.randint(1, 100000),
            'ID_RECORDIO': random.randint(1, 100000),
            'IN_DOC_FISCAL': ''.join(random.choices(string.ascii_uppercase + string.digits, k=1)),
            'DS_ORIGEM_BOLETO': faker.text(5),
            'DS_CPF_CNPJ': faker.cpf(),
            'NR_ATENDIMENTO': random.randint(1, 100),
            'UFLAG': ''.join(random.choices(string.ascii_uppercase + string.digits, k=1))
        }


class BASECOMPRASECM_DDL:
    def __init__(self):
        self.info = {
            'CPF': ''.join(random.choices(string.digits, k=11)),
            'CD_PRODUTO': ''.join(random.choices(string.ascii_uppercase + string.digits, k=18)),
            'DS_UNIDADE_NEGOCIO': random.choice(lista_un_negocio),
            'DT_VENDA': str(random_dates('ini'))[0:10],
            'NR_CUPOM': random.randint(1, 100000),
            'CD_LOJA': random.choice(lista_lojas),
            'NR_PDV': random.randint(1, 100000),
            'DS_STATUS_CUPOM': faker.text(50),
            'ID_VENDEDOR': faker.text(20),
            'NR_ATENDIMENTO': random.randint(1, 1000000),
            'DES_MATERIAL': faker.text(40),
            'COD_MARCA': random.choice(lista_marca),
            'DES_MARCA': faker.text(40),
            'COD_LINHA': random.choice(lista_linha),
            'COD_CATEGORIA': random.choice(lista_categoria),
            'DES_CATEGORIA': faker.text(40),
            'COD_SUBCATEGORIA': random.choice(lista_subcategoria),
            'DES_SUBCATEGORIA': faker.text(40),
            'DES_SUBMODELO': faker.text(40),
            'QT_VENDA': random.randint(1, 1000),
            'VL_VENDA': round(random.uniform(1, 1000), 2),
            'VL_DSCT_TOTAL': round(random.uniform(1, 100), 2),
            'VL_VENDA_LIQ': round(random.uniform(1, 1000), 2),
            'QT_PONTOS_UTILIZADOS': random.randint(1, 100),
            'DT_ATUALIZACAO': random_dates('ini')
        }


def gera_ciclo(data_ini, data_fim, exibir_insert):
    """
    Função para gerar os comandos de insert para a tabela de ciclo e gerar os ids da lista de ciclos
    Retorna uma lista com os ids dos ciclos

    :param data_ini:
    :param data_fim:
    :param exibir_insert:
    :return lista_ciclos:
    """
    lista_ciclos = []
    id_ciclo = 1
    data = datetime.strptime(data_ini, '%Y-%m-%d %H:%M:%S')
    datafim = datetime.strptime(data_fim, '%Y-%m-%d %H:%M:%S')
    while data < datafim:
        info = {
            'COD_UN_NEGOCIO': random.choice(lista_un_negocio),
            'NR_CICLO': id_ciclo,
            'DT_FIM_CICLO': str(data + timedelta(days=21)),
            'DT_INI_CICLO': str(data),
            'DES_CICLO': faker.text(50),
            'DUMMY': random.randint(1, 10000)
        }
        # if exibir_insert:
        #     print(gera_sql(info, 'CA_CICLOS_DDL'))
        data = data + timedelta(days=21)
        lista_ciclos.append('cic' + str(id_ciclo))
        id_ciclo = id_ciclo + 1

    return lista_ciclos


data_ini = '2016-01-01 00:00:01'
data_fim = '2018-12-01 23:59:59'


def random_dates(opcao, data_ini='2016-01-01', data_fim='2018-12-01'):
    """
    Funcao para gerar datas faker. Nao esta sendo utilizado o faker para geracao de datas por conta do seu carater randomico.
    Com esta funcao é possivel garantir que as datas estejam dentro de um intervalo, melhorando a integridade dos dados

    :param opcao:
    :param data_ini:
    :param data_fim:
    :return:
    """
    if opcao == 'ini':
        start = pd.to_datetime(data_ini)
        end = pd.to_datetime('2018-01-01')
    else:
        start = pd.to_datetime('2018-01-02')
        end = pd.to_datetime(data_fim)
    ndays = (end - start).days + 1
    return pd.to_timedelta(np.random.rand() * ndays, unit='D') + start


def gera_sql(dicionario, tabela):
    """
    Função para gerar os comandos SQL a partir de um dicionario.
    Está retornando uma string, pode ser adaptado para gerar um stmt

    :param dicionario:
    :param tabela:
    :return:
    """
    keys = tuple(dicionario)
    dictsize = len(dicionario)
    sql = ''
    for i in range(dictsize):
        if type(dicionario[keys[i]]).__name__ == 'str' or type(dicionario[keys[i]]).__name__ == 'Timestamp':
            sql += '\'' + str(dicionario[keys[i]]) + '\''
        else:
            sql += str(dicionario[keys[i]])
        if i < dictsize - 1:
            sql += ', '
    keys = str(keys).replace("'", "")
    sql = f'insert into {tabela} {keys} values ({sql}) returning ID'
    return sql


def corrompe_campo(dicio):
    """
    Função para corromper os campos de um registro.
    Escolhe aletoriamente um campo e faz a modificação de valor
    Se o tipo do campo for string, pode deixar vazio, remover formatacao ou inserir uma @
    Se o tipo do campo for timestamp, deixa o campo vazio
    Se o tipo do campo for numerico, transforma o valor em negativo
    :param dic:
    :return dicio:
    :return mudancas:
    """

    keys = tuple(dicio)
    indice = random.randint(0, len(dicio) - 1)

    mudancas = {}
    mudancas['tabela'] = dicio.__class__.__name__
    mudancas['id'] = indice
    mudancas['campo_modificado'] = keys[indice]
    mudancas['valor_original'] = dicio[keys[int(indice)]]

    if type(dicio[keys[indice]]).__name__ == 'Timestamp':
        dicio[keys[indice]] = ''
    elif type(dicio[keys[indice]]).__name__ == 'str':
        v = random.random()
        if v >= 0.9:
            dicio[keys[indice]] = ''  # campo vazio
        elif 0.5 < v < 0.9:
            re.sub('[^A-Za-z0-9]+', '', dicio[keys[indice]])  # remove qualquer formatação
        else:
            dicio[keys[indice]] = dicio[keys[indice]][0:3] + '@' + dicio[keys[indice]][4:]  # insere um caracter estranho
    else:
        dicio[keys[indice]] = dicio[keys[indice]] * (-1)  # corrompe um campo numerico

    mudancas['valor_modificado'] = dicio[keys[indice]]

    return dicio, mudancas


def gera_multiplos_inserts():
    """
    Funcao para gerar multiplos inserts em quantidade randomica
    :return:
    """
    qtde_inserts = random.randint(1, 10000)
    lista_tabelas = ['BASECOMPRASPDV_DDL', 'BASECONSUMIDOR_BOT_DDL', 'CA_CICLOS_DDL', 'SELLOUT_TB_LOJA_VENDA_SO_DDL']
    for i in range(qtde_inserts):
        tabela = random.choice(lista_tabelas)
        registro = globals()[tabela]()
        # escolhe aletorioamente se o registro vai ser corrompido
        if random.random() < 0.3:
            registro.info = corrompe_campo(registro.info)

        # gera o comando de insert
        cmd_insert = gera_sql(registro.info, tabela)


def gera_multiplos_inserts_tempo_random():
    """
    Funcao para gerar multiplos inserts em tempos randomicos
    :return:
    """
    qtde_chamadas = random.randint(1, 10000)
    for i in range(qtde_chamadas):
        gera_multiplos_inserts()
        time.sleep(random.randint(1, 30))


# Para manter a integridade entre as tabelas, as listas irão atuar como categorias.

data_ini = '2016-01-01 00:00:01'
data_fim = '2018-12-01 23:59:59'

lista_produtos = []
lista_lojas = []
lista_un_negocio = []
lista_vendedor = []
lista_sexo = ['M', 'F']
lista_canal = []
lista_franquia = []
lista_grupo_contas = []
lista_marca = []
lista_linha = []
lista_categoria = []
lista_subcategoria = []

for x in range(1, 10):
    lista_produtos.append('prod' + str(x))
    lista_lojas.append('shop' + str(x))
    lista_un_negocio.append('uni' + str(x))
    lista_vendedor.append('vend' + str(x))
    lista_canal.append('can' + str(x))
    lista_franquia.append('fran' + str(x))
    lista_grupo_contas.append('gcon' + str(x))
    lista_marca.append('m' + str(x))
    lista_linha.append('l' + str(x))
    lista_categoria.append('c' + str(x))
    lista_subcategoria.append('sc' + str(x))

lista_ciclos = gera_ciclo(data_ini, data_fim, False)
