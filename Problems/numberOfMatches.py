def numberOfMatches(n):
    matches = 0
    while n > 1:
        matches += n // 2
        n = n // 2 + n % 2
    return matches

numberOfMatches(8)


# Runtime: 58 ms, faster than 5.42% of Python3 online submissions for Count of Matches in Tournament.
# Memory Usage: 14.2 MB, less than 37.69% of Python3 online submissions for Count of Matches in Tournament.