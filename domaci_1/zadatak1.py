""" 
Марко планира рођенданску забаву. Има ограничен буџет и мора да израчуна колико му новца треба за храну, пиће и торту.
Зна да по особи треба да потроши 500 динара за храну и 250 динара за пиће, као и да за торту мора да потроши 1500 динара.
Напиши програм који ће израчунати укупан износ који је потребан Марку за храну, пиће и торту.

Програм треба да прочита број гостију са стандардног улаза и да испише укупан износ на стандардни излаз.

Пример улаза: 5

Пример излаза: Ukupan iznos je: 6000

"""


broj_ljudi = int(input("Koliko ljudi zove Marko? ")) + 1

iznos = (250+500)*broj_ljudi + 1500

print("Ukupan iznos je: ", iznos)


