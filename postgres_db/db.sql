CREATE DATABASE btdb
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

\c btdb

/*
CA_CICLOS_DDL
Esta tabela mantem informacoes sobre os ciclos de venda, periodos onde ocorrem campanhas com preços promocionais dos produtos
Esta tabela NAO ira receber dados novos, serao carregados com um dump e nao sera modificada novamente
*/

CREATE TABLE CA_CICLOS_DDL(
	ID		SERIAL,
	COD_UN_NEGOCIO   VARCHAR(50),
	NR_CICLO         VARCHAR(50),
	DT_FIM_CICLO     VARCHAR(50),
	DT_INI_CICLO     VARCHAR(50),
	DES_CICLO        VARCHAR(50),
	DUMMY            INTEGER
);

ALTER TABLE CA_CICLOS_DDL ADD CONSTRAINT CA_CICLOS_DDL_PK PRIMARY KEY ( ID );

/*
BASECOMPRASPDV_DDL
Tabela que mantem a associacao entre venda, loja e consumidor considerando PDV (ponto de venda)
Essa tabela sera utilizada para a carga Batch
*/
CREATE TABLE BASECOMPRASPDV_DDL(
	ID						  SERIAL,
	CPF                  VARCHAR(14),
	COD_GRUPO_FRANQUIA   VARCHAR(10),
	CD_LOJA              VARCHAR(10),
	Z_CD_LOJA            VARCHAR(10),
	NR_PDV               INTEGER,
	NR_CUPOM             BIGINT,
	DT_VENDA             VARCHAR(50),
	CD_PRODUTO           VARCHAR(18),
	CD_STATUS_CUPOM      INTEGER,
	DH_TIMESTAMP         VARCHAR(50),
	DH_TIMESTAMP_DEC     VARCHAR(50),
	NR_ATENDIMENTO       INTEGER,
	DS_ORIGEM_BOLETO     VARCHAR(50),
	CD_CONSULTOR         VARCHAR(20),
	COD_GRUPO_CONTAS     VARCHAR(100),
	DES_MATERIAL         VARCHAR(40),
	COD_MARCA            VARCHAR(100),
	DES_MARCA            VARCHAR(40),
	COD_LINHA            VARCHAR(10),
	COD_CATEGORIA        VARCHAR(18),
	DES_CATEGORIA        VARCHAR(40),
	COD_SUBCATEGORIA     VARCHAR(18),
	DES_SUBCATEGORIA     VARCHAR(40),
	DES_SUBMODELO        VARCHAR(40),
	QT_VENDA             INTEGER,
	VL_VENDA             DECIMAL(17,2),
	VL_VENDA_LIQ         DECIMAL(17,2),
	VL_DSCT_TOTAL        DECIMAL(17,2),
	VL_DSCT_FIDELI       DECIMAL(17,2),
	VL_COMISSAO          DECIMAL(17,2),
	FIDELIDADE           VARCHAR(10),
	QT_PONTOS_UTILIZADOS DECIMAL(17,2),
	DT_ATUALIZACAO       VARCHAR(50)
);

ALTER TABLE BASECOMPRASPDV_DDL ADD CONSTRAINT BASECOMPRASPDV_DDL_PK PRIMARY KEY ( ID );


