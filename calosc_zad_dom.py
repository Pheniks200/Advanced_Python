#generator nowych zamówień
#wykorzystanie generatora 
def nowe_zamowienie():
    numer = 1
    while True:
        yield f"ZAMOWIENIE/2026/{numer}"
        numer += 1

# dodawanie nowych produktów do koszyka
# wykorzystanie zmiennej liczby argumentów
koszyk_klienta = []
def do_koszyka(*produkty):
    for przedmiot in produkty:
        koszyk_klienta.append(przedmiot)

#podawanie kodu rabatowego
#funkcja łańcuchu znaków
#przynależność
#typowanie funkcji 
zestaw_akt_kodow = ["WARS", "PROM", "OKAZJA"]
rabat_z_kodu = 0
def podaj_kod(kod: str) -> float:
    kod = kod.upper().strip()
    if kod in zestaw_akt_kodow:
        return 0.1   
    else:
        return 0.0

#karta lojalnosciowa
# instrukcja match 

def karta_lojalnosciowa(poziom_klienta: int):
    match poziom_klienta:
        case 1:
            return 0.1
        case 2:
            return 0.15
        case 3: 
            return 0.2
        case _:
            return 0
        
#Przywitanie
#wykorzsytanie funkcji łańcucha znaków
def przywitanie(imie: str):
    imie = imie.strip().capitalize()
    
    return(f"Dzień dobry {imie}. \nOto twoje podsumowanie zakupu:\n\n")

#Podsumowanie zamówienia

#argument domyślny
def podsumowanie(podane_imie, podany_poziom_klienta,podany_kod, waluta = "PLN"):

    wartosc_koszyka = sum(produkt["cena"] for produkt in koszyk_klienta)

    rabat= karta_lojalnosciowa(podany_poziom_klienta) + podaj_kod(podany_kod)

    # operator warunkowy (potrójny) 
    koszt_dostawy = 0 if wartosc_koszyka > 100 else 15
    
    suma_koncowa = wartosc_koszyka - wartosc_koszyka*rabat + koszt_dostawy

    #funkcja anonimowa
    koszyk_klienta.sort(key=lambda p: p["cena"], reverse=True)

    generator = nowe_zamowienie()
    nr_zamowienia = next(generator)

    #zastowanie instrukcji with
    #formatowanie łańcucha znaków
    with open("zapisane_podsumowanie_2.txt", "w", encoding="utf-8") as plik:
        plik.write(f"\t SKLEP U PIOTRA\n\n")
        plik.write(przywitanie(podane_imie))
        plik.write(f"Twój numer zamówienia to: {nr_zamowienia}\n")
        for p in koszyk_klienta:
            plik.write(f"- {p['nazwa']}: {p['cena']:.2f} {waluta}\n")
        plik.write(f"\nWartość koszyka przed rabatem i bez kosztów dostawy: {wartosc_koszyka:.2f} {waluta}\n")
        plik.write(f"Przyznano {rabat*100}% rabatu\n")
        plik.write(f"Koszt dostawy {koszt_dostawy:.2f} {waluta}\n")
        plik.write(f"\nDO ZAPŁATY: {suma_koncowa:.2f} {waluta}\n ")

 # test programu

if __name__ == '__main__':

    produkt1 = {"nazwa": "Słuchawki", "cena": 150.0}
    produkt2 = {"nazwa": "Klawiatura Mechaniczna", "cena": 320.0}
    produkt3 = {"nazwa": "Podkładka", "cena": 40.0}

    do_koszyka(produkt1, produkt2, produkt3)
    
    # argumenty nazwane
    podsumowanie(
       podane_imie = "Antek",podany_kod = "WARS", podany_poziom_klienta = 2
    )