# 📊 Relatório Técnico – Análise de Faixas Musicais no Spotify

### 🎯 Objetivo do Projeto

Este projeto tem como finalidade analisar dados de faixas musicais disponíveis no Spotify a fim de identificar padrões que contribuem para o desempenho de músicas na plataforma. A análise busca mapear como aspectos técnicos (como BPM, tonalidade, dançabilidade) e fatores de visibilidade (como presença em playlists e rankings) influenciam a popularidade medida por número de streams. A partir desses insights, pretende-se subsidiar decisões estratégicas nas áreas de marketing musical, curadoria e posicionamento de artistas.

### 👥 Equipe

- 👩‍💻 Thais Lira Apolinario
- 👩‍💻 Stephanie Cerqueira Silva

### 🛠️ Ferramentas e Tecnologias Utilizadas

- BigQuery
- Looker Studio

## 🟦  Processamento e Preparação dos Dados

### 🔵 Conexão e Importação de Dados

- track_in_spotify: dados de desempenho no Spotify.

- track_in_competition: presença em competidores (Apple, Deezer, Shazam).

- track_technical: atributos musicais (BPM, key, danceability, etc.).

### 🔵 Identificar e tratar valores nulos

#### Análise de Valores Nulos na Tabela track_in_competition
Na etapa de análise exploratória dos dados, realizamos a verificação de valores nulos nas colunas principais da tabela **track_in_competition**. Os resultados encontrados foram:

- A tabela possui um total de **953** registros.
- Não foram identificados valores nulos nas colunas críticas para identificação, como **track_id**.
- As colunas que indicam presença em playlists e charts da Apple e Deezer (in_apple_playlists, in_apple_charts, in_deezer_playlists, in_deezer_charts) também não apresentaram dados ausentes, indicando que esses campos estão completos para todos os registros.
- Foi identificado um total de **50 valores** nulos na coluna **in_shazam_charts**, o que corresponde a aproximadamente 5,25% do total de registros. Utilizei o WHERE para visualizar as células com o valor NULL.

#### Análise de Valores Nulos na Tabela track_technical
Na etapa de análise exploratória dos dados, realizamos a verificação de valores nulos nas colunas principais da tabela **track_technical**. Os resultados encontrados foram:

A tabela possui um total de **953** registros.
- Não foram identificados valores nulos nas colunas críticas para identificação, como track_id.
- As colunas (bpm, mode, danceability_%,valence_%, energy_%, acousticness_%, instrumentalness_%, liveness_%, speechiness_%) também não apresentaram dados ausentes, indicando que esses campos estão completos para todos os registros.
- Foi identificado um total de **95 valores** nulos na coluna key, o que corresponde a aproximadamente 10% do total de registros. Utilizei o WHERE para visualizar as células com o valor NULL.

#### Análise de Valores Nulos na Tabela track_in_spotify
Na etapa de análise exploratória dos dados, realizamos a verificação de valores nulos nas colunas principais da tabela **track_in_spotify**. Os resultados encontrados foram:
- A tabela possui um total de **953** registros.
- Não foram identificados valores nulos nas colunas críticas para identificação, como track_id.
- As colunas (artists_name, artist_count, released_year, released_month, released_day, in_spotify_playlists, in_spotify_charts, streams) também não apresentaram dados ausentes, indicando que esses campos estão completos para todos os registros.

### 🧼 Tratamento realizado
- A variável **key**, que representa o tom musical da faixa, foi emover as linhas com valores nulos na coluna, com o objetivo de manter apenas faixas com tonalidade definida e garantir consistência na análise técnica. embora a variável key não seja central para os objetivos da análise, optou-se por manter os registros completos e evitar distorções nos dados derivados de campos incompletos.

- A variável **in_shazam_charts**, representa presença e classificação da música nas paradas da Shazam. Teve valores nulos (50 registros) substituídos por 0, com base na premissa de que a ausência de entrada indica que a música não esteve nas paradas do Shazam. 

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

### 🔵 Identificar e tratar valores duplicados

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

🧼 Conclusão: Duplicata técnica. Optamos por manter apenas um dos registros com maior número de streams. Item excluido ID: 3814670

