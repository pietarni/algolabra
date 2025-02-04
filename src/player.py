'''
Pelaajan toiminnot
'''

def get_player_choice(choices, override_choice=""):
    '''
    choices: lista mahdollisia valintoja, k,p tai s.
    Pelaaja voi valita yhden, tai valita q, jolloin game.py keskeyttää pelin.
    '''
    choice = override_choice
    if choice == "":
        choice = input(
            f"Valitse siirtosi: ({
                ', '.join(choices)}) tai muu valinta poistuaksesi: ").strip().lower()

    if choice in choices:
        return choice
    return "q"
