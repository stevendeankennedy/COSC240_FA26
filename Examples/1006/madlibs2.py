'''
    MAD LIBS 2!  Madder and Libber!

    Authors: Ehren, Declan, Cole, Bailey, Trent
'''
import random

def get_verb():
    verbs = ["jump", "flip", "eat", "sleep"]
    r = random.randrange(len(verbs))
    verb = verbs[r]
    return verb

def get_noun():
    nouns = ["dog", "taco", "dinosaur", "cow"]
    r = random.randrange(len(nouns))
    noun = nouns[r]
    return noun

def get_sentence(verb, noun1, noun2):
    return f"The {noun1} {verb}ed over the {noun2}"
    

verb = get_verb()
noun1 = get_noun()
noun2 = get_noun()

#print(f"The {noun1} {verb}ed over the {noun2}")

print(get_sentence(verb, noun1, noun2))
