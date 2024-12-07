# Gravity glide

U ovom zadatku potrebno je implementirati igricu u kojoj igrač kontrolira svemirski brod. Svemirski brod se kreće automatski horizontalno i prati trenutni smjer gravitacije. Cilj igrice je izbjegavati asteroide i ostale prepreke, a skupiti što više novca. Svemirski brod također može pokupiti _power-upove_

## Statički funkcionalni zahtjevi

Sljedeći zahtjevi moraju biti ispunjeni za maksimalan broj bodova.

1. Pritiskom tipke `space`, smjer gravitacije se mijenja za 180. Početni smjer gravitacije je pozitivan (y koordinata raste s vremenom)
1. Svemirski brod stalno ima horizontalnu brzinu
1. Dinamički i nasumično se stvaraju prepreke. Prepreke mogu biti asteroidi koji se nalaze u sredini ili šiljci koji se nalaze na dnu ili na vrhu prozora.
1. Nasumično se stvaraju novčići koji povećavaju broj ostvarenih bodova
1. Nasumično se stvaraju _power-upovi_.
1. Štit _power-up_ omogućuje svemirskom brodu preživljavanje kolizije s nekom preprekom
1. Magnet _power-up_ omogućuje svemirskom brodu skupljanje svih novčića pored kojih prođe
1. Sudar s nekom preprekom prekida igru
1. Sudar s vrhom ili dnom prozora također prekida igru

## Dinamički funkcionalni zahtjevi

1. Promjena postavki igre (brzina balona, brzina prepreka ...) na jednom mjestu
2. Dodavanje novih vrsta prepreka i mogućnost upravljanja preprekama kao flotom i jednostavno računanje kolizija
3. Mogućnost dodavanja novih vrsta _power-upova_
4. Jednostavna mogućnost promjene postojećih prepreka
5. Jednostavna promjena načina stvaranja objekata u igri (više/manje prepreka, više/manje _power-upova_)

Neki oblikovni obrasci će biti neophodni, dok bez nekih drugih možete. Ovdje nisu svi dinamički zahtjevi navedeni, zato što je njih teško definirati u statičkom kontekstu. Razmišljajte prilikom oblikovanja da vaše rješenje prati SOLID principe (to u pravilu, omogućavaju obrasci) i shodno tome oblikujte vaše rješenje. Ne postoji samo jedan ispravan način, ali očekuje se da možete jasno argumentirati vaš pristup. Fokus ovog kolegija nije na slijepoj primjeni obrazaca, već na razvoju inženjerskog načina razmišljanja.

## Savjeti

Nije potrebno ulagati previše vremena za dizajn vaše igre te možete koristit već gotove slike za objekte unutar igre. Postoji više takvih kolekcija, a jedna od popularnijih je [ova](https://itch.io/game-assets/free/tag-pixel-art). Preporučam korištenje pikseliziranih slika.

Poželjno je da brzina svemirskog broda i ostalih elemenata ne ovisi o brzini iscrtavnja (_frame rate_) već o proteklom vremenu, kako bi se igra slično ponašala na računalima različitih performansi.
