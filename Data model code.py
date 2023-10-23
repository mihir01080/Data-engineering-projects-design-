import pandas as pd
import psycopg2

df = pd.read_csv("spotify_data.csv", encoding = "latin1")


#Create connection to database

conn = psycopg2.connect("host = 127.0.0.1 dbname =postgres user=postgres password = Padmaja!972")

#Use the connection to get a cursor that can be used to execute queries
cur = conn.cursor()
#Set automatic commit to be true so each action is automatically comitted without calling conn.commit()
conn.set_session(autocommit=True)


cur.execute("DROP database myfirstdb")
cur.execute("CREATE database myfirstdb")

#Close connection
conn.close()

#Create connection to database
conn = psycopg2.connect("host = 127.0.0.1 dbname = myfirstdb user=postgres password = Padmaja!972")
#Use the connection to get a cursor that can be used to execute queries
cur = conn.cursor()
#Set automatic commit to be true so each action is automatically comitted without calling conn.commit()
conn.set_session(autocommit=True)


# Create Artist Table
create_artist_table = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id serial PRIMARY KEY,
    artist_name text,
    artist_count integer
)
""")

# Create Track Table
create_track_table = ("""
CREATE TABLE IF NOT EXISTS Track (
    track_id serial PRIMARY KEY,
    track_name text
)
""")



# Create Track_Artist Table
create_track_artist_table = ("""
CREATE TABLE IF NOT EXISTS Track_Artist (
    track_artist_id serial PRIMARY KEY,
    track_id INT,
    artist_id INT,
    FOREIGN KEY (track_id) REFERENCES Track (track_id),
    FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
)
""")

# Create Track_Audio_Features Table
create_track_audio_features_table = ("""
CREATE TABLE IF NOT EXISTS Track_Audio_Features (
    track_artist_id INT,    
    bpm integer,
    key TEXT,
    mode TEXT,
    danceability_percent integer,
    valence_percent integer,
    energy_percent integer,
    acousticness_percent integer,
    instrumentalness_percent integer,
    liveness_percent integer,
    speechiness_percent integer,
    FOREIGN KEY (track_artist_id) REFERENCES Track_Artist (track_artist_id)
    )
""")

# Create Track_Release_Info Table
create_track_release_info_table = ("""
CREATE TABLE IF NOT EXISTS Track_Release_Info (
    track_id INT, 
    released_year integer,
    CHECK (released_year >= 1000 AND released_year <= 9999),
    released_month integer,
    CHECK (released_month >= 1 AND released_month <= 12),
    released_day integer,
    CHECK (released_day >=1 AND released_day <=31),
    FOREIGN KEY (track_id) REFERENCES Track (track_id)
    )