#### About Damn Time – Lizzo track_id: 7173596 e 5080031

- Valores idênticos de BPM, tonalidade, modo e streams.

- Diferença apenas nas playlists associadas.

🧼 Conclusão: Duplicata técnica. Optamos por manter apenas um dos registros com maior número de streams. Item excluido ID: 5080031

#### Take My Breath – The Weeknd  track_id: 1119309 e 4586215

- Mesmo BPM, mas tonalidades e modos distintos, além de diferenças de popularidade.

🧼 Conclusão: São versões diferentes da mesma faixa. Ambas foram mantidas para possibilitar uma análise mais completa sobre o comportamento de consumo.

#### SPIT IN MY FACE! – ThxSoMch  track_id: 4967469 e 8173823

- BPMs e tonalidades diferentes sugerem edições distintas.

- Ambas as versões apresentam números relevantes de streams.

🧼 Conclusão: São versões diferentes da mesma faixa. Ambas foram mantidas para possibilitar uma análise mais completa sobre o comportamento de consumo.

✅  Ações realizadas

- Identificamos e tratamos duplicatas técnicas, mantendo apenas uma versão da música para evitar distorções nas métricas.

- Mantivemos as versões os dados indicaram diferenças reais nas características sonoras ou no comportamento de consumo.

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

### 🔵 Identificar dados fora do escopo de análise

Durante a análise do escopo do projeto, optamos por manter todas as variáveis disponíveis, com o objetivo de explorar o contexto musical de forma ampla. Essa decisão foi tomada para garantir uma visão mais completa dos fatores que influenciam o desempenho das faixas nas plataformas de streaming e suas características musicais.

Dessa forma, foram mantidas as seguintes variáveis por tabela:

- 🎵 track_in_spotify: `track_id`, `track_name`, `artist_s__name`, `artist_count`, `released_year`, `released_month`, `released_day`, `in_spotify_playlists`, `in_spotify_charts`, `streams`;

- 🎵 track_in_competition: `track_id`, `in_apple_playlists`, `in_apple_charts`, `in_deezer_playlists`, `in_deezer_charts`, `in_shazam_charts`;

- 🎵 track_technical:  `track_id`, `bpm`, `key`, `mode`, `danceability_%`, `valence_%`, `energy_%`, `acousticness_%`, `instrumentalness_%`, `liveness_%`, `speechiness_%`;

### 🔵 Identificar dados discrepantes em variáveis ​​categóricas

Durante a análise exploratória, foram identificados possíveis dados discrepantes em variáveis categóricas, como **track_name** e **artist_s__name**, totalizando **48 ocorrências**. Esses registros apresentavam caracteres especiais, emojis ou variações de acentuação, o que poderia comprometer a padronização, além de impactar negativamente agrupamentos, contagens e comparações futuras. 

#### 🧼 Tratamento realizado 

Para garantir a padronização dos dados categóricos, aplicamos a função REGEXP_REPLACE() com o objetivo de remover caracteres especiais, símbolos e emojis, mantendo apenas letras, números e espaços. Em seguida, utilizamos a função LOWER() para padronizar todos os valores em letras minúsculas, evitando divergências em contagens e agrupamentos causadas por diferenças de formatação.

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

### 🔵 Identificar dados discrepantes em variáveis ​​numéricas

Durante a análise exploratória, não foram encontradas discrepâncias relevantes nas tabelas track_in_competition e track_technical. Embora inicialmente valores como 0 em variáveis como instrumentalness_% parecessem inconsistências, observamos que ocorrem em 866 registros — o que indica que se trata de um padrão legítimo e frequente no conjunto de dados.

Já na tabela track_in_spotify, foram identificados alguns dados que destoam do esperado:

- Ano de lançamento incorreto: músicas com ano de lançamento 1930, associadas a artistas contemporâneos como Styrx, Utku INC e Thezth, o que sugere um possível erro de digitação ou preenchimento.

- Texto em campos numéricos: presença de valores textuais em colunas que deveriam conter apenas números.

- Registro com dados ausentes: a linha de ID 4061483 possui valor nulo para streams e outras variáveis importantes, comprometendo sua relevância para a análise.

