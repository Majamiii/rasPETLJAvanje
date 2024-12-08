zapremina = int(input("Unesite zapreminu bazena: "))
x = int(input("Unesite brzinu prve pumpe (l/h): "))
y = int(input("Unesite brzinu druge pumpe (l/h): "))

vreme = zapremina / (x + y)

print("Punjenje bazena ce trajati " + str(vreme) + " sati")
