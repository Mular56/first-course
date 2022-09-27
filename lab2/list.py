#1 швидке сортування
myList = [1, 4, 56, 3, 87, 678, 344, 66, 36, 89, -12]
def q_sort(s):
    if len(s) <= 1:
        return s
    el = s[0]
    left = list(filter(lambda x: x < el, s))
    centre = [i for i in s if i == el]
    right = list(filter(lambda x: x> el, s))
    return q_sort(left) + centre + q_sort(right)
print(q_sort(myList))


#2 пошук елементів за значенням
myList2 = [1,2,3,5,6,7,8,11]
def Search1(s):
    for i in myList2:
        if i == 7:
            return(i)
print(Search1(myList2))

#3)пошук послідовності елементів
myList3 = [1,2,3,4,5,6,7,8,9]
def Search2(s):
    for idx, a in enumerate(s):
        if s [idx:idx+4] == [a,a+1,a+2,a+3]:
            return([a, a+1,a+2,a+3])
            break
print(Search2(myList3))


#4)пошук перших п’яти мінімальних елементів
myList4 = [1, 4, 56, 3, 87, 678, 344, 66, 36, 89, -12]
list4 = []
def searchMin(s, q):
    q = s
    q.sort()
    return q[:5]
print(searchMin(myList4, list4))

#5)пошук перших п’яти максимальних елементів
myList5 = [1, 4, 56, 3, 87, 678, 344, 66, 36, 89, -12]
list5 = []
def searchMax(s, q):
    q = s
    q.sort()
    return q[6:]
print(searchMax(myList5, list5))

#6)пошук середнього арифметичного
myList6 = [1, 4, 56, 3, 87, 678, 344, 66, 36, 89, -12]
def sered(s):
    return sum(s)/len(s)
print(sered(myList6))

#7) Повернення списку, що сформований з початкового списку, але не містить повторів (залишається лише перший з однакових елементів).
myList7 = [1, 4, 56, 3, 87, 4, 678, 344, 66, 36, 89, 66, -12]
newlist = []
def returnList(s, q):
    for i in s:
        if i not in q:
            q.append(i)
    return q
print(returnList(myList7, newlist))

#порахувати кількість елементів
myList8 = [1, 4, 56, 3, 87, 678, 344, 66, 36, 89, -12]
count = 0
def number(s, c):
    for i in s:
        c += 1
    return c
print(number(myList8, count))

#Посчитать количество одинаковых элементов в списке
myList9 = [1, 4, 56, 3, 87, 4, 678, 344, 66, 36, 89, 66, -12]
newlist = []
count = 0
def returnList2(s, q, c):
    for i in s:
        if i not in q:
            q.append(i)
        else:
            c += 1
    return c
print(returnList2(myList9, newlist, count))

#цикличный сдвиг -
#Наименьшее общее кратное -
#Зробити описи Doc strings для кожної реалізованої функції -
