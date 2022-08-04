def numere_pare():
    n = 0
    while True:
        yield n
        n+=2

generator = numere_pare()

for _ in range(10):
    print(next(generator))
