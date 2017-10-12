#!/usr/bin/python3

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
#
#
# Write a Python program that accepts text from standard input,
# lowercases it,
# tokenizes it into Yupik graphemes using the tokenize function from d.py, 
# applies the following devoicing rules, 
# and then prints the corresponding output (formatted as words, not lists of graphemes).
#
# (Note: you must import tokenize from d.py)
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



def undouble(graphemes):
    pass


if __name__ == "__main__":
    pass
