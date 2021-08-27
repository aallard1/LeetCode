def checkIfPangram(self, sentence: str) -> bool:
    # This solution does not work
    # isPangram = False
    # for i in sentence:
    #     if 'a' and 'b' and 'c' and 'd' and 'e' and 'f' and 'g' and 'h' and 'i' and 'j' and 'k' and 'l' and 'm' and 'n' and 'o' and 'p' and 'q' and 'r' and 's' and 't' and 'u' and 'v' and 'w' and 'x' and 'y' and 'z' in sentence or (len(set(sentence)) == 26):
    #         isPangram = True
    #     else:
    #         isPangram = False
    # return isPangram

    # if the length of set(sentence) == 26, then there is one of
    # each lowercase letter in sentence:
    return(len(set(sentence)) == 26)

checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
checkIfPangram("leetcode")