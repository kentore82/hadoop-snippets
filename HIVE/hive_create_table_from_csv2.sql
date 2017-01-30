hive -S -e "SET skip.header.line.count = 0;
	USE enova;
	DROP TABLE IF EXISTS amsmeta;
	CREATE EXTERNAL TABLE IF NOT EXISTS amsmeta(
        maaleID INT, 
        type STRING,
        frekvens INT,
	f_sluttbruker INT,
	f_enova INT,
	byggtype STRING,
	knummer INT,
	kanal STRING)
    COMMENT 'Smartmeter data ENOVA'
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n'
    STORED AS TEXTFILE
    location '/tmp/enova_dummy/eidsiva/meta/';
"
