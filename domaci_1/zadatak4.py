"""
Направи програм који израчунава збир цифара троцифреног броја. Програм треба да прочита троцифрени број са стандардног улаза и да испише збир цифара тог броја.


Пример улаза: 123

Пример излаза: Zbir cifara broja 123 je 6
"""

broj = int(input("Upisi broj: "))

prva_cifra = int(broj/100)
treca_cifra = broj%10
druga_cifra = int ( (broj//10)%10 )

print("Zbir cifara je ", prva_cifra+druga_cifra+treca_cifra)
