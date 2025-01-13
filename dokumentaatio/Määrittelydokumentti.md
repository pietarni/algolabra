Mitä ohjelmointikieltä käytät?

-Python

Kerro myös mitä muita kieliä hallitset siinä määrin, että pystyt tarvittaessa vertaisarvioimaan niillä tehtyjä projekteja.

Javascript, C#

Mitä algoritmeja ja tietorakenteita toteutat työssäsi?

Usean eri asteen Markovin ketjut
1.Asteen ketju - ennustaa käyttäjän siirtoa perustuen aikaisempaan siirtoon.
2.Asteen ketju ottaa huomioon kaksi edellistä siirtoa
n.asteen ketju - vaatii enemmän työaikaa ja pähkäilyä.

Markovin ketju- algoritmilla luomme siis siirtymätaulukon, jonka avulla siirron ennustus on nopeaa.

Minkä ongelman ratkaiset?

Kivi-Sakset-Paperi pelin tekoälyn toteutus

Mitä syötteitä ohjelma saa ja miten niitä käytetään?

Käyttäjältä kysytään syötteenä hänen seuraava liikkeensä pelissä. Syötteet tallennetaan historialliseksi dataksi, jonka perusteella luodaan Markovin ketjuja joilla pyritään ennustamaan pelaajan seuraavaa siirtoa.

Tavoitteena olevat aika- ja tilavaativuudet (esim. O-analyysit)

Markovin ketjun päivitys : O(1)
Siirtymätaulukon viemä tila: n^k - n on siirtojen määrä (kivi, sakset, paperi) ja k on markovin ketjun aste.
Ennustus: O(1), sillä ennuste lasketaan siirtymätaulukosta


Harjoitustyön ydin: 
Pelin tekoäly. Eli markovin ketjujen perusteella se ennustaa käyttäjän todennäköisen seuraavan siirron historiallisen datan perusteella, ja valitsee oman siirtonsa sen perusteella.


Tietojenkäsittelytieteen kandidaatti.
