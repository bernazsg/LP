# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
while True:
    time_sec = input("Введите целое число в секундах,но не более 356519 >>> ")
    if not str.isdigit(time_sec):
        print(
            "Введённый форма данных неверен, вы ввели дробное число, отрицательное число или символ. Попробуйте снова")
        continue
    if int(time_sec) > 356519:
        print("Вы ввели число более 356519. Попробуйте снова.")
        continue
    else:
        time_sec = int(time_sec)
        hour_time = time_sec // 3600
        ostatok = time_sec % 3600
        time_min = ostatok // 60
        sec_time = ostatok % 60
        break
print(f"Рассчитанное время: {hour_time:<02}:{time_min:<02}:{sec_time:<02}.")
