"""
Se citeste un numar intreg de la tastatura

Daca numarul este divizibil cu:

3 - se afiseaza Fizz
5 - se afiseaza Buzz
3 si 5 - se afiseaza FizzBuzz
In caz contrar se afiseaza numarul citit

Exemplu

1 - 1
2 - 2
3 - Fizz
4 - 4
5 - Buzz
6 - Fizz
7 - 7 
8 - 8
9 - Fizz
10 - Buzz
11 - 11
12 - Fizz
13 - 13
14 - 14
15 - FizzBuzz
16 - 16
"""
print("Dati un numar")
n = int(input())
if n % 15 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)