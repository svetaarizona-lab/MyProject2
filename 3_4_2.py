#Реалізуйте функцію, яка приймає два словники і повертає новий словник, який є об'єднанням обох словників.
def dicton (a1, a2):
    dic = a1.copy()
    for key in a2:
        dic[key] = a2[key]
    return dic
c ={"a":1, "b":2, "k":3}
d={"a":4, "b":5, "k":6}
print (dicton(c, d))