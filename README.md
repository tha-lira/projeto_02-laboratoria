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
- A variável **key**, que representa o tom musical da faixa, foi emover as linhas com valores nulos na coluna, com o objetivo de manter apenas faixas com tonalidade definida e garantir consistência na análise técnica. embora a variável key não seja central para os objetivos da análise, optou-se por manter os registros completos e evitar distorções nos dados derivados de campos incompletos.

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

Durante a análise do escopo do projeto, optamos por manter todas as variáveis disponíveis, com o objetivo de explorar o contexto musical de forma ampla. Essa decisão foi tomada para garantir uma visão mais completa dos fatores que influenciam o desempenho das faixas nas plataformas de streaming e suas características musicais.

Dessa forma, foram mantidas as seguintes variáveis por tabela:

- 🎵 track_in_spotify: `track_id`, `track_name`, `artist_s__name`, `artist_count`, `released_year`, `released_month`, `released_day`, `in_spotify_playlists`, `in_spotify_charts`, `streams`;

- 🎵 track_in_competition: `track_id`, `in_apple_playlists`, `in_apple_charts`, `in_deezer_playlists`, `in_deezer_charts`, `in_shazam_charts`;

- 🎵 track_technical:  `track_id`, `bpm`, `key`, `mode`, `danceability_%`, `valence_%`, `energy_%`, `acousticness_%`, `instrumentalness_%`, `liveness_%`, `speechiness_%`;

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


## ✅ Conclusão da Limpeza de Dados

Após todas as etapas de inspeção, limpeza e padronização, obtivemos uma base consolidada, confiável e pronta para análise. As ações aplicadas garantem:

- Eliminação de duplicidades técnicas;

- Padronização de nomes e formatos;

- Correção e exclusão de dados discrepantes;

- Preenchimento ou remoção de valores nulos conforme o contexto.

Essa preparação foi essencial para garantir a qualidade e integridade dos dados, permitindo que as próximas análises sejam mais precisas e relevantes para os objetivos do projeto.

## 📍Unir (join) as tabelas de dados 

Após a realização das limpezas individuais em cada uma das tabelas brutas, foi possível realizar a junção dos dados com segurança e consistência. A união teve como objetivo centralizar as informações técnicas e de desempenho das faixas musicais em uma única tabela, facilitando as análises exploratórias e estatísticas.

Para garantir a integridade dos dados, a query de união foi elaborada considerando apenas os registros cujo track_id estava presente simultaneamente em todas as tabelas. 

Essa abordagem permitiu evitar que fossem incluídos na tabela unificada registros com valores nulos oriundos de track_id ausentes em uma das fontes. Dessa forma, não foi necessário realizar uma exclusão posterior dos nulos, pois a query já foi desenhada para filtrar esses casos desde o início.

Foram utilizadas três tabelas tratadas:

- track_in_spotify_tratado (ts): contém informações sobre nome da faixa, artista, data de lançamento e métricas de desempenho no Spotify.

- track_in_competition_tratado (tc): traz os dados sobre a presença das faixas em plataformas concorrentes como Apple Music, Deezer e Shazam.

- track_technical_tratado (tt): armazena as características técnicas das músicas, como BPM, tonalidade, energia e dançabilidade.

A união foi feita com base na coluna track_id, comum às três tabelas, utilizando a instrução INNER JOIN, que garante que apenas os registros presentes em todas as tabelas sejam considerados. Abaixo, a query utilizada:

