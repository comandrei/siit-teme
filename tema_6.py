"""
Creati o metoda de validare a numelui unei persoane.

Restrictiile sunt:

   - trebuie sa inceapa cu litera mare 

   - trebuie sa fie maxim 25 de caractere

   - trebuie sa nu contina caractere speciale (!@#$%^&*() )



Creati exceptii pentru fiecare tip de eroare pornind de la urmatorul cod:



class NameInvalidException(ValueError):

     pass



Pentru cazul 1 (numele nu incepe cu litera mare), ca modalitate de tratare a exceptiei inlocuiti valoarea folosind una din metodele title/upper de pe string.
"""
# Exception definition
class NameInvalidException(ValueError):
     pass

class LowerCaseNameException(NameInvalidException):
    pass

class NameTooLongException(NameInvalidException):
    pass

class SpecialCharsException(NameInvalidException):
    pass

def validare_nume(nume):
    if len(nume) >= 25:
        raise NameTooLongException("Name too long")
    for char in "!@#$%^&*()":
        if char in nume:
            raise SpecialCharsException(f"{char} found in name")
    if nume.title() != nume:
        raise LowerCaseNameException("Name should start with uppercase")
    
    return nume

nume = "dorelas$"
try:
    nume = validare_nume(nume)
except LowerCaseNameException:
    nume = nume.title()

print(nume)