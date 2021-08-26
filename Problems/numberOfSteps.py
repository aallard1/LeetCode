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