#!/usr/bin/env python3
"""Modul med klassen Rektangel.

Rektangel har en startpunkt (övre vänstra hörnet), samt höjd och bredd.
Höjd och bredd hålls privata och hanteras via get/set-metoder.
"""

class Rektangel:
    def __init__(self, startpunkt=(0, 0), hojd=0, bredd=0):
        self.startpunkt = startpunkt
        # privata variabler
        self.__hojd = hojd
        self.__bredd = bredd

    # Setters
    def set_hojd(self, value):
        if value < 0:
            raise ValueError("Höjden måste vara icke-negativ")
        self.__hojd = value

    def set_bredd(self, value):
        if value < 0:
            raise ValueError("Bredden måste vara icke-negativ")
        self.__bredd = value

    # Getters
    def get_hojd(self):
        return self.__hojd

    def get_bredd(self):
        return self.__bredd

    # Beräkningar
    def area(self):
        return self.__hojd * self.__bredd

    def omkrets(self):
        return 2 * (self.__hojd + self.__bredd)

    def __str__(self):
        return f"Startpunkt: {self.startpunkt}, Höjd: {self.__hojd}, Bredd: {self.__bredd}"


if __name__ == "__main__":
    # Ingen demo här — separat program körs i rektangel_program.py
    pass
