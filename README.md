# Advent of Code 2024 Python

My solutions to [Advent of Code 2024](https://adventofcode.com/2024) done in Python

[Viewer](https://sergiorgiraldo.github.io/AdventOfCode2024/viewer/)

## Performance

![](https://img.shields.io/badge/day%20📅-24-blue)
 
![](https://img.shields.io/badge/stars%20⭐-50-yellow)

---

# Based on @xavdid's Python Advent of Code Project Template

## running a day

`cd` to the day

`python -m tests --verbose` && `python -m solution`

to make easier, I have this rule for [`ondir`](https://github.com/alecthomas/ondir) 

> .ondirrc

```
enter ~/source/AdventOfCode2024/(.*)
    alias pt="python -m tests --verbose"
    alias pr="python -m solution"

leave ~/source/AdventOfCode2024/(.*)
    unalias pt
    unalias pr
```

## Commands

### `./deploy.sh` 

Create viewer, commit to Github and make PR

#### Usage

> `./deploy.sh [day]`

### `./start` 

Scaffold files to start a new Advent of Code solution and download the puzzle input

#### Usage

> `./start [-h] [--year YEAR] [day]`

### `./build-viewer` 

Generate HTML for viewing the day's solution

#### Usage

> `./build-viewer [day]`

