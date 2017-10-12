#!/usr/bin/python3

# PART D (65 points)
#
# Define a function called tokenize that accepts a lowercased Yupik word,
# and tokenizes it into Yupik graphemes.
#
# When this program is run, it should accept text from standard input,
# lowercase it, remove punctuation outside words, and use your function
# to tokenize it into Yupik graphemes.
#
# Punctuation outside words should be disregarded.
#
# Punctuation within words (apostrophes, etc) is used to separate distinct graphemes
# when they would otherwise be confusable.
#
# For example, "n" followed by "g" would be indicated "n'g" to prevent confusion with "ng"
#
# If the word contains such an apostrophe, then you should use the keep_apostrophes parameter.
# If this parameter is set to True, then you should include the apostrophe in the list of graphemes.
# Otherwise, you should not include the apostrophe in the list of graphemes

def tokenize(word, keep_apostrophes=False):
    pass


if __name__ == "__main__":
    pass

