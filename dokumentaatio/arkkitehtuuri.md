# Arkkitehtuuri

## Sovelluslogiikka

Pelin logiikka on jaettu kolmiosaiseen luokka-arkkitehtuuriin. Peliluokka Game hyödyntää toiminnassaan lautaa, joka puolestaan hyödyntää useita kortteja.

![Luokkakaavio](luokkakaavio.png)

Uuden pelin luomisen prosessi käy ilmi seuraavasta kaaviosta:

![Sekvenssikaavio](sekvenssikaavio.png)

## Käyttöliittymä

Käyttöliittymä sisältää 3 (käytännössä 5) erilaista näkymää.

Aloitusnäkymästä voi valita haluamansa pelitilan (yksin- tai moninpeli)

Pelitilassa tapahtuu itse pelaaminen. Siinä näkyy kortteja, joita voi avata klikkaamalla. Suurin osa toiminnallisuudesta painottuu tähän näkymään. Pelitilasta on olemassa kaksi eri versiota riippuen siitä, pelataanko yksin- vai moninpeliä. Pelin päätyttyä siirrytään voittonäkymään.

Voittonäkymässä näkyy pelin lopputulos. Siitä voi siirtyä takaisin aloitusnäkymään.



