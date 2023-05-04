import random

def random_dna(n, nucleotides = ["A", "C", "G", "T"]):
    return "".join([random.choice(nucleotides) for i in range(n)])



def get_kmers(seq, k):
    kmers = []
    end = len(seq)+1
    for i in range(0, end-k):
        kmers.append(seq[i:i+k])
    return kmers



# a function to get the counts
def get_kmer_counts(kmers):
    # this will store the kmers and their counts
    kmer_counts_dict = {}
    # go through each kmer
    for kmer in kmers:
        # if we don't have it in the dictionary
        if kmer not in kmer_counts_dict.keys():
            # give it a count of one
            kmer_counts_dict[kmer] = 1
        else:
            # if we do, increase the number of times we've seen it by 
            kmer_counts_dict[kmer] += 1
    return kmer_counts_dict 