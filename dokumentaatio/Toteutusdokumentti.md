Viikko2:
ChatGPT:n avulla tutustuin poetry juttuihin. Elikkä poetry testaus asioiden alustamisessa oli itsellä muistissa vähän mustia aukkoja, tällaiset yksityiskohdat tarkistin ChatGPT:llä:

[tool.pytest.ini_options]
addopts = "--cov=src --cov-report=term-missing"
testpaths = ["tests"]






Toteutusdokumentin tulee sisältää seuraavat:

Ohjelman yleisrakenne

game.py: Päälogiikka, kysyy inputtia ja suorittaa muista scripteistä pelin tarvitsemia funktioita
markov.py: Markovin ketjujen toteutus, tallentaa pelaajan siirtoja siirtymätaulukkoonsa, sen avulla arvaa pelaajan seuraavan siirron aikaisemman perusteella
player.py: Pelaajan input:in käsittely
utils.py: Tällä hetkellä tämä ainoastaan pitää huolen kivi-sakset-paperin logiikasta, eli mikä voittaa minkä.

tests-kansiossa yksikkötestit

Saavutetut aika- ja tilavaativuudet (esim. O-analyysit pseudokoodista)
Määrittelydokumentin mukaiset

Suorituskyky- ja O-analyysivertailu (mikäli sopii työn aiheeseen)
Määrittelydokumentin mukaiset


Työn mahdolliset puutteet ja parannusehdotukset
Tällä hetkellä vain yhden asteen markovin ketjut. Eli voisi parantaa lisäämällä sitä, kuinka monta askelta pelihistoriaa tämä botti tarkastelee suunitellessaan siirtoaan
