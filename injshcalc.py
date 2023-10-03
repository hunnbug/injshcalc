import math
work = True
def sloj():
    num1 = float(input(("введите первое число: ")))
    num2 = float(input(("введите второе число: ")))
    answer = num1 + num2
    print("ваш результат: " + str(answer))
def minus():
    num1 = float(input(("введите первое число: ")))
    num2 = float(input(("введите второе число: ")))
    answer = num1 - num2
    print("ваш результат: " + str(answer))
def umnoj():
    num1 = float(input(("введите первое число: ")))
    num2 = float(input(("введите второе число: ")))
    answer = num1 * num2
    print("ваш результат: " + str(answer))
def deli():
    num1 = float(input(("введите первое число: ")))
    num2 = float(input(("введите второе число: ")))
    answer = num1 / num2
    print("ваш результат: " + str(answer))
def stepen():
    num1 = float(input(("введите число ")))
    num2 = float(input(("введите показатель степени: ")))
    answer = num1**num2
    print("ваш результат: " + str(answer))
def koren():
    num1 = float(input(("введите число: ")))
    answer = math.sqrt(num1)
    print("ваш результат: " + str(answer))
def factorial():
        num1 = int(input(("введите число: ")))
        fact = 1
        for i in range(num1):
            i = i + 1
            fact = fact * i
        print("ваш результат: " + str(fact))
def sinus():
    num1 = float(input(("введите величину противолежащего катета: ")))
    num2 = float(input(("введите величину гипотенузы: ")))
    answer = num1 / num2
    print("ваш результат: " + str(answer))
def cos():
    num1 = float(input(("введите величину прилежащего катета: ")))
    num2 = float(input(("введите величину гипотенузы: ")))
    answer = num1 / num2
    print("ваш результат: " + str(answer))
def tan():
    num1 = float(input(("введите величину противолежащего катета ")))
    num2 = float(input(("введите величину прилежащего катета: ")))
    answer = num1 / num2
    print("ваш результат: " + str(answer))  
while work == True:
    try:
        print(" ")
        print("выберите действие написав соответствующую цифру:")
        print("1. сложение")
        print("2. вычитание")
        print("3. умножение")
        print("4. деление")
        print("5. возведение в степень")
        print("6. квадратный корень")
        print("7. факториал")
        print("8. синус")
        print("9. косинус")
        print("10. тангенс")
        print("11. выход из программы")
        print(" ")

        a = input()
        deystv = int(a)

        if deystv == 1:
            sloj()

        elif deystv == 2:
            minus()

        elif deystv == 3:
            umnoj()

        elif deystv == 4:
            deli()

        elif deystv == 5:
            stepen()

        elif deystv == 6:
            koren()

        elif deystv == 7:
            factorial()

        elif deystv == 8:
            sinus()

        elif deystv == 9:
            cos()

        elif deystv == 10:
            tan()

        elif deystv == 11:
            break
    except:
        print(" ")
        print("ошибка 6, пиши по человечески")
