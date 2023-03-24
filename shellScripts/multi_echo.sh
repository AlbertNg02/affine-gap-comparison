
#!/bin/bash

./echo_python.sh ../data/BRCA1_score_0.txt ../data/BRCA1-partial.txt ../data/BRCA1-exons.txt global

./echo_python.sh ../data/BRCA1_score_1.txt ../data/BRCA1-partial.txt ../data/BRCA1-exons.txt global

./echo_python.sh ../data/TP53_score.txt ../data/TP53-Rat.fasta ../data/TP53-Cat.fasta global

./echo_python.sh ../data/TP53_score.txt ../data/TP53-Rat.fasta ../data/TP53-Cat.fasta local

./echo_python.sh ../data/TP53_score.txt ../data/TP53-Human.fasta ../data/TP53-Cat.fasta global

./echo_python.sh ../data/TP53_score.txt ../data/TP53-Human.fasta ../data/TP53-Cat.fasta local

./echo_python.sh ../data/TP53_score.txt ../data/TP53-Human.fasta ../data/TP53-Rat.fasta global

./echo_python.sh ../data/TP53_score.txt ../data/TP53-Human.fasta ../data/TP53-Rat.fasta local