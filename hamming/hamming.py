def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length')
    diff = 0
    for c_a, c_b in zip(strand_a, strand_b):
        if c_a != c_b:
            diff += 1
    return diff