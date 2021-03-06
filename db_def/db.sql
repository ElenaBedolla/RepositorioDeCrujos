CREATE TABLE EARTHQUAKE(
    id INT UNSIGNED PRIMARY KEY,
    date_time DATETIME NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    depth FLOAT NOT NULL,
    magnitude FLOAT NOT NULL)
    
CREATE TABLE STATION(
    symbol VARCHAR(10) PRIMARY KEY,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    elevation FLOAT NOT NULL)
    
CREATE TABLE CHANNEL(
    symbol CHAR(3) NOT NULL,
    station VARCHAR(10) NOT NULL,
    FOREIGN KEY(station) REFERENCES STATION(symbol),
    PRIMARY KEY(symbol,station))
    
CREATE TABLE CHANNEL_EARTHQUAKE(
    station VARCHAR(10) NOT NULL,
    channel CHAR(3) NOT NULL,
    earthquake_id INT UNSIGNED NOT NULL,
    sample_rate INT UNSIGNED NOT NULL,
    waveform JSON NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,

    FOREIGN KEY(station, channel) REFERENCES CHANNEL(station, symbol),
    FOREIGN KEY(earthquake_id) REFERENCES EARTHQUAKE(id))
    
