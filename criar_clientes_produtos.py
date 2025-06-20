
import random
from faker import Faker
from datetime import datetime, timedelta
import pandas as pd
import csv

fake = Faker('pt_BR')

categorias_produtos = {
    "Consoles": ["PlayStation 2", "PlayStation 3", "PlayStation 4", "PlayStation 5",
                 "Xbox", "Xbox 360", "Xbox One X", "Xbox One S", "Xbox Series X", "Xbox Series S",
                "SNES", "Nintendo 64", "Game Cube", "Nintendo DS", "Nintendo 3DS", "Nintendo Wii",
                "Nintendo Wii U", "Nintendo Switch", "Nintendo Switch 2", "Game Boy", "Game Boy Advance"],
    "Jogos": ["Elden Ring", "Marvel's Spider-Man 2", "Final Fantasy XVI", "Demon's Souls",
              "Ratchet & Clank: Rift Apart", "Halo 2", "Fable", "Star Wars: Knights of the Old Republic",
              "Grand Theft Auto: San Andreas", "Counter-Strike: Source", "Mario Kart 8 Deluxe",
              "Animal Crossing: New Horizons", "Super Smash Bros. Ultimate", "The Legend of Zelda: Breath of the Wild"],
    "Periféricos": ["Controle DualSense", "Headset Gamer", "Teclado Mecânico", "Mouse Gamer", "Webcam Full HD"]
}

def gerar_clientes(n=200):
    id_cliente = 1
    clientes = []
    for i in range(n):
        clientes.append({
            "id_cliente": id_cliente,
            "nome_cliente": fake.name(),
            "email_cliente": fake.email(),
            "cidade_cliente": fake.city(),
            "estado_cliente": fake.estado_sigla(),
            "data_cadastro": fake.date_between(start_date='-5y', end_date='today')
            })
        id_cliente += 1
    return clientes

def gerar_preco_produto(categoria):
    if categoria == "Consoles":
        return round(random.uniform(850, 5500), 2)
    elif categoria == "Jogos" or categoria == "Periféricos":
        return round(random.uniform(50, 450), 2)

def gerar_produtos():
    produtos = []
    id_produto = 1
    for categoria, nomes in categorias_produtos.items():
        for nome in nomes:
            produtos.append({
                "id_produto": id_produto,
                "nome_produto": nome,
                "categoria_produto": categoria,
                "preco_produto": gerar_preco_produto(categoria),
                "estoque": random.randint(5, 350)
                })
            id_produto += 1
    return produtos

def criar_csvs():
    clientes = gerar_clientes()
    produtos = gerar_produtos()

    csv_clientes = "clientes.csv"
    csv_produtos = "produtos.csv"

    header_clientes = clientes[0].keys()
    header_produtos = produtos[0].keys()

    with open(csv_clientes, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header_clientes)
        writer.writeheader()
        writer.writerows(clientes)

    with open(csv_produtos, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header_produtos)
        writer.writeheader()
        writer.writerows(produtos)
    