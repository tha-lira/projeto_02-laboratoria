# 📊 

### 🎯 Objetivo do Projeto
O objetivo deste projeto é analisar dados do Spotify para identificar padrões de comportamento relacionados às músicas, artistas e seu desempenho em playlists, rankings (charts) e número de streams. A análise visa gerar insights estratégicos que possam orientar ações de marketing, posicionamento de faixas e crescimento da plataforma.

### 👥 Equipe
...

### 🛠️ Ferramentas e Tecnologias Utilizadas
- BigQuery
- PowerBi
- Python

## 🔧 Processar e preparar a base de dados

## 📍Conectar/importar dados para as ferramentas

Criei o projeto na plataforma **Google Cloud** com o ID:

- ✅ spotify-analysis-465623

Em seguida, criei o **conjunto de dados** (dataset) no BigQuery com o nome:

- ✅ spotify_data

Foram importadas e organizadas três principais tabelas no BigQuery:

- ✅ track_in_spotify

Contém os dados principais das faixas, como: Nome da música e do artista, Data de lançamento, Presença em playlists e rankings, Número de streams.

- ✅ track_in_competition

Inclui informações sobre músicas em competição, podendo conter dados de comparação de desempenho, relevância ou participações em rankings.

- ✅ track_technical

Apresenta informações técnicas complementares das faixas, como: BPM, tonalidade, duração, energia, dançabilidade, entre outros atributos úteis para análise musical.

## 📍 Identificar e tratar valores nulos

### Análise de Valores Nulos na Tabela track_in_competition
Na etapa de análise exploratória dos dados, realizamos a verificação de valores nulos nas colunas principais da tabela **track_in_competition**. Os resultados encontrados foram:

- A tabela possui um total de **953** registros.
- Não foram identificados valores nulos nas colunas críticas para identificação, como **track_id**.
- As colunas que indicam presença em playlists e charts da Apple e Deezer (in_apple_playlists, in_apple_charts, in_deezer_playlists, in_deezer_charts) também não apresentaram dados ausentes, indicando que esses campos estão completos para todos os registros.
- Foi identificado um total de **50 valores** nulos na coluna **in_shazam_charts**, o que corresponde a aproximadamente 5,25% do total de registros. Utilizei o WHERE para visualizar as células com o valor NULL.

### Análise de Valores Nulos na Tabela track_technical
Na etapa de análise exploratória dos dados, realizamos a verificação de valores nulos nas colunas principais da tabela **track_technical**. Os resultados encontrados foram:

A tabela possui um total de **953** registros.
- Não foram identificados valores nulos nas colunas críticas para identificação, como track_id.
- As colunas (bpm, mode, danceability_%,valence_%, energy_%, acousticness_%, instrumentalness_%, liveness_%, speechiness_%) também não apresentaram dados ausentes, indicando que esses campos estão completos para todos os registros.
- Foi identificado um total de **95 valores** nulos na coluna key, o que corresponde a aproximadamente 10% do total de registros. Utilizei o WHERE para visualizar as células com o valor NULL.

### Análise de Valores Nulos na Tabela track_in_spotify
Na etapa de análise exploratória dos dados, realizamos a verificação de valores nulos nas colunas principais da tabela **track_in_spotify**. Os resultados encontrados foram:
- A tabela possui um total de **953** registros.
- Não foram identificados valores nulos nas colunas críticas para identificação, como track_id.
- As colunas (artists_name, artist_count, released_year, released_month, released_day, in_spotify_playlists, in_spotify_charts, streams) também não apresentaram dados ausentes, indicando que esses campos estão completos para todos os registros.


### 🧼 Tratamento realizado
- A variável **key**, representa o tom musical da música foi removida devido à alta proporção de valores nulos (95 registros) e à baixa relevância para os objetivos da análise, que não contemplam aspectos harmônicos da música.

- A variável **in_shazam_charts**, representa presença e classificação da música nas paradas da Shazam. Teve valores nulos (50 registros) substituídos por 0, com base na premissa de que a ausência de entrada indica que a música não esteve nas paradas do Shazam. 

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## 📍 Identificar e tratar valores duplicados

Durante a análise da base de dados, foi identificada a presença de múltiplos registros para uma mesma música, como nos casos abaixo:

- **SNAP** (Rosa Linn): **track_id** 5675634 e 3814670

