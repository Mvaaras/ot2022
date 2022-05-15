# Muistipeli

Muistipelissä tarkoitus on löytää kaksi samaa korttia. Muistipelisovelluksella kaksi pelaajaa voivat vuorotellen avata kortteja. Enemmän kortteja avannut pelaaja voittaa. Tämä muistipeli on luotu Helsingin Yliopiston Ohjelmistotekniikan kurssin harjoitustyöksi (Kevät 2022)

---

## Dokumentaatio

[Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](/dokumentaatio/changelog.md)

[Arkkitehtuuri](/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](/dokumentaatio/kayttohje.md)

[Testaus](/dokumentaatio/testaus.md)


## Asennus

1. Asenna tarvittavat riippuvuudet ajamalla komento "poetry install" projektin pääkansiossa
2. Nyt voit käynnistää pelin komennolla "poetry run invoke start"

## Releases

[Releases](https://github.com/Mvaaras/ot2022/releases)

## Hyödyllisiä komentoja

Testien ajaminen: "poetry run invoke test" _huomaa, että testaamiseen liittyvien komentojen ajaminen tyhjentää aiemmin tallennetut tulokset_

Coverage report: "poetry run invoke coverage-report"

Pylint tarkistus: "poetry run invoke lint"
