#Реалізуйте функцію, яка приймає число і повертає його квадрат.
def square(num):
    return num **2
print(square(3))
#Створіть функцію, яка приймає два числа і повертає їхню суму.
def suma(a, b):
    return a + b
print(suma(3,4))
#Створіть функцію яка приймає 2 числа типу int, виконує операцію ділення та повертає чілу частину і залишок.
def divmod(a, b):
    chilep = a // b
    zulushok = a % b
    return chilep, zulushok
c,z = divmod(10,3)
print ("chile", c)
print ("zulushok", z)
