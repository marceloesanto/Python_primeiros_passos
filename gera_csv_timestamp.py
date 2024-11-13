import pandas as pd
import random
from datetime import datetime, timedelta

# Função para gerar URLs fictícias
def gerar_url():
    radicais = ["example", "teste", "demo", "site", "pagina"]
    subdominio = random.choice(radicais)
    return f"https://www.{subdominio}.com"

# Função para gerar timestamps no formato desejado
def gerar_timestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S.%f")[:-3]

# Função para gerar IDs de pessoa (pode se repetir)
def gerar_id_pessoa():
    return random.randint(1, 50)  # IDs de 1 a 50 para repetição

# Função para gerar dados
def gerar_dados():
    dados = []
    for _ in range(100):
        linha = [
            gerar_id_pessoa(),  # Coluna 1: ID de pessoa
            random.uniform(1.0, 100.0),  # Coluna 2: Número decimal aleatório
            f"Texto{random.randint(1, 1000)}",  # Coluna 3: Texto aleatório
            gerar_url(),  # Coluna 4: URL fictícia
            gerar_timestamp(),  # Coluna 5: Timestamp
            random.choice([True, False])  # Coluna 6: Valor booleano aleatório
        ]
        dados.append(linha)
    return dados

# Gerar e salvar os arquivos CSV
for i in range(1, 4):
    df = pd.DataFrame(gerar_dados(), columns=['ID', 'ValorDecimal', 'Texto', 'URL', 'Timestamp', 'Booleano'])
    df.to_csv(f"arquivo_{i}.csv", sep=';', index=False)
    print(f"arquivo_{i}.csv criado com sucesso!")
