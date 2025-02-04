
Yksikkötestauksen kattavuusraportti:

Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
src\__init__.py       0      0   100%
src\game.py          21      8    62%   23-32
src\markov.py        30      1    97%   30
src\player.py         7      1    86%   12
src\utils.py          6      0   100%
-----------------------------------------------
TOTAL                64     10    84%



Mitä on testattu, miten tämä tehtiin?

test_game.py:
Varmistaa, että manuaalisilla syötteillä, pelilogiikka toimii. esim kivi k voittaa sakset s.

test_markov.py:
Varmistaa että markovin ketjuilla pelaajan toimintaa ennustava botti toimii eri tilanteissa. Syöttämällä manuaalista dataa, ja olettamalla tulokset.

Esim eräässä testissä syötetään manuaalisesti siirtymätaulukon datat yhdelle inputille:
self.ai.transition_matrix["k"] = {"k": 0.1, "s": 0.8, "p": 0.1}
Eli, jos pelaajan viimeisin siirto on k, täydennetään siirtymätaulukkoa siten, että
oletamme todennäköisimmin pelaajan seuraavan siirron olevan s eli sakset.

Tähän todennäköiseen siirtoon bottimme tulisi vastata vastasiirrolla k, sillä kivi päihittää sakset. Sitä juuri testaammekin: self.assertEqual(ai_choice, "k")


test_player.py:
Tämä varmistaa toistaiseksi vain sen, että pelaaja pystyy valita valintansa, ja poistumaan pelistä.

test_utils.py:
Tämä varmistaa että pelin pisteytys toimii oikein. 1: pelaajan voitto. 0: tasapeli. -1: botin voitto
