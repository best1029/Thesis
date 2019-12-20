import enchant
import splitter

def split(words):
    res = []

    for word in words:
        compounds = splitter.split(word, 'de_de')  

        # check if no compounds found 
        if not compounds or len(compounds) > 3:
            res.append(word)
        else:
            for comp in compounds:
                res.append(comp)

    return res