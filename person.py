#!/usr/bin/env python3
"""En enkel Person-klass som kan användas som bilägare."""

class Person:
    def __init__(self, namn):
        self.namn = namn

    def __str__(self):
        return self.namn

    def __repr__(self):
        return f"Person({self.namn!r})"
