# 📊 Fórmulas Utilizadas – Para analisar os dados 

Este documento apresenta as principais consultas SQL utilizadas no Projeto 2 da Jornada de Dados da Laboratória, explicando por que e como cada uma delas foi aplicada na análise de dados musicais.

## 🎯 Processar e preparar a base de dados

### 📍 Identificar valores nulos

Para verificar a integridade dos dados, iniciamos a análise identificando registros com valores ausentes. Usamos **COUNT(*)** para saber o total de linhas da tabela e **COUNTIF(coluna IS NULL)** para contar quantos valores estão ausentes em cada coluna:

```
 SELECT
 COUNT(*) AS total_linhas,
 COUNTIF(track_id IS NULL) AS nulos_track_id,
 COUNTIF(in_apple_playlists IS NULL) AS nulos_in_apple_playlists,
 COUNTIF(in_apple_charts IS NULL) AS nulos_in_apple_charts,
 COUNTIF(in_deezer_playlists IS NULL) AS nulos_in_deezer_playlists,
 COUNTIF(in_deezer_charts IS NULL) AS nulos_in_deezer_charts,
 COUNTIF(in_shazam_charts IS NULL) AS nulos_in_shazam_charts
 FROM `spotify-analysis-465623.spotify_data.track_in_competition`
```

Depois, inspecionamos os dados ausentes:

```
SELECT
  *
FROM `spotify-analysis-465623.spotify_data.track_in_competition`
where
  in_shazam_charts 
is null
```

#### 📌 Explicação rápida:

- COUNT(*) → Conta o total de registros.

- COUNTIF(coluna IS NULL) → Identifica quantos valores estão ausentes em cada coluna.

- WHERE coluna IS NULL → Permite inspecionar detalhadamente os registros com valores nulos.


### 📍Identificar valores duplicados

Identificar duplicatas é essencial para evitar contagens erradas e distorções nas análises. Usamos **GROUP BY** com **HAVING COUNT(*) > 1** para encontrar registros duplicados baseados em track_name e artist_s__name:

```
 SELECT
 track_name,
 artist_s__name,
 count(*)
 FROM
 `spotify-analysis-465623.spotify_data.track_in_spotify`
 group by track_name, artist_s__name
 having count(*) > 1
```

Depois, investigamos caso a caso:

```
SELECT
*
FROM `spotify-analysis-465623.spotify_data.track_in_spotify`
WHERE
artist_s__name = 'Rosa Linn'
```

E, por fim, comparamos os dados técnicos dessas músicas:

```
SELECT
 *
FROM `spotify-analysis-465623.spotify_data.track_technical`
WHERE track_id IN (
  '5675634', '3814670',
  '7173596', '5080031',
  '1119309','4586215',
  '4967469', '8173823'
)
```

#### 📌 Explicação rápida:

- GROUP BY → Agrupa os dados por uma ou mais colunas, permitindo realizar agregações, como contar quantas vezes cada combinação aparece.

- HAVING COUNT(*) > 1 → Filtra os grupos formados pelo GROUP BY, retornando apenas aqueles com mais de uma ocorrência (ou seja, duplicatas).

- SELECT * WHERE condição → Filtra e exibe todos os registros da tabela que atendem a uma condição específica, útil para investigar mais a fundo registros suspeitos ou específicos.

- IN() → Permite filtrar múltiplos valores de uma vez, útil para consultar vários track_id ao mesmo tempo.

### 📍Identificar e gerenciar dados fora do escopo de análise

Por enquanto, não identificamos valores que estejam claramente fora do escopo da análise. Todas as variáveis presentes parecem relevantes neste momento. No entanto, alguns casos poderão ser reavaliados durante as próximas etapas da análise, como por exemplo a quantidade de artistas por faixa.

### 📍Identificar dados discrepantes em variáveis ​​categóricas

Valores categóricos (como nomes de artistas ou músicas) podem conter caracteres especiais, acentos incomuns, emojis ou símbolos invisíveis, o que pode comprometer a consistência dos dados e causar erros em agrupamentos, contagens e visualizações.

Para identificar essas discrepâncias, usamos a seguinte consulta:

```
SELECT  
artists_name,
REGEXP_REPLACE(artists_name, r'[^\x20-\x7E]', ' ') AS artists_name_ok
FROM `musicproject2-466100.spotify_data.track_in_spotify`
```

#### 📌 Explicação rápida:

- REGEXP_CONTAINS() → Verifica se a variável contém caracteres fora da faixa ASCII padrão (letras, números e sinais comuns).

- A expressão r'[^\x20-\x7E]' identifica quaisquer símbolos especiais, acentos diferentes, emojis ou espaços invisíveis.

