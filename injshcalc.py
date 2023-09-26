import math
work = True
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
            num1 = float(input(("введите первое число: ")))
            num2 = float(input(("введите второе число: ")))
            answer = num1 + num2
            print("ваш результат: " + str(answer))

        elif deystv == 2:
            num1 = float(input(("введите первое число: ")))
            num2 = float(input(("введите второе число: ")))
            answer = num1 - num2
            print("ваш результат: " + str(answer))

        elif deystv == 3:
            num1 = float(input(("введите первое число: ")))
            num2 = float(input(("введите второе число: ")))
            answer = num1 * num2
            print("ваш результат: " + str(answer))

        elif deystv == 4:
            num1 = float(input(("введите первое число: ")))
            num2 = float(input(("введите второе число: ")))
            answer = num1 / num2
            print("ваш результат: " + str(answer))

        elif deystv == 5:
            num1 = float(input(("введите число ")))
            num2 = float(input(("введите показатель степени: ")))
            answer = num1**num2
            print("ваш результат: " + str(answer))

        elif deystv == 6:
            num1 = float(input(("введите число: ")))
            answer = math.sqrt(num1)
            print("ваш результат: " + str(answer))

        elif deystv == 7:
            num1 = int(input(("введите число: ")))
            fact = 1
            for i in range(num1):
                i = i + 1
                fact = fact * i
            print("ваш результат: " + str(fact))

        elif deystv == 8:
            num1 = float(input(("введите величину противолежащего катета: ")))
            num2 = float(input(("введите величину гипотенузы: ")))
            answer = num1 / num2
            print("ваш результат: " + str(answer))

        elif deystv == 9:
            num1 = float(input(("введите величину прилежащего катета: ")))
            num2 = float(input(("введите величину гипотенузы: ")))
            answer = num1 / num2
            print("ваш результат: " + str(answer))

        elif deystv == 10:
            num1 = float(input(("введите величину противолежащего катета ")))
            num2 = float(input(("введите величину прилежащего катета: ")))
            answer = num1 / num2
            print("ваш результат: " + str(answer))
        elif deystv == 11:
            work = False
    except:
        print(" ")
        print("ошибка 6, пиши по человечески")
