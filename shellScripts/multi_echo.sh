
#!/bin/bash

./echo_python.sh ../data/TP53_score.txt ../data/TP53-Rat.fasta ../data/TP53-Cat.fasta global

./echo_python.sh ../data/TP53_score.txt ../data/TP53-Rat.fasta ../data/TP53-Cat.fasta local

./echo_python.sh ../data/TP53_score.txt ../data/TP53-Human.fasta ../data/TP53-Cat.fasta global

./echo_python.sh ../data/TP53_score.txt ../data/TP53-Human.fasta ../data/TP53-Cat.fasta local

./echo_python.sh ../data/TP53_score.txt ../data/TP53-Human.fasta ../data/TP53-Rat.fasta global

./echo_python.sh ../data/TP53_score.txt ../data/TP53-Human.fasta ../data/TP53-Rat.fasta local