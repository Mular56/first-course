import pandas as pd
import matplotlib.pyplot as plt

question = str()
point = 0
test =  open('D:\lab7.txt', 'r', encoding= "utf-8").read().lower()
for i in test:
    if '?' in i:
        question = question + ("?")
    elif '!' in i:
        question = question + ("!")
    elif '.' in i:
        question = question + (".")
    elif '.' in i:
        question = question + ("")

print (point)
char_list = list(question)

df = pd.DataFrame({'chars': char_list})
df = df[df.chars != ' ']
df['num'] = 10
df = df.groupby('chars').sum().sort_values('num', ascending=False) / len(df)

plt.bar(df.index, df.num, width=0.5, color='g')
plt.show()
plt.savefig(input('Дайте назву гістограммі: \n'))
print("Ваша гістограмма збережена біля файла .py")