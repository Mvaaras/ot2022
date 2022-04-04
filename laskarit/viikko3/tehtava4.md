```mermaid
sequenceDiagram

main ->> laitehallinto: HKLLaitehallinto()
main ->> rautatientori: Lukijalaite()
main ->> ratikka6: Lukijalaite()
main ->> bussi244: Lukijalaite()
main ->> laitehallinto: lisaa_lataaja(rautatietori)
main ->> laitehallinto: lisaa_lataaja(ratikka6)
main ->> laitehallinto: lisaa_lataaja(bussi244)
main ->> lippu_luukku: Kioski()
main ->> kallen_kortti: lippu_luukku.osta_matkakortti("Kalle")
kallen_kortti ->>+ lippu_luukku: osta_matkakortti("Kalle")
lippu_luukku ->>- kallen_kortti: Matkakortti("Kalle")
main ->>+ rautatientori: lataa_arvoa(kallen_kortti, 3)
rautatientori ->> kallen_kortti: kasvata_arvoa(3)
rautatientori -->>- main: ‎
main ->>+ ratikka6: osta_lippu(kallen_kortti, 0)
ratikka6 ->> main: RATIKKA
main ->> ratikka6: 1.5
ratikka6 ->> kallen_kortti: arvo
kallen_kortti ->> ratikka6: 3
ratikka6 ->> kallen_kortti: vahenna_arvoa(1.5)
ratikka6 -->>- main: True

main ->>+ bussi244: osta_lippu(kallen_kortti, 0)
bussi244 ->> main: SEUTU
main ->> bussi244: 3.5
bussi244 ->> kallen_kortti: arvo
kallen_kortti ->> bussi244: 1.5
bussi244 -->>- main: False

