#!/bin/bash
# ketot - 20.12.2016

UNAME='username'
PASS='passwd'
HOST='my.host.com'
DB='database'
HIVEDB='table'

#Connect to remote SQL server and fetch table list wihtin database

tables=( $(echo "show tables;"|mysql -u $UNAME  -p$PASS -h $HOST $DB|grep -v '^Tables_in_') )

#Scoop imort all tables in remote database
for table in "${tables[@]}"
do
	echo "Importing table: $table"
	sqoop import --connect jdbc:mysql://$HOST/$DB --username $UNAME --password $PASS --table $table --hive-import --hive-table ${HIVEDB}.$table
done

echo "Finito...."
