# Sovelluksen käyttöohje
Lataa projektin viimeisimmän [releasen](https://github.com/aadnw/ot-harjoitustyo/releases/tag/loppupalautus) lähdekoodi Assets-osion alta kohdasta source code.

## Konfigurointi
Halutessasi voit konfiguroida tallennukseen käytettävät tiedostot haluamallasi tavalla juurihakemiston .env-tiedostossa. Jos näitä tiedostoja ei ole vielä olemassa luodaan ne automaattisesti data-hakemistoon. .env-tiedoston sisältö on seuraava, muuta siis täällä tiedostojen nimet jos haluat:
```
DREAMS_FILENAME=dreams.csv
DATABASE_FILENAME=database.sqlite
```

## Ohjelman käynnistys

1. Ennen ohjelman käynnistystä asenna riippuvuudet komennolla:
   ```
   poetry install
   ```
2. Ja suorita tarvittavat alustustoimenpiteet komennolla:
   ```
   poetry run invoke setup
   ```
3. Käynnistä sovellus komennolla:
   ```
   poetry run invoke start
   ```

## Kirjautuminen
Sovelluksen käynnistyessä avautuu kirjautumissivu. Kirjaudu sisään syöttämällä tekstikenttiin olemassaoleva käyttäjätunnus ja salasana, sekä painamalla sen jälkeen "Kirjaudu sisään" -nappia.
![Kotisivu](https://github.com/user-attachments/assets/fd4fa633-b548-4d14-ae01-3c9f42cc3eff)

## Uuden käyttäjän luominen/rekisteröityminen
Painamalla kirjautumissivulla olevaa "Rekisteröidy tästä" -nappia akueaa rekisteröitymissivu, jossa voi luoda uuden käyttäjätunnuksen syöttämällä tekstikenttiin uniikki 3-20 merkkiä pitkä käyttäjänimi sekä vähintään 5 merkkiä pitkä salasana.
Painamalla "Luo käyttäjä" -nappia uusi käyttäjätunnus rekisteröityy ja siirrytään kotisivulle.
"Takaisin kirjautumissivulle" -nappia painamalla pääsee takaisin kirjautumissivulle.
![Rekisteröitymissivu](https://github.com/user-attachments/assets/13995764-4c8f-4b9d-976c-4fc6003bfa7a)

## Haaveen lisääminen ja saavutetuksi merkitseminen
Uuden haaveen/tavoitteen voi lisätä kirjoittamalla sen "Lisää tavoite" -tekstikenttään, valitsemalla aikarajan kalenterista sekä painamalla "Luo" -nappia. 
![Kotisivu](https://github.com/user-attachments/assets/950f2910-5c47-4187-af8a-004315da7aa7)

Uusi haave ilmestyy kotisivulle ja sen voi merkitä saavutetuksi painamalla "Saavutettu" -nappia, jolloin se häviää näkymästä.
Ulos kirjautuminen tapahtuu painamalla "Kirjaudu ulos" -nappia, jolloin siirrytään takaisin kirjautumissivulle.
![Lisätty haave](https://github.com/user-attachments/assets/db6cabac-923b-4962-9c7a-bf9a64cd9f40)

## Haaveen lisätietojen muokkaaminen
Painamalla kotisivulla haaveen vieressä olevaa "Edistyminen" -nappia aukeaa haaveen edistymistä ja yksityiskohtia kuvaava sivu. Sivulla näkyy päiväkirjamerkintöjä siitä, mitä haaveen saavuttamisen eteen on tehty, kuinka tärkeäksi haave on määritelty sekä monta päivää tavoitteen valmistumiseen on aikaa. Uuden merkinnän voi lisätä kirjoittamalla sen tekstikenttään ja painamalla "Lisää" -nappia. Takaisin kotisivulle pääsee painamalla "Kotisivulle" -nappia.
![Haavesivu](https://github.com/user-attachments/assets/63959a60-1759-4282-bbca-73faa9de95ca)

Uudella haavella on pienin mahdollinen prioriteetti (1/5), mutta sen voi muuttaa oikeassa alalaidassa aukeavasta pudotusvalikosta, jossa näkyy senhetkinen tähtimäärä (1).
![Tähtien asettaminen](https://github.com/user-attachments/assets/0a2b1cb4-b35c-4219-933b-b860c558b814)

## Haaveen poistaminen
Haaveen voi poistaa painamalla "Poista haave" -nappia, jolloin sivulle aukeaa vahvistusikkuna. Painamalla "Kyllä", haave ja siihen liittyvät päiväkirjamerkinnät poistuvat pysyvästi ja palaat kotisivulle. 
![Haaveen poistaminen](https://github.com/user-attachments/assets/33d924a2-3ce4-41d3-9f08-c94021e39574)

## Haaveiden järjestäminen
Kotisivulla haaveita voi järjestää eri tavoin painamalla "Järjestä" -nappia, ja valitsemalla mieluisan järjestyksen, joita ovat: tärkeimmät ensin, tavoiteaika ensin, uusin ensin ja vanhin ensin.
![Järjestä haaveet](https://github.com/user-attachments/assets/9caaf320-55d5-4abc-880c-079b2fc05e77)

## Käyttäjätunnusten poistaminen
Jos haluat poistaa käyttäjätunnuksesi järjestelmästä, voit tehdä sen painamalla "Poista käyttäjä" -nappia. Tällöin sivulle aukeaa vahvistusikkuna. Painamalla "Kyllä" käyttäjätunnuksesi, haaveesi sekä niihin liittyvät päiväkirjamerkinnät poistuvat pysyvästi, ja sinut palautetaan kotisivulle. Voit halutessasi luoda uuden käyttäjätunnuksen rekisteröitymällä aikaisemman ohjeen mukaan.
![Käyttäjätunnusten poistaminen](https://github.com/user-attachments/assets/e72a5d63-3e7e-44b6-b46b-b8254266dc76)
