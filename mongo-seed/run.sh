#!/bin/bash
ls -1 *.json | sed 's/.json$//' | while read col; do 
    mongoimport --host db --db usda --collection $col < $col.json; 
done
