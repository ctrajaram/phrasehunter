# Import your Game class

# Create your Dunder Main statement.

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop

from phrasehunter.game import Game

def print_phrase(phrase_object):
    print(f"The phrase is : {phrase_object.phrase}")

if __name__ == "__main__":
    game = Game()
    # for phrase in game.phrases:
    #     print(phrase.phrase)
    # print_phrase(game.get_random_phrase())
    # print_phrase(game.get_random_phrase())
    # print_phrase(game.get_random_phrase())
    # print_phrase(game.get_random_phrase())
    # print_phrase(game.get_random_phrase())

    # print(game.active_phrase)
    # print(game.active_phrase.phrase)

    # print(game.active_phrase.phrase)
    # game.active_phrase.display(game.guesses)
    print(game.active_phrase.phrase)
    game.start()
    