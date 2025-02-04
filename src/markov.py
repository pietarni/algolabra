'''
Botti, joka ennustaa pelaajan seuraavan siirron käyttäen Markovin ketjua.
'''
import random
from collections import defaultdict


class MarkovAI:
    '''
    Botti, joka ennustaa pelaajan seuraavan siirron käyttäen Markovin ketjua.
    '''
    def __init__(self, choices):
        '''
        choices: lista mahdollisia siirtoja, tämän ohjelman tapauksessa oletuksena ["k", "s", "p"]
        transition_matrix: siirtymätaulukko jonka avulla voidaan pyrkiä ennustamaan tulevia siirtoja
        '''
        self.choices = choices
        self.transition_matrix = defaultdict(
            lambda: {c: 1 / len(choices) for c in choices})
        self.last_move = None

    def _update_transition_matrix(self, last_move, current_move):
        '''
        Päivittää pelaajan siirtojen siirtymätodennäköisyyksiä.

        last_move: edellinen pelaajan siirto.
        current_move: nykyinen pelaajan siirto.
        '''
        if last_move is None:
            return
        decay = 0.9  # vanhojen todennäköisyyksien hajoituskerroin
        bump = 0.1   # lisäys havaittuun siirtymään
        for move in self.choices:
            self.transition_matrix[last_move][move] *= decay
        self.transition_matrix[last_move][current_move] += bump

    def predict_next(self):
        '''
        Ennustaa pelaajan seuraavan siirron edellisen siirron perusteella.

        palautusarvo: arvaus pelaajan seuraavasta siirrosta (merkkijono).
        Jos botilla ei ole "kokemusta", se valitsee satunnaisesti
        '''
        if self.last_move:
            probabilities = self.transition_matrix[self.last_move]
            weights = [probabilities[m] for m in self.choices]
            prediction = random.choices(self.choices, weights=weights)[0]
        else:
            prediction = random.choice(self.choices)
        return prediction

    def get_ai_choice(self):
        '''
        Valitsee tekoälyn siirron pelaajan ennustetun seuraavan liikkeen perusteella.

        palautusarvo: tekoälyn siirto (merkkijono).
        '''
        predicted_move = self.predict_next()
        # paperi (p) lyö kiven (k), kivi (k) lyö sakset (s) ja sakset (s)
        # lyövät paperin (p).
        counter_moves = {"k": "p", "s": "k", "p": "s"}
        return counter_moves[predicted_move]

    def update_after_round(self, player_choice):
        '''
        Päivittää botin muistia kierroksen jälkeen.

        player_choice: pelaajan viimeisin siirto.
        '''

        if self.last_move:
            self._update_transition_matrix(self.last_move, player_choice)
        self.last_move = player_choice
