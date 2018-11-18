#!/usr/bin/python3

# PART D (65%)
#
# Define a function called tokenize that accepts a lowercased Yupik word,
# and tokenizes it into Yupik graphemes.
#
# Punctuation within words (apostrophes, etc) is used to separate distinct graphemes
# when they would otherwise be confusable.
#
# For example, "n" followed by "g" would be indicated "n'g" to prevent confusion with "ng"
#
# If the word contains such an apostrophe, then you should use the keep_apostrophes parameter.
# If this parameter is set to True, then you should include the apostrophe in the list of graphemes.
# Otherwise, you should not include the apostrophe in the list of graphemes
#
# Sometimes, your function may be passed an English loan word.
# Such a word is likely to contain alphabetic characters that are not in the Yupik alphabet.
# If a word contains any alphabetic characters that are not in the Yupik alphabet,
#    any such character should be tokenized as an individual token.
#
# For example, the sample text contains the word culturemeng
# 
# The result of tokenize("culturemeng") 
#     should be the list ['c', 'u', 'l', 't', 'u', 'r', 'e', 'm', 'e', 'ng']
#
# If the word contains a character that is not alphabetic and is not an apostrophe,
#     you should discard it.
#
# Sometimes, a word could be tokenized multiple ways, but only one of them will be correct.
# You should implement a greedy longest match, starting at the end of the word.
#
# For example:
#
# The result of tokenize("aanghuutuq")
#     should be the list ['a', 'a', 'n', 'gh', 'u', 'u', 't', 'u', 'q']
#
# The result of tokenize("neghneghngwaaq")
#     should be the list ['n', 'e', 'gh', 'n', 'e', 'gh', 'ngw', 'a', 'a', 'q']
#
#
# When this program is run, it should accept text from standard input,
# lowercase it, remove punctuation outside words, and use your function
# to tokenize it into Yupik graphemes (with keep_apostrophes=False).
#uwu
# Punctuation outside words should be disregarded.
import sys
import string


yupikIPA = ["a", "e", "u", "i", "p", "t", "k", "qw", "kw", "q", "v", "l", "z", "y", "r", "g", "w", "gh", "ghw", "f", "ll", "s", "rr", "gg", "wh", "ghh", "ghhw", "h", "m", "n", "ng", "ngw", "mm", "nn", "ngng", "ngngw"]
ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def tokenize(word, keep_apostrophes):
    currentToken = ""
    word = word.lower()
    tokenized = []
    currentPos = 0
    prevPos = currentPos
    while currentPos < len(word):
        #print(str(currentPos) + ": " + word[currentPos])
        if word[currentPos] == ',':
            currentToken = ""
            currentPos+=1
        elif word[currentPos] not in yupikIPA and word[currentPos] in ascii_letters:
            tokenized.append(word[currentPos])
            currentToken = ""
            currentPos +=1
        elif word[currentPos] == "'":
            if keep_apostrophes:
                tokenized.append(currentToken)
            currentPos+=1
        elif word[currentPos] == "n":
            appended = False
            if currentPos + 1 > len(word) and not appended:
                tokenized.append(word[currentPos])
                appended = True
                currentPos+=1
            if currentPos + 4 < len(word) and not appended:
                if word[currentPos:currentPos+5] == "ngngw":
                    tokenized.append(word[currentPos:currentPos+5])
                    currentPos+=5
                    appended = True
            if currentPos + 3 < len(word) and not appended:
                if word[currentPos:currentPos+4] == "ngng":
                    tokenized.append(word[currentPos:currentPos+4])
                    currentPos +=4
                    appended = True
            if currentPos + 2 < len(word) and not appended:
                if word[currentPos:currentPos+3] == "ngw":
                    tokenized.append(word[currentPos:currentPos+3])
                    currentPos+=3
                    appended = True
            if currentPos + 1 < len(word) and not appended:
                if word[currentPos:currentPos+2] == "ng" or word[currentPos:currentPos+2] == "nn":
                    tokenized.append(word[currentPos:currentPos+2])
                    currentPos+=2
                    appended = True
            if not appended:
                tokenized.append(word[currentPos])
                currentPos+=1
        elif word[currentPos] == "m":
            appended = False
            if currentPos + 1 < len(word) and not appended: #length 1 mm
                if word[currentPos:currentPos+2] == "mm":
                    tokenized.append(word[currentPos:currentPos+2])
                    appended = True
                    currentPos+=2
            if not appended: #Prob just m
                tokenized.append(word[currentPos])
                currentPos+=1
        elif word[currentPos] == "g":
            #gh,ghw,gg,ghh,ghhw
            appended = False
            if currentPos + 3 < len(word) and not appended: #ghhw
                if word[currentPos:currentPos+4] == "ghhw":
                    tokenized.append(word[currentPos:currentPos+4])
                    appended=True
                    currentPos+=4
            if currentPos + 2 < len(word) and not appended: #ghh,ghw
                if word[currentPos:currentPos+3] == 'ghh' or word[currentPos:currentPos+3] == "ghw":
                    tokenized.append(word[currentPos:currentPos+3])
                    appended=True
                    currentPos+=3
            if currentPos + 1 < len(word) and not appended: #gh,gg
                if(word[currentPos:currentPos+2]) == "gh" or word[currentPos:currentPos+2] == "gg":
                    tokenized.append(word[currentPos:currentPos+2])
                    appended=True
                    currentPos+=2
            if not appended:
                tokenized.append(word[currentPos])
                currentPos+=1
        elif word[currentPos] == "w":
            #wh,w
            appended = False
            if currentPos + 1 < len(word) and not appended:
                if word[currentPos:currentPos+2] == "wh":
                    tokenized.append(word[currentPos:currentPos+2])
                    currentPos+=2
                    appended = True
            if not appended:
                tokenized.append(word[currentPos])
                currentPos+=1
        elif word[currentPos] == "k":
            #k,kw
            appended = False
            if currentPos + 1 < len(word) and not appended:
                if word[currentPos:currentPos+2] == "kw":
                    tokenized.append(word[currentPos:currentPos+2])
                    currentPos+=2
                    appended = True
            if not appended:
                tokenized.append(word[currentPos])
                currentPos+=1
                appended = True
        elif word[currentPos] == "q":
            #q,qw
            appended = False
            if currentPos + 1 < len(word) and not appended:
                if word[currentPos:currentPos+2] == "qw":
                    tokenized.append(word[currentPos:currentPos+2])
                    currentPos+=2
                    appended = True
            if not appended:
                tokenized.append(word[currentPos])
                currentPos+=1
                appended = True
        elif word[currentPos] == "l":
            #l,ll
            appended = False
            if currentPos + 1 < len(word) and not appended:
                if word[currentPos:currentPos+2] == "ll":
                    tokenized.append(word[currentPos:currentPos+2])
                    currentPos+=2
                    appended = True
            if not appended:
                tokenized.append(word[currentPos])
                currentPos+=1
                appended = True
        elif word[currentPos] == "r":
            #r,rr
            appended = False
            if currentPos + 1 < len(word) and not appended:
                if word[currentPos:currentPos+2] == "rr":
                    tokenized.append(word[currentPos:currentPos+2])
                    currentPos+=2
                    appended = True
            if not appended:
                tokenized.append(word[currentPos])
                currentPos+=1
                appended = True
        else:
            tokenized.append(word[currentPos])
            currentPos+=1



    return tokenized





if __name__ == "__main__":
    f = open("sample-ocr.txt",'r')
    for line in f:
        ln = line
        ln = str(ln).replace("\r","")
        ln = str(ln).replace("\n","")
        ln = str(ln).replace(",","")
        ln = str(ln).replace(". ","")
        ln = str(ln).replace(".","")
        ln = ln.split(" ")
        g = open("test.txt",'w+')
        #print(ln)
        for word in ln:
            print(str(tokenize(word)),end="")
        print()
    
    #print(tokenize("Akulkim Apellgha"))