""")

# Create Shazam_Chart Table
create_shazam_chart_table = ("""
CREATE TABLE IF NOT EXISTS Shazam_Chart (
    shazam_chart_id serial PRIMARY KEY,
    shazam_chart_value numeric,
    shazam_playlist_value integer
)
""")

# Create ShazamChartEntries Table (to store tracks in a Shazam chart along with positions)
create_shazam_chart_entries_table = ("""
CREATE TABLE IF NOT EXISTS ShazamChartEntries (
    shazam_entry_id serial PRIMARY KEY,
    artist_id integer,
    shazam_chart_id integer,
    track_id integer,
    FOREIGN KEY (shazam_chart_id) REFERENCES Shazam_Chart (shazam_chart_id),
    FOREIGN KEY (track_id) REFERENCES Track (track_id),
    FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
)
""")

# Create Spotify Chart Table
create_spotify_chart_table = ("""
CREATE TABLE IF NOT EXISTS Spotify_Chart (
    spotify_chart_id serial PRIMARY KEY,
    spotify_chart_value integer,
    spotify_playlist_value integer
)
""")

# Create SpotifyChartEntries Table (to store tracks in a Spotify chart along with positions)
create_spotify_chart_entries_table = ("""
CREATE TABLE IF NOT EXISTS SpotifyChartEntries (
    spotify_entry_id serial PRIMARY KEY,
    artist_id integer,
    spotify_chart_id integer,
    track_id integer,
    FOREIGN KEY (spotify_chart_id) REFERENCES Spotify_Chart (spotify_chart_id),
    FOREIGN KEY (track_id) REFERENCES Track (track_id),
    FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
)
""")


# Create Apple Chart Table
create_apple_chart_table = ("""
CREATE TABLE IF NOT EXISTS Apple_Chart (
    apple_chart_id serial PRIMARY KEY,
    apple_chart_value integer,
    apple_playlist_value integer
)
""")

# Create AppleChartEntries Table (to store tracks in an Apple chart along with positions)
create_apple_chart_entries_table = ("""
CREATE TABLE IF NOT EXISTS AppleChartEntries (
    apple_entry_id serial PRIMARY KEY,
    artist_id integer,
    apple_chart_id integer,
    track_id integer,
    FOREIGN KEY (apple_chart_id) REFERENCES Apple_Chart (apple_chart_id),
    FOREIGN KEY (track_id) REFERENCES Track (track_id),
    FOREIGN KEY (artist_id) REFERENCES artists (artist_id)

)
""")

# Create Deezer Chart Table
create_deezer_chart_table = ("""
CREATE TABLE IF NOT EXISTS Deezer_Chart (
    deezer_chart_id serial PRIMARY KEY,
    deezer_chart_value numeric,
    deezer_playlist_value integer
)
""")

# Create DeezerChartEntries Table (to store tracks in a Deezer chart along with positions)
create_deezer_chart_entries_table = ("""
CREATE TABLE IF NOT EXISTS DeezerChartEntries (
    deezer_entry_id serial PRIMARY KEY,
    artist_id integer,
    deezer_chart_id integer,
    track_id integer,
    FOREIGN KEY (deezer_chart_id) REFERENCES Deezer_Chart (deezer_chart_id),
    FOREIGN KEY (track_id) REFERENCES Track (track_id),
    FOREIGN KEY (artist_id) REFERENCES artists (artist_id)

)
""")

# Create Stream Table
create_stream_table = ("""
CREATE TABLE IF NOT EXISTS Stream (
    stream_id serial PRIMARY KEY,
    track_id integer,
    shazam_chart_id integer,
    apple_chart_id integer,
    deezer_chart_id integer,
    spotify_chart_id integer,
    streams numeric,
    FOREIGN KEY (track_id) REFERENCES Track (track_id),
    FOREIGN KEY (shazam_chart_id) REFERENCES Shazam_Chart (shazam_chart_id),
    FOREIGN KEY (apple_chart_id) REFERENCES Apple_Chart (apple_chart_id),
    FOREIGN KEY (deezer_chart_id) REFERENCES Deezer_Chart (deezer_chart_id),
    FOREIGN KEY (spotify_chart_id) REFERENCES Spotify_Chart (spotify_chart_id)

)
""")






#Execute code to create tables:
    
try:
    cur.execute(create_artist_table)
    cur.execute(create_track_table)
    cur.execute(create_track_artist_table)
    cur.execute(create_shazam_chart_table)
    cur.execute(create_shazam_chart_entries_table)
    cur.execute(create_apple_chart_table)
    cur.execute(create_apple_chart_entries_table)
    cur.execute(create_deezer_chart_table)
    cur.execute(create_deezer_chart_entries_table)
    cur.execute(create_spotify_chart_table)
    cur.execute(create_spotify_chart_entries_table)
    cur.execute(create_stream_table)
    cur.execute(create_track_audio_features_table)
    cur.execute(create_track_release_info_table)
    conn.commit()
    
except psycopg2.Error as e:
    print("Error creating tables")
    print(e)
    #conn.rollback()

#Create blank lists which will be inserted into the tables as columns
artist_name = []
artist_count = []
track_name = []
spotify_chart_value = []
apple_chart_value = []
deezer_chart_value = []
shazam_chart_value = []
spotify_playlist_value = []
apple_playlist_value = []
shazam_playlist_value= []
deezer_playlist_value = []
danceability_percent = []
valence_percent = [] 
energy_percent = [] 
acousticness_percent = [] 
instrumentalness_percent = []
liveness_percent = [] 
speechiness_percent = []
bpm = [] 
key = []
mode = []
released_year = []
released_month = []
released_day = []
streams = []
#Insert data into tables 
artists_insert = ("""INSERT INTO artists(
    artist_name,
    artist_count)
    VALUES (%s, %s)
    """)
    
track_insert = ("""INSERT INTO Track(
    track_name)
    VALUES (%s)
    """)
    
spotify_insert = ("""INSERT INTO Spotify_Chart(
    spotify_chart_value,
    spotify_playlist_value)
    VALUES (%s, %s)
    """)

apple_insert = ("""INSERT INTO Apple_Chart(
    apple_chart_value,
    apple_playlist_value)
    VALUES (%s, %s)
    """)
    
shazam_insert = ("""INSERT INTO Shazam_Chart(
    shazam_chart_value,
    shazam_playlist_value)
    VALUES (%s, %s)
    """)
    
deezer_insert = ("""INSERT INTO Deezer_Chart(
    deezer_chart_value,
    deezer_playlist_value)
    VALUES (%s, %s)
    """)
    
insert_audio_features = ("""INSERT INTO Track_Audio_Features (
    track_artist_id, bpm, key, mode,
   danceability_percent, valence_percent, energy_percent, acousticness_percent,
   instrumentalness_percent, liveness_percent, speechiness_percent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

insert_track_release_info = ("""INSERT INTO Track_Release_Info(
    track_id, released_year, released_month, released_day)
    VALUES (%s, %s, %s, %s)
    
                             
""")

shazam_chart_entries_insert = ("""
INSERT INTO ShazamChartEntries (artist_id, shazam_chart_id, track_id)
VALUES (%s, %s, %s)
""")

deezer_chart_entries_insert = ("""
INSERT INTO DeezerChartEntries (artist_id, deezer_chart_id, track_id)
VALUES (%s, %s, %s)
""")

apple_chart_entries_insert = ("""
INSERT INTO AppleChartEntries (artist_id, apple_chart_id, track_id)
VALUES (%s, %s, %s)
""")

spotify_chart_entries_insert = ("""
INSERT INTO SpotifyChartEntries (artist_id, spotify_chart_id, track_id)
VALUES (%s, %s, %s)
""")

stream_insert = ("""
INSERT INTO Stream (track_id, shazam_chart_id, apple_chart_id, deezer_chart_id, spotify_chart_id, streams)
VALUES (%s, %s, %s, %s, %s, %s)
""")



#Use csv files to insert each row
for index, row in df.iterrows():
    artist_name1 = row["artist(s)_name"]
    artist_name.append(artist_name1) 
    artist_count1 = row["artist_count"]
    artist_count.append(artist_count1)
    track_name1 = row["track_name"]
    track_name.append(track_name1)
    spotify_chart_value1 = row["in_spotify_charts"]
    spotify_chart_value.append(spotify_chart_value1)
    spotify_playlist_value1 = row["in_spotify_playlists"]
    spotify_playlist_value.append(spotify_playlist_value1)
    apple_chart_value1 = row["in_apple_charts"]
    apple_chart_value.append(apple_chart_value1)
    apple_playlist_value1 = row["in_apple_playlists"]
    apple_playlist_value.append(apple_playlist_value1)
    shazam_chart_value1 = row["in_shazam_charts"]
    shazam_chart_value.append(shazam_chart_value1)
    shazam_playlist_value1 = row["in_shazam_playlists"]
    shazam_playlist_value.append(shazam_playlist_value1)
    deezer_chart_value1 = row["in_deezer_charts"]
    deezer_chart_value.append(deezer_chart_value1)
    deezer_playlist_value1 = row["in_deezer_playlists"]
    deezer_playlist_value.append(deezer_playlist_value1)
    danceability_percent1 =row["danceability_%"]
    danceability_percent.append(danceability_percent1)
    valence_percent1 =row["valence_%"]
    valence_percent.append(valence_percent1)
    energy_percent1 =row["energy_%"]
    energy_percent.append(energy_percent1)
    bpm_value1 =row["bpm"]
    bpm.append(bpm_value1)
    acousticness_percent1 = row["acousticness_%"]
    acousticness_percent.append(acousticness_percent1)
    key_value1 = row["key"]
    key.append(key_value1)
    instrumentalness_percent1 = row["instrumentalness_%"]
    instrumentalness_percent.append(instrumentalness_percent1)
    mode_value1 = row["mode"]
    mode.append(mode_value1)
    liveness_percent1 = row["liveness_%"]
    liveness_percent.append(liveness_percent1)
    speechiness_percent1 = row["speechiness_%"]
    speechiness_percent.append(speechiness_percent1)
    released_year1 = row["released_year"]
    released_year.append(released_year1)
    released_month1 = row["released_month"]
    released_month.append(released_month1)
    released_day1 = row["released_day"]
    released_day.append(released_day1)
    stream1 = row["streams"]
    streams.append(stream1)
    
# Insert data into the tables
for i in range(len(artist_name)):
    cur.execute(spotify_insert, (spotify_chart_value[i], spotify_playlist_value[i]))
    cur.execute(apple_insert, (apple_chart_value[i], apple_playlist_value[i]))
    cur.execute(shazam_insert, (shazam_chart_value[i], shazam_playlist_value[i]))
    cur.execute(deezer_insert, (deezer_chart_value[i], deezer_playlist_value[i]))
   
    conn.commit()  # Commit the changes
    
    # Execute the SQL to insert into the artists and Track tables
    cur.execute(artists_insert, (artist_name[i], artist_count[i]))
    cur.execute(track_insert, (track_name[i],))

    # Commit the changes for artists and Track tables
    conn.commit()


    # Retrieve the artist_id and track_id that were generated during the insertions
    cur.execute("SELECT artist_id FROM artists WHERE artist_name = %s", (artist_name[i],))
    artist_id = cur.fetchone()[0]

    cur.execute("SELECT track_id FROM Track WHERE track_name = %s", (track_name[i],))
    track_id = cur.fetchone()[0]

    # Insert data into the Track_Artist table to establish the relationship
    cur.execute("INSERT INTO Track_Artist (track_id, artist_id) VALUES (%s, %s)", (track_id, artist_id))
   
    conn.commit()
    
    
     # Now, execute the SQL to retrieve the newly inserted track_artist_id
    cur.execute("SELECT track_artist_id FROM Track_Artist WHERE track_id = %s AND artist_id = %s", (track_id, artist_id))
    track_artist_id = cur.fetchone()[0]
    #print("Retrieved track_artist_id:", track_artist_id)  # Debug print
    # Insert data into the Track_Audio_Features table using the retrieved track_artist_id
    cur.execute(insert_audio_features, (track_artist_id, bpm[i], key[i], mode[i], danceability_percent[i], valence_percent[i], energy_percent[i], acousticness_percent[i], instrumentalness_percent[i], liveness_percent[i], speechiness_percent[i]))
 
    conn.commit()  # Commit the changes
    
    
    
    # Insert data into the Track_Release_Info table using the retrieved track_id
    cur.execute(insert_track_release_info, (track_id, released_year[i], released_month[i], released_day[i]))

    conn.commit()  # Commit the changes    
    
    # Retrieve the shazam_chart_id/deezer/apple/spotify that was generated during the insertion
    cur.execute("SELECT shazam_chart_id FROM Shazam_Chart WHERE shazam_chart_value = %s", (shazam_chart_value[i],))
    shazam_chart_id = cur.fetchone()[0]
    cur.execute("SELECT deezer_chart_id FROM Deezer_Chart WHERE deezer_chart_value = %s", (deezer_chart_value[i],))
    deezer_chart_id = cur.fetchone()[0]
    cur.execute("SELECT apple_chart_id FROM Apple_Chart WHERE apple_chart_value = %s", (apple_chart_value[i],))
    apple_chart_id = cur.fetchone()[0]
    cur.execute("SELECT spotify_chart_id FROM Spotify_Chart WHERE spotify_chart_value = %s", (spotify_chart_value[i],))
    spotify_chart_id = cur.fetchone()[0]
    
    # Insert data into the ShazamChartEntries/deeezer/apple/spotify table to establish the relationship
    cur.execute(shazam_chart_entries_insert, (artist_id, shazam_chart_id, track_id))
    cur.execute(deezer_chart_entries_insert, (artist_id, deezer_chart_id, track_id))
    cur.execute(apple_chart_entries_insert, (artist_id, apple_chart_id, track_id))
    cur.execute(spotify_chart_entries_insert, (artist_id, spotify_chart_id, track_id))
    
    #Insert data into Stream table
    cur.execute(stream_insert, (track_id, shazam_chart_id, apple_chart_id, deezer_chart_id, spotify_chart_id, streams[i]))

    conn.commit()
    
# Commit the changes
conn.commit()



# # Perform a SELECT query to retrieve data from table
# cur.execute("SELECT * FROM track_audio_features limit 5")

# # Fetch all the rows from the result set
# rows = cur.fetchall()

# # Create a DataFrame to display the results
# columns = [desc[0] for desc in cur.description]
# df2 = pd.DataFrame(rows, columns=columns)

# # Display the DataFrame
# print(df2)

# Close the connection
conn.close()



