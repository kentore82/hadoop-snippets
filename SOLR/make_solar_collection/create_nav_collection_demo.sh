#!/bin/bash
echo "---Creating demo collection---"
solrctl instancedir --create nav_collection /home/kentt/repos/hadoop_code/SOLR/nav_collection/ais_collection_config
solrctl collection --create nav_collection -s 1 -r 2
echo "---Finished---"

