import random

'''
choices: lista mahdollisia valintoja, k,p tai s.
Pelaaja voi valita yhden, tai valita q, jolloin game.py keskeyttää pelin.
'''
def get_player_choice(choices, override_choice = ""):
    choice = override_choice
    if choice == "":
        choice = input(f"Valitse siirtosi: ({', '.join(choices)}) tai muu valinta poistuaksesi: ").strip().lower()

    if choice in choices:
        return choice
    else:
        return "q"

'''
choices: lista mahdollisia valintoja, k,p tai s.
Valitsee satunnaisesti yhden
'''
def get_ai_choice(choices):
    return random.choice(choices)