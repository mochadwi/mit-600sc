from time import sleep

EtoF = {'bread': 'du pain', 'wine': 'du vin',\
'eats': 'mange', 'drinks': 'bois',\
'likes': 'aime', 1: 'un',\
'6.00':'6.00'}

def translateWord(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    else:
        return word

def translate(sentences):
    translation = ''
    word = ''
    for c in sentences:
        if c != ' ':
            word = word + c
            print "Word: " + word
            sleep(0.001)
        else:
            translation = translation + ' '\
                            + translateWord(word, EtoF)
            word = ''
            print "Translation: " + translation
            sleep(0.001)
    # return translation[1:] + ' ' + translateWord(word, EtoF)
    return translation[1:] + ' '

print translate("John eats bread")
