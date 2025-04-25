# Sovelluksen käyttöohje

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
![Kirjautumissivu](https://github.com/user-attachments/assets/a10f0988-d2a9-4cbb-bb56-b1ea806871ed)

## Uuden käyttäjän luominen/rekisteröityminen
Painamalla kirjautumissivulla olevaa "Rekisteröidy tästä" -nappia akueaa rekisteröitymissivu, jossa voi luoda uuden käyttäjätunnuksen syöttämällä tekstikenttiin uniikki 3-20 merkkiä pitkä käyttäjänimi sekä vähintään 5 merkkiä pitkä salasana.
Painamalla "Luo käyttäjä" -nappia uusi käyttäjätunnus rekisteröityy ja siirrytään kotisivulle. "Takaisin kirjautumissivulle" -nappia painamalla pääsee takaisin kirjautumissivulle.
![Rekisteröitymissivu](https://github.com/user-attachments/assets/13995764-4c8f-4b9d-976c-4fc6003bfa7a)

## Haaveen lisääminen ja saavutetuksi merkitseminen
Uuden haaveen/tavoitteen voi lisätä kirjoittamalla sen "Lisää tavoite" -tekstikenttään sekä painamalla "Luo" -nappia. 
![Kotisivu](https://github.com/user-attachments/assets/fe8a2326-f032-41e0-b80c-869dcfc43da0)

Uusi haave ilmestyy kotisivulle ja sen voi merkitä saavutetuksi painamalla "Saavutus" -nappia, jolloin se häviää näkymästä.
Ulos kirjautuminen tapahtuu painamalla "Kirjaudu ulos" -nappia, jolloin siirrytään takaisin kirjautumissivulle.
![Lisätty haave](https://github.com/user-attachments/assets/6b77879c-43cd-4dbc-a99a-c5773cce2bee)

## Haaveen lisätietojen muokkaaminen
Painamalla kotisivulla haaveen vieressä olevaa "Edistyminen" -nappia aukeaa haaveen edistymistä ja yksityiskohtia kuvaava sivu. Sivulla näkyy päiväkirjamerkintöjä siitä, mitä haaveen saavuttamisen eteen on tehty. 
Uuden merkinnän voi lisätä kirjoittamalla sen tekstikenttään ja painamalla "Lisää" -nappia. Uudella haavella on pienin mahdollinen prioriteetti (1/5), mutta sen voi muuttaa oikeassa alalaidassa aukeavasta pudotusvalikosta, jossa näkyy senhetkinen tähtimäärä (1).
Haaveen voi poistaa painamalla "Poista haave" -nappia. Takaisin kotisivulle pääsee painamalla "Kotisivulle" -nappia.
![Haavesivu](https://github.com/user-attachments/assets/69f34ccc-2184-4bca-b422-03912017ab70)




