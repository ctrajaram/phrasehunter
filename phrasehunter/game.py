# Create your Game class logic in here.
from typing import List
from .phrase import Phrase
from random import choice

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
        Game.welcome_to_game()
        while(self.missed < 6 and not self.active_phrase.check_complete(self.guesses)):
            print(f'Number missed: {self.missed} ' )
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            self.active_phrase.display(self.guesses)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        self.game_over()

    def game_over(self):
        if self.missed > 5:
            print("You have lost the game")
        else:
            print("Congrats on winning the game")

    def get_guess(self):
        return (user_guess := input("Enter the letter you are guessing: "))

    @staticmethod
    def welcome_to_game():
        print("                                ")
        print("================================")
        print("    Welcome to Phrase Hunter    ")
        print("================================")
        print("                                ")
 