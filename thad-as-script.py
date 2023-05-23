# %%
import subprocess
import random
import fastaparser
import os

from src.dna import *

# %% [markdown]
# We will need to modify a sequences using the tool, then compare it against the background.

# %%
random.seed(867530)

min = 8
max = 20

sequences = [random_dna(i) for i in range(min, max+1)]

sequences

# %%
filepath = "data/"
filename = "U00096.3.fasta"

for seq in sequences:

    fasta_obj = read_fasta(filepath+filename)
    fasta_header = fasta_obj["header"]
    fasta_seq = fasta_obj["sequence"]

    new_sequence = insert_sequence(seq, fasta_seq)

    seq_id = str(len(seq)) + "_" + seq

    new_filename = filepath + "modified/" + seq_id + "_" + filename

    with open(new_filename, "w") as fasta_file:
        fasta_seq_mod = fastaparser.FastaSequence(
            sequence = new_sequence,
            # id = seq_id,
            description = filename + " with " + seq + "introduced"
        )

# %%
f = read_fasta(filename="data/U00096.3.fasta")

type(f)

# %%
mod_files = os.listdir("data/modified/")

mod_files

# %%
for f in mod_files:
    print(f)
    print(f.split("_")[1])

# %%
# example motifs
# findMotifs.pl targets.fa fasta motifResults/ -fasta background.fa
for f in mod_files:
    seq = f.split("_")[1]
    len_arg = "-len " + str(len(seq))
    print(len_arg)
    subprocess.call([
        "findMotifs.pl",
        "data/U00096.3.fasta",
        "fasta",
        "homer-results/motifs_" + seq,
        "-fasta",
        "data/modified/" + f,
        "-len " + str(len(seq))
    ])

print("end")

# %%



