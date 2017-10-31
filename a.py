#!/usr/bin/python3

# PART A (15%)
#
# Yupik syllables must be of the form:
#
# * CV
# * CVC
# * CVV
# * CVVC
#
# Additionally, the first syllable of a word may be of the form:
#
# * V
# * VC
# * VV
# * VVC
#
# Where C represents a Yupik consonant and V represents a Yupik vowel.
# 
#
# In all cases, the only instances of VV that are allowed are:
#
# * ii
# * aa
# * uu
#
#
# Yupik words may contain apostrophe (to separate otherwise ambiguous grapheme sequences).
#
#
# You will need to import tokenize from d.py
#
#
# Implement the violates_spelling_rules function.
# The function should take a string representing a word,
#     tokenize it using your tokenize function,
#     and return True if the word violates Yupik spelling rules (contains a non-Yupik grapheme or violates syllable structure),
#     and return False otherwise.
#
# 
# When this file is executed, it should:
#     * accept text from standard input
#     * tokenize it into words
#     * check each word to see if it violates Yupik spelling rules (using your function)
#     * and output a list of all words that violate Yupik spelling rules (one word per line)
#
# In other words, this program will function as a basic Yupik spell checker.
#
#
# No sample expected output will be provided for this program, but sample-ocr.txt contains many misspelled words.


def violates_spelling_rules(word):
    pass


if __name__ == '__main__':
    pass
