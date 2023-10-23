select track.track_name, artists.artist_name from track inner join track_artist on track.track_id = track_artist.track_id inner join artists on track_artist.artist_id = artists.artist_id limit 5;


select features.danceability_percent, track.track_name from track_audio_features as features inner join track_artist as tr on features.track_artist_id = tr.track_artist_id inner join track on tr.track_id = track.track_id order by features.danceability_percent DESC limit 50;

