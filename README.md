# Haavemaa ☁️✨🐚
Haavemaa -sovelluksessa toteutat suurimmatkin haaveesi ja tavoitteesi! Rekisteröitymällä käyttäjäksi voit listata haaveita ja tavoitteita näkyviin, ja näin helposti seurata niiden edistymistä ja merkitä niitä saavutetuiksi. Sovellus toimii myös ohjelmistotekniikan harjoitustyönä. 

## Dokumentaatio
- [Arkkitehtuuri](https://github.com/aadnw/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Changelog](https://github.com/aadnw/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Käyttöohje](https://github.com/aadnw/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Tekoälyn käyttö](https://github.com/aadnw/ot-harjoitustyo/blob/master/dokumentaatio/tekoalyn_kaytto.md)
- [Testausdokumentti](https://github.com/aadnw/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)
- [Työaikakirjanpito](https://github.com/aadnw/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [Vaatimusmäärittely](https://github.com/aadnw/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Vko 5 Release](https://github.com/aadnw/ot-harjoitustyo/releases/tag/viikko5)
- [Vko 6 Release](https://github.com/aadnw/ot-harjoitustyo/releases/tag/viikko6)

## Sovelluksen asennusohje
1. Kloonaa tämä repositorio tai lataa viimeisimmän [releasen](https://github.com/aadnw/ot-harjoitustyo/releases/tag/loppupalautus) lähdekoodi omalle koneellesi ja siirry sen juurihakemistoon.
2. Asenna riippuvuudet komennolla:
   ```
   poetry install
   ```
3. Suorita tarvittavat alustustoimenpiteet komennolla:
   ```
   poetry run invoke setup
   ```
4. Käynnistä sovellus komennolla:
   ```
   poetry run invoke start
   ```

## Komentorivitoiminnot

### Ohjelman käynnistäminen
Ohjelma käynnistyy komennolla:
```
poetry run invoke start
```

### Testaaminen
Testaaminen suoritetaan komennolla:
```
poetry run invoke test
```

### Testikattavuus
Testikattavuusraportin, joka aukeaa selaimeen, voi generoida komennolla:
```
poetry run invoke coverage-report
```

### Pylint-tarkistus
Pylint-tarkistuksen voi suorittaa komennolla:
```
poetry run invoke lint
```