### 🧼 Tratamento realizado

Corrigimos o ano de lançamento das músicas que estavam incorretas, utilizando uma referência média de lançamentos dos respectivos artistas (quando possível). Removemos registros inconsistentes, como a linha com ID 4061483, que apresentava streams nulo e demais variáveis com valores muito baixos. Garantimos que campos numéricos estivessem corretamente preenchidos, eliminando ou ajustando valores textuais indevidos.

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## ✅ Conclusão da Limpeza de Dados

Após todas as etapas de inspeção, limpeza e padronização, obtivemos uma base consolidada, confiável e pronta para análise. As ações aplicadas garantem:

- Eliminação de duplicidades técnicas;

- Padronização de nomes e formatos;

- Correção e exclusão de dados discrepantes;

- Preenchimento ou remoção de valores nulos conforme o contexto.

Essa preparação foi essencial para garantir a qualidade e integridade dos dados, permitindo que as próximas análises sejam mais precisas e relevantes para os objetivos do projeto.

### 🔵 Unir (join) as tabelas de dados 

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

### 🔵 Criar novas variáveis

Nesta etapa, o objetivo foi criar novas variáveis derivadas para enriquecer a base de dados e permitir análises mais profundas sobre o comportamento musical dos artistas, distribuição de lançamentos e volume de produção.

#### 🧩 Variáveis Criadas

| Variável                      | Descrição                                                                                            |
| ----------------------------- | ---------------------------------------------------------------------------------------------------- |
| `data_lancamento`             | Data de lançamento no formato `YYYY-MM-DD`, criada a partir do ano, mês e dia das colunas originais. |
| `total_playlists`   | soma das participações nas playlists (Apple e Deezer).                                                 |                     

### 🔵 Construir tabelas de dados auxiliares

1. Tabela Auxiliar: musicas_recentes

Objetivo: Criar uma base auxiliar contendo apenas as músicas lançadas após o ano de 2020. Essa filtragem permite explorar tendências musicais mais atuais, ajudando a identificar artistas em ascensão, gêneros populares no período recente e mudanças no perfil das faixas em relação a atributos técnicos (como danceability, valence e energy).

Justificativa Técnica: O uso da função EXTRACT(YEAR FROM data_lancamento) possibilita isolar o ano da data de lançamento, permitindo a filtragem das faixas mais recentes. A ordenação descendente por data_lancamento facilita a visualização cronológica das novidades no catálogo.

2. Tabela Auxiliar: ranking_streams

Objetivo: Criar uma tabela de apoio com as 100 músicas mais tocadas, com base na métrica de streams. Essa tabela é essencial para analisar quais faixas dominam a audiência nas plataformas de streaming, fornecendo insumos para análise de popularidade, padrões de sucesso e possíveis correlações com atributos técnicos ou estratégias de divulgação.

Justificativa Técnica: A ordenação por streams em ordem decrescente, seguida do uso de LIMIT 100, garante a seleção apenas das faixas com maior volume de execução, permitindo foco nas músicas com maior alcance e relevância entre os usuários.

[Consulta SQL usada no projeto](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/formulas_projeto_spotify.md)

## 🟪 Análise Exploratória de Dados

A análise exploratória de dados (AED) tem como objetivo compreender o comportamento das variáveis presentes no conjunto de dados, identificar padrões, outliers, tendências temporais e possíveis correlações. No caso das músicas disponíveis no Spotify, a investigação foi conduzida considerando variáveis categóricas (como ano de lançamento), numéricas (streams, BPM, danceability, energy) e métricas derivadas (percentis, correlações).

### 🟣  Agrupar dados por variáveis categóricas	

Objetivo: entender comportamentos médios ou totais com base em categorias.

🔹 1. Streams por faixa de total de playlists:

| Faixa       | Média de Streams |
| ----------- | ---------------- |
| `>5000`     | **1.16B**        |
| `1001-5000` | 322M             |
| `100-1000`  | 150M             |
| `<100`      | 53M              |

🔹 2. Top 20 artistas por total de streams no Spotify:

