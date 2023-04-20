import random

def random_dna(n, nucleotides = ["A", "C", "G", "T"]):
    return [random.choice(nucleotides) for i in range(n)]
    