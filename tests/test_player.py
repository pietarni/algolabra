from src.player import get_ai_choice
from src.player import get_player_choice

def test_ai_choice():
    assert get_ai_choice(["k","s","p"]) in ["k","s","p"]
    assert get_ai_choice(["k","s","p"]) in ["k","s","p"]
    assert get_ai_choice(["k","s","p"]) in ["k","s","p"]

def test_player_choice():
    assert get_player_choice(["k","s","p"], "k") == "k"
    assert get_player_choice(["k","s","p"], "q") == "q"