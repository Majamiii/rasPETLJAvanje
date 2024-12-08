broj = int(input())

if broj % 15 == 0:
	print("Deljiv je sa 15")
elif broj % 3 == 0:
	print("Deljiv je sa 3")
elif broj % 5 == 0:
	print("Deljiv je sa 5")
else:
	print("Nije deljiv ni sa 3, ni sa 5")
