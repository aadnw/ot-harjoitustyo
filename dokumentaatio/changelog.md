## Viikko 3
- Käyttäjä voi kirjautua sisään
- Käyttäjä voi kirjautua ulos
- Käyttäjä näkee etusivun kirjautumalla sisään
- Käyttäjä voi luoda uuden käyttäjätunnuksen eli rekisteröityä käyttäjäksi
- Lisätty User-luokka, joka vastaa käyttäjän tiedoista
- Lisätty DreamlandLogic-luokka, joka vastaa sovelluslogiikasta
- Lisätty UserRepository-luokka, joka vastaa käyttäjien tallentamisesta CSV-tiedostoon
- Lisätty TestUserRepository-luokka, joka vastaa UserRepository-luokan testaamisesta
- Lisätty HomepageView- ja DreamListView-luokka, jotka vastaavat kotisivun näkymästä
- Lisätty LoginView-luokka, joka vastaa kirjautumissivun näkymästä
- Lisätty RegistrationView-luokka, joka vastaa rekisteröitymissivun näkymästä
- Lisätty UI-luokka, joka vastaa käyttöliittymästä

## Viikko 4
- Käyttäjä voi luoda uusia haaveita etusivulla
- Käyttäjä näkee saavuttamattomat haaveensa etusivulla
- Käyttäjä voi merkitä haaven saavutetuksi, jolloin se katoaa näkyvistä
- Lisätty Dream-luokka, joka vastaa haaveiden sisällöstä
- Lisätty DreamRepository-luokka, joka vastaa haaveiden tallentamisesta CSV-tiedostoon
- Lisätty TestDreamRepository-luokka, joka vastaa DreamRepository-luokan testaamisesta

## Viikko 5
- Käyttäjä voi päiväkirjanomaisesti pitää kirjaa siitä, mitä on tehnyt haaveensa saavuttamisen eteen
- Lisätty Diary-luokka, joka vastaa haaveeseen liittyvistä päiväkirjamerkinnöistä
Lisätty 
- Lisätty DiaryRepository-luokka, joka vastaa päiväkirjamerkintöjen tallentamisesta tietokantaan
- Lisätty DreamView- ja DiaryListView-luokka, jotka vastaavat haaveen yksityiskohdista ja etenemisestä vastaavasta näkymästä
- Lisätty TestDreamlandLogic-luokka, joka vastaa DreamlandLogic-luokan testaamisesta
- Lisätty TestDiaryRepository-luokka, joka vastaa DiaryRepository-luokan testaamisesta

## Viikko 6
- Käyttäjä voi asettaa tähtiä haaveelle merkitsemään sen tärkeyttä
- Käyttäjä voi poistaa haaveen, jolloin haave ja siihen liittyvä päiväkirja poistuu kokonaan
- Käyttäjä voi poistaa käyttäjätunnuksensa, jolloin käyttäjä, sen haaveet sekä niihin liittyvät päiväkirjat poistuvat kokonaan
- Käyttäjä voi järjestää haaveensa etusivulla seuraavilla tavoilla: tärkein ensin, aikaraja ensin, uusin ensin, vanhin ensin
- Käyttäjän tulee vahvistaa käyttäjätunnusten tai haaveen poistaminen uudesta ikkunasta
- Lisätty FormHandler-luokka, jonka kautta View-luokat saavat käyttöönsä attribuutteja ja argumentteja
