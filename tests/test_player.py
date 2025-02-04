from src.player import get_player_choice

def test_player_choice():
    assert get_player_choice(["k","s","p"], "k") == "k"
    assert get_player_choice(["k","s","p"], "q") == "q"