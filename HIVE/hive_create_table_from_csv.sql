hive -S -e "SET skip.header.line.count = 0;
	USE enova;
	DROP TABLE IF EXISTS amsdata;
	CREATE EXTERNAL TABLE IF NOT EXISTS amsdata(
        maaleID INT, 
        tid INT,
        kWh INT)
    COMMENT 'Smartmeter data ENOVA'
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n'
    STORED AS TEXTFILE
    location '/tmp/enova_dummy/eidsiva/data/';
"