/*
BASECONSUMIDOR_BOT_DDL
Tabela que mantem os dados dos consumidores
Essa tabela sera utilizada para a carga Batch
*/
CREATE TABLE BASECONSUMIDOR_BOT_DDL(
	ID						  SERIAL,
	CPF                                 VARCHAR(50),
	BUSINESS_PARTNER                    VARCHAR(50),
	NOME_PRIMEIRO                       VARCHAR(80),
	NOME_ULTIMO                         VARCHAR(80),
	NOME_COMPLETO                       VARCHAR(200),
	SEXO                                VARCHAR(50),
	DT_NASCIMENTO                       VARCHAR(50),
	IDADE                               INTEGER,
	NACIONALIDADE                       VARCHAR(50),
	COD_ORIGEM_CADASTRO                 VARCHAR(50),
	DES_ORIGEM_CADASTRO                 VARCHAR(50),
	COD_LOJA_CADASTRO                   VARCHAR(50),
	COD_LOJA_ALTERACAO                  VARCHAR(50),
	COD_CANAL_ALTERACAO                 VARCHAR(50),
	DT_CADASTRO                         VARCHAR(100),
	DT_ALTERACAO                        VARCHAR(100),
	COD_CONSULTOR_CADASTRO              VARCHAR(50),
	COD_TIPO_CLIENTE                    VARCHAR(50),
	DES_TIPO_CLIENTE                    VARCHAR(50),
	ENDER_RUA                           VARCHAR(200),
	ENDER_NUMERO                        VARCHAR(50),
	ENDER_COMPLEMENTO                   VARCHAR(200),
	BAIRRO                              VARCHAR(200),
	CIDADE                              VARCHAR(200),
	CEP                                 VARCHAR(50),
	ESTADO                              VARCHAR(50),
	PAIS                                VARCHAR(50),
	TEL_RESIDENCIAL                     VARCHAR(50),
	TEL_COMERCIAL                       VARCHAR(50),
	TEL_CELULAR                         VARCHAR(50),
	EMAIL                               VARCHAR(100),
	EMAIL_2                             VARCHAR(100),
	IN_EMAIL_VALIDO_2                   VARCHAR(50),
	EMAIL_3                             VARCHAR(100),
	IN_EMAIL_VALIDO_3                   VARCHAR(50),
	COD_LOJA_PREF                       VARCHAR(50),
	CIDADE_PREF                         VARCHAR(200),
	ESTADO_PREF                         VARCHAR(50),
	DT_ULTIMO_RESGATE_DESCONTO          VARCHAR(50),
	IN_RESGATE_ANO_ATUAL                VARCHAR(50),
	IN_RESGATE_ANO_ANTERIOR             VARCHAR(50),
	COD_LOJA_PRIMEIRA_COMPRA_FIDELIDADE VARCHAR(50),
	DT_PRI_COMPRA_FIDELIDADE            VARCHAR(50),
	DT_ULT_COMPRA_FIDELIDADE            VARCHAR(50),
	DT_PRI_COMPRA_MV                    VARCHAR(50),
	DT_ULT_COMPRA_MV                    VARCHAR(50),
	DT_PRI_COMPRA_PDV                   VARCHAR(50),
	DT_ULT_COMPRA_PDV                   VARCHAR(50),
	COD_FRANQ_PREF                      VARCHAR(50),
	DES_SEGMENTACAO                     VARCHAR(50),
	QTD_PONTOS_FID_ATUAL                INTEGER,
	QTD_PONTOS_FID_VENCER_MES_ATUAL     INTEGER,
	QTD_PONTOS_FID_VENCER_30            INTEGER,
	QTD_PONTOS_FID_VENCER_60            INTEGER,
	QTD_PONTOS_FID_VENCER_90            INTEGER,
	QTD_PONTOS_FID_VENCER_90_MAIS       INTEGER,
	QTD_DIAS_PRI_COMPRA                 INTEGER,
	QTD_DIAS_ULT_COMPRA                 INTEGER,
	QTD_BOLETOS_12MESES                 INTEGER,
	VLR_BOLETOS_12MESES                 DECIMAL(18,2),
	DT_ATUALIZACAO                      VARCHAR(50)
);

ALTER TABLE BASECONSUMIDOR_BOT_DDL ADD CONSTRAINT BASECONSUMIDOR_BOT_DDL_PK PRIMARY KEY ( ID );

/*
SELLOUT_TB_LOJA_VENDA_SO_DDL
Tabela que mantem os registros associando vendas a lojas
Essa tabela sera utilizada para a carga Batch
*/

CREATE TABLE SELLOUT_TB_LOJA_VENDA_SO_DDL(
	ID						  SERIAL,
	CD_PRODUTO       VARCHAR(50),
	CD_LOJA          VARCHAR(10),
	DT_VENDA         VARCHAR(50),
	NR_HORA          INTEGER,
	NR_CUPOM         BIGINT,
	NR_PDV           INTEGER,
	ID_VENDEDOR      VARCHAR(20),
	CD_STATUS_CUPOM  INTEGER,
	NR_SEQ           INTEGER,
	NR_QTD_VENDA     INTEGER,
	VL_VENDA         DECIMAL(17,2),
	VL_DSCT_TOTAL    DECIMAL(17,2),
	VL_DSCT_FIDELI   DECIMAL(17,2),
	VL_COMISSAO      DECIMAL(17,2),
	CD_TIPO_DOC      VARCHAR(50),
	Z_CD_LOJA        VARCHAR(50),
	DH_TIMESTAMP     VARCHAR(50),
	DH_TIMESTAMP_DEC VARCHAR(50),
	ID_RECORDO       BIGINT,
	ID_RECORDIO      BIGINT,
	IN_DOC_FISCAL    VARCHAR(50),
	DS_ORIGEM_BOLETO VARCHAR(50),
	DS_CPF_CNPJ      VARCHAR(50),
	NR_ATENDIMENTO   INTEGER,
	UFLAG            VARCHAR(50)
);

ALTER TABLE SELLOUT_TB_LOJA_VENDA_SO_DDL ADD CONSTRAINT SELLOUT_TB_LOJA_VENDA_SO_PK PRIMARY KEY ( ID );

/*
BASECOMPRASECM_DDL
Tabela que mantem a associacao entre venda, loja e consumidor para ECM (campanha especial do boticario)
Esta tabela recebera constantemente os dados do gerador
*/


