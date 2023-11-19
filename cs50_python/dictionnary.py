words = set() #Implement a hashtable



def check(word):
    if word.lower() in words:
        return True

def load(dictionnary):
    file = open(dictionnary, "r") #Open dictionnarie in read mode
    for line in file :
        word = line.rstrip()
        words.add(word)
    close(file)
    return True


def size():
    return len(words) #donner la taille du dictionnaire
    



def unload():
    return True