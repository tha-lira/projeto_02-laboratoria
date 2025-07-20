# 📊 Fórmulas Utilizadas – Para analisar os dados 

Este documento apresenta as principais consultas SQL utilizadas no Projeto 2 da Jornada de Dados da Laboratória, explicando por que e como cada uma delas foi aplicada na análise de dados musicais.

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

## 📍Identificar e gerenciar dados fora do escopo de análise

Por enquanto, não identificamos valores que estejam claramente fora do escopo da análise. Todas as variáveis presentes parecem relevantes neste momento. No entanto, alguns casos poderão ser reavaliados durante as próximas etapas da análise, como por exemplo a quantidade de artistas por faixa.

## 📍Identificar dados discrepantes em variáveis ​​categóricas

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

## 📍Identificar e tratar dados discrepantes em variáveis ​​numéricas

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

## 📍Verificar e alterar os tipos de dados




## ✅ Conclusão da Limpeza de Dados

Para unir corretamente as tabelas e garantir a integridade dos dados, realizamos limpezas específicas com base na análise inicial. Abaixo estão descritas as ações executadas em cada tabela, seguidas das queries utilizadas.

### 🎯 O que precisa ser feito na tabela track_in_spotify

| Coluna           | Ação                                                                              |
| ---------------- | --------------------------------------------------------------------------------- |
| `track_name`     | Remover caracteres especiais e deixar tudo em letra **minúscula**                 |
| `artist_s__name` | Mesmo tratamento: remover especiais e deixar **minúsculo**                        |
| Duplicatas       | Remover os IDs: **5080031 e 3814670**                                             |
| `streams`        | Remover linha com ID **4061483** e converter a coluna para **numérica** (`INT64`) |

### 🧪 Query de Tratamento

```
CREATE OR REPLACE TABLE `spotify-analysis-465623.spotify_data.track_in_spotify_tratado` AS
WITH
limpeza_texto AS (
  SELECT
    track_id,
    LOWER(REGEXP_REPLACE(artist_s__name, r'[^\x20-\x7E]', '')) AS artists_name_tratado,
    LOWER(REGEXP_REPLACE(track_name, r'[^\x20-\x7E]', '')) AS track_name_tratado,
    
    * EXCEPT (artist_s__name, track_name)
  FROM `spotify-analysis-465623.spotify_data.track_in_spotify`
),
remocao_duplicatas AS (
  SELECT *
  FROM limpeza_texto
  WHERE track_id NOT IN (5080031, 3814670)
),
tratamento_streams AS (
  SELECT
    *,
    SAFE_CAST(streams AS INT64) AS streams_tratado
  FROM remocao_duplicatas
  WHERE track_id != 4061483
)
SELECT
  track_id,
  artists_name_tratado AS artists_name,
  track_name_tratado AS track_name,
  artist_count,
  released_year,
  released_month,
  released_day,
  in_spotify_playlists,
  in_spotify_charts,
  streams_tratado AS streams
FROM tratamento_streams;
```

### 🎯 O que precisa ser feito na tabela track_in_competition

### 🧪 Query de Tratamento 
```
```

### 🎯 O que precisa ser feito na tabela track_technical

### 🧪 Query de Tratamento 
```
```

## 📍Unir (join) as tabelas de dados

## 📍Criar novas variáveis

## 📍Construir tabelas de dados auxiliares
