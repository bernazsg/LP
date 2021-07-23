# vyruchka = float(input("Введите размер выручки фирмы руб. >>> "))
# izderjki = float(input("Введите размер издержек фирмы руб. >>> "))
# if vyruchka > izderjki:
#     pribyl = vyruchka - izderjki
#     rentabelnostj = (vyruchka / izderjki) * 100
#     print(f"Фирма отработала в прибыль на {pribyl:.2f} руб. Рентабельность составила: {rentabelnostj:.2f} %")
#     chisl_sotrudn = int(input("Введите численность сотрудников фирмы >>> "))
#     print(f"Прибыль фирмы в расчёте на одного сотрудника составила: {pribyl / chisl_sotrudn:.2f} руб.")
# elif vyruchka == izderjki:
#     print('Фирма вышла в "ноль"')
# else:
#     ubytok = izderjki - vyruchka
#     print(f"Компания отработала в убыток на -{ubytok:.2f} руб.")
# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
while True:
    vyruchka = input("Введите целочисленное значение выручки фирмы в руб. >>> ")
    if not str.isdigit(vyruchka):
        print(
            "Введен некорректный формат данных - дробное, отрицательное число или текстовый символ. Попробуйте снова.")
        continue
    else:
        vyruchka = int(vyruchka)
        break
while True:
    izderjki = input("Введите целочисленное значение издержек фирмы в руб. >>> ")
    if not str.isdigit(izderjki):
        print(
            "Введён некорректный формат данных - дробное, отрицательное число или текстовый символ. Попробуйте снова.")
        continue
    else:
        izderjki = int(izderjki)
        break
pribyl = 0
ubytok = 0
while True:
    raschet = vyruchka - izderjki
    if raschet > 0:
        pribyl = raschet
        print(f"Фирма вышла в прибыль на + {pribyl} руб.")
        break
    elif raschet == 0:
        print("Фирма вышла в ноль.")
        exit()
    else:
        ubytok = raschet
        print(f"Фирма отработала в убыток на {ubytok} руб.")
        break
while True:
    kolvo_sotr = input("Введите количество сотрудников фирмы >>> ")
    if not str.isdigit(kolvo_sotr):
        print(
            "Введен некорректный формат данных - дробное, отрицательное число или текстовый символ. Попробуйте снова.")
        continue
    print(f"Прибыль фирмы в расчёте на одного сотрудника составила: {pribyl / int(kolvo_sotr):.2f} руб.")
    break
