#!/bin/sh

./build-viewer $1

./ruff.sh

git bumpmajor

git add --all . 

git commit -S -m 'feat!: day '"$1"' completed.'

git push -u origin HEAD

gh pr create --fill --base main

gh pr merge --merge --auto