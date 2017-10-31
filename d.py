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
#
# Punctuation outside words should be disregarded.


def tokenize(word, keep_apostrophes=False):
    pass


if __name__ == "__main__":
    pass

