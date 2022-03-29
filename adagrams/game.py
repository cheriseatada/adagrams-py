import copy
import random

def draw_letters():
    letter_pool = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3,
                   'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6,
                   'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4,
                   'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1}
    hand = []
    for i in range(10):
        letter = random.choice(list(letter_pool.keys()))
        hand.append(letter)
        letter_pool[letter] -= 1
        if letter_pool[letter] == 0:
            letter_pool.pop(letter)
    return hand
        

def uses_available_letters(word, letter_bank):
    copy_letters = copy.deepcopy(letter_bank)
    for letter in word:
        if letter not in copy_letters:
            return False
        copy_letters.remove(letter)
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass