# Create your Game class logic in here.
from typing import List
from random import choice
from string import ascii_letters
from phrasehunter.phrase import Phrase

class Game:
    """Class to manage the functioning of the game"""

    def __init__(self) -> None:
        self.missed = 0
        self.phrases: List[str] = self.create_phrases()
        self.active_phrase: str = self.get_random_phrase()
        self.guesses = [" "]

    def get_random_phrase(self):
        return choice(self.phrases)

    @staticmethod
    def create_phrases():
        return [Phrase("Hello World"), 
                Phrase("Hello"),
                Phrase("Hai"),
                Phrase("You"),
                Phrase("We are awesome")]

    def start(self):
        self.welcome_to_game()
        while(self.missed < 5 and not self.active_phrase.check_complete(self.guesses)):
            print()
            print(f'Number missed: {self.missed} ' )
            user_guess = self.get_guess().lower()
            while len(user_guess) > 1 or user_guess not in ascii_letters:
                print("Invalid guess as a single letter was not chosen, please try again...")
                user_guess = self.get_guess().lower()
            
            self.guesses.append(user_guess)
            self.active_phrase.display(self.guesses)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        self.game_over()

    def game_over(self):
        if self.missed > 4:
            print("You have lost the game")
        else:
            print("Congrats on winning the game")
        play_game_again = input("Do you want to play the game again(Y/N)?: ")
        if play_game_again.lower() == 'y':
            game = Game()
            print()
            print(f"The random phrase to be guessed is: {game.active_phrase.phrase}")
            game.start()
        else:
            print("Since you opted to not play again, ending the game, thank you.")

    def get_guess(self):
        return (user_guess := input("Enter the letter you are guessing(must be only 1 letter): "))

    
    def welcome_to_game(self):
        print("                                ")
        print("================================")
        print("    Welcome to Phrase Hunter    ")
        print("================================")
        print("                                ")
        self.active_phrase.display(self.guesses)