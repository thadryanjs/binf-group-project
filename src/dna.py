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

"""
    reads in the fasta file we're experimenting on

"""
def read_fasta(filename = "data/U00096.3.fasta"):
    # open the file
    with open(filename, "r") as input_stream:
        # read in the lines
        text = input_stream.readlines()
        # the header will be first
        header = text[0].rstrip()
        # the sequences are the rest
        raw_sequences = text[1:]
        return {
            "header": header,
            # they're in a list, split on newlines. We remove the newlines and join into one long sequence
            "sequence": "".join([l.strip() for l in raw_sequences])
        }
    


"""
    degenerates a sequence outside the promoter region
"""
def degenerate_outside_region(seq, reg_start, reg_length):

    seq_before = seq[0:reg_start]
    seq_after = seq[(reg_start+reg_length):len(seq)]
    promoter = seq[reg_start:(reg_start+reg_length)]
    
    mutate_choice = random.choice([0,1])
    # randomly decide to mutate pre-promoter or post-promoter
    if mutate_choice == 0:
        seq_to_mutate = seq_before
    else:
        seq_to_mutate = seq_after

    seq_to_mutate_chars = [c for c in seq_to_mutate]

    index_to_mutate = random.choice([i for i in range(len(seq_to_mutate_chars))])

    nucleotide_observed = seq_to_mutate[index_to_mutate]

    possible_mutations = [n for n in ["A", "C", "G", "T"] if n != nucleotide_observed]

    nuc_to_insert = random.choice(possible_mutations)

    seq_to_mutate_chars[index_to_mutate] = nuc_to_insert

    new_region = "".join(seq_to_mutate_chars)

    if mutate_choice == 0:
        new_seq = "".join([new_region, promoter, seq_after])
    else:
        new_seq = "".join([seq_before, promoter, new_region])
    return new_seq



"""
    chooses a random region of length x to be a promoter region
"""
def select_random_promoter(seq, length = 15):
    # it can start at zer0 but can't start so that it goes off the end
    sample_space = [i for i in range(length, len(seq) - length)]
    start_location = random.choice(sample_space)
    return {
        "promoter": seq[start_location:start_location + length],
        "promoter_start": start_location,
        "promoter_length": 15
    }