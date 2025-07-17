# 📊 Fórmulas Utilizadas – Para analisar os dados 

Este documento contém as principais fórmulas e cálculos utilizados no Projeto 2 da Jornada de Dados da Laboratória, que envolveu a análise de dados musicais.


### 📍 Identificar valores nulos

Iniciamos a análise com **SELECT COUNT(*)** para contar os registros totais e **COUNTIF(coluna IS NULL)** para identificar a quantidade de valores ausentes em cada coluna.

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

Além disso, apliquei um **SELECT * WHERE** variável **IS NULL** para inspecionar os registros ausentes nessa coluna antes de tratá-las.

```
 SELECT
 *
 FROM `spotify-analysis-465623.spotify_data.track_in_competition`
 where
 in_shazam_charts 
 is null
```

#### 📌 Explicação rápida:

- SELECT COUNT(*) → Conta todas as linhas da tabela.

- COUNTIF(variável IS NULL) → Conta quantas linhas têm valor nulo em uma coluna específica.

- SELECT * FROM tabela WHERE coluna IS NULL → Mostra as linhas com valor nulo em determinada coluna.


### 📍Identificar valores duplicados

🎧 Durante a análise, utilizamos a função **GROUP BY** combinada com **HAVING COUNT(*) > 1** para identificar possíveis duplicatas com base na combinação de **track_name** e **artist_s__name**. Esse procedimento revelou quatro músicas com múltiplos registros associados ao mesmo artista e título:

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

🎧 Após identificar os casos, investigamos individualmente os registros utilizando o nome do artista. Por exemplo, para analisar os dados de Rosa Linn, utilizamos a seguinte consulta:

```
SELECT
*
FROM `spotify-analysis-465623.spotify_data.track_in_spotify`
WHERE
artist_s__name = 'Rosa Linn'
```

🎧 Em seguida, recuperamos os dados técnicos das faixas usando o track_id, o que permitiu verificar diferenças em aspectos como BPM, tonalidade, modo, número de playlists e streams:

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
Para detectar anos fora do intervalo de análise (ex: 1930):

```
 SELECT DISTINCT released_year
 FROM `spotify-analysis-465623.spotify_data.track_in_spotify`
 ORDER BY released_year;
```
#### 📌 Explicação rápida:

- SELECT DISTINCT → Retorna apenas valores únicos.

- ORDER BY → Organiza os valores em ordem crescente (ou decrescente).

## 📍Identificar dados discrepantes em variáveis ​​categóricas

Para identificar valores que apresentam discrepâncias, utilizamos a seguinte consulta SQL:

```
 SELECT artist_s__name, track_name
 FROM `spotify-analysis-465623.spotify_data.track_in_spotify`
 WHERE REGEXP_CONTAINS(artist_s__name, r'[^\x20-\x7E]')
```

#### 📌 Explicação rápida:

- REGEXP_CONTAINS(campo, 'padrão') → verifica se o texto no campo contém o padrão definido pela expressão regular e retorna TRUE ou FALSE.

## 📍Identificar e tratar dados discrepantes em variáveis ​​numéricas

- Ao verificar a variável `streams`, identificamos divergências nos dados, como valores muito baixos ou muito altos que podem indicar outliers.

```
 SELECT
 MIN(streams) AS menor_stream,
 MAX(streams) AS maior_stream,
 FROM `spotify-analysis-465623.spotify_data.track_in_spotify`
```
#### 📌 Explicação rápida:

- MIN() e MAX() retornam, respectivamente, o menor e o maior valor da coluna streams, ajudando a identificar possíveis valores discrepantes.

## 📍Verificar e alterar os tipos de dados
Para converter a coluna streams para tipo numérico inteiro:

```
 SELECT
 SAFE_CAST(streams AS INT64) AS streams_limpo
 FROM `spotify-analysis-465623.spotify_data.track_in_spotify`
```

#### 📌 Explicação rápida:

- SAFE_CAST(coluna AS tipo) → Tenta converter o valor de forma segura (sem erro se falhar).

## 🧼 Criação da tabela final tratada

A consulta abaixo:

- Remove duplicatas (mantendo a com mais streams).

- Remove anos fora do intervalo 2000 a 2025.

- Padroniza nomes.

- Substitui valores nulos de in_shazam_charts por 0 (ajuste incluído).

- Remove a coluna key.
```
 CREATE OR REPLACE VIEW spotify-analysis-465623.spotify_data.track_in_spotify_consolidade AS
 SELECT
 track_id,
 REGEXP_REPLACE(track_name, r'[^a-zA-Z0-9 ]', '') AS track_name, REGEXP_REPLACE(artist_s__name, r'[^a-zA-Z0-9 ]', '') AS artist_name, artist_count, released_year, released_month, released_day, in_spotify_playlists, in_spotify_charts, streams FROM ( SELECT *, ROW_NUMBER() OVER(PARTITION BY track_name, artist_s__name ORDER BY streams DESC) AS ordem FROM spotify-analysis-465623.spotify_data.track_in_spotify ) WHERE ordem = 1 AND released_year BETWEEN 2000 AND 2025 -- Exclusão de valores fora do escopo, como 1930
```
📌 Explicação rápida:

- ROW_NUMBER() OVER(PARTITION BY ... ORDER BY ...) → Numera os registros, mantendo só o primeiro (mais relevante).

- IFNULL(campo, valor) → Substitui valores nulos por um valor definido.

- CREATE OR REPLACE VIEW → Cria ou atualiza uma view (tabela virtual com dados tratados).

## 📍Unir (join) as tabelas de dados


## 📍Criar novas variáveis

Adição de uma nova variável (data_de_lançamento):

```
SELECT released_year, released_month, released_day
```

```
PARSE_DATE('%Y-%m-%d', FORMAT('%04d-%02d-%02d', released_year, released_month, released_day)) AS data_de_lanc
```

## 📍Construir tabelas de dados auxiliares
