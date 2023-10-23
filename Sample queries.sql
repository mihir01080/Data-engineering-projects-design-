-- Retrieve the top 10 tracks on Spotify by chart position:
SELECT
    t.track_name,
    s.spotify_chart_value
FROM
    Track AS t
JOIN
    SpotifyChartEntries AS sce ON t.track_id = sce.track_id
JOIN
    Spotify_Chart AS s ON s.spotify_chart_id = sce.spotify_chart_id
ORDER BY
    s.spotify_chart_value DESC
LIMIT 10;

--Find the artists with the most charted tracks on Spotify:
SELECT
    a.artist_name,
    COUNT(sce.artist_id) AS num_charted_tracks
FROM
    artists AS a
JOIN
    SpotifyChartEntries AS sce ON a.artist_id = sce.artist_id
GROUP BY
    a.artist_name
ORDER BY
    num_charted_tracks DESC
LIMIT 10;
--Retrieve the average danceability, valence, and energy percentages of tracks on Spotify
SELECT
    AVG(taf.danceability_percent) AS avg_danceability,
    AVG(taf.valence_percent) AS avg_valence,
    AVG(taf.energy_percent) AS avg_energy
FROM
    Track_Audio_Features AS taf;
	
-- Find the tracks with the highest acousticness percentages:
SELECT
    t.track_name,
    taf.acousticness_percent
FROM
    Track AS t
JOIN
    Track_Audio_Features AS taf ON t.track_id = taf.track_artist_id
ORDER BY
    taf.acousticness_percent DESC
LIMIT 10;

-- Retrieve the tracks that were streamed the most on Apple Music:
SELECT
    t.track_name,
    s.streams
FROM
    Track AS t
JOIN
    Stream AS s ON t.track_id = s.track_id
WHERE
    s.apple_chart_id IS NOT NULL
ORDER BY
    s.streams DESC
LIMIT 10;

-- Get the most popular tracks on Deezer:
SELECT
    t.track_name,
    D.deezer_chart_value
FROM
    Track AS t
JOIN
   DeezerChartEntries AS dce ON t.track_id = dce.track_id
JOIN
    Deezer_Chart AS D ON D.Deezer_chart_id = dce.Deezer_chart_id
WHERE
    D.Deezer_chart_value IS NOT NULL
ORDER BY
    D.Deezer_chart_value DESC
LIMIT 10;
