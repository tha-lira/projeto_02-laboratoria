# 🎵 Relatório Final de Aplicação de Técnica de Análise – Análise de Dados do Spotify

## 📌 Objetivo

Avaliar quais fatores influenciam o sucesso de músicas no Spotify (streams), validando hipóteses levantadas pela gravadora e fornecendo recomendações estratégicas para o lançamento de um novo artista.

## 📌 Metodologia e Ferramentas Utilizadas

Esta análise foi realizada com base em variáveis objetivas disponíveis nas plataformas de streaming (como características musicais, presença em playlists, número de faixas e volume de streams). Variáveis externas ao ambiente digital, como investimentos em marketing, presença em redes sociais, clipes no YouTube ou campanhas promocionais, não foram consideradas, devido à indisponibilidade de dados padronizados. Portanto, o foco da análise está na relação entre atributos musicais e a performance nas plataformas de streaming.

### 🎧 Hipótese 1: Músicas com BPM mais altos fazem mais sucesso em termos de número de streams.

📊 Gráficos utilizados: Dispersão (BPM vs Streams), boxplot por quartis de BPM

✅ Resultado:

- Correlação de Spearman = -0.0024, p-valor = 0.9436

- Quartis de BPM (Q1: <90, Q2: 90-110, Q3: 110-130, Q4: >130) não apresentaram diferenças significativas nos streams médios (Mann-Whitney U p > 0.1)

📌 Conclusão: Não há relação estatisticamente significativa entre BPM e número de streams. A hipótese é refutada com os dados atuais.

👉 Interpretação: O BPM isoladamente não determina o sucesso da faixa; há grande variação de streams em todos os intervalos de BPM.

### 🎧 Hipótese 2: As músicas mais populares no Spotify também possuem comportamento semelhante em outras plataformas (Apple, Deezer).

📊 Gráficos utilizados: Heatmap de correlação, dispersão entre plataformas, análise de regressão linear cruzada

✅ Resultado: 

| Plataforma  | Correlação com Spotify (Spearman) | R² (Regressão Linear) | p-valor  |
| ----------- | --------------------------------- | --------------------- | -------- |
| Apple Music | **0.3312**                        | **0.1087**            | < 0.0001 |
| Deezer      | **0.2376**                        | **0.0557**            | < 0.0001 |
| Shazam      | **0.1215**                        | **0.0148**            | 0.0002   |


📌 Conclusão: Existe correlação moderada entre Spotify e Apple Music, e fraca com Deezer. Com Shazam, a correlação é muito baixa. A hipótese é parcialmente validada.

👉 Interpretação: Apple e Deezer seguem um padrão similar de consumo. Já o Shazam é mais usado para descoberta de músicas (momento de escuta pontual), não refletindo necessariamente sucesso em volume de streams.

### 🎧 Hipótese 3: A presença em maior número de playlists está correlacionada com um maior número de streams.

📊 Gráficos utilizados: Dispersão (Playlists x Streams), boxplots por faixas de inserção em playlists

✅ Resultado: 

- Correlação Spearman (Spotify playlists x Streams): 0.836, p < 0.0001

- Correlação Spearman (Total playlists x Streams): 0.837, p < 0.0001

- Músicas em +5.000 playlists: média de 1.134.000.000 streams

- Músicas com menos de 500 playlists: média de 22.000.000 streams

📌 Conclusão: Hipótese fortemente validada. A inserção em playlists é o fator isolado mais fortemente correlacionado ao sucesso de uma música.

👉 Interpretação: Algoritmos de recomendação e curadoria editorial possuem poder direto de amplificação. Atingir a recomendação automática do Spotify (e.g., Discover Weekly, Today's Top Hits) pode multiplicar os streams em escala exponencial.

### 🎧 Hipótese 4: Artistas com mais músicas no Spotify têm mais streams.

📊 Gráficos utilizados: Dispersão (número de músicas por artista x streams totais), ranking de artistas

✅ Resultado:

- Correlação Spearman: 0.428, p-valor < 0.0001

- Artistas com mais de 200 músicas: stream médio total = 3,1 bilhões

- Artistas com menos de 20 músicas: stream médio total = 380 milhões

📌 Conclusão: A hipótese é validada. Existe uma relação clara, embora não absoluta, entre volume de catálogo e total de streams.

👉 Interpretação: Artistas com catálogos extensos tendem a acumular mais streams devido à presença recorrente em playlists, efeito de catálogo e potencial de viralização de faixas antigas.

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
| Speechiness      | -0.108              | 0.0016  | Sim (mas fraca)                  |

📌 Conclusão: As correlações são baixas e negativas. Nenhuma característica isolada explica de forma significativa o sucesso. A hipótese é refutada em termos absolutos.

👉 Interpretação: O sucesso de uma faixa depende menos da composição musical objetiva e mais de fatores como campanhas, marketing, engajamento social e inserção em playlists.

### 📈 Análises Adicionais

- Concentração de mercado:

Top 10% das músicas = 70,3% dos streams

Top 1% = 41,6% dos streams

📌 O mercado é altamente desigual e concentrado. Um pequeno número de músicas/nomes dominam a atenção.

- Análise Temporal (2016–2025):

Volume total de streams cresceu 384% entre 2016 e 2024.

Desde 2021, a média de danceability passou de 0.61 para 0.68, e o BPM médio aumentou de 104 para 114.

Músicas mais recentes tendem a ser mais curtas, dançantes e energéticas, refletindo as exigências do consumo digital e redes sociais (e.g., TikTok).

### 🎯 Conclusões Estratégicas para a Gravadora

1. Foco em playlists: Investir em curadoria editorial e relacionamento com curadores é a principal alavanca para gerar tração. Playlists são o maior diferencial competitivo.

2. Qualidade e quantidade: Um catálogo extenso ajuda, mas o sucesso real vem de faixas com forte impacto individual. Trabalhar a narrativa e o lançamento de singles com alto potencial de engajamento.

3. Características musicais como tendência, não regra: Danceability e energy são tendências crescentes, mas não garantem sucesso por si só. Apostar em autenticidade sonora e testes A/B com o público pode ser mais eficaz.

4. Presença multi-plataforma: Apesar da dominância do Spotify, manter estratégia cross-plataforma (Apple Music, Deezer) é fundamental para diversificação de receita e público.

5. Apostar em colaborações: O efeito de cross-fanbase é comprovado. Lançamentos com artistas já consolidados ampliam alcance inicial, elevando a probabilidade de inserção em playlists e viralização.