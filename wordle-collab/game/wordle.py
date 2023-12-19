def generate_random_word():
    return "WORDS"


def check_word_exists(word):
    return True


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