### 🧼 Tratamento realizado
[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## 📍Criar novas variáveis

Nesta etapa, o objetivo foi criar novas variáveis derivadas para enriquecer a base de dados e permitir análises mais profundas sobre o comportamento musical dos artistas, distribuição de lançamentos e volume de produção.

#### 🧩 Variáveis Criadas

| Variável                      | Descrição                                                                                            |
| ----------------------------- | ---------------------------------------------------------------------------------------------------- |
| `data_lancamento`             | Data de lançamento no formato `YYYY-MM-DD`, criada a partir do ano, mês e dia das colunas originais. |
| `total_playlists`   | soma das participações nas playlists (Apple e Deezer).                                                 |                     

## 📍Construir tabelas de dados auxiliares

1. Tabela Auxiliar: musicas_recentes

Objetivo: Criar uma base auxiliar contendo apenas as músicas lançadas após o ano de 2020. Essa filtragem permite explorar tendências musicais mais atuais, ajudando a identificar artistas em ascensão, gêneros populares no período recente e mudanças no perfil das faixas em relação a atributos técnicos (como danceability, valence e energy).

Justificativa Técnica: O uso da função EXTRACT(YEAR FROM data_lancamento) possibilita isolar o ano da data de lançamento, permitindo a filtragem das faixas mais recentes. A ordenação descendente por data_lancamento facilita a visualização cronológica das novidades no catálogo.

2. Tabela Auxiliar: ranking_streams

Objetivo: Criar uma tabela de apoio com as 100 músicas mais tocadas, com base na métrica de streams. Essa tabela é essencial para analisar quais faixas dominam a audiência nas plataformas de streaming, fornecendo insumos para análise de popularidade, padrões de sucesso e possíveis correlações com atributos técnicos ou estratégias de divulgação.

Justificativa Técnica: A ordenação por streams em ordem decrescente, seguida do uso de LIMIT 100, garante a seleção apenas das faixas com maior volume de execução, permitindo foco nas músicas com maior alcance e relevância entre os usuários.

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

# Fazer uma análise exploratória	

### 📍 Agrupar dados por variáveis categóricas	

Foi realizada uma triagem das variáveis categóricas presentes na tabela tabela_unificada_tratada, utilizadas como dimensões na análise e nos dashboards no **Looker Studio**:

- track_id: Identificador único da faixa

- artists_name: Nome do(s) artista(s)

- track_name: Nome da música

- key: Tom musical (ex: C, D#, F#m)

- mode: Modo musical (maior/menor)

- released_year, released_month, released_day: Datas de lançamento

- data_lancamento: Data completa de lançamento

Essas variáveis permitiram segmentações por artista, data e características musicais, fundamentais para a geração de gráficos e insights.

### 📌 Visualizar variáveis ​​categóricas

- 📊 Gráfico 1: Top 10 artistas com mais músicas

O gráfico mostra os 10 artistas com o maior número de músicas no conjunto de dados. A artista com maior presença é Taylor Swift(29), seguida de SZA(17) e Bad Bunny(16). Isso indica que esses artistas são os mais produtivos (ou com mais músicas listadas na base de dados). Artistas como The Weeknd, Harry Styles, Kendrick Lamar e BTS também aparecem, mostrando forte presença musical. BTS(8) é o último do top 10, com uma quantidade menor de músicas em relação aos demais.

### 📌 Aplicar medidas de tendência central

- 🎧 Média e Mediana de Streams e Playlists:

Streams médios:     513.1 milhões  
Streams mediana:    284.9 milhões  
Playlists médias:   5.208  
Playlists mediana:  2.163

A média de streams é significativamente superior à mediana, evidenciando uma distribuição assimétrica onde poucas faixas de altíssimo sucesso puxam a média para cima.

- 📊 Média de streams por artista

Este gráfico apresenta os 10 artistas com maior média de streams por música. A artista com a maior média de streams é Tones and I, o que sugere que, embora possa ter poucas músicas, elas são altamente populares. Em seguida, aparecem Post Malone, Swae Lee, Drake, Wizkid e Kyla, todos com média de streams muito elevada, indicando grande alcance por música.

Artistas como The Weeknd, que estavam no gráfico anterior (com muitas músicas), aparecem aqui em posição intermediária. Isso indica que, mesmo com muitos lançamentos, a média de streams por música não é a mais alta.

Na parte inferior do ranking estão The Chainsmokers e Coldplay, o que mostra que, em média, suas músicas são menos ouvidas em comparação com os líderes do gráfico, mesmo que sejam artistas conhecidos.

### 📌 Visualizar a distribuição dos dados

| Faixa de Streams | Nº de Músicas |
| ---------------- | ------------- |
| 0 - 1M           | 1             |
| 1M - 5M          | 1             |
| 5M - 10M         | 0             |
| **10M+**         | **854**       |

A enorme concentração de músicas com mais de 10 milhões de streams e baixa presença em playlists mostra que o sucesso não depende apenas de curadoria — viralização e alcance orgânico também são determinantes.

### 📌 Aplicar medidas de dispersão

### 📌 Visualizar o comportamento dos dados ao longo do tempo

- 📅 Lançamentos por Mês e Ano

A análise da quantidade de faixas lançadas por mês e ano mostrou sazonalidade nos lançamentos, com alguns picos em meses específicos (a explorar mais no dashboard).

- 📊 Média de Streams por Mês

Revelou-se que a média de streams não acompanha exatamente o volume de lançamentos, sugerindo que existem momentos mais estratégicos para atingir altos números, independentemente da quantidade de faixas lançadas.

### 📌 Calcular quartis, decis ou percentis

### 📌 Calcular correlação entre variáveis ​​

#### Limitações

Durante o desenvolvimento deste projeto, a ferramenta inicialmente proposta para a construção do dashboard foi o Power BI. No entanto, a execução local do Power BI Desktop apresentou limitações técnicas, principalmente devido à incompatibilidade com o sistema operacional Ubuntu utilizado no meu equipamento pessoal, além de restrições de hardware que inviabilizaram o uso de máquinas virtuais com Windows.

Diante desse cenário, optei pelo uso do Looker Studio (antigo Data Studio), uma ferramenta de visualização de dados do Google, 100% baseada na web, que se integra de forma nativa com o Google BigQuery, onde os dados tratados do projeto estavam armazenados. Essa escolha se mostrou tecnicamente viável, gratuita, compatível com o ambiente Linux e adequada aos objetivos da análise.