#Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен
# увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который результат спортсмена
# составит не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число
# — номер дня.

while True:
    a = input("Введите целочисленное значение результата спортсмена в первый день, км >>> ")
    if not str.isdigit(a):
        print("Введён неверный формат данных - дробное, отрицательное число или текстовый символ. Попробуйте снова.")
        continue
    a = int(a)
    while True:
        b = input("Введите целочисленное значение результата спортсмена, который нужно достичь, км >>> ")
        if not str.isdigit(b):
            print("Введён неверный формат данных - дробное, отрицательное число или текстовый символ. Попробуйте снова.")
            continue
        b = int(b)
        break
    break

denj = 1 # День на который спортсмен достигнет заданного результата км.
while b >= a:
    a = a + a / 10
    denj += 1
print(f"На {denj}-й день спортсмен достигнет результата - не менее {b} км.")

