import pandas as pd
import glob

# Defina o texto específico que deseja verificar
texto_especifico = "www.demo"

# Use glob para obter todos os arquivos CSV no diretório raiz do programa
arquivos_csv = glob.glob("./*.csv")

# Lista para armazenar os DataFrames válidos
dataframes_validos = []

# Loop através dos arquivos CSV e filtre as linhas
for arquivo in arquivos_csv:
    df = pd.read_csv(arquivo, sep=';')
    
    # Verificar todas as colunas para o texto específico
    df_filtrado = df[df.apply(lambda row: row.astype(str).str.contains(texto_especifico, na=False).any(), axis=1)]
    
    # Adicionar DataFrame válido à lista
    dataframes_validos.append(df_filtrado)
    
    # Log do número de linhas que atenderam à condição
    linhas_validas = len(df_filtrado)
    print(f"{arquivo}: {linhas_validas} linhas atenderam à condição.")

# Consolide todos os DataFrames em um único DataFrame
df_consolidado = pd.concat(dataframes_validos, ignore_index=True)

# Ordenar o DataFrame consolidado por data e hora
df_consolidado = df_consolidado.sort_values(by=[ 'ID', 'Data', 'Hora'])

# Salvar o DataFrame consolidado em um novo arquivo CSV
df_consolidado.to_csv("./arquivo_consolidado.csv", sep=';', index=False)
print("Arquivo consolidado criado com sucesso!")

# Criar uma coluna datetime combinando Data e Hora
df_consolidado['Datetime'] = pd.to_datetime(df_consolidado['Data'].astype(str) + ' ' + df_consolidado['Hora'].astype(str))

# Gerar o novo DataFrame com colunas desejadas
df_novo = df_consolidado[['ID', 'Data', 'Hora', 'Datetime']].copy()

# Adicionar a contagem de IDs em intervalos de 5 minutos
df_novo['Contagem_ID'] = df_novo.groupby(['ID', pd.Grouper(key='Datetime', freq='5Min')])['ID'].transform('count')

# Remover a coluna 'Datetime' para o arquivo final
df_novo = df_novo.drop(columns=['Datetime'])

# Remover duplicatas
df_novo = df_novo.drop_duplicates()

# Salvar o novo DataFrame em um novo arquivo CSV
df_novo.to_csv("./arquivo_consolidado_com_contagem.csv", sep=';', index=False)
print("Arquivo consolidado com contagem criado com sucesso!")
