
# Squadron

U ovom zadatku potrebno je implementirati igricu u kojoj igrač kontrolira flotu od dva aviona koja mora izbjegavati projektile. Cilj igre je preći što veću udaljenost i time osvojiti što više bodova. Postoji mogućnost skupljanja _power-upova_ koji mijenjaju dijelove igre. 

## Statički funkcionalni zahtjevi

Sljedeći zahtjevi moraju biti ispunjeni za maksimalan broj bodova.

1. Avioni se pomiču skupa uvijek na istoj distanci jedan od drugog. U slučaju da jedan avion dođe do ruba zaslona, drugi se također ne smije pomicati.
2. Pritiskom na tipke `w` i `s` avioni se pomiču vertikalno
3. U trenutku kolizije jednog od aviona s projektilom igra završava i korisniku se prikazuje broj bodova
4. Projektili se pomiču s desna na lijevo na fiksnoj visni
5. Projektili se izlaskom kroz lijevi rub zaslona brišu s memorije
6. Cijelo vrijeme se mora prikazivati i osvježavati trenutačno pređen put kao i najdulji put od svih pokušaja
7. Flota može pokupiti barem dva različita _power-upa_. Dovoljno je da jedan avion napravi koliziju s _power-upom_. 
8. Štit _power-up_ određeno vrijeme omogućava koliziju balona s preprekama bez kraja igre
9. Povećalo _power-up_ određeno vrijeme smanjuje veličinu svih projektila koji trenutno postoje za 50%
10. Projektili i _power-upovi_ generiraju se proceduralno (nasumično) te morate omogućiti barem dvije težine, s manje i više projektila. Moraju postojati barem dvije veličine projektila.
11.  Moraju postojati barem tri fromacije flote koje se izabiru numeričkim tipkama. Primjerice avioni koji su jako blizu, srednje razmaknuti i značajno razmaknuti. Morate omogućiti automatsku promjenu flote pritiskom na tipku.

## Dinamički funkcionalni zahtjevi

Uz obavezne statičke zahtjeve, potrebno je ispuniti i generalne dinamičke zahtjeve. Morate osmisliti takvu arhitekturu koja će omogućiti lako održavanje i nadogradnju igre. Sljedeće stavke moraju biti ispunjene za maksimalne bodove.

1. Promjena postavki igre (brzina aviona, brzina projektila ...) na jednom mjestu
2. Dodavanje novih vrsta projektila 
3. Mogućnost dodavanja novih vrsta _power-upova_
4. Jednostavna mogućnost promjene postojećih prepreka
5. Jednostavna mogućnost dodavanja nove težine
6. Jednostavna mogućnost dodavanja novih formacija


Neki oblikovni obrasci će biti neophodni, dok bez nekih drugih možete. Ovdje nisu svi dinamički zahtjevi navedeni, zato što je njih teško definirati u statičkom kontekstu. Razmišljajte prilikom oblikovanja da vaše rješenje prati SOLID principe (to u pravilu, omogućavaju obrasci) i shodno tome oblikujte vaše rješenje. Ne postoji samo jedan ispravan način, ali očekuje se da možete jasno argumentirati vaš pristup. Fokus ovog kolegija nije na slijepoj primjeni obrazaca, već na razvoju inženjerskog načina razmišljanja.

## Savjeti

Nije potrebno ulagati previše vremena za dizajn vaše igre te možete koristit već gotove slike za objekte unutar igre. Postoji više takvih kolekcija, a jedna od popularnijih je [ova](https://itch.io/game-assets/free/tag-pixel-art). Preporučam korištenje pikseliziranih slika.

Poželjno je da brzina aviona i ostalih elemenata ne ovisi o brzini iscrtavnja (_frame rate_) već o proteklom vremenu, kako bi se igra slično ponašala na računalima različitih performansi.
