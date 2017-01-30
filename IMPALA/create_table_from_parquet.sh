#!/bin/bash

input_table=$1
input_database=$2
p_schema_file=$3
p_folder=$4

if [ $1 = '--help' ]
	then printf '\nUsage: ./create_table_from_parquet.sh table_name database_name parquet_schema_file parquet_folder\n\n\n./create_table_from_parquet.sh mydatabase mytable hdfspath/parquet_folder/test.parquet hdfspath/parquet_folder\n\n';
	exit;
fi


impala-shell -i 2.sherpa.client.sysedata.no:21000 -q "CREATE DATABASE IF NOT EXISTS ${input_database};
DROP TABLE IF EXISTS ${input_database}.${input_table};
CREATE EXTERNAL TABLE ${input_database}.${input_table} LIKE PARQUET '${p_schema_file}'
 STORED AS PARQUET
 LOCATION '${p_folder}';
DESCRIBE ${input_database}.${input_table};
SELECT * FROM ${input_database}.${input_table} LIMIT 1;"
