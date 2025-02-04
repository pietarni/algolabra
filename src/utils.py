'''
utils
'''

def get_score(player_choice, ai_choice):
    '''
    Metodi vertaa pelaajan ja tekoälyn valintoja, ja päättää voittajan.

    player_choice: k, p tai s.
    ai_choice: k, p tai s.

    palautusarvo:
    0 jos tasapeli (valinnat ovat samat). 
    1 jos pelaaja voittaa, 
    -1 jos tietokone voittaa.
    '''

    if player_choice == ai_choice:
        return 0

    if (
    (player_choice == "k" and ai_choice == "s") 
    or 
    (player_choice == "s" and ai_choice == "p")
    or 
    (player_choice == "p" and ai_choice == "k")
    ):
        return 1

    return -1
