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

