"""
[ { 
   'nume': 'George',
   'filme': ['Shrek', 'Bond', 'Fight Club']
 },
{
 'nume' : 'Cristian',
 'filme': ['Fight Club', 'The Nun', 'Dracula']
}]


Avand o lista de utilizatori si filme vizionate, listati 

Cel mai vizionat film - Fight Club in cazul de mai sus

Utilizatorul cu cele mai multe filme vizionate - Cristian in cazul de mai sus

Extra
Top filme dupa vizionari: Fight Club, Bond, Dracula, Shrek, The nun

Top utilizatori cu cele mai multe filme vizionate - Cristian, George
"""
prieteni = [{
    'nume': 'George',
    'filme': ['Shrek', 'Bond', 'Fight Club']
},
    {
    'nume': 'Cristian',
    'filme': ['Fight Club', 'The Nun', 'Dracula']
},
{
    'nume': 'Gigi',
    'filme': ['Fight Club', 'The Nun', 'Dracula', 'Film3']
}
]

view_count = {}
for prieten in prieteni:
    filme = prieten["filme"]
    for film in filme:
        if film in view_count:
            view_count[film] += 1
        else:
            view_count[film] = 1
print(sorted(view_count.items(), key=lambda film: film[1], reverse=True))
print(view_count)

from collections import Counter
view_count = Counter()
for prieten in prieteni:
    view_count.update(prieten["filme"])

top_movie = view_count.most_common()[0]
print(f"Cel mai vizualizat film este {top_movie}")

print("Top filme", top_movie)

top = Counter()
for prieten in prieteni:
    top.update([prieten['nume'] for _ in range(len(prieten['filme']))])

print("Cel mai cinefil este", top.most_common(1))
print("Topul cinefil", top)