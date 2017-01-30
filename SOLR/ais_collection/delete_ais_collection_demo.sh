#!/bin/bash
echo "---Deleting demo collection---"
solrctl instancedir --delete ais_collection_demo
solrctl collection --delete ais_collection_demo
echo "---Finished---"

