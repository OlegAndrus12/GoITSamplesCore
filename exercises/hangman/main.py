import random
from models.man import Man
from models.word import Word


def main():
    letters = random.randint(5, 7)
    word = Word(letters)
    man = Man()

    while not man.is_game_over() and not word.is_word_guessed():
        guess = input()
        if word.check_letter(guess):
            pass
        else:
            man.add_body_part()

    if word.is_word_guessed():
        print("You won")
    else:
        print("You lose")


if __name__ == "__main__":
    main()
