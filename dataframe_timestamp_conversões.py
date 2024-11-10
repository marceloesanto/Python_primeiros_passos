import pandas as pd
from datetime import datetime, timedelta
import random
import string

# Função para gerar timestamps no formato especificado
def gerar_timestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S.%f")[:-3]

# Função para gerar um status code aleatório
def gerar_status_code():
    return random.choice([200, 400, 404, 500])

# Função para gerar um texto aleatório de 10 posições
def gerar_texto_aleatorio():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

# Gerar 10 timestamps com intervalos de 1 minuto entre cada um
timestamps = [(datetime.now() + timedelta(minutes=i)).strftime("%Y%m%d%H%M%S.%f")[:-3] for i in range(10)]

# Gerar listas de status codes e textos aleatórios
status_codes = [gerar_status_code() for _ in range(10)]
textos_aleatorios = [gerar_texto_aleatorio() for _ in range(10)]

# Criar o primeiro DataFrame
df1 = pd.DataFrame({
    'Timestamp': timestamps,
    'StatusCode': status_codes,
    'TextoAleatorio': textos_aleatorios
})

# Imprimir o primeiro DataFrame
print("Primeiro DataFrame:")
print(df1)

# Função para converter timestamp em data e hora
def converter_timestamp(timestamp):
    dt = datetime.strptime(timestamp, "%Y%m%d%H%M%S.%f")
    data_formatada = dt.strftime("%d/%m/%Y")
    hora_formatada = dt.strftime("%H:%M:%S")
    return data_formatada, hora_formatada

# Aplicar a conversão e criar o segundo DataFrame
df2 = pd.DataFrame(df1['Timestamp'].apply(converter_timestamp).tolist(), columns=['Data', 'Hora'])
df2['StatusCode'] = df1['StatusCode']
df2['TextoAleatorio'] = df1['TextoAleatorio']

# Imprimir o segundo DataFrame
print("\nSegundo DataFrame:")
print(df2)
