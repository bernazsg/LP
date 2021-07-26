# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
while True:
    tceloe = input("Введите целое положительное число >>> ")
    if not str.isdigit(tceloe):
        print("Введён неверный формат данных - дробное, отрицательное число или символ. Попробуйте снова.")
        continue
    else:
        print(f"Будет найдена самая большая цифра в числе {tceloe}")
        break

tceloe = int(tceloe)
naibolsh = 0
ostatok = 0
while tceloe >= 1 and ostatok < 9:
    ostatok = tceloe % 10
    tceloe //= 10
    if naibolsh < ostatok:
        naibolsh = ostatok

print(f"Наибольшая цифра во введённом числе - {naibolsh}.")

# Альтернативное решение:
# tceloe_chislo = input("Введите целое положительное число >>> ")
# kolichestvo_cifr = len(tceloe_chislo) - 1
# index = 0
# while kolichestvo_cifr > index:
#     if int(tceloe_chislo[index]) > int(tceloe_chislo[index + 1]):
#         naibolshee = int(tceloe_chislo[index])
#     else:
#         naibolshee = int(tceloe_chislo[index + 1])
#     index += 1
# print("Самая большая цифра в вашем числе", naibolshee)