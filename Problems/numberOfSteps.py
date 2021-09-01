def numberOfSteps(num):
    count = 0
    while num > 0:
        if num % 2 == 0:
            num /= 2
        elif num % 2 != 0:
            num -= 1
        count += 1
    return count

numberOfSteps(14)


# Runtime: 52 ms, faster than 5.04% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 14.2 MB, less than 37.89% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.