CREATE TABLE BASECOMPRASECM_DDL(
	ID				     SERIAL,
	CPF                  VARCHAR(50),
	CD_PRODUTO           VARCHAR(18),
	DS_UNIDADE_NEGOCIO   VARCHAR(30),
	DT_VENDA             VARCHAR(50),
	NR_CUPOM             BIGINT,
	CD_LOJA              VARCHAR(10),
	NR_PDV               INTEGER,
	DS_STATUS_CUPOM      VARCHAR(50),
	ID_VENDEDOR          VARCHAR(20),
	NR_ATENDIMENTO       BIGINT,
	DES_MATERIAL         VARCHAR(40),
	COD_MARCA            VARCHAR(40),
	DES_MARCA            VARCHAR(40),
	COD_LINHA            VARCHAR(50),
	COD_CATEGORIA        VARCHAR(18),
	DES_CATEGORIA        VARCHAR(40),
	COD_SUBCATEGORIA     VARCHAR(18),
	DES_SUBCATEGORIA     VARCHAR(40),
	DES_SUBMODELO        VARCHAR(40),
	QT_VENDA             INTEGER,
	VL_VENDA             DECIMAL(17,2),
	VL_DSCT_TOTAL        DECIMAL(17,2),
	VL_VENDA_LIQ         DECIMAL(17,2),
	QT_PONTOS_UTILIZADOS DECIMAL(17,2),
	DT_ATUALIZACAO       VARCHAR(50)
);

ALTER TABLE BASECOMPRASECM_DDL ADD CONSTRAINT BASECOMPRASECM_DDL_PK PRIMARY KEY ( ID );