| Rank | Artista            | Total de Streams | Percentual (%) |
|------|---------------------|------------------|----------------|
| 1    | Ed Sheeran          | 13,908,947,204   | 3.17%          |
| 2    | Taylor Swift        | 11,851,151,082   | 2.70%          |
| 3    | The Weeknd          | 10,069,328,661   | 2.29%          |
| 4    | Bad Bunny           | 8,582,384,095    | 1.95%          |
| 5    | Harry Styles        | 8,546,679,005    | 1.95%          |
| 6    | Olivia Rodrigo      | 7,442,148,916    | 1.69%          |
| 7    | Eminem              | 6,183,805,596    | 1.41%          |
| 8    | Imagine Dragons     | 5,272,484,650    | 1.20%          |
| 9    | Lewis Capaldi       | 4,734,698,360    | 1.08%          |
| 10   | Doja Cat            | 4,702,294,655    | 1.07%          |
| 11   | Adele               | 4,508,746,590    | 1.03%          |
| 12   | BTS                 | 4,389,891,591    | 1.00%          |
| 13   | SZA                 | 4,197,341,485    | 0.96%          |
| 14   | Bruno Mars          | 4,185,733,280    | 0.95%          |
| 15   | The Neighbourhood   | 4,010,009,939    | 0.91%          |
| 16   | Justin Bieber       | 3,919,813,522    | 0.89%          |
| 17   | Coldplay            | 3,825,176,058    | 0.87%          |
| 18   | Avicii              | 3,426,754,746    | 0.78%          |
| 19   | Dua Lipa            | 3,227,639,000    | 0.73%          |
| 20   | Arctic Monkeys      | 3,055,659,795    | 0.70%          |

Uma das principais formas de análise foi agrupar os dados com base na variável categórica artists_name, o que permitiu identificar os artistas mais ouvidos na base de dados. Ed Sheeran lidera o ranking com mais de 13,9 bilhões de streams, seguido por Taylor Swift com 11,8 bilhões e The Weeknd com 10 bilhões. Esses três artistas juntos concentram quase 9% de todos os streams do conjunto de dados, o que mostra uma concentração considerável de popularidade em poucos nomes.

### 🟣  Visualizar variáveis ​​categóricas

Objetivo: entender visualmente a distribuição em faixas/categorias.

- Top 10 artistas com mais músicas

| Artista         | Qtd. de Músicas |
|------------------|------------------|
| Taylor Swift     | 29               |
| The Weeknd       | 17               |
| SZA              | 17               |
| Bad Bunny        | 16               |
| Harry Styles     | 13               |
| Kendrick Lamar   | 12               |
| Morgan Wallen    | 9                |
| Ed Sheeran       | 9                |
| Feid             | 8                |
| BTS              | 8                |

💡 Taylor Swift lidera com folga, com 29 músicas na base de dados — o que sugere uma presença marcante no período recente, especialmente entre 2021 e 2023. Artistas como The Weeknd, SZA, Bad Bunny e Harry Styles reforçam a dominância dos gêneros pop, R&B e reggaeton nos lançamentos mais populares do período analisado.

- Distribuição por tonalidade (key)

| Tonalidade (Key) | Qtd. de Músicas |
|-------------------|------------------|
| C#                | 120              |
| G                 | 96               |
| G#                | 91               |
| F                 | 89               |
| D                 | 81               |
| B                 | 81               |
| A                 | 74               |
| F#                | 73               |
| E                 | 62               |
| A#                | 56               |
| D#                | 33               |

💡  A tonalidade C# aparece como a mais frequente, com 120 músicas — algo comum em produções eletrônicas contemporâneas. As tonalidades mais utilizadas são majoritariamente sustenidas, o que sugere o uso recorrente de produção digital e vocais processados (ex: autotune). Ainda assim, tonalidades clássicas como G, D, A e F permanecem relevantes, indicando diversidade de estilos musicais.

- Quantidade de músicas lançadas por ano

| Ano de Lançamento | Qtd. de Músicas |
|--------------------|------------------|
| 2019               | 33               |
| 2020               | 29               |
| 2021               | 107              |
| 2022               | 361              |
| 2023               | 159              |

