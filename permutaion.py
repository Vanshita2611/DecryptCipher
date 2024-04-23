from itertools import permutations
from nltk.corpus import words

def generate_permutations(word):
    perms = [''.join(perm) for perm in permutations(word)]
    return perms

def find_best_fits(sentence):
    sentence = sentence.upper()
    words_in_sentence = sentence.split()
    best_fits = []
    for word in words_in_sentence:
        possible_permutations = generate_permutations(word)
        valid_words = [perm for perm in possible_permutations if perm in words.words()]
        if valid_words:
            best_fits.append(min(valid_words, key=len))
        else:
            best_fits.append(None)
    return best_fits

# Example usage:
sentence = "The quick brown fox"
best_fits = find_best_fits(sentence)
print("Best fits for each word:", best_fits)
