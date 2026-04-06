#Напишіть функцію для обчислення середнього значення списку чисел.
def sered (ch):
    if len (ch)  ==0:
        return 0
    return sum (ch) / len (ch)
chusla= [5,8,9,20,15]
print (sered(chusla))
#Реалізуйте функцію, яка приймає два списки і повертає список, який містить спільні елементи обох списків.
def sp(list1, list2):
    neww = []
    for t in list1:
        if t in list2 and t not in neww:
            neww.append(t)
    return neww
list1 = [12, 3, 40, 9]
list2 = [30, 9, 7, 8, 3]
print(sp(list1, list2))