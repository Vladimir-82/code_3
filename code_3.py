def greatest_common_factor(seq):
    """
    Greatest Common Factor of an Array
    """
    minimum = min(seq)
    work = seq[:]
    while work:
        if not work[0] % minimum:
            del work[0]
            if not work:
                return minimum
        else:
            minimum -= 1
            work = seq[:]



print(greatest_common_factor([32, 96, 120, 80]))