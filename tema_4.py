# Jocul 'piatra-foarfeca-hartie':
# a. Se citesc pe rand alegerile celor 2 jucatori
# b. Se afiseaza castigatorul rundei
# Reguli:
# - Hartia bate piatra
# - Foarfecele bat hartia
# - Piatra bate foarfecele
# Extra: faceti jocul cu 3 si/sau 5 runde si determinati castigatorul meciului (jucatorul cu cele
# mai multe runde castigate)
from collections import Counter
PIATRA = 1
FOARFECA = 2
HARTIE = 3
jucator_1_castiga = [
    (HARTIE, PIATRA),
    (FOARFECA, HARTIE),
    (PIATRA, FOARFECA)
]

def castigator(jucator1, jucator2):
    if jucator1 == jucator2:
        print("Egalitate")
        return 0
    elif (jucator1, jucator2) in jucator_1_castiga:
        print("Castiga jucatorul 1")
        return 1
    else:
        print("Castiga jucatorul 2")
        return 2

def citeste_optiuni():
    print("1 - Piatra")
    print("2 - Foarfeca")
    print("3 - Hartie")
    print("Jucator 1:")
    j1 = int(input())
    print("Jucator 2:")
    j2 = int(input())
    return j1, j2

def main():
    runde = 3
    scor = Counter()
    while(runde):
        j1, j2 = citeste_optiuni()
        winner = castigator(j1, j2)
        scor.update([winner])
        runde-=1
    winner = scor.most_common()[0][0]
    if winner == '0':
        print('Remiza')
    else:
        print(f'Castigatorul este jucatorul {winner}')

main()
