import random
a = random.randint(1,30)
print(f"a = {a}")

b = random.randint(1,30)
print(f"b = {b}")

if a > b :
    print("Le nombre a est plus grand que le nombre b.")
elif b > a :
    print("Le nombre b est plus grand que le nombre a.")
elif a == b :
    print("Le nombre a et le nombre b sont égaux.")