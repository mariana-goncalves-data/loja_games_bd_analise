CREATE DATABASE loja_games;

USE loja_games;

CREATE TABLE cliente (
    id_cliente SERIAL PRIMARY KEY,
    nome_cliente VARCHAR(40) NOT NULL,
    email_cliente VARCHAR(40)  NOT NULL,
    cidade_cliente VARCHAR(40) NOT NULL,
    estado_cliente VARCHAR(40) NOT NULL,
    data_cadastro DATE NOT NULL
);

CREATE TABLE produto (
    id_produto SERIAL PRIMARY KEY,
    nome_produto VARCHAR(30) NOT NULL,
    categoria_produto ENUM("Consoles", "Jogos", "Periféricos") NOT NULL,
    preco_produto FLOAT NOT NULL,
    estoque INT NOT NULL
);

CREATE TABLE venda (
    id_venda SERIAL PRIMARY KEY,
    valor_venda FLOAT NOT NULL,
    data_venda DATE NOT NULL,
    id_cliente INT
);

CREATE TABLE item_venda (
    id SERIAL PRIMARY KEY,
    id_venda INT NOT NULL,
    id_produto INT NOT NULL,
    preco_produto FLOAT NOT NULL,
    qtd_produto INT NOT NULL,
    data_venda DATE NOT NULL
)


ALTER TABLE item_venda ADD CONSTRAINT FK_ITEM_VENDA
FOREIGN KEY(id_venda) REFERENCES venda(id_venda);

ALTER TABLE item_venda ADD CONSTRAINT FK_ITEM_PRODUTO
FOREIGN KEY(id_produto) REFERENCES produto(id_produto);

ALTER TABLE venda ADD CONSTRAINT FK_VENDA_CLIENTE
FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente);


/*
criar github novo ok
add clientes
add produtos
criar procedures para inserir vendas
realiar analises

*/


