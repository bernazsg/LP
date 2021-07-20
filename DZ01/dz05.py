vyruchka = float(input("Введите размер выручки фирмы руб. >>> "))
izderjki = float(input("Введите размер издержек фирмы руб. >>> "))
if vyruchka > izderjki:
    pribyl = vyruchka - izderjki
    rentabelnostj = (vyruchka / izderjki) * 100
    print(f"Фирма отработала в прибыль на {pribyl:.2f} руб. Рентабельность составила: {rentabelnostj:.2f} %")
    chisl_sotrudn = int(input("Введите численность сотрудников фирмы >>> "))
    print(f"Прибыль фирмы в расчёте на одного сотрудника составила: {pribyl / chisl_sotrudn:.2f} руб.")
elif vyruchka == izderjki:
    print('Фирма вышла в "ноль"')
else:
    ubytok = izderjki - vyruchka
    print(f"Компания отработала в убыток на -{ubytok:.2f} руб.")