💡 A partir de 2019, nota-se um crescimento acelerado no número de lançamentos. O ano de 2022 representa o pico da série, concentrando mais de 42% do total de músicas lançadas nesse recorte recente. Em 2023 há uma leve queda, mas o volume ainda permanece elevado em relação aos anos anteriores.

- Distribuição por modo (maior/menor)

| Modo  | Qtd. de Músicas |
| ----- | --------------- |
| Maior | 474             |
| Menor | 382             |


💡 A maioria das músicas está em modo maior, com 474 faixas, contra 382 em modo menor. Isso sugere uma leve preferência por sonoridades mais alegres ou brilhantes, típicas de faixas pop comerciais — embora a presença significativa do modo menor indique também espaço para sonoridades mais introspectivas, comuns em R&B, trap e baladas.

### 🟣  Aplicar medidas de tendência central

Objetivo: calcular média, mediana, etc.

- Estatísticas gerais (média, mínimo, máximo)

| Variável         | Média          | Mínimo | Máximo        | Desvio Padrão  |
| ---------------- | -------------- | ------ | ------------- | -------------- |
| danceability     | 67.25          | 23     | 96            | 14.65          |
| instrumentalness | 1.61           | 0      | 91            | 8.58           |
| streams          | 513,109,400.48 | 2,762  | 3,703,895,074 | 571,774,193.76 |
| bpm              | 122.86         | 65     | 206           | 28.21          |
| speechiness      | 10.40          | 2      | 64            | 10.10          |
| liveness         | 18.16          | 3      | 97            | 13.57          |
| acousticness     | 26.66          | 0      | 97            | 25.70          |
| energy           | 64.33          | 14     | 97            | 16.06          |
| valence          | 51.20          | 4      | 97            | 23.60          |


📌 Danceability tem uma média alta (67.25) — indica músicas dançantes, com foco em pop, reggaeton, R&B. BPM médio de ~123 indica uma predominância de músicas moderadamente rápidas, ideais para rádio e streaming. Streams variam de milhares a bilhões, sugerindo forte assimetria (grande desigualdade de popularidade entre músicas).

### 🟣  Visualizar a distribuição dos dados

Objetivo: analisar como os dados se espalham em faixas.

- 📊 1. Danceability

Faixa vai de 23 a 74

Pico por volta de 56 a 74, com destaque para:

56 → 27 músicas

59 → 22 músicas

60 → 19 músicas

63 → 20 músicas

65 → 24 músicas

70 → 37 músicas (maior valor)

- 📊 2. Energy

Faixa vai de 14 a 69

Distribuição mais "espalhada", com picos entre:

62 → 28 músicas (pico máximo)

60 → 22 músicas

66 → 24 músicas

65 e 67 → 20 músicas cada

63 e 64 → 18–20 músicas

### 🟣  Aplicar medidas de dispersão

Objetivo: entender a variabilidade dos dados.

| Variável     | Desvio Padrão     |
|--------------|-------------------|
| Energy       | 16.06             |
| Streams      | 571.77 milhões    |
| BPM          | 28.21             |

📌 A avaliação da variabilidade incluiu amplitude, variância, desvio-padrão e quartis. Constatou-se que os streams possuem elevada dispersão, evidenciando desigualdade na distribuição do sucesso musical. Já variáveis como energy e danceability apresentaram dispersão mais controlada, indicando que a maioria das músicas segue padrões semelhantes nesses atributos.

### 🟣  Visualizar o comportamento dos dados ao longo do tempo

Objetivo: detectar tendências temporais.

- Streams médios por ano

| Linha | Ano  | Média de Streams |
| ----- | ---- | ---------------- |
| 1     | 1930 | 90,598,517.0     |
| 2     | 1942 | 395,591,396.0    |
| 3     | 1946 | 389,771,964.0    |
| 4     | 1950 | 473,248,298.0    |
| 5     | 1957 | 459,981,011.0    |
| ----- | ---- | ---------------- |
| 43    | 2019 | 998,433,019.42   |
| 44    | 2020 | 945,308,475.79   |
| 45    | 2021 | 631,264,055.78   |
| 46    | 2022 | 284,987,927.78   |
| 47    | 2023 | 143,932,389.40   |