- **About Damn Time** (Lizzo): **track_id** 7173596 e 5080031

- **Take My Breath** (The Weeknd): **track_id** 1119309 e 4586215

- **SPIT IN MY FACE!** (ThxSoMch): **track_id** 4967469 e 8173823

Essa duplicidade ocorre porque uma mesma faixa pode estar cadastrada com diferentes identificadores, seja por versões lançadas em momentos distintos, inclusão em álbuns ou singles separados, edições remixadas ou por outras estratégias de distribuição nas plataformas de streaming.

Para garantir a consistência da análise, foi necessário investigar cada caso individualmente e decidir qual registro manter. A escolha se baseou no número de streams e na completude dos metadados técnicos. Essa etapa foi fundamental para evitar distorções nos resultados e garantir que cada música fosse considerada apenas uma vez nas análises estatísticas e de desempenho.

### 🎧 Análise individual das músicas

#### SNAP – Rosa Linn

- Registros com mesmo BPM e modo.

- Diferença pequena no número de playlists e streams.

- 🧼 Conclusão: Trata-se da mesma versão da música distribuída com dois track_id. Mantivemos o registro com maior número de streams.

#### About Damn Time – Lizzo

- Valores idênticos de BPM, tonalidade, modo e streams.

- Diferença apenas nas playlists associadas.

- 🧼 Conclusão: Duplicata técnica. Optamos por manter apenas um dos registros.

#### Take My Breath – The Weeknd

- Mesmo BPM, mas tonalidades e modos distintos, além de diferenças de popularidade.

- 🧼 Conclusão: São versões diferentes (ex: versão do álbum e remix). Mantivemos a versão com maior número de streams para evitar viés.

#### SPIT IN MY FACE! – ThxSoMch

- BPMs e tonalidades diferentes sugerem edições distintas.

- Ambas as versões apresentam números relevantes de streams.

- 🧼 Conclusão: São versões diferentes da mesma faixa. Ambas foram mantidas para possibilitar uma análise mais completa sobre o comportamento de consumo.


✅  Ações realizadas

- Identificamos e tratamos duplicatas técnicas, mantendo apenas uma versão da música para evitar distorções nas métricas.

- Mantivemos versões distintas quando os dados indicaram diferenças reais nas características sonoras ou no comportamento de consumo.

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## 📍Identificar dados fora do escopo de análise
Durante a análise, foram identificados registros que estavam fora do escopo temporal definido para o projeto, como músicas com ano de lançamento muito antigo (ex: 1930), que destoavam do restante da base (que abrange majoritariamente os anos 2000 a 2025).

### 🧼 Tratamento realizado
Para garantir a consistência da análise e evitar distorções nos resultados, esses registros foram excluídos utilizando a cláusula WHERE released_year BETWEEN 2000 AND 2025.

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## 📍Identificar dados discrepantes em variáveis ​​categóricas

Durante a análise exploratória, foram identificados possíveis dados discrepantes em variáveis categóricas, como track_name e artist_s__name. Esses dados, por conterem caracteres especiais, emojis ou acentos variados, poderiam comprometer agrupamentos e contagens precisas.

### 🧼 Tratamento realizado 

Para isso, aplicamos a função REGEXP_REPLACE() para limpar esses campos, removendo tudo que não fosse letra, número ou espaço.

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## 📍Identificar dados discrepantes em variáveis ​​numéricas

As variáveis numéricas também foram avaliadas para detectar valores que estivessem fora do padrão esperado. Um exemplo claro foi a variável released_year, que continha valores como 1930, muito fora do intervalo esperado para a base.

### 🧼 Tratamento realizado

Com base nessa análise, foi definido um intervalo válido entre os anos de 2000 e 2025, considerando a relevância e atualidade dos dados. Registros com ano de lançamento fora desse intervalo foram considerados fora do escopo e excluídos da visualização consolidada.

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## 📍Verificar e alterar os tipos de dados

Para garantir que todos os campos estivessem no formato correto para análise, foi feita a conversão de algumas colunas de texto para número. 

### 🧼 Tratamento realizado 

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## 📍Unir (join) as tabelas de dados

### 🧼 Tratamento realizado
[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## 📍Criar novas variáveis

### 🧼 Tratamento realizado ​​
[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## 📍Construir tabelas de dados auxiliares

### 🧼 Tratamento realizado
[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)