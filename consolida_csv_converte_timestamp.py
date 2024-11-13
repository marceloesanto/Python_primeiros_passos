import pandas as pd
import glob
from datetime import datetime

# Defina o texto específico que deseja verificar
texto_especifico = "www.demo"

# Use glob para obter todos os arquivos CSV no diretório raiz do programa
arquivos_csv = glob.glob("./*.csv")

# Lista para armazenar os DataFrames válidos
dataframes_validos = []

# Função para converter timestamp em data e hora separadamente
def converter_timestamp(timestamp):
    dt = datetime.strptime(timestamp, "%Y%m%d%H%M%S.%f")
    data = dt.date()
    hora = dt.strftime("%H:%M:%S")
    return data, hora

# Loop através dos arquivos CSV e filtre as linhas
for arquivo in arquivos_csv:
    df = pd.read_csv(arquivo, sep=';', dtype={'Timestamp': str})
    
    # Verificar todas as colunas para o texto específico
    df_filtrado = df[df.apply(lambda row: row.astype(str).str.contains(texto_especifico, na=False).any(), axis=1)]
    
    if 'Timestamp' in df_filtrado.columns:
        # Separar o timestamp em data e hora
        df_filtrado['Data'], df_filtrado['Hora'] = zip(*df_filtrado['Timestamp'].apply(converter_timestamp))
        
        # Remover a coluna de timestamp original
        df_filtrado = df_filtrado.drop(columns=['Timestamp'])
        
        # Adicionar DataFrame filtrado e modificado à lista
        dataframes_validos.append(df_filtrado)
    
        # Log do número de linhas que atenderam à condição
        linhas_validas = len(df_filtrado)
        print(f"{arquivo}: {linhas_validas} linhas atenderam à condição.")
    else:
        print(f"{arquivo}: Coluna 'Timestamp' não encontrada.")

# Consolide todos os DataFrames em um único DataFrame
if dataframes_validos:
    df_consolidado = pd.concat(dataframes_validos, ignore_index=True)

    # Ordenar o DataFrame consolidado por ID, Data e Hora
    df_consolidado = df_consolidado.sort_values(by=['ID', 'Data', 'Hora'])

    # Salvar o DataFrame consolidado em um novo arquivo CSV
    df_consolidado.to_csv("./arquivo_consolidado.csv", sep=';', index=False)
    print("Arquivo consolidado criado com sucesso!")
else:
    print("Nenhum dado válido encontrado para consolidar.")
