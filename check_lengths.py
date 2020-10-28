import pandas

from collections import defaultdict
from Bio import SeqIO


def check():
    sizes = defaultdict(int)

    for record in SeqIO.parse("transcripts.fasta", format="fasta"):
        size = int(record.id.split("_")[3])
        sizes[size] += 1

    sorted_keys = sorted(sizes.keys())

    maximum = max(sizes.keys())

    values = list()

    for i in range(0, maximum + 1):
        values.append(sizes.get(i, 0))

    binned = list()

    chunk = 1000

    for i in range(0, len(values), chunk):
        end = i + chunk
        print(end, sum(values[i:end]))

if __name__ == "__main__":
    check()