- Essa etapa é importante para detectar dados que podem ter sido inseridos de forma inconsistente (ex: “Beyoncé”, “Beyoncé”, “BEYONCÉ”).

### 📍Identificar e tratar dados discrepantes em variáveis ​​numéricas

Para verificar possíveis discrepâncias em variáveis numéricas, utilizamos a seguinte query, que nos ajuda a identificar valores muito baixos ou muito altos, que podem indicar outliers:

```
 SELECT
  MIN(Variavel) AS menor_variavel,
  MAX(Variavel) AS maior_variavel,
  AVG(Variavel) AS media_variavel,
 FROM `spotify-analysis-465623.spotify_data.track_in_spotify`
```

Essa análise fornece uma visão geral da distribuição dos dados e possibilita identificar se há valores extremos que precisam ser investigados ou tratados.

#### 📌 Explicação rápida:

- MIN() → Retorna o menor valor da variável.

- MAX() → Retorna o maior valor da variável.

- AVG() → Retorna a média dos valores da variável.

### 📍Verificar e alterar os tipos de dados
SELECT  
SAFE_cast(streams AS INT64) AS streams_ok
FROM `musicproject2-466100.spotify_data.track_in_spotify

Modificação do tipo de dados de string para integer, trocando para nulo a variável

## ✅ Conclusão da Limpeza de Dados

Para unir corretamente as tabelas e garantir a integridade dos dados, realizamos limpezas específicas com base na análise inicial. Abaixo estão descritas as ações executadas em cada tabela, seguidas das queries utilizadas.

### tabela track_in_spotify

- Padronização de texto: os nomes de artistas e faixas foram convertidos para letras minúsculas e limpos de caracteres especiais.

- Remoção de duplicatas: registros duplicados com track_id específico foram excluídos para evitar distorções analíticas.

- Conversão da coluna streams: valores não numéricos foram tratados e convertidos para o tipo INT64, removendo linhas com dados inconsistentes.

### 🧪 Query de Tratamento

```
CREATE OR REPLACE TABLE `spotify-analysis-465623.spotify_data.track_in_spotify_tratado` AS 
WITH
-- Etapa 1: Limpeza de texto
limpeza_texto AS (
  SELECT
    LOWER(REGEXP_REPLACE(artist_s__name, r'[^\x20-\x7E]', '')) AS artists_name_tratado,
    LOWER(REGEXP_REPLACE(track_name, r'[^\x20-\x7E]', '')) AS track_name_tratado,
    * EXCEPT (artist_s__name, track_name)
  FROM `spotify-analysis-465623.spotify_data.track_in_spotify`
),

-- Etapa 2: Remoção de duplicatas
remocao_duplicatas AS (
  SELECT *
  FROM limpeza_texto
  WHERE track_id NOT IN ('5080031', '3814670')
),

-- Etapa 3: Conversão da coluna streams e remoção de valor inválido
tratamento_streams AS (
  SELECT
    *,
    SAFE_CAST(streams AS INT64) AS streams_tratado
  FROM remocao_duplicatas
  WHERE track_id != '4061483'
)

-- Resultado final
SELECT
  t.track_id,
  t.artists_name_tratado AS artists_name,
  t.track_name_tratado AS track_name,
  t.artist_count,
  t.released_year,
  t.released_month,
  t.released_day,
  t.in_spotify_playlists,
  t.in_spotify_charts,
  t.streams_tratado AS streams
FROM tratamento_streams t;
```

### tabela track_in_competition
- Tratamento de valores nulos: a coluna in_shazam_charts apresentava valores ausentes que foram substituídos por zero com uso da função IFNULL(). Essa decisão garante consistência na análise de presença em plataformas, sem interferência de nulos.

### 🧪 Query de Tratamento 

```
CREATE OR REPLACE TABLE `spotify-analysis-465623.spotify_data.track_in_competition_tratado` AS
SELECT
  track_id,
  in_apple_playlists,
  in_apple_charts,
  in_deezer_playlists,
  in_deezer_charts,
  IFNULL(in_shazam_charts, 0) AS in_shazam_charts
