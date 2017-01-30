#!/bin/bash
# ketot - 20.12.2016

UNAME='' 
PASS='' 
HOST=''
PORT='1433'
DB='AdventureWorks2012'
CONNECTOR='sqlserver'
DRIVER='com.microsoft.sqlserver.jdbc.SQLServerDriver'

sqoop list-tables --connect "jdbc:$CONNECTOR://$HOST:$PORT;database=$DB" --username $UNAME --password $PASS --driver $DRIVER

echo "Finito...."
