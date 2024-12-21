#!/bin/sh

cd solutions

for day in $(ls -d day*); do
    cd $day

    echo ""
    echo $day
    
    python -m tests --verbose
    
    cd ..
done