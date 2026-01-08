# PotionMixer

U ovom zadatku potrebno je implementirati igricu u kojoj igrač kontrolira alkemista u laboratoriju koji mora miješati napitke prema dolazećim sastojcima i pritom izjegavati otrove. Cilj igre je napraviti što više ispravnih napitaka i osvojiti što više bodova. Postoje _power-upovi_ koji mijenjaju dijelove igre, npr. usporavaju dolazak sastojaka ili udvostručuju bodove.

## Statički funkcionalni zahtjevi

Sljedeći zahtjevi moraju biti ispunjeni za maksimalan broj bodova.

1. Igrač može pomicati posudu gore i dolje tipkama `w` i `s`.
2. Sastojci dolaze s desne strane ekrana i pomiču se prema lijevoj strani.
3. Sudar s zabranjenim sastojkom (otrovom) poništava napitak; nakon previše grešaka igra završava i korisniku se prikazuje broj bodova.
4. Sastojci i _power-upovi_ koji izađu s lijevog ruba zaslona brišu se iz memorije.
5. Cijelo vrijeme se mora prikazivati i osvježavati trenutačni broj ispravnih napitaka kao i najbolji rezultat svih pokušaja.
6. Igrač može pokupiti barem dva različita _power-upa_. Dovoljno je da jedan sastojak dođe do posude.
8. _Double Mix_ _power-up_ određeno vrijeme udvostručuje bodove za sve ispravne napitke.
9. Sastojci i _power-upovi_ generiraju se proceduralno (nasumično). Moraju postojati barem dvije brzine sastojaka.
10. Moraju postojati barem tri posude koje igrač može birati numeričkim tipkama. Također omogućite automatsku promjenu posuda pritiskom na tipku. Promjenom posude napitci u posudi se ne brišu. Na ovaj način igrač može miješati više napitaka istodobno
11. Zaslon mora biti podijeljen u dva dijela, na donjem dijelu se nalazi popis posuda i sastojaka koji su trenutno u njima, kao i popis svih recepata koji postoje. 

## Dinamički funkcionalni zahtjevi

Uz obavezne statičke zahtjeve, potrebno je ispuniti i generalne dinamičke zahtjeve:

1. Promjena postavki igre (brzina sastojaka, trajanje power-upova ...) na jednom mjestu.
2. Dodavanje novih vrsta sastojaka ili napitaka.
3. Mogućnost dodavanja novih vrsta _power-upova_.
4. Jednostavna mogućnost promjene postojećih sastojaka.
5. Jednostavna mogućnost dodavanja nove težine igre.
6. Jednostavna mogućnost dodavanja novih posuda.
7. Jednostavna mogućnost dodavnja "tetris" moda gdje postoji samo jedan ispravan napitak i 5 posuda. Igrač ne smije propustiti ni jedan napitak. U slučaju da se jedna posuda napuni, ili dođe u stanje u kojem nije moguće napraviti validan napitak igrač gubi život

## Savjeti

Nije potrebno ulagati previše vremena za dizajn grafike. Možete koristiti jednostavne oblike (kvadratići i krugovi) za sastojke, posudu i power-upove.  
Poželjno je da brzina sastojaka i power-upova ne ovisi o brzini iscrtavanja (_frame rate_) već o proteklom vremenu, kako bi se igra ponašala isto na računalima različitih performansi.
