#!/usr/bin/env python3
"""Program som skapar två Bil-objekt, tilldelar värden och skriver ut dem.

Detta visar hur Bil-klassen kan användas med init-värden och ägare.
"""

from Bil import Bil
from person import Person


def main():
    # Skapa ägare
    agare1 = Person("Anna Andersson")
    agare2 = Person("Björn Berg")

    # Skapa två Bil-objekt med initieringsvärden
    bil1 = Bil(registreringsnummer="ABC123", fabrikat="Volvo", arsmodell=2020,
               tjanstevikt=1600, motoreffekt=150, agare=agare1)

    bil2 = Bil(registreringsnummer="XYZ987", fabrikat="Toyota", arsmodell=2018,
               tjanstevikt=1400, motoreffekt=120, agare=agare2)

    # Skriv ut information om bilarna
    print("Bil 1:")
    print(bil1)
    print()
    print("Bil 2:")
    print(bil2)


if __name__ == "__main__":
    main()
