def isSumEqual(firstWord, secondWord, targetWord):
    newFirstWord = ''
    newSecondWord = ''
    newTargetWord = ''
    for i in range(len(firstWord)):
        newFirstWord += str(ord(firstWord[i])-97)
    for i in range(len(secondWord)):
        newSecondWord += str(ord(secondWord[i])-97)
    for i in range(len(targetWord)):
        newTargetWord += str(ord(targetWord[i])-97)
    isEqual = int(newFirstWord) + int(newSecondWord)
    if isEqual == int(newTargetWord):
        return True 
    else:
        return False

print(isSumEqual("acb","cba","cdb"))


# Runtime: 21 ms, faster than 95.99% of Python3 online submissions for Check if Word Equals Summation of Two Words.
# Memory Usage: 14.1 MB, less than 80.87% of Python3 online submissions for Check if Word Equals Summation of Two Words.