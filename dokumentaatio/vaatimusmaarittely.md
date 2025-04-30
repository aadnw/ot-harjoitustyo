# Vaatimusmäärittely

## Sovelluksen idea
Haavemaa on sovellus, jossa käyttäjä voi ideoida, tutkia ja seurata omia haaveitaan ja tavoitteitaan, sekä matkaa niitä kohti. Käyttäjä voi rekisteröityä Haavemaahan ja näin luoda omia haaveita/tavoitteita ja seurata niiden edistymistä. Sovelluksessa voi olla useampia uniikkeja peruskäyttäjiä, joilla kaikilla on omat yksilölliset haaveet.

## Käyttöliittymä
Sovellus koostuu neljästä eri näkymästä: 
![Käyttöliittymä](https://github.com/user-attachments/assets/08670498-1e9d-4461-8cff-04a06b5a7407)
Sovellus käynnistyy kirjautumissivulle, josta pääsee rekisteröitymissivulle luomaan uuden käyttäjätunnuksen. Rekisteröitymällä oikeilla tunnuksilla tai kirjautumalla jo olemassa olevilla tunnuksilla sisään, pääsee kotisivulle. Kotisivulla näkyy käyttäjän haaveet ja tavoitteet, sekä niitä voi luoda lisää. Takaisin kirjautumissivulle pääsee kirjautumalla ulos. Jos poistaa käyttäjätunnukset, päätyy myös takaisin kirjautumissivulle. Kotisivulla voi myös asettaa haaven saavutetuksi. Lisätietoja haaveesta näkee siirtymällä haaveen vierestä haavesivulle, jossa näkyy päiväkirjamerkintöjä, haaveen aikaraja sekä tärkeys. Näitä tietoja voi lisätä ja muokata haavesivulla. Haavesivulta pääsee takaisin kotisivulle painamalla siihen tarkoitettua nappia. Myös haaveen poistaessa siirrytään takaisin kotisivulle.

## Sovelluksen toiminnallisuus
### Ennen kirjautumista:
- Käyttäjä voi luoda käyttäjätunnuksen, jonka tulee olla uniikki ja 3-20 merkkiä pitkä sekä salasanan, jonka tulee olla vähintään 5 merkkiä pitkä. Jos jokin näistä ehdoista ei täyty, tulee siitä ilmoitus.
- Käyttäjä voi kirjautua sisään syöttämällä käyttäjätunnuksen ja salasanan. Jos käyttäjää ei ole olemassa tai tunnus/salasana ei täsmää, tulee siitä ilmoitus.
### Kirjautumisen jälkeen:
- Käyttäjä näkee omat haaveet/tavoitteet.
- Käyttäjä näkee etusivulla kannustavia, motivoivia ja inspiroivia tekstejä.
- Käyttäjä voi lisätä uuden haaveen/tavoitteen kirjoittamalla sen tekstikenttään sekä valitsemalla tavoiteajan.
- Käyttäjä voi merkitä haaveen/tavoitteen saavutetkuksi, jolloin se häviää näkymästä.
- Käyttäjä voi kirjautua ulos.
- Käyttäjä voi päiväkirjanomaisesti pitää kirjaa siitä, mitä konkreettista on tehnyt haaveen/tavoitteen saavuttamiseksi.
- Käyttäjä voi merkitä tärkeys "pisteitä" haaveelle/tavoitteelle.
- Käyttäjä voi järjestää haaveet/tavoitteeet eri tavoin: tärkein ensin, aikaraja ensin, uusin ensin, vanhin ensin.
- Käyttäjä voi poistaa haaveen/tavoitteen. Poistaminen tulee vahvistaa.
- Käyttäjä voi poistaa käyttäjätunnuksen järjestelmästä. Poistaminen tulee vahvistaa.
