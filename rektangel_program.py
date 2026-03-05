#!/usr/bin/env python3
"""Program som läser in höjd och bredd för ett godtyckligt antal rektanglar.

Programmet skapar en ny Rektangel per varv i while-loopen, sätter höjd och bredd
via set-metoder och skriver ut area och omkrets. Avsluta genom att trycka Enter
vid prompten för höjd eller bredd.
"""

from rektangel import Rektangel


def main():
    print("Skriv in höjd och bredd för rektanglar. Tom rad för att avsluta.")
    while True:
        hojd_str = input("Höjd: ").strip()
        if hojd_str == "":
            print("Avslutar.")
            break
        bredd_str = input("Bredd: ").strip()
        if bredd_str == "":
            print("Avslutar.")
            break

        try:
            hojd = float(hojd_str)
            bredd = float(bredd_str)
        except ValueError:
            print("Ogiltigt tal. Försök igen.")
            continue

        r = Rektangel()
        r.set_hojd(hojd)
        r.set_bredd(bredd)

        print(f"Area: {r.area()}")
        print(f"Omkrets: {r.omkrets()}")
        print()


if __name__ == "__main__":
    main()
