apart_a = input()
apart_b = input()
a = apart_a.split(",")
b = apart_b.split(",")

area_a = int(a[0]) * int(a[1])
area_b = int(b[0]) * int(b[1])

if area_a > area_b:
	print('Apartment A')
else:
	print('Apartment B')
