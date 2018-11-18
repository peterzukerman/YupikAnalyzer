#!/usr/bin/python3

# PART B (10%)
#
# Implement the graphemes2ipa function.
# It should accept a list of graphemes, and return a list of IPA symbols.
# If any grapheme is not a Yupik letter, it should be passed through unchanged.
#
# When this file is executed, it should:
#     * accepts text from standard input,
#     * lowercases it, 
#     * tokenizes it into Yupik graphemes using your tokenize function from d.py (with keep_apostrophes=False),
#     * applies the automatic devoicing rules using your apply_devoicing function from c.py, 
#     * converts each grapheme into the appropriate IPA symbol using your graphemes2ipa function,
#     * and then print the corresponding output (formatted as words, not lists of graphemes).
#
# You will need to import tokenize from d.py
# You will need to import apply_devoicing from c.py
#
# Your output should not contain any apostrophes.
from d import tokenize
from c import apply_devoicing
def graphemes2ipa(graphemes):
    ipa = {
        "i":"i", 
        "a":"ɑ", 
        "u":"u",
        "e":"ə", 
        "p":"p", 
        "t": "t", 
        "k":"k",
        "kw":"kʷ",
        "q":"q",
        "qw":"qʷ",
        "v":"v",
        "l":"ɮ",
        "z":"z",
        "y":"j",
        "r":"ʐ",
        "g":"ɣ",
        "w":"ɣʷ",
        "gh":"ʁ",
        "ghw":"ʁʷ",
        "f":"f",
        "ll":"ɬ",
        "s":"s",
        "rr":"ʂ",
        "gg":"x",
        "wh":"xʷ",
        "ghh":"χ",
        "ghhw":"χʷ",
        "h":"h",
        "m":"m",
        "n":"n",
        "ng":"ŋ",
        "ngw":"ŋʷ",
        "mm":"m̥",
        "nn":"n̥",
        "ngng":"ŋ̊",
        "ngngw":"ŋ̊ʷ"
        }
    adjusted = []
    for grapheme in graphemes:
        for x in grapheme:
            if str(x) not in ipa:
                adjusted.append(str(x))
            else:
                adjusted.append(ipa[str(x)])

    for x in adjusted:
        newArr = ""
        for chara in x:
            newArr = newArr + chara
        print(newArr, end="")
    




if __name__ == "__main__":
    f = open("sample-ocr.txt","r")
    for line in f:
        ln = line
        ln = str(ln).replace("\r","")
        ln = str(ln).replace("\n","")
        ln = str(ln).replace(",","")
        ln = str(ln).replace(". ","")
        ln = str(ln).replace(".","")
        ln = ln.split(" ")
        #print(ln)
        tokens = []
        for word in ln:
            tokens.append(tokenize(word, False))
        #tokens = apply_devoicing(tokens)
        graphemes2ipa(tokens)
