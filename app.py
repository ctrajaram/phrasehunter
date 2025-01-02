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
    print()
    print(f"The random phrase to be guessed is: {game.active_phrase.phrase}")
    game.start()
    