# 📊 

### 🎯 Objetivo
O objetivo deste projeto é analisar dados do Spotify para identificar padrões de comportamento relacionados às músicas, artistas e seu desempenho em playlists, rankings (charts) e número de streams. A análise visa gerar insights estratégicos que possam orientar ações de marketing, posicionamento de faixas e crescimento da plataforma.

### 👥 Equipe
...

### 🛠️ Ferramentas e Tecnologias Utilizadas
- BigQuery
- PowerBi
- Python

# 🔧 Processar e preparar a base de dados

### ➡️ Conectar/importar dados para outras ferramentas

Criei o projeto na plataforma **Google Cloud** com o ID:

- ✅ spotify-analysis-465623

Em seguida, criei o **conjunto de dados** (dataset) no BigQuery com o nome:

- ✅ spotify_data

### 📂 Bases de Dados Importadas
Foram importadas e organizadas três principais tabelas no BigQuery:

- ✅ track_in_spotify
Contém os dados principais das faixas, como: Nome da música e do artista, Data de lançamento, Presença em playlists e rankings, Número de streams.

- ✅ track_in_competition
Inclui informações sobre músicas em competição, podendo conter dados de comparação de desempenho, relevância ou participações em rankings.

- ✅ track_technical
Apresenta informações técnicas complementares das faixas, como: BPM, tonalidade, duração, energia, dançabilidade, entre outros atributos úteis para análise musical.

## Identificar e tratar valores nulos

### 🔍 Análise de Valores Nulos na Tabela track_competition
Na etapa de análise exploratória dos dados, realizamos a verificação de valores nulos nas colunas principais da tabela track_competition. Os resultados encontrados foram:
- A tabela possui um total de **953** registros.
- Não foram identificados valores nulos nas colunas críticas para identificação, como **track_id**.
- As colunas que indicam presença em playlists e charts da Apple e Deezer (in_apple_playlists, in_apple_charts, in_deezer_playlists, in_deezer_charts) também não apresentaram dados ausentes, indicando que esses campos estão completos para todos os registros.
- Foi identificado um total de **50 valores** nulos na coluna **in_shazam_charts**, o que corresponde a aproximadamente 5,25% do total de registros. Utilizei o WHERE para visualizar as células com o valor NULL.

### 🔍 Análise de Valores Nulos na Tabela track_technical
Na etapa de análise exploratória dos dados, realizamos a verificação de valores nulos nas colunas principais da tabela track_technical. Os resultados encontrados foram:
A tabela possui um total de **953** registros.
- Não foram identificados valores nulos nas colunas críticas para identificação, como track_id.
- As colunas (bpm, mode, danceability_%,valence_%, energy_%, acousticness_%, instrumentalness_%, liveness_%, speechiness_%) também não apresentaram dados ausentes, indicando que esses campos estão completos para todos os registros.
- Foi identificado um total de **95 valores** nulos na coluna key, o que corresponde a aproximadamente 10% do total de registros. Utilizei o WHERE para visualizar as células com o valor NULL.

### 🔍 Análise de Valores Nulos na Tabela track_spotify
Na etapa de análise exploratória dos dados, realizamos a verificação de valores nulos nas colunas principais da tabela track_spotify. Os resultados encontrados foram:
- A tabela possui um total de **953** registros.
- Não foram identificados valores nulos nas colunas críticas para identificação, como track_id.
- As colunas (artists_name, artist_count, released_year, released_month, released_day, in_spotify_playlists, in_spotify_charts, streams) também não apresentaram dados ausentes, indicando que esses campos estão completos para todos os registros.
- Foi identificado um total de **2 valores** nulos na coluna track_name, o que corresponde a aproximadamente 0,2% do total de registros.  Utilizei o WHERE para visualizar as células com o valor NULL.

### 🧼 Tratamento realizado
- A variável **key**, representa o tom musical da música foi removida devido à alta proporção de valores nulos (95 registros) e à baixa relevância para os objetivos da análise, que não contemplam aspectos harmônicos da música.
- A variável **in_shazam_charts**, representa presença e classificação da música nas paradas da Shazam. Teve valores nulos (50 registros) substituídos por 0, com base na premissa de que a ausência de entrada indica que a música não esteve nas paradas do Shazam.

## Identificar e tratar valores duplicados

Durante a etapa de limpeza e preparação dos dados, foi identificado que algumas músicas estavam presentes mais de uma vez na base(track_in_spotify), com mesmo nome, mesmo artista e mesma data de lançamento, porém com variações nos valores das métricas, como streams, in_spotify_playlists e in_spotify_charts.

- Esses registros foram classificados como duplicatas com divergência de dados, provavelmente decorrentes da consolidação de fontes distintas ou atualizações em momentos diferentes.

### 🧼 Tratamento realizado
Para cada música duplicada, foi mantido apenas o registro com o maior número de streams, considerando também, em caso de empate, o maior número de in_spotify_playlists e, posteriormente, in_spotify_charts. Essa abordagem garante que os dados utilizados nas análises refletem a versão mais atual e representativa da popularidade de cada faixa. Ao final do processo, a base de dados ficou livre de duplicidades, assegurando maior precisão na apuração de métricas e geração de insights.