💡 No que diz respeito à média de streams por ano de lançamento, os maiores valores ocorrem entre 1998 e 2018, com picos entre 1 e 1,5 bilhão de reproduções por música. A partir de 2019, há uma queda contínua nessa média: 998 milhões em 2019, 945 milhões em 2020, caindo para 631 milhões em 2021, 284 milhões em 2022 e 143 milhões em 2023.

Essa redução não indica necessariamente perda de popularidade, mas sim fatores como o aumento exponencial de lançamentos (o que dilui a média geral) e o fato de que músicas mais recentes ainda estão em fase de acumular streams. Em resumo, o cenário atual é marcado por uma produção musical massiva, impulsionada pela digitalização e plataformas de streaming, ao mesmo tempo em que a atenção do público se distribui entre um número muito maior de faixas.

- Quantidade de Músicas por Ano

| Linha | Ano  | Qtde de Músicas |
| ----- | ---- | --------------- |
| 1     | 1930 | 1               |
| 2     | 1942 | 1               |
| 3     | 1946 | 1               |
| 4     | 1950 | 1               |
| 5     | 1957 | 2               |
| ----- | ---- | --------------- |
| 43    | 2019 | 33              |
| 44    | 2020 | 29              |
| 45    | 2021 | 107             |
| 46    | 2022 | 361             |
| 47    | 2023 | 159             |

💡 De 1942 até o fim dos anos 1990, a quantidade de músicas lançadas por ano é bastante limitada (geralmente de 1 a 3 faixas), o que torna as médias de streams desses anos pouco representativas — uma única música de grande sucesso pode inflar significativamente os resultados. Um exemplo notável é 1975, que registra uma média de mais de 2 bilhões de streams com apenas uma música cadastrada.

A partir de 1999, observa-se um aumento gradual na quantidade de lançamentos, que se intensifica consideravelmente a partir de 2010. Entre 2016 e 2020, esse crescimento se mantém estável, mas em 2021 ocorre um salto expressivo, com 107 músicas. Em 2022, atinge-se o maior valor da série, com 361 faixas lançadas. Embora haja uma queda para 159 em 2023, o número ainda é alto comparado aos anos anteriores.

### 🟣  Calcular quartis, decis ou percentis

Objetivo: entender distribuição de forma precisa.

🔍 1. Quartis (Q1, Q2, Q3)

| Variável         | Q0  | Q1  | Q2  | Q3  | Q4  |
| ---------------- | -------- | --- | ------------ | --- | -------- |
| instrumentalness | 0  | 0   | 0            | 0   | 91       |
| speechiness      | 2  | 4   | 6            | 12  | 64       |
| liveness         | 3        | 10  | 12           | 24  | 97       |
| energy           | 14 | 53  | 65           | 76  | 97       |
| valence          | 4  | 32  | 51           | 70  | 97       |
| acousticness     | 0  | 5   | 17           | 42  | 97       |
| bpm              | 65 | 100 | 121          | 142 | 206      |
| danceability     | 23 | 57  | 69           | 78  | 96       |

📌 Os quartis dividem os dados em quatro partes iguais. Destacamos:

- instrumentalness possui valores extremamente concentrados no zero (Q0 = Q1 = Q2 = Q3 = 0), com um valor máximo (Q4) de 91. Isso indica que a maioria das músicas não são instrumentais, e apenas alguns casos isolados possuem alto nível de instrumentalidade.

- speechiness e liveness também têm valores baixos para a maior parte dos dados (medianas em 6 e 12, respectivamente), indicando baixa presença de fala ou "ambiência ao vivo" nas faixas.

- energy, valence, danceability e bpm apresentam uma distribuição mais equilibrada, com mediana em:

- Energy: 65

- Valence: 51

- Danceability: 69

- BPM: 121

Isso sugere que boa parte das músicas possuem energia e dançabilidade moderadas a altas, além de valores rítmicos compatíveis com músicas comerciais.

🔍 2. Decis (10 em 10)

| Variável         | D1 | D2 | D3 | D4  | D5  | D6  | D7  | D8  | D9  | Máx |
| ---------------- | -- | -- | -- | --- | --- | --- | --- | --- | --- | --- |
| instrumentalness | 0  | 0  | 0  | 0   | 0   | 0   | 0   | 0   | 0   | 91  |
| liveness         | 3  | 8  | 9  | 10  | 11  | 12  | 15  | 19  | 28  | 97  |
| speechiness      | 2  | 3  | 4  | 4   | 5   | 6   | 7   | 10  | 15  | 64  |
| acousticness     | 0  | 1  | 4  | 7   | 11  | 17  | 26  | 36  | 49  | 97  |
| bpm              | 65 | 89 | 96 | 104 | 113 | 121 | 128 | 138 | 146 | 206 |
| valence          | 4  | 20 | 27 | 37  | 44  | 51  | 58  | 65  | 74  | 97  |
| energy           | 14 | 43 | 51 | 56  | 62  | 65  | 70  | 74  | 79  | 97  |
| danceability     | 23 | 46 | 55 | 60  | 65  | 70  | 73  | 77  | 80  | 96  |

📌 Os decis nos permitem observar como os valores estão concentrados em intervalos menores. Alguns destaques:

- instrumentalness reforça sua concentração total nos primeiros decis (D1 a D9 = 0), com 91 apenas no D10, caracterizando forte assimetria.

- acousticness, apesar de também ter valores baixos nos primeiros decis, cresce gradualmente, sugerindo que embora muitas músicas sejam pouco acústicas, há uma porção considerável com características acústicas elevadas.

- bpm apresenta uma distribuição bem espalhada, indo de 65 (D1) até 206 (máx), com distribuição crescente e consistente, o que reflete a variação nos estilos musicais.

- valence e energy mostram uma distribuição mais homogênea, com aumento progressivo, indicando variedade de emoções e intensidade nas músicas.

🔍 3. Percentil 95 (P95)

| Variável         | Percentil 95 (P95) |
| ---------------- | ------------------ |
| bpm              | 174                |
| danceability     | 90                 |
| valence          | 90                 |
| acousticness     | 81                 |
| speechiness      | 34                 |
| liveness         | 44                 |
| energy           | 89                 |
| instrumentalness | 5                  |

📌 O P95 indica o valor abaixo do qual estão 95% dos dados. Valores acima disso são potenciais outliers. Veja os principais destaques:

- bpm: 95% das músicas têm BPM até 174, o que indica que músicas com BPM acima disso são raras e provavelmente mais aceleradas (e.g., eletrônica ou techno).

- speechiness: apenas 5% das faixas têm valor acima de 34, logo, músicas com muitos elementos de fala (como rap ou podcasts) são minoria.

- instrumentalness: apesar do valor máximo ser 91, o P95 é apenas 5, reforçando que a grande maioria das faixas tem baixa ou nenhuma instrumentalidade.

- danceability, valence, energy e acousticness têm P95 entre 81 e 90, sugerindo que faixas com altíssimos níveis nessas características são menos comuns, mas ainda relevantes.

### 🟣  Calcular correlação entre variáveis ​​

Objetivo: entender relações lineares.

| Variável           | Correlação |
|--------------------|------------|
| Danceability       | -0.101     |
| Energy             | -0.030     |
| Valence            | -0.043     |
| BPM                | -0.002     |
| Acousticness       | +0.011     |
| Liveness           | -0.055     |
| Speechiness        | -0.113     |
| Nº de Playlists    | **+0.782** |

📌 A análise de correlação demonstrou que:

Streams x Playlists: forte correlação positiva (0,78).

👉 Quanto mais playlists uma música aparece, maior seu número de streams.

Streams x Danceability, Energy, Valence, BPM: correlação fraca (quase nula).

Streams x Speechiness: leve correlação negativa (–0,11).

👉 Popularidade não depende do perfil sonoro, mas sim da exposição em playlists.

