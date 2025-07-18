# 📊 

### 🎯 Objetivo do Projeto
O objetivo deste projeto é analisar dados de **faixas musicais presentes no Spotify** a fim de identificar padrões que influenciam o desempenho das músicas na plataforma. A análise busca compreender como características técnicas e comportamentais das faixas — como presença em playlists, rankings e número de streams — se relacionam com seu sucesso. A partir desses insights, pretende-se apoiar a tomada de decisões estratégicas em áreas como marketing musical, curadoria de conteúdo e posicionamento de artistas.

### 👥 Equipe
- 👩‍💻 Thais Lira Apolinario
- 👩‍💻 Stephanie Cerqueira Silva

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
- A variável **key**, que representa o tom musical da faixa, foi removida devido à alta proporção de valores nulos (95 registros) e à baixa relevância para os objetivos da análise, que não contemplam aspectos harmônicos da música.

- A variável **in_shazam_charts**, representa presença e classificação da música nas paradas da Shazam. Teve valores nulos (50 registros) substituídos por 0, com base na premissa de que a ausência de entrada indica que a música não esteve nas paradas do Shazam. 

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## 📍 Identificar e tratar valores duplicados

Durante a análise da base de dados, foi identificada a presença de múltiplos registros para uma mesma música, como nos casos abaixo:

- **SNAP** (Rosa Linn): **track_id** 5675634 e 3814670

- **About Damn Time** (Lizzo): **track_id** 7173596 e 5080031

- **Take My Breath** (The Weeknd): **track_id** 1119309 e 4586215

- **SPIT IN MY FACE!** (ThxSoMch): **track_id** 4967469 e 8173823

Essa duplicidade ocorre porque uma mesma faixa pode ser cadastrada com diferentes identificadores, seja por versões lançadas em momentos distintos, inclusão em álbuns ou singles separados, edições remixadas ou por outras estratégias de distribuição nas plataformas de streaming.

Para garantir a consistência da análise, foi necessário investigar cada caso individualmente e decidir qual registro manter. A escolha se baseou no número de streams e na completude dos metadados técnicos. Essa etapa foi fundamental para evitar distorções nos resultados e garantir que cada música fosse considerada apenas uma vez nas análises estatísticas e de desempenho.

### 🎧 Análise individual das músicas

#### SNAP – Rosa Linn Track_id = 5675634 e 3814670

- Registros com mesmo BPM e modo.

- Diferença pequena no número de playlists e streams.

- 🧼 Conclusão: Duplicata técnica. Optamos por manter apenas um dos registros com maior número de streams. Item excluido ID: 3814670

#### About Damn Time – Lizzo track_id: 7173596 e 5080031

- Valores idênticos de BPM, tonalidade, modo e streams.

- Diferença apenas nas playlists associadas.

- 🧼 Conclusão: Duplicata técnica. Optamos por manter apenas um dos registros com maior número de streams. Item excluido ID: 5080031

#### Take My Breath – The Weeknd  track_id: 1119309 e 4586215

- Mesmo BPM, mas tonalidades e modos distintos, além de diferenças de popularidade.

- 🧼 Conclusão: São versões diferentes da mesma faixa. Ambas foram mantidas para possibilitar uma análise mais completa sobre o comportamento de consumo.

#### SPIT IN MY FACE! – ThxSoMch  track_id: 4967469 e 8173823

- BPMs e tonalidades diferentes sugerem edições distintas.

- Ambas as versões apresentam números relevantes de streams.

- 🧼 Conclusão: São versões diferentes da mesma faixa. Ambas foram mantidas para possibilitar uma análise mais completa sobre o comportamento de consumo.


✅  Ações realizadas

- Identificamos e tratamos duplicatas técnicas, mantendo apenas uma versão da música para evitar distorções nas métricas.

- Mantivemos as versões os dados indicaram diferenças reais nas características sonoras ou no comportamento de consumo.

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## 📍Identificar dados fora do escopo de análise

Por enquanto, não identificamos valores que estejam claramente fora do escopo da análise. Todas as variáveis presentes parecem relevantes neste momento. No entanto, alguns casos poderão ser reavaliados durante as próximas etapas da análise, como por exemplo a quantidade de artistas por faixa.

## 📍Identificar dados discrepantes em variáveis ​​categóricas

Durante a análise exploratória, foram identificados possíveis dados discrepantes em variáveis categóricas, como **track_name** e **artist_s__name**, totalizando **48 ocorrências**. Esses registros apresentavam caracteres especiais, emojis ou variações de acentuação, o que poderia comprometer a padronização, além de impactar negativamente agrupamentos, contagens e comparações futuras. 

### 🧼 Tratamento realizado 

Para garantir a padronização dos dados categóricos, aplicamos a função REGEXP_REPLACE() com o objetivo de remover caracteres especiais, símbolos e emojis, mantendo apenas letras, números e espaços. Em seguida, utilizamos a função LOWER() para padronizar todos os valores em letras minúsculas, evitando divergências em contagens e agrupamentos causadas por diferenças de formatação.

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## 📍Identificar dados discrepantes em variáveis ​​numéricas

Durante a análise exploratória, não foram encontradas discrepâncias relevantes nas tabelas track_in_competition e track_technical. Embora inicialmente valores como 0 em variáveis como instrumentalness_% parecessem inconsistências, observamos que ocorrem em 866 registros — o que indica que se trata de um padrão legítimo e frequente no conjunto de dados.

Já na tabela track_in_spotify, foram identificados alguns dados que destoam do esperado:

- Ano de lançamento incorreto: músicas com ano de lançamento 1930, associadas a artistas contemporâneos como Styrx, Utku INC e Thezth, o que sugere um possível erro de digitação ou preenchimento.

- Texto em campos numéricos: presença de valores textuais em colunas que deveriam conter apenas números.

- Registro com dados ausentes: a linha de ID 4061483 possui valor nulo para streams e outras variáveis importantes, comprometendo sua relevância para a análise.

### 🧼 Tratamento realizado

Corrigimos o ano de lançamento das músicas que estavam incorretas, utilizando uma referência média de lançamentos dos respectivos artistas (quando possível). Removemos registros inconsistentes, como a linha com ID 4061483, que apresentava streams nulo e demais variáveis com valores muito baixos. Garantimos que campos numéricos estivessem corretamente preenchidos, eliminando ou ajustando valores textuais indevidos.

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## 📍Verificar e alterar os tipos de dados
 
### 🧼 Tratamento realizado 

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## 📍Unir (join) as tabelas de dados

### 🧼 Tratamento realizado
[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## 📍Criar novas variáveis

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## 📍Construir tabelas de dados auxiliares

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## ✅ Conclusão da Limpeza de Dados

Após todas as etapas de inspeção, limpeza e padronização, obtivemos uma base consolidada, confiável e pronta para análise. As ações aplicadas garantem:

- Eliminação de duplicidades técnicas;

- Padronização de nomes e formatos;

- Correção e exclusão de dados discrepantes;

- Preenchimento ou remoção de valores nulos conforme o contexto.

Essa preparação foi essencial para garantir a qualidade e integridade dos dados, permitindo que as próximas análises sejam mais precisas e relevantes para os objetivos do projeto.