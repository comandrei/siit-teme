"""
Masini
Modelati folosind OOP caracteristicile unui vechiul.

Puteti porni de la o structura de forma:

 class Vehicul:

   # viteza maxima

   # capacitate motor

  #capacitate portbagaj

 # nume

  # tip - sedan/ SUV

Faceti mai multe instante de masini si afisati topul celor mai:

 1. rapide

 2. spatioase



Ca hint: la sorted puteti folosi key=obj.attr
"""

class Vehicul:
    def __init__(self, producator, model, viteza_maxima, capacitate_portbagaj):
        self.producator = producator
        self.model = model
        self.viteza_maxima = viteza_maxima
        self.capacitate_portbagaj = capacitate_portbagaj
    
    def __repr__(self):
        return f"{self.producator} {self.model}"

    # Defineste ordinea implicita
    def __lt__(self, other):
        return self.viteza_maxima < other.viteza_maxima
    
    def __gt__(self, other):
        return self.viteza_maxima > other.viteza_maxima

    def __eq__(self, other):
        return self.viteza_maxima == other.viteza_maxima



skoda = Vehicul("Skoda", "Octavia", 200, 700)
passat = Vehicul("Volkswagen", "Passat", 190, 690)
bmw = Vehicul("BMW", "320", 230, 500)

lista_masini = [skoda, passat, bmw]
print("Cele mai rapide masini")
print(sorted(lista_masini, 
             key=lambda vehicul: vehicul.viteza_maxima,
             reverse=True)
    )
print("Cele mai spatioase masini")
print(sorted(lista_masini, 
             key=lambda vehicul: vehicul.capacitate_portbagaj,
             reverse=True)
    )

print("Sortare folosind __lt__, __gt__, __eq__")
print(sorted(lista_masini, reverse=True))