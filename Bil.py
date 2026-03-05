#!/usr/bin/env python3
"""Modul med klassen Bil.

Klassen beskriver en bil med registreringsnummer, fabrikat, årsmodell,
tjänstevikt, motoreffekt och en referens till ägaren (Person).
"""

class Bil:
    """Representerar en bil.

    Attribut (kan ges i konstruktorn):
    - registreringsnummer (str)
    - fabrikat (str)
    - arsmodell (int)
    - tjanstevikt (int) i kg
    - motoreffekt (int) i hk
    - agare (valfri referens, t.ex. ett Person-objekt)
    """

    def __init__(self, registreringsnummer="", fabrikat="", arsmodell=None,
                 tjanstevikt=None, motoreffekt=None, agare=None):
        self.registreringsnummer = registreringsnummer
        self.fabrikat = fabrikat
        self.arsmodell = arsmodell
        self.tjanstevikt = tjanstevikt
        self.motoreffekt = motoreffekt
        self.agare = agare

    def __str__(self):
        agare_str = str(self.agare) if self.agare is not None else "Ingen"
        parts = [
            f"Registreringsnummer: {self.registreringsnummer}",
            f"Fabrikat: {self.fabrikat}",
            f"Årsmodell: {self.arsmodell}",
            f"Tjänstevikt: {self.tjanstevikt} kg",
            f"Motoreffekt: {self.motoreffekt} hk",
            f"Ägare: {agare_str}"
        ]
        return " | ".join(parts)


if __name__ == "__main__":
    # När man kör filen direkt händer inget enligt uppgiften (inget program ännu).
    pass
