# 📊 

## 🎯 Objetivo
O objetivo deste projeto é analisar dados do Spotify para identificar padrões de comportamento relacionados às músicas, artistas e seu desempenho em playlists, rankings (charts) e número de streams. A análise visa gerar insights estratégicos que possam orientar ações de marketing, posicionamento de faixas e crescimento da plataforma.

## 👥 Equipe
...

## 🛠️ Ferramentas e Tecnologias Utilizadas
- BigQuery
- PowerBi
- Python

## 🔧 Processamento e Análises
- **Conectar/importar dados**
Criei o projeto na plataforma **Google Cloud** com o ID:
- spotify-projeto2-465223

Em seguida, criei o **conjunto de dados** (dataset) no BigQuery com o nome:
- spotify_dados

Observei que algumas bases estavam corrompidas (com caracteres inválidos). Para garantir a integridade dos dados durante a importação:

- Desenvolvi um script em Python que percorre os arquivos CSV, Remove espaços e caracteres especiais nos nomes das colunas, Corrige a codificação para UTF-8, E salva novas versões limpas para facilitar a leitura pelo BigQuery.

## 📂 Bases de Dados Importadas
Foram importadas e organizadas três principais tabelas no BigQuery:
✅ track_spotify
Contém os dados principais das faixas, como: Nome da música e do artista, Data de lançamento, Presença em playlists e rankings, Número de streams.
✅ track_competition
Inclui informações sobre músicas em competição, podendo conter dados de comparação de desempenho, relevância ou participações em rankings.
✅ track_technical
Apresenta informações técnicas complementares das faixas, como: BPM, tonalidade, duração, energia, dançabilidade, entre outros atributos úteis para análise musical.
