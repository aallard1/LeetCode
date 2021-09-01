def checkIfPangram(sentence):
    return(len(set(sentence)) == 26)

checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
checkIfPangram("leetcode")


# Runtime: 32 ms, faster than 64.17% of Python3 online submissions for Check if the Sentence Is Pangram.
# Memory Usage: 14.2 MB, less than 47.92% of Python3 online submissions for Check if the Sentence Is Pangram.

    # isPangram = False
    # for i in sentence:
    #     if 'a' and 'b' and 'c' and 'd' and 'e' and 'f' and 'g' and 'h' and 'i' and 'j' and 'k' and 'l' and 'm' and 'n' and 'o' and 'p' and 'q' and 'r' and 's' and 't' and 'u' and 'v' and 'w' and 'x' and 'y' and 'z' in sentence or (len(set(sentence)) == 26):
    #         isPangram = True
    #     else:
    #         isPangram = False
    # return isPangram

    # if the length of set(sentence) == 26, then there is one of
    # each lowercase letter in sentence:

    # This solution does not work