from src.utils import get_score
from src.player import get_player_choice
from src.markov import MarkovAI

class GameManager:
    '''
    Mahdolliset valinnat alustetaan, k,p,s kivi sakset paperi.
    '''
    def __init__(self):
        self.choices = ["k", "s", "p"]
        self.ai = MarkovAI(self.choices)

    '''
    Pelin loop
    '''
    def run(self):
        while True:

            player_choice = get_player_choice(self.choices)
            if (player_choice not in self.choices):
                print("Poistutaan")
                break
            
            ai_choice = self.ai.get_ai_choice()
            self.play_round(player_choice, ai_choice)
            self.ai.update_after_round(player_choice)

    def play_round(self, player_choice, ai_choice):
        print(f"AI:n valinta: {ai_choice}")
        
        result = get_score(player_choice, ai_choice)
        print(f"TULOS: {result}\n")
        return result