# Euroviisupisteytyssovellus

Tietokantasovellukseni on sovellus, joka on tarkoitettu Euroviisu-kappaleiden pisteyttämiseen ja kommentoimiseen. <br>
Kommentteja voi lukea kuka tahansa käyttäjä, mutta niiden kirjoittamista sekä pisteyttämistä varten täytyy luoda käyttäjätunnus. <br>
Sisäänkirjautunut käyttäjä näkee listauksen antamistaan pisteistä sekä kommenteista. Käyttäjä voi myös halutessaan päivittää antamansa pisteet. <br>
Sovelluksessa on myös ylläpitäjiä, jotka voivat tarvittaessa poistaa kommentteja esimerkiksi epäasiallisuuden vuoksi. <br>
<p>
  
[Tietokantakaavio](https://github.com/tirhelen/tietokantasovellus/blob/main/datastructure.png)
  
<strong> Lopullinen tilanne ja ominaisuudet: </strong> <br>
- Sovellukseen voi luoda käyttäjätilin. <br>
   - Käyttäjänimen tulee olla uniikki ja salasanan vähintään 8 merkkiä pitkä, jotta 	rekisteröityminen onnistuu. <br>
- Käyttäjä voi kirjautua sisään. <br>
  - Käyttäjän kirjautuessa sisään luodaan csrf-token. <br>
- Sisäänkirjautunut käyttäjä voi antaa kappaleille pisteitä sekä nähdä koosteen antamistaan pisteistä ja kommenteista. <br>
  - Käyttäjä näkee omalla sivullaan myös ne kommentit, jotka ylläpitäjä on poistanut. <br>
  - Käyttäjä pystyy muuttamaan antamiaan pisteitä. Pisteiden tulee olla 0-12. <br>
- Sisäänkirjautunut käyttäjä voi kommentoida kappaleita. <br>
	- Kommenttien tulee olla alle 5000 merkkiä. <br>
- Käyttäjä voi lukea muiden kommentteja, vaikka ei olisi kirjautunut sisälle tai luonut käyttäjätiliä. <br>
- Ylläpitäjä voi poistaa kommentteja. <br>
- Käyttäjä voi kirjautua ulos. <br>
  - Samalla poistetaan csrf-token. <br>
  
<p>
  
<strong> Sovelluksen testaaminen: </strong> <br>
Sovellus löytyy osoitteesta: https://tsoha-euron-visiot.herokuapp.com/ <br>
Sovellusta voi kokeilla tavallisena käyttäjänä tunnuksilla: <br>
nimi: testityyppi <br>
salasana: tsoha <br>
<p>
Sovellusta voi kokeilla ylläpitäjänä tunnuksilla: <br>
nimi: ylläpitäjätyyppi <br>
salasana: hyväsalana <br>
