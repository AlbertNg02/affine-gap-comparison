

# Dependencies

- Biopython

# How to execute script

1. Running all comparisons
```
./multi_echo.sh
```

2. Running individual scripts
Formatting

```
./echo_python.sh [scoring_scheme] [sequence_file_0] [sequence_file_1] [global/local]
```

```
Execute inside ShellScript Folder

./echo_python.sh ../data/TP53_score.txt ../data/TP53-Human.fasta ../data/TP53-Rat.fasta local
```

# Bugs
- Choosing path when gap and match/mismatch had the same score.
- Keeping track of whether the previous choice was a gap to account for gap extend and gap open
- Did not initially remember that gap_open_score = score open + score extend
- Keeping track of where to stop in local alignment

# Design choices

- To keep track of where the local alignment stops, I put in the score matrix to keep track of when to stop.

# Collaboration

**Partner**: Usif

**Discussed**: Paola, Emory, Alvin



