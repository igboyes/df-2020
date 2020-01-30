from argparse import ArgumentParser
from Bio import SeqIO

parser = ArgumentParser()

parser.add_argument(
    "headers",
    help="path to text file containing list of headers"
)

parser.add_argument(
    "fasta",
    help="path to FASTA file to filter by header list"
)

args = parser.parse_args()

with open(args.headerse, "r") as f:
    seq_ids = {line.rstrip() for line in f}


with open(args.fasta, "r") as f:
    for record in SeqIO.parse(f, "fasta"):
        if record.name in seq_ids:
            print(f">{record.name}")
            print(record.seq)
