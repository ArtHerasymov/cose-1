def get_leveshtein(s1, s2):
    """Returns levenshtein's length, i.e. the number of characters to modify to get a pattern string"""
    if s1 is None or s2 is None:
        return -1

    if len(s1) < len(s2):
        return get_leveshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[
                             j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def trim(inquiry, candidate):
    """Trims input string to eliminate excessive words from
    the inquiry, and successively invokes get_livenshtein() method"""
    if inquiry is None or candidate is None:
        return -1

    inquiry_words = inquiry.lower().split()
    candidate_words = candidate.lower().split()
    indexes = []

    for i in range(0, len(inquiry_words)):
        for j in range(0, len(candidate_words)):
            if inquiry_words[i] == candidate_words[j]:
                indexes.append(j)

    if len(indexes) == 0:
        return -1
    return get_leveshtein("".join(candidate_words[min(indexes):max(indexes) + 1]), "".join(inquiry_words))
