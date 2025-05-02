# Testausdokumentti
Sovellusta on testattu automatisoidusti pytestillä yksikkö- ja integraatiotasolla. Järjestelmän testaus on suoritettu manuaalisesti. 

## Yksikkö- ja integraatiotestaus
### Sovelluslogiikka
`DreamlandLogic`-luokka, joka vastaa sovelluslogiikasta testataan testiluokalla [TestDreamlandLogic](https://github.com/aadnw/ot-harjoitustyo/blob/master/src/tests/dreamland_logic_test.py). DreamlandLogic-olio alustetaan injektoimalla repositories-oliot riippuvuuksiksi, jota varten on luotu testiluokat `FakeDreamRepositoryForTesting`, `FakeUserRepositoryForTesting` ja `FakeDiaryRepositoryForTesting`, jotka tallentavat tiedot muistiin. 

### Repositorio-luokat
Luokkia `DreamRepository`, `UserRepository` ja `DreamRepository` testataan vain testikäytössä olevalla csv-tiedostolla ja sqlite-tietokannalla, jotka on konfiguroitu .env.test-tiedostossa. Repositorio-luokkia vastaavat testiluokat ovat [TestDreamRepository](https://github.com/aadnw/ot-harjoitustyo/blob/master/src/tests/dream_repository_test.py), [TestUserRepository](https://github.com/aadnw/ot-harjoitustyo/blob/master/src/tests/user_repository_test.py) ja [TestDiaryRepository](https://github.com/aadnw/ot-harjoitustyo/blob/master/src/tests/diary_repository_test.py). 

## Testikattavuus 
Sovelluksen haaraumakattavuus käyttöliittymää lukuunottamatta on 96%
![Haaraumakattavuus](https://github.com/user-attachments/assets/02ea8766-cd4a-4787-aa8d-aba48857a007)
Testaamatta jäi konfiguraatiotiedosto __config.py__ sekä __build.py__ ja __initialize_database.py__, jotka olisi voinut jättää myös testikattavuuden ulkopuolelle. 

## Järjestelmätestaus
Järjestelmä on testattu manuaalisesti. Sovellus on asennettu ja testattu [käyttöohjeen](https://github.com/aadnw/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) mukaan Linux-ympäristössä. Sovellusta on myös testattu eri konfiguraatioilla [.env](https://github.com/aadnw/ot-harjoitustyo/blob/master/.env)-tiedoston kautta sekä tilanteissa, joissa tallennukseen käytettävät tiedostot on luotu etukäteen tai ne luodaan jos niitä ei ole vielä olemassa.

Kaikki [määrittelydokumentin](https://github.com/aadnw/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) ja käyttöohjeen kuvaamat toiminnallisuudet ja tilanteet on käyty läpi, myös virheellisillä syötteillä, jolloin on testattu samalla virheilmoitusten toiminnallisuutta. 
