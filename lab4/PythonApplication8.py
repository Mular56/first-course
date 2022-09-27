def file_size(filename): #количество символов с учётом пробела
   with open(filename) as f:
      return len(f.read())

print(file_size('D:\lab4.txt'), ": количество символов с учётом пробела")

file = open("D:\lab4.txt", "r+")
countsimbol = 0 #количество символов без учёта пробела
for simbol in file.read():
    if simbol != " ":
        countsimbol = countsimbol + 1
print(countsimbol, ": количество символов без учёта пробела")
file.close()

file = open("D:\lab4.txt", "r+")
count = 0 
for word in file.read().split(): #количество слов в тексте 
    count = count + 1
print(count, ": количество слов в тексте")
file.close()

with open("D:\lab4.txt", "r") as file: #количество слов что встречаются только 1 раз
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Уникальных слов: {len(uniques)}")
    file.close()
