temperaturas = [22, 25, 21, 24, 26, 23, 22]

print(f"Na lista tem {len(temperaturas)} temperaturas")


print(f"{temperaturas[0]} tem o indice = {temperaturas.index(22)}")
print(f"{temperaturas[6]} tem o indice = {temperaturas.index(20)}")

i = 0
while i < len(temperaturas):
    print(temperaturas[i])
    i += 1