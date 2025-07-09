import os
import pandas as pd

# Caminho da pasta onde estão os arquivos
pasta = '/home/thaislira/projeto-spotify'

# Pega todos os arquivos CSV na pasta
arquivos_csv = [f for f in os.listdir(pasta) if f.endswith('.csv')]

for nome_arquivo in arquivos_csv:
    caminho_arquivo = os.path.join(pasta, nome_arquivo)

    try:
        # Tenta ler o CSV usando UTF-8 com fallback para ISO-8859-1 se falhar
        try:
            df = pd.read_csv(caminho_arquivo, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(caminho_arquivo, encoding='iso-8859-1')

        # Remove espaços em branco das colunas
        df.columns = [col.strip().replace(' ', '_').replace('(', '').replace(')', '').replace('/', '_').replace('-', '_') for col in df.columns]

        # Remove valores inválidos
        df.replace({'\uFFFD': ''}, regex=True, inplace=True)

        # Gera novo nome com _limpo.csv
        novo_nome = nome_arquivo.replace('.csv', '_limpo.csv')
        novo_caminho = os.path.join(pasta, novo_nome)

        # Salva o arquivo limpo
        df.to_csv(novo_caminho, index=False, encoding='utf-8')

        print(f'✅ Arquivo limpo criado: {novo_nome}')
    except Exception as e:
        print(f'⚠️ Erro ao processar {nome_arquivo}: {e}')

