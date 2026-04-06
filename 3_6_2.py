#Створіть функцію, яка приймає список чисел і повертає новий список, що містить тільки парні числа.
def n_spusok(numbers):
    ch = []
    for n in numbers:
        if n % 2 == 0:
            ch.append(n)
    return ch
a = [1, 2, 3]
print(n_spusok(a))  