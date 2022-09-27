import random
a = ["Данило", "Петро", "Андрій"]
b = ["робив", "їв", "підпалив"]
c = ["траву", "стуло", "лампу"]
k = [1, 2, 3]
k[0] = random.choice(a)
k[1] = random.choice(b)
k[2] = random.choice(c)
print(k[0], k[1], k[2])
