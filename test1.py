threshold = 5

def check_threshold(value):
	if value >= threshold:
		print(f"{value} est plus grand que {threshold}")
	else:
		print(f"{value} est plus petit que {threshold}")

for a in range(10):
	check_threshold(a)


# if a >= 10:
# 	print("a est plus grand que 10")
# else:
# 	print("a est plus petit que 10")
# # Rémi je t'aime
