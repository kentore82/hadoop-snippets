hive -S -e "USE spk;
	DROP TABLE IF EXISTS spk_first;
	create external table spk_first (sakid STRING,
					feilmeldingListe ARRAY<STRING>,
					feilmelding STRING,
					produktkode STRING,
					timestamp TIMESTAMP,
					ID STRING,
					korrelasjonsid STRING,
					oppgavenavn STRING,
					saknavn STRING,
					oppgavekode STRING,
					regel STRING,
					oppgaveid INT,
					fodselsnummer INT,
					sakkode STRING)
	ROW FORMAT SERDE 'parquet.hive.serde.ParquetHiveSerDe'
  	STORED AS 
    	INPUTFORMAT 'parquet.hive.DeprecatedParquetInputFormat'
    	OUTPUTFORMAT 'parquet.hive.DeprecatedParquetOutputFormat'
    	LOCATION 'hdfs://1.sherpa.client.sysedata.no:8020/DATASETS/SPK/DATASETS/SPK/PARQUET/firstdata.parquet';
"
	#TBLPROPERTIES ('parquet.compression' = 'GZIP');	
