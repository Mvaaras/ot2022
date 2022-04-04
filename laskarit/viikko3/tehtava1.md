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
      
```
