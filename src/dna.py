import random


"""

    generates random DNA.


"""
def random_dna(n, nucleotides = ["A", "C", "G", "T"]):
    return "".join([random.choice(nucleotides) for i in range(n)])



"""

    gets the kmers from a DNA strand.


"""
def get_kmers(seq, k):
    kmers = []
    end = len(seq)+1
    for i in range(0, end-k):
        kmers.append(seq[i:i+k])
    return kmers



"""

    counts the kmers in a DNA strand.

"""
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



"""

    takes a sequence and hides it in another sequence, preserving the overall length (writing over sequences)
    to do so.

"""
def insert_sequence(seq, dna, insert_index = None):


    if not insert_index:
        # we need to pick a random spot to insert it that doesn't go over the edge
        insert_location = random.choice(range(0, len(dna) - (len(seq))+1))
    else:
        insert_location = insert_index


    left_boundary = 0
    right_boundary = len(dna) - len(seq)


    # if it's at the start or the end
    if insert_index == left_boundary:
        left = seq
        right = dna[len(seq):len(dna)]
        result = "".join([left, right])


    elif insert_index == right_boundary:
        left = dna[0:right_boundary]
        right = seq
        result = "".join([left, right])
    

    # if it's in the middle somewhere
    else:   
        # get the sequence before that insertion point 
        before_insertion = dna[0:insert_location]

        after_insertion = dna[insert_location+len(seq):len(dna)]

        result =  "".join([before_insertion, seq, after_insertion])


    assert len(result) == len(dna)


    return result