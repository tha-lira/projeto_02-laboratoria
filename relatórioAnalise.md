# 🎵 Relatório Final de Aplicação de Técnica de Análise – Análise de Dados do Spotify

### 📌 Objetivo

Este estudo tem como objetivo identificar os principais fatores que influenciam o sucesso de músicas no Spotify, medido pelo número de streams. A análise visa validar hipóteses formuladas previamente pela gravadora e, a partir disso, fornecer recomendações estratégicas para orientar o lançamento de um novo artista.

### 📌 Metodologia e Ferramentas Utilizadas

A análise foi conduzida com base em variáveis internas às plataformas de streaming, como:

- Características musicais (BPM, danceability, energy, etc.);

- Presença em playlists (editoriais e algorítmicas);

- Número de faixas publicadas por artista;

- Volume de streams em Spotify e outras plataformas digitais (Apple Music, Deezer, Shazam).

Variáveis externas ao ambiente digital — como investimentos em marketing, campanhas promocionais, clipes no YouTube ou engajamento em redes sociais — não foram consideradas, devido à ausência de dados estruturados e padronizados. Com isso, a análise se concentrou exclusivamente em fatores objetivos e mensuráveis dentro do ecossistema digital.

### 🔍 Etapas Analíticas Realizadas:

- Análise exploratória de dados (EDA);

- Segmentação por quartis e agrupamentos;

- Cálculo de correlações estatísticas (Spearman e Pearson);

- Testes de significância (Mann-Whitney U);

- Criação de visualizações interativas para análise comparativa.

### 🛠️ Ferramentas Utilizadas:

- Google BigQuery – Extração, limpeza e estruturação dos dados;

- Python (Google Colab) – Análises estatísticas, testes de hipótese e modelagem;

- Power BI – Visualizações, dashboards e geração de insights interativos.

### 🎧 Hipótese 1: Músicas com BPM mais altos fazem mais sucesso em termos de número de streams.

📊 Gráficos utilizados: Dispersão (BPM vs Streams), boxplot por quartis de BPM

✅ Resultado:

- Correlação Spearman: -0.0024, p = 0.9436

- Correlação Pearson: 0.0049, p = 0.8854

- Teste Mann-Whitney (Q1 vs Q4): p = 0.5043

📌 Conclusão: **Hipótese refutada** BPM não tem relação significativa com o número de streams.
📌 Interpretação: O BPM isoladamente não influencia o sucesso de uma faixa. Músicas com diferentes BPMs podem ter alto ou baixo desempenho.

### 🎧 Hipótese 2: As músicas mais populares no Spotify também possuem comportamento semelhante em outras plataformas (Apple, Deezer).

📊 Gráficos utilizados: Heatmap de correlação, dispersão entre plataformas, análise de regressão linear cruzada

✅ Resultado: 

| Plataforma  | Correlação com Spotify (Spearman) | R² (Regressão Linear) | p-valor  |
| ----------- | --------------------------------- | --------------------- | -------- |
| Apple Music | **0.3312**                        | **0.1087**            | < 0.0001 |
| Deezer      | **0.2376**                        | **0.0557**            | < 0.0001 |
| Shazam      | **0.1215**                        | **0.0148**            | 0.0002   |


📌 Conclusão: **Hipótese parcialmente validada** Correlação moderada com Apple Music, fraca com Deezer e muito baixa com Shazam.
📌 Interpretação: Apple Music e Deezer seguem um padrão próximo ao Spotify, mas Shazam reflete mais momentos pontuais de descoberta do que popularidade sustentada.

### 🎧 Hipótese 3: A presença em maior número de playlists está correlacionada com um maior número de streams.

📊 Gráficos utilizados: Dispersão (Playlists x Streams), boxplots por faixas de inserção em playlists

✅ Resultado: 

- Correlação Spearman (Spotify playlists): 0.836, p < 0.0001

- Correlação Spearman (Total playlists): 0.837, p < 0.0001

- Correlação Pearson (Total playlists x log(streams)): 0.621, p < 0.0001

- Músicas em +5.000 playlists: média 1,13 bi streams

- Músicas em <500 playlists: média 22 mi streams

📌 Conclusão: **Hipótese fortemente validada** A inserção em playlists é o fator isolado mais fortemente correlacionado ao sucesso de uma música.
📌 Interpretação: A inserção em playlists é o fator mais fortemente relacionado ao sucesso. Curadoria editorial e algoritmos (e.g. Discover Weekly, Today's Top Hits) amplificam o alcance de forma exponencial.

### 🎧 Hipótese 4: Artistas com mais músicas no Spotify têm mais streams.

📊 Gráficos utilizados: Dispersão (número de músicas por artista x streams totais), ranking de artistas

✅ Resultado:

- Correlação Spearman: 0.428, p < 0.0001

- Correlação Pearson: 0.382, p < 0.0001

- Artistas com >200 músicas: média 3,1 bilhões de streams

- Artistas com <20 músicas: média 380 milhões de streams

📌 Conclusão: **A hipótese é validada** Existe uma relação clara, embora não absoluta, entre volume de catálogo e total de streams.
📌 Interpretação: Um catálogo maior favorece o acúmulo de streams via presença contínua em playlists, efeito de cauda longa e redescoberta de faixas antigas.

### 🎧 Hipótese 5: As características musicais influenciam o sucesso em termos de streams.

📊 Gráficos utilizados: Matriz de correlação, regressão multivariada, teste de diferença entre grupos

✅ Resultado: 

| Característica   | Correlação Spearman | p-valor | Diferença Significativa (Grupos) |
| ---------------- | ------------------- | ------- | -------------------------------- |
| Danceability     | -0.083              | 0.0156  | Não (p = 0.1308)                 |
| Energy           | -0.029              | 0.4046  | Não                              |
| Valence          | -0.047              | 0.1725  | Não                              |
| Acousticness     | -0.048              | 0.1612  | Não                              |
| Instrumentalness | -0.014              | 0.6863  | Não                              |
| Liveness         | -0.071              | 0.0383  | Marginalmente                    |
| Speechiness      | -0.108              | 0.0016  | Sim (fraca)                      |

📌 Conclusão: **Hipótese refutada** As correlações são fracas e inconsistentes.
📌 Interpretação: O sucesso de uma faixa não é explicado por variáveis musicais isoladas. Fatores como marketing, redes sociais e curadoria têm impacto muito maior.

### 📈 Análises Adicionais

🎯 Concentração de Mercado

- Top 10% das músicas concentram 36,9% dos streams

- Top 1% concentram 5,4% dos streams

📌 O mercado é altamente concentrado, embora menos extremo do que sugerido anteriormente. Um pequeno grupo de faixas domina a atenção.

### Análise Temporal (2016–2025):

- Volume total de streams cresceu +384% desde 2016

- BPM médio aumentou de 104 → 114

- Danceability médio subiu de 0.61 → 0.68

- Músicas estão ficando mais curtas, mais dançantes e mais energéticas, refletindo o consumo em plataformas como TikTok.


## 🎯 Conclusões Estratégicas para a Gravadora

1. Foco em playlists: Investir em curadoria editorial e relacionamento com curadores é a principal alavanca para gerar tração. Playlists são o maior diferencial competitivo.

2. Qualidade e quantidade: Um catálogo extenso ajuda, mas o sucesso real vem de faixas com forte impacto individual. Trabalhar a narrativa e o lançamento de singles com alto potencial de engajamento.

3. Características musicais como tendência, não regra: Danceability e energy são tendências crescentes, mas não garantem sucesso por si só. Apostar em autenticidade sonora e testes A/B com o público pode ser mais eficaz.

4. Presença multi-plataforma: Apesar da dominância do Spotify, manter estratégia cross-plataforma (Apple Music, Deezer) é fundamental para diversificação de receita e público.

5. Apostar em colaborações: O efeito de cross-fanbase é comprovado. Lançamentos com artistas já consolidados ampliam alcance inicial, elevando a probabilidade de inserção em playlists e viralização.
