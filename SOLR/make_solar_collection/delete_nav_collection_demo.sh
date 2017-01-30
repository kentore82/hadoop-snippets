#!/bin/bash
echo "---Deleting demo collection---"
solrctl instancedir --delete nav_collection
solrctl collection --delete nav_collection
echo "---Finished---"

