# Data-engineering-projects-design-
Project Name: Spotify Music Database Design

Description:

This project showcases the design and implementation of a relational database model to store and manage Spotify music data. 
The goal of this project is to demonstrate database design skills and practice creating a database from scratch. 
The database includes tables for artists, tracks, audio features, release information, various music charts (e.g., Spotify, Apple Music, Shazam, Deezer), and their associated entries.


Table Structure:

The database includes the following tables:

Artists: Stores information about music artists.
Tracks: Stores information about music tracks.
Track_Artist: Establishes a many-to-many relationship between tracks and artists.
Track_Audio_Features: Stores audio features data for each track.
Track_Release_Info: Stores information about the release date of tracks.
Shazam_Chart: Stores Shazam chart data.
ShazamChartEntries: Stores entries for tracks in the Shazam chart.
Spotify_Chart: Stores Spotify chart data.
SpotifyChartEntries: Stores entries for tracks in the Spotify chart.
Apple_Chart: Stores Apple Music chart data.
AppleChartEntries: Stores entries for tracks in the Apple Music chart.
Deezer_Chart: Stores Deezer chart data.
DeezerChartEntries: Stores entries for tracks in the Deezer chart.
Stream: Stores streaming data for tracks across different platforms.
How to Use:

Ensure you have PostgreSQL installed and running on your local machine.
Create a PostgreSQL database with the name "myfirstdb."
Update the database connection parameters in the code with your PostgreSQL credentials.
Run the Python script to create the database and tables, as well as populate them with data from a CSV file.
The dataset was found in Kaggle. The CSV file should contain the necessary data for artists, tracks, and chart-related information.
The code includes SQL statements to create the tables and relationships between them.

Normalization notes: 
First Normal Form (1NF): This level of normalization has been achieved. Each table contains only atomic (indivisible) values, and there are no repeating groups. 
For example, the "Artists" and "Tracks" tables have fields like artist_name, artist_count, and track_name, each containing atomic values.

Second Normal Form (2NF): You have achieved 2NF by ensuring that all non-key attributes are fully functionally dependent on the primary key. 
For instance, the "Track_Release_Info" table has a composite primary key (track_id, released_year, released_month, released_day), and all other attributes are functionally dependent on this key.

Third Normal Form (3NF): Your design complies with 3NF by eliminating transitive dependencies. For example, in the "Track_Audio_Features" table, attributes like bpm, key, mode, danceability_percent, valence_percent, energy_percent, etc., are all directly dependent on the primary key (track_artist_id).