/* inserts para a tabela de ciclo */
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni5', 1, '2016-01-22 00:00:01', '2016-01-01 00:00:01', 'Porro excepturi quia ab ratione.', 9061);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni2', 2, '2016-02-12 00:00:01', '2016-01-22 00:00:01', 'Architecto praesentium eum ex dolores enim.', 5793);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni6', 3, '2016-03-04 00:00:01', '2016-02-12 00:00:01', 'Temporibus iste rem eveniet accusantium.', 4071);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni5', 4, '2016-03-25 00:00:01', '2016-03-04 00:00:01', 'Repellat rerum autem earum perspiciatis.', 4657);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni9', 5, '2016-04-15 00:00:01', '2016-03-25 00:00:01', 'Cum porro ipsum eveniet accusamus.', 3139);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni9', 6, '2016-05-06 00:00:01', '2016-04-15 00:00:01', 'Labore ipsa nam quasi repellendus.', 101);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni5', 7, '2016-05-27 00:00:01', '2016-05-06 00:00:01', 'Quia a eos deserunt sequi placeat est.', 835);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni6', 8, '2016-06-17 00:00:01', '2016-05-27 00:00:01', 'Consequuntur cupiditate saepe libero rem earum.', 6030);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni2', 9, '2016-07-08 00:00:01', '2016-06-17 00:00:01', 'Placeat minus distinctio iure atque.', 3525);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni1', 10, '2016-07-29 00:00:01', '2016-07-08 00:00:01', 'Iure voluptatem corporis odio.', 623);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni2', 11, '2016-08-19 00:00:01', '2016-07-29 00:00:01', 'Nihil suscipit eum laudantium placeat commodi.', 7604);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni3', 12, '2016-09-09 00:00:01', '2016-08-19 00:00:01', 'Veritatis natus dicta error ad architecto cum.', 9001);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni1', 13, '2016-09-30 00:00:01', '2016-09-09 00:00:01', 'Delectus voluptates neque delectus.', 8496);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni2', 14, '2016-10-21 00:00:01', '2016-09-30 00:00:01', 'Debitis quidem esse ratione.', 2926);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni1', 15, '2016-11-11 00:00:01', '2016-10-21 00:00:01', 'Iure quas autem numquam dolore.', 2458);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni8', 16, '2016-12-02 00:00:01', '2016-11-11 00:00:01', 'Inventore provident laudantium quia harum.', 8283);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni6', 17, '2016-12-23 00:00:01', '2016-12-02 00:00:01', 'Laboriosam minima sed ex veritatis.', 843);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni4', 18, '2017-01-13 00:00:01', '2016-12-23 00:00:01', 'Asperiores error vel consequuntur ex corporis.', 3757);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni8', 19, '2017-02-03 00:00:01', '2017-01-13 00:00:01', 'Cum natus rerum natus laborum perspiciatis.', 9517);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni7', 20, '2017-02-24 00:00:01', '2017-02-03 00:00:01', 'Harum ipsa placeat iste. Blanditiis totam beatae.', 5088);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni3', 21, '2017-03-17 00:00:01', '2017-02-24 00:00:01', 'Exercitationem animi quod.', 5131);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni2', 22, '2017-04-07 00:00:01', '2017-03-17 00:00:01', 'Corporis neque dicta quaerat odio id.', 6285);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni6', 23, '2017-04-28 00:00:01', '2017-04-07 00:00:01', 'Eos repellat qui nesciunt eveniet.', 4876);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni8', 24, '2017-05-19 00:00:01', '2017-04-28 00:00:01', 'Nihil vel neque quasi minima aliquid quam sit.', 9305);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni6', 25, '2017-06-09 00:00:01', '2017-05-19 00:00:01', 'Ut laboriosam repellendus quidem eum.', 3520);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni6', 26, '2017-06-30 00:00:01', '2017-06-09 00:00:01', 'Dolor veritatis debitis perferendis sit.', 5462);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni4', 27, '2017-07-21 00:00:01', '2017-06-30 00:00:01', 'Accusantium ipsa sit quos molestias quis.', 3119);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni3', 28, '2017-08-11 00:00:01', '2017-07-21 00:00:01', 'Soluta vero corrupti. Iusto quae iusto.', 8340);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni4', 29, '2017-09-01 00:00:01', '2017-08-11 00:00:01', 'Tempora et porro quisquam.', 297);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni5', 30, '2017-09-22 00:00:01', '2017-09-01 00:00:01', 'Cupiditate at fugit.', 1943);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni4', 31, '2017-10-13 00:00:01', '2017-09-22 00:00:01', 'Sit distinctio asperiores rerum.', 8752);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni3', 32, '2017-11-03 00:00:01', '2017-10-13 00:00:01', 'Officiis cumque et.', 4347);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni2', 33, '2017-11-24 00:00:01', '2017-11-03 00:00:01', 'Eius voluptate qui qui blanditiis.', 8529);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni5', 34, '2017-12-15 00:00:01', '2017-11-24 00:00:01', 'Iste alias rem at optio optio sequi.', 4600);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni6', 35, '2018-01-05 00:00:01', '2017-12-15 00:00:01', 'Natus voluptatem repellat hic quidem.', 6499);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni9', 36, '2018-01-26 00:00:01', '2018-01-05 00:00:01', 'Incidunt provident laboriosam repellendus.', 4806);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni8', 37, '2018-02-16 00:00:01', '2018-01-26 00:00:01', 'Voluptas perspiciatis eius cumque.', 5877);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni4', 38, '2018-03-09 00:00:01', '2018-02-16 00:00:01', 'Harum dolor ipsam quo ratione incidunt rem.', 7523);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni6', 39, '2018-03-30 00:00:01', '2018-03-09 00:00:01', 'Vitae nam ab perferendis ipsa similique.', 529);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni2', 40, '2018-04-20 00:00:01', '2018-03-30 00:00:01', 'Consequatur repellat nihil quis.', 714);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni9', 41, '2018-05-11 00:00:01', '2018-04-20 00:00:01', 'Quae esse impedit fugiat error quod.', 5676);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni6', 42, '2018-06-01 00:00:01', '2018-05-11 00:00:01', 'Incidunt illum ab assumenda.', 9157);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni6', 43, '2018-06-22 00:00:01', '2018-06-01 00:00:01', 'Impedit placeat tempore excepturi.', 2662);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni2', 44, '2018-07-13 00:00:01', '2018-06-22 00:00:01', 'Ab modi deleniti minima.', 7444);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni9', 45, '2018-08-03 00:00:01', '2018-07-13 00:00:01', 'Nemo ad vitae consequuntur.', 2372);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni8', 46, '2018-08-24 00:00:01', '2018-08-03 00:00:01', 'Minus doloremque consequuntur.', 6540);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni8', 47, '2018-09-14 00:00:01', '2018-08-24 00:00:01', 'Debitis ratione vitae eveniet molestias dolorum.', 9813);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni6', 48, '2018-10-05 00:00:01', '2018-09-14 00:00:01', 'Iusto corporis qui est quia fugit facilis.', 2315);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni3', 49, '2018-10-26 00:00:01', '2018-10-05 00:00:01', 'Voluptas odit quam. Rerum beatae iste.', 2113);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni2', 50, '2018-11-16 00:00:01', '2018-10-26 00:00:01', 'Id magnam accusamus excepturi inventore.', 9403);
insert into CA_CICLOS_DDL (COD_UN_NEGOCIO, NR_CICLO, DT_FIM_CICLO, DT_INI_CICLO, DES_CICLO, DUMMY) values ('uni2', 51, '2018-12-07 00:00:01', '2018-11-16 00:00:01', 'Natus sint quis tenetur molestias eos.', 6554);
