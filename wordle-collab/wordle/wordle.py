import os
import json
import random

CURRENT_DIR = os.path.dirname(__file__)

with open(os.path.join(CURRENT_DIR, "words_list.json")) as f:
    words = json.load(f)


def generate_random_word():
    return random.choice(list(words))


def check_word_exists(word):
    return word in words


def give_hint(attempt, word):
    hint = ""
    for i in range(len(attempt)):
        if attempt[i] == word[i]:
            hint += "2"  # means correct letter
        elif attempt[i] in word:
            hint += "1"  # means letter exists but in wrong position
        else:
            hint += "0"  # means letter doesn't exist
    return hint
