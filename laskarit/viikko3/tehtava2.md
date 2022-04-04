```mermaid
 classDiagram
      Pelilauta "1" --> "40" Ruutu
      Ruutu "1" --> "1" Ruutu
      Monopolipeli "1" -- "2..8" Pelaaja
      Monopolipeli "1" -- "1" Pelilauta
      Pelaaja "1" -- "1" Pelinappula
      Pelinappula "1" ..> "1" Ruutu
      Monopolipeli "1" -- "2" Noppa
      Pelaaja "1" ..> "2" Noppa
      Aloitusruutu --|>   Ruutu
      Vankila --|>   Ruutu
      Sattuma --|>   Ruutu
      Yhteismaa --|>   Ruutu
      Asema --|> Ruutu
      Laitos --|>   Ruutu
      Katu --|>   Ruutu
      Monopolipeli "1" --> "1" Vankila
      Monopolipeli "1" --> "1" Aloitusruutu
      Sattuma "1" ..> "1" Kortti
      Yhteismaa "1" ..> "1" Kortti
      Kortti "1" -- "1" Toiminto
      Ruutu "1" -- "1" Toiminto
      Katu "1" ..> "0..3" Talo
      Katu "1" ..> "0..1" Hotelli
      Katu "1" .. "0..1" Pelaaja
      Pelaaja "1" --> "*" Raha 
      
      class Katu {
      Nimi
      }
```