FROM `spotify-analysis-465623.spotify_data.track_in_competition`;
```
#### ✅ Explicação

- Por que usamos **IFNULL**?
A função **IFNULL(coluna, valor)** substitui os valores nulos da coluna por um valor padrão — neste caso, zero.
Isso é importante porque valores nulos poderiam afetar análises estatísticas, somatórios ou visualizações gráficas. Substituir por 0 representa ausência de presença nas paradas do Shazam.

### tabela track_technical

- Padronização de nomes de variáveis: foram removidos os símbolos % para facilitar análises futuras e evitar erros.

- Filtragem de nulos: registros com valores ausentes na coluna key foram excluídos, já que essa variável é relevante para análises técnicas das faixas.

### 🧪 Query de Tratamento 

```
CREATE OR REPLACE TABLE `spotify-analysis-465623.spotify_data.track_technical_tratado` AS
SELECT
  track_id,
  bpm,
  `key`,
  mode,
  `danceability_%` AS danceability,
  `valence_%` AS valence,
  `energy_%` AS energy,
  `acousticness_%` AS acousticness,
  `instrumentalness_%` AS instrumentalness,
  `liveness_%` AS liveness,
  `speechiness_%` AS speechiness
FROM
  `spotify-analysis-465623.spotify_data.track_technical`
WHERE
  `key` IS NOT NULL;
```

### 📍Unir (join) as tabelas de dados

A união foi feita com base na coluna track_id, comum às três tabelas, utilizando a instrução INNER JOIN, que garante que apenas os registros presentes em todas as tabelas sejam considerados. Abaixo, a query utilizada:

```
-- Cria ou substitui a tabela unificada tratada com novas variáveis derivadas
CREATE OR REPLACE TABLE `spotify-analysis-465623.spotify_data.tabela_unificada_tratada` AS

WITH
  -- Dados do Spotify
  sp AS (
    SELECT *
    FROM `spotify-analysis-465623.spotify_data.track_in_spotify_tratado`
  ),
  
  -- Dados técnicos das faixas
  tc AS (
    SELECT *
    FROM `spotify-analysis-465623.spotify_data.track_technical_tratado`
  ),
  
  -- Dados de presença nas plataformas concorrentes
  comp AS (
    SELECT *
    FROM `spotify-analysis-465623.spotify_data.track_in_competition_tratado`
  )

SELECT
  -- Informações básicas
  sp.track_id,
  sp.artists_name,
  sp.track_name,
  sp.artist_count,
  sp.released_year,
  sp.released_month,
  sp.released_day,

  -- Criação da variável derivada: data_lancamento (como campo de data)
  PARSE_DATE('%Y-%m-%d', FORMAT('%04d-%02d-%02d', sp.released_year, sp.released_month, sp.released_day)) AS data_lancamento,

  -- Métricas do Spotify
  sp.in_spotify_playlists,
  sp.in_spotify_charts,
  sp.streams,

  -- Métricas técnicas
  tc.bpm,
  tc.key,
  tc.mode,
  tc.danceability,
  tc.valence,
  tc.energy,
  tc.acousticness,
  tc.instrumentalness,
  tc.liveness,
  tc.speechiness,

  -- Métricas das outras plataformas
  comp.in_apple_playlists,
  comp.in_apple_charts,
  comp.in_deezer_playlists,
  comp.in_deezer_charts,
  comp.in_shazam_charts,

  -- Criação da variável derivada: total_playlists
  (sp.in_spotify_playlists + comp.in_apple_playlists + comp.in_deezer_playlists) AS total_playlists

FROM sp
LEFT JOIN tc ON sp.track_id = tc.track_id
LEFT JOIN comp ON sp.track_id = comp.track_id

-- Filtros para garantir qualidade dos dados (sem nulos)
WHERE
  sp.track_id IS NOT NULL
  AND sp.artists_name IS NOT NULL
  AND sp.track_name IS NOT NULL
  AND sp.streams IS NOT NULL
  AND tc.bpm IS NOT NULL
  AND tc.key IS NOT NULL
  AND tc.mode IS NOT NULL
  AND tc.danceability IS NOT NULL
  AND tc.valence IS NOT NULL
  AND tc.energy IS NOT NULL
  AND tc.acousticness IS NOT NULL
  AND tc.instrumentalness IS NOT NULL
  AND tc.liveness IS NOT NULL
  AND tc.speechiness IS NOT NULL
  AND comp.in_apple_playlists IS NOT NULL
  AND comp.in_apple_charts IS NOT NULL
  AND comp.in_deezer_playlists IS NOT NULL
  AND comp.in_deezer_charts IS NOT NULL
  AND comp.in_shazam_charts IS NOT NULL;
```

### 📍Construir tabelas de dados auxiliares

1. Tabela Auxiliar: musicas_recentes

```
WITH musicas_recentes AS (
  SELECT
    track_name,
    artists_name,
    data_lancamento
  FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`
  WHERE EXTRACT(YEAR FROM data_lancamento) > 2020
)

SELECT *
FROM musicas_recentes
ORDER BY data_lancamento DESC;
```

2. Tabela Auxiliar: ranking_streams

```
WITH ranking_streams AS (
  SELECT *
  FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`
  ORDER BY streams DESC
  LIMIT 100
)

SELECT *
FROM ranking_streams;
```

# 🎯 Análise exploratória	

### 📍 Agrupar dados por variáveis categóricas

```
-- Top 10 artistas com mais músicas

SELECT 
  artists_name,
  COUNT(track_id) AS qtd_musicas
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`
GROUP BY artists_name
ORDER BY qtd_musicas DESC
LIMIT 10;

-- Distribuição de músicas por ano de lançamento

SELECT 
  released_year,
  COUNT(track_id) AS qtd_musicas
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`
GROUP BY released_year
ORDER BY released_year;

-- Distribuição por tonalidade (key)

SELECT 
  key,
  COUNT(track_id) AS qtd_musicas
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`
GROUP BY key
ORDER BY qtd_musicas DESC;

-- Distribuição por modo (maior/menor)

SELECT 
  mode,
  COUNT(track_id) AS qtd_musicas
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`
GROUP BY mode
ORDER BY qtd_musicas DESC;
```

### 📍 Visualizar variáveis ​​categóricas

```
-- Top 10 artistas com mais músicas
SELECT artists_name, COUNT(track_id) AS qtd_musicas
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`
GROUP BY artists_name
ORDER BY qtd_musicas DESC
LIMIT 10;

-- Distribuição por ano
SELECT released_year, COUNT(track_id) AS qtd_musicas
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`
GROUP BY released_year
ORDER BY released_year;

-- Distribuição por tonalidade (key)
SELECT key, COUNT(track_id) AS qtd_musicas
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`
GROUP BY key
ORDER BY qtd_musicas DESC;

-- Distribuição por modo (maior/menor)
SELECT mode, COUNT(track_id) AS qtd_musicas
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`
GROUP BY mode
ORDER BY qtd_musicas DESC;
```

### 📍 Aplicar medidas de tendência central

```
-- Estatísticas básicas: média, mínimo, máximo, desvio
SELECT
  'streams' AS variavel, AVG(streams) AS media, MIN(streams) AS minimo, MAX(streams) AS maximo
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`

UNION ALL
SELECT 'bpm', AVG(bpm), MIN(bpm), MAX(bpm)
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`

UNION ALL
SELECT 'danceability', AVG(danceability), MIN(danceability), MAX(danceability)
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`;
```

### 📍 Visualizar a distribuição dos dados

```
-- Distribuição de danceability por faixas
SELECT ROUND(danceability,1) AS faixa_dance, COUNT(*) AS qtd
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`
GROUP BY faixa_dance
ORDER BY faixa_dance;

-- Distribuição de energy
SELECT ROUND(energy,1) AS faixa_energy, COUNT(*) AS qtd
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`
GROUP BY faixa_energy
ORDER BY faixa_energy;
```

### 📍 Aplicar medidas de dispersão

```
-- Estatísticas com desvio padrão incluído
SELECT
  'streams' AS variavel, STDDEV(streams) AS desvio
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`

UNION ALL
SELECT 'bpm', STDDEV(bpm)
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`

UNION ALL
SELECT 'energy', STDDEV(energy)
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`;
```

### 📍 Visualizar o comportamento dos dados ao longo do tempo

```
-- Streams médios por ano
SELECT released_year, AVG(streams) AS media_streams
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`
GROUP BY released_year
ORDER BY released_year;

-- Contagem de músicas lançadas por ano
SELECT released_year, COUNT(track_id) AS qtd_musicas
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`
GROUP BY released_year
ORDER BY released_year;
```

### 📍 Calcular quartis, decis e percentis

```
-- Quartis de streams
SELECT APPROX_QUANTILES(streams, 4) AS quartis
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`;

-- Percentis (10 em 10)
SELECT APPROX_QUANTILES(streams, 10) AS decis
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`;

-- Percentil 95 (outliers)
SELECT APPROX_QUANTILES(streams, 100)[OFFSET(95)] AS p95
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`;
```

### 📍 Calcular correlação entre variáveis ​​

```
SELECT
  CORR(streams, danceability) AS corr_streams_dance,
  CORR(streams, energy) AS corr_streams_energy,
  CORR(streams, valence) AS corr_streams_valence,
  CORR(streams, bpm) AS corr_streams_bpm,
  CORR(streams, acousticness) AS corr_streams_acousticness,
  CORR(streams, liveness) AS corr_streams_liveness,
  CORR(streams, speechiness) AS corr_streams_speechiness,
  CORR(streams, total_playlists) AS corr_streams_playlists
FROM `spotify-analysis-465623.spotify_data.tabela_unificada_tratada`;
```
