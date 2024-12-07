"""
Група ученика иде на излет, а учитељица мора да организује превоз.
Постоји аутобус који може да прими максимално 50 ученика.

Напиши програм који ће прочитати број ученика са стандардног улаза и исписати колико је 
аутобуса потребно да би се превезли сви ученици, као и број ученика у последњем аутобусу.


Пример улаза: 123

Пример излаза: Potrebno je 3 autobusa, u poslednjem autobusu ima 23 ucenika.
"""

br_ucenika = int(input("Broj ucenika: "))

br_bus = int(br_ucenika/50) + 1

br_u_poslednjem = br_ucenika - 50*(br_bus-1)

print("Potrebno je ", br_bus, " autobusa, u poslednjem autobusu ima ", br_u_poslednjem, " ucenika.\n")

#   potrebni uslovi da bi se resio uslov da je br ucenika deljiv sa 50 (if-else)


'''
if (br_ucenika % 50)==0 :
    br_bus = int(br_ucenika/50)
    br_u_poslednjem = 0

else:
    br_bus = int(br_ucenika/50) + 1
    br_u_poslednjem = br_ucenika - 50*(br_bus-1)

print("Potrebno je ", br_bus, " autobusa, u poslednjem autobusu ima ", br_u_poslednjem, " ucenika.\n")

'''

