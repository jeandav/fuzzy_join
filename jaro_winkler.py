def jaro_winkler_distance(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)

    if s1_len == 0 and s2_len == 0:
        return 0.0, 1.0

    match_distance = (max(s1_len, s2_len) // 2) - 1

    s1_matches = [False] * s1_len
    s2_matches = [False] * s2_len

    matches = 0
    transpositions = 0

    for i in range(s1_len):
        start = max(0, i - match_distance)
        end = min(i + match_distance + 1, s2_len)

        for j in range(start, end):
            if s2_matches[j]:
                continue
            if s1[i] != s2[j]:
                continue
            s1_matches[i] = True
            s2_matches[j] = True
            matches += 1
            break

    if matches == 0:
        return 1.0, 0.0

    k = 0
    for i in range(s1_len):
        if not s1_matches[i]:
            continue
        while not s2_matches[k]:
            k += 1
        if s1[i] != s2[k]:
            transpositions += 1
        k += 1

    transpositions //= 2

    jaro = ((matches / s1_len) +
            (matches / s2_len) +
            ((matches - transpositions) / matches)) / 3

    prefix = 0
    for i in range(min(4, s1_len, s2_len)):
        if s1[i] != s2[i]:
            break
        prefix += 1

    jaro_winkler = jaro + (prefix * 0.1 * (1 - jaro))

    similarity = jaro_winkler

    distance = 1 - similarity

    return distance, similarity