from src.utils import get_score

def test_get_winner():
    assert get_score("k", "s") == 1
    assert get_score("p", "k") == 1
    assert get_score("s", "p") == 1
    assert get_score("k", "k") == 0
    assert get_score("s", "k") == -1