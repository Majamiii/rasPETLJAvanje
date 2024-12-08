broj = int(input("Unesite cetvorocifreni broj: "))

prva_cifra = broj // 1000
druga_cifra = (broj % 1000) // 100
treca_cifra = (broj % 100) // 10
cetvrta_cifra = broj % 10

obrnuti = cetvrta_cifra * 1000 + treca_cifra * 100 + druga_cifra * 10 + prva_cifra

print("Ako se taj broj obrne, dobija se broj: " + str(obrnuti))