[Relatório Final](https://github.com/tha-lira/projeto_02-laboratoria/blob/master/relat%C3%B3rioAnalise.md)

## 🟥 Aplicar técnica de análise

### 🔴 Aplicar segmentação

| Variável        | Categoria         | Média de Streams |
|-----------------|------------------|------------------|
| Acousticness    | Q1 - Muito Baixa | 620.171.492      |
| Acousticness    | Q2 - Baixa/Média | 436.783.424      |
| Acousticness    | Q3 - Média/Alta  | 445.149.431      |
| Acousticness    | Q4 - Muito Alta  | 550.333.254      |
|-----------------|------------------|------------------|
| BPM             | Q1 - Muito Baixa | 540.415.402      |
| BPM             | Q2 - Baixa/Média | 538.812.898      |
| BPM             | Q3 - Média/Alta  | 448.144.598      |
| BPM             | Q4 - Muito Alta  | 525.064.704      |
|-----------------|------------------|------------------|
| Danceability    | Q1 - Muito Baixa | 583.840.158      |
| Danceability    | Q2 - Baixa/Média | 533.939.249      |
| Danceability    | Q3 - Média/Alta  | 505.183.992      |
| Danceability    | Q4 - Muito Alta  | 429.474.202      |
|-----------------|------------------|------------------|
| Energy          | Q1 - Muito Baixa | 550.799.660      |
| Energy          | Q2 - Baixa/Média | 503.034.486      |
| Energy          | Q3 - Média/Alta  | 506.344.796      |
| Energy          | Q4 - Muito Alta  | 492.258.660      |
|-----------------|------------------|------------------|
| Instrumentalness| Q1 - Muito Baixa | 861.370.606      |
| Instrumentalness| Q2 - Baixa/Média | 228.355.325      |
| Instrumentalness| Q3 - Média/Alta  | 670.259.919      |
| Instrumentalness| Q4 - Muito Alta  | 292.451.752      |
|-----------------|------------------|------------------|
| Liveness        | Q1 - Muito Baixa | 578.523.706      |
| Liveness        | Q2 - Baixa/Média | 507.008.092      |
| Liveness        | Q3 - Média/Alta  | 496.602.340      |
| Liveness        | Q4 - Muito Alta  | 470.303.463      |
|-----------------|------------------|------------------|
| Speechiness     | Q1 - Muito Baixa | 610.549.468      |
| Speechiness     | Q2 - Baixa/Média | 517.771.052      |
| Speechiness     | Q3 - Média/Alta  | 516.450.894      |
| Speechiness     | Q4 - Muito Alta  | 407.666.189      |
|-----------------|------------------|------------------|
| Valence         | Q1 - Muito Baixa | 525.918.604      |
| Valence         | Q2 - Baixa/Média | 557.138.298      |
| Valence         | Q3 - Média/Alta  | 501.454.306      |
| Valence         | Q4 - Muito Alta  | 467.926.394      |

### 🔴 Validar hipótese

### 🔴 Regressão linear

## 🟧 Resumir as informações em um dashboard ou relatório

### 🟠 Representar os dados por meio de tabela resumo ou scorecards

### 🟠 Representar os dados através de gráficos simples

### 🟠 Representar os dados por meio de gráficos ou recursos visuais avançados

### 🟠 Aplicar opções de filtros para gerenciamento e interação

## 🟩 Apresentar os Resultados

### 🟢 Selecionar gráficos e informações relevantes

### 🟢 Criar uma apresentação

### 🟢 Apresentar resultados com conclusões e recomendações

#### Limitações

Durante o desenvolvimento deste projeto, a ferramenta inicialmente proposta para a construção do dashboard foi o Power BI. No entanto, a execução local do Power BI Desktop apresentou limitações técnicas, principalmente devido à incompatibilidade com o sistema operacional Ubuntu utilizado no meu equipamento pessoal, além de restrições de hardware que inviabilizaram o uso de máquinas virtuais com Windows.

Diante desse cenário, optei pelo uso do Looker Studio (antigo Data Studio), uma ferramenta de visualização de dados do Google, 100% baseada na web, que se integra de forma nativa com o Google BigQuery, onde os dados tratados do projeto estavam armazenados. Essa escolha se mostrou tecnicamente viável, gratuita, compatível com o ambiente Linux e adequada aos objetivos da análise.