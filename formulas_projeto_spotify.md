# 📊 Fórmulas Utilizadas – Para analisar dados do Spotify

Este documento contém as principais fórmulas e cálculos utilizados no Projeto 2 da Jornada de Dados da Laboratória, que envolveu a análise de dados musicais do Spotify.


### 📍 Identificar e tratar valores nulos

- 🔍 Análise de Valores Nulos na Tabela **track_in_competition**

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

- 🔍 Análise de Valores Nulos na Tabela **track_in_spotify**

```
 SELECT
  COUNT(*) AS total_linhas,
  COUNTIF(track_id IS NULL) AS nulos_track_id,
  COUNTIF(track_name IS NULL) AS nulos_track_name,
  COUNTIF(artist_s__name IS NULL) AS nulos_artists_name,
  COUNTIF(artist_count IS NULL) AS nulos_artist_count,
  COUNTIF(released_year IS NULL) AS nulos_released_year,
  COUNTIF(released_month IS NULL) AS nulos_released_month,
  COUNTIF(released_day IS NULL) AS nulos_released_day,
  COUNTIF(in_spotify_playlists IS NULL) AS nulos_in_spotify_playlists,
  COUNTIF(in_spotify_charts IS NULL) AS nulos_in_spotify_charts,
  COUNTIF(streams IS NULL) AS nulos_streams
 FROM `spotify-analysis-465623.spotify_data.track_in_spotify`
```

- 🔍 Análise de Valores Nulos na Tabela **track_technical**

```
 SELECT 
   COUNT(*) AS total_linhas,
   COUNTIF(track_id IS NULL) AS nulos_track_id,
   COUNTIF(bpm IS NULL) AS nulos_bpm,
   COUNTIF(key IS NULL) AS nulos_key,
   COUNTIF(mode IS NULL) AS nulos_mode,
   COUNTIF('danceability_%' IS NULL) AS nulos_danceability,
   COUNTIF('valence_%' IS NULL) AS nulos_valence,
   COUNTIF('energy_%' IS NULL) AS nulos_energy,
   COUNTIF('acousticness_%' IS NULL) AS nulos_acousticness,
   COUNTIF('instrumentalness_%' IS NULL) AS nulos_instrumentalness,
   COUNTIF('liveness_%' IS NULL) AS nulos_liveness,
   COUNTIF('speechiness_%' IS NULL) AS nulos_speechiness
 FROM `spotify-analysis-465623.spotify_data.track_technical`
```

- 🔍  Visualização de Registros com NULL **track_in_competition**.

```
SELECT
*
 FROM `spotify-analysis-465623.spotify_data.track_in_competition`
 where
 in_shazam_charts 
 is null
```

- 🔍 visualizar as células com o valor NULL **track_in_technical**.

```
 SELECT 
 *
 FROM `spotify-analysis-465623.spotify_data.track_technical`
 where
 key
 is null
```

### 📍Identificar e tratar valores duplicados

- Detecção de registros duplicados por nome da música e artista:

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
- Visualização de duplicatas específicas (ex: Rosa Linn): 

```
SELECT
*
FROM `spotify-analysis-465623.spotify_data.track_in_spotify`
WHERE
artist_s__name = 'Rosa Linn'
```