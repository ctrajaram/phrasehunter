class Phrase:
    """Class to manage inidividual phrases"""
    
    def __init__(self, phrase: str)-> None:
        self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in self.phrase:
            print(f"{letter if letter in guesses else '_'}", end=" ")
        print()

    def check_guess(self,guess):
        return  guess.lower() in self.phrase
    
    def check_complete(self,guesses):
        for phrase in self.phrase:
            if phrase not in guesses:
                return False
            else:
                continue
        return True  
        

if __name__ == "__main__":
    print("In phrase")
