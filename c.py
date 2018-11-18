#!/usr/bin/python3

# PART C (10%)
#
# Yupik has voiced and voiceless nasals and fricatives.
#
# Certain Yupik fricatives and nasals are "doubleable";
#    that is, they exist in voiced/voiceless pairs
#    where the voiced/voiceless distinction is denoted graphemically through "doubling":
#
# l   -> ll
# r   -> rr
# g   -> gg
# gh  -> ghh
# ghw -> ghhw
# n   -> nn
# m   -> mm
# ng  -> ngng
# ngw -> ngngw
#
#
# The remaining Yupik consonants do not show this doubling pattern.
#
# For each tokenized word, apply the following automatic devoicing rules:
#
# 1a) If an undoubled (but doubleable) fricative occurs immediately before OR after an unvoiced consonant
#     (where that other consonant is not doubleable),
#     the grapheme for the doubleable voiced fricative is replaced with its voiceless counterpart.
#
# 2) If an undoubled (but doubleable) nasal occurs immediately after an unvoiced consonant
#     (where that other consonant is not doubleable), 
#     the grapheme for the doubleable voiced nasal is replaced with its voiceless counterpart.
#
# 3a) If an undoubled (but doubleable) nasal or fricative occurs immediately after an unvoiced fricative
#     (where that other consonant is doubled),
#     the grapheme for the doubleable voiced consonant is replaced with its voiceless counterpart.
#
# 3b) If an undoubled (but doubleable) nasal or fricative occurs immediately before the unvoiced fricative ll
#     the grapheme for the doubleable voiced consonant is replaced with its voiceless counterpart.
#
# Implement a function called apply_devoicing that accepts a list of graphemes,
#     and returns a list of graphemes with the above rules applied.
#
# When this file is executed, it should:
#    * accept text from standard input,
#    * lowercase it,
#    * tokenizes it into Yupik graphemes using the tokenize function from d.py (with keep_apostrophes=True), 
#    * apply the devoicing rules by calling your apply_devoicing function, 
#    * and print the corresponding output (formatted as words, not lists of graphemes).
#
# (Note: you must import tokenize from d.py)
from d import tokenize
doubleable = ['l', 'r', 'g', 'gh', 'ghw', 'n', 'm', 'ng', 'ngw']
undoubledFric = ['l', 'r', 'g', 'gh', 'ghw']
undoubledNasal = ['m', 'n', 'ng', 'ngw']
unvoicedConsonants = ['f', 'll', 's', 'rr', 'gg', 'wh', 'ghh', 'ghhw', 'h', 'mm', 'nn', 'ngng', 'ngngw', 'b', 'c', 'd', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', ]
unvoicedFric = ['f', 'll', 's', 'rr', 'gg', 'wh', 'ghh', 'ghhw', 'h']

def apply_devoicing(graphemes):
    graphemesTokenized = []
    for grapheme in graphemes:
        graphemesTokenized.append(str(grapheme))
    currPosition = 0
    while currPosition < len(graphemesTokenized):
        currToken = graphemesTokenized[currPosition]
        if currPosition + 1 >= len(graphemesTokenized):
            nextToken = ''
        else:
            nextToken = graphemesTokenized[currPosition + 1]
        if currPosition - 1 < 0:
            prevToken = ''
        else:
            prevToken = graphemesTokenized[currPosition - 1]
        # 1a) If an undoubled (but doubleable) fricative occurs immediately before OR after an #unvoiced consonant
        #(where that other consonant is not doubleable),
        #the grapheme for the doubleable voiced fricative is replaced with its voiceless counterpart.
        if (currToken in undoubledFric and currToken in doubleable and prevToken in unvoicedConsonants and prevToken not in doubleable) or (currToken in undoubledFric and nextToken in unvoicedConsonants and currToken in doubleable and nextToken not in doubleable):
            graphemesTokenized[currPosition] = currToken + currToken
        
        # 2) If an undoubled (but doubleable) nasal occurs immediately after an unvoiced consonant
        #(where that other consonant is not doubleable), 
        #the grapheme for the doubleable voiced nasal is replaced with its voiceless counterpart.
        if currToken in undoubledNasal and currToken in doubleable and prevToken in unvoicedConsonants and prevToken not in doubleable:
            graphemesTokenized[currPosition] = currToken + currToken

        # 3a) If an undoubled (but doubleable) nasal or fricative occurs immediately after an unvoiced fricative
        #(where that other consonant is doubled),
        #the grapheme for the doubleable voiced consonant is replaced with its voiceless counterpart.
        if (currToken in undoubledNasal or currToken in undoubledFric) and currToken in doubleable and prevToken in unvoicedFric and prevToken not in doubleable:
            graphemesTokenized[currPosition] = currToken + currToken
        
        # 3b) If an undoubled (but doubleable) nasal or fricative occurs immediately before the unvoiced fricative ll
        #the grapheme for the doubleable voiced consonant is replaced with its voiceless counterpart.
        if (currToken in undoubledNasal or currToken in undoubledFric) and currToken in doubleable and nextToken == 'll':
            graphemesTokenized[currPosition] = currToken + currToken
        
        return graphemesTokenized




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
        #g = open("test.txt",'w+')
        #print(ln)
        tokens = []
        for word in ln:
            tokens.append(tokenize(word, True))
        print(apply_devoicing(tokens))
