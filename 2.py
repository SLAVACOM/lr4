print("Вычисление НОД двух целых чисел по алгоритму Евклида")
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))


def gcd(num1, num2):
    if num1 == 0:
        return num2
    elif num1 < num2:
        return gcd(num2, num1)
    return gcd(num1 - num2, num2)


print("Результат",gcd(num1, num2))
