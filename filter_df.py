from Bio import SeqIO

with open("data/sorted_unique.txt", "r") as f:
    seq_ids = {line.rstrip() for line in f}


with open("data/df_genome.fna", "r") as f:
    for record in SeqIO.parse(f, "fasta"):
        if record.name in seq_ids:
            print(f">{record.name}")
            print(record.seq)
