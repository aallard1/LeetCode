def numberOfMatches(n):
    matches = 0
    while n > 1:
        matches += n // 2
        n = n // 2 + n % 2
    return matches

numberOfMatches(8)