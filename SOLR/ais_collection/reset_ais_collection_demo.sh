#!/bin/bash
echo "---Deleting demo collection---"
solrctl instancedir --delete ais_collection_demo
solrctl collection --delete ais_collection_demo

echo "---Creating demo collection---"
solrctl instancedir --create ais_collection_demo /home/kentt/repos/hadoop_code/SOLR/ais_collection/ais_collection_config
solrctl collection --create ais_collection_demo -s 1 -r 2
echo "---Finished---"

