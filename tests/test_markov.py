import unittest
from src.markov import MarkovAI

class TestMarkovAI(unittest.TestCase):

    def setUp(self):
        self.ai = MarkovAI(["k", "s", "p"])


    '''
    Ilman "kokemusta", botti valitsee satunnaisesti minkä vaan vaihtoehdoista.
    '''
    def test_initial_choice(self):
        initial_choice = self.ai.get_ai_choice()
        self.assertIn(initial_choice, ["k", "s", "p"])

    '''
    Siirtymätaulukko päivittyy oikein
    '''
    def test_transition_update(self):
        self.ai.update_after_round("k")
        self.ai.update_after_round("s")
        
        self.assertGreater(self.ai.transition_matrix["k"]["s"], 1/3)
        self.assertLess(self.ai.transition_matrix["k"]["k"], 1/3)
        self.assertLess(self.ai.transition_matrix["k"]["p"], 1/3)

    '''
    Yksinkertaisessa tilanteessa botti ennustaa pelaajan siirron historiallisen datan perusteella
    '''
    def test_prediction_accuracy(self):
        moves = ["k", "s", "k", "s", "k", "s"]
        for move in moves:
            self.ai.update_after_round(move)
        
        self.ai.last_move = "k"
        predicted_move = self.ai.predict_next()
        self.assertEqual(predicted_move, "s")

    '''
    Siirtymätaulukko alustetaan manuaalisesti. Botti tekee liikkeensä sen perusteella pyrkien valitsemaan voittavan siirron.
    '''
    def test_ai_counter_move(self):

        self.ai.last_move = "k"
        self.ai.transition_matrix["k"] = {"k": 0.1, "s": 0.8, "p": 0.1}
        
        ai_choice = self.ai.get_ai_choice()
        self.assertEqual(ai_choice, "k")

if __name__ == "__main__":
    unittest.main()