# Haavemaa ☁️✨🐚
Haavemaa -sovelluksessa toteutat suurimmatkin haaveesi ja tavoitteesi! Rekisteröitymällä käyttäjäksi voit listata haaveita ja tavoitteita näkyviin, ja näin helposti seurata niiden edistymistä ja merkitä niitä saavutetuiksi. Sovellus toimii myös ohjelmistotekniikan harjoitustyönä. 

## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/aadnw/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/aadnw/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/aadnw/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/aadnw/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Sovelluksen asennusohje
1. Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurihakemistoon.
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

## Testaaminen
Testaaminen suoritetaan komennolla:
```
poetry run invoke test
```

## Testikattavuus
Testikattavuusraportin, joka aukeaa selaimeen, voi generoida komennolla:
```
poetry run invoke coverage-report
```
