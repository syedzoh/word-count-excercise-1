#! /bin/bash

DATADIR="data"
RESULTSDIR="results"
FIGDIR="figures"

mkdir -p ${RESULTSDIR}
mkdir -p ${FIGDIR}

for title in abyss isles last sierra; do
    python3 code/count.py ${DATADIR}/${title}.txt -o ${RESULTSDIR}/${title}.json
    python code/plot.py ${RESULTSDIR}/${title}.json -o ${FIGDIR}/${title}.png
done