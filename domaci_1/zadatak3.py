"""
Направити програм који рачуна плату радника.
Радник се плаћа по сату све док не достигне 40 радних сати недељно.
Ако радник пређе 40 радних сати, прековремени сати се не плаћају.
Плата по сату је 200 динара.
Програм треба да прочита број радних сати у недељи са стандардног улаза и да испише колико је радник зарадио.

Пример улаза: 45

Пример излаза: Plata radnika je: 8000
"""

br_sati = int(input("Broj sati koje je radnik radio: "))

if(br_sati <= 40):
    print("Plata radnika je: ", br_sati*200)


if(br_sati > 40):
    print("Plata radnika je: ", 40*200)

