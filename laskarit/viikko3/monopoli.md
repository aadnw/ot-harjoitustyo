
```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Monopolipeli "1" -- "1" Aloitusruutu
    Monopolipeli "1" -- "1" Vankila
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "5" Toiminto
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Ruutu "1" -- "1" Aloitusruutu
    Ruutu "1" -- "1" Vankila
    Ruutu "1" -- "3" Sattuma
    Sattuma "1" -- "10" Kortit
    Ruutu "1" -- "3" Yhteismaa
    Yhteismaa "1" -- "10" Kortit
    Ruutu "1" -- "4" Asemat
    Ruutu "1" -- "2" Laitokset 
    Ruutu "1" -- "22" Normaalit kadut
    Normaalit kadut "1" -- "1..4" Talo
    Normaalit kadut "1" -- "1" Hotelli
    Normaalit kadut "1" -- "1" Pelaaja
    Kortit "1" -- "1" Toiminto
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Pelaaja "1" -- "1-1000" Raha
```