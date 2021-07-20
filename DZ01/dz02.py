import datetime

time_sec = int(input("Введите время в секундах (число не более 86400) >>> "))
if time_sec > 86400:
    print("Заданное вами число превышает указанный предел в 86400 секунд.")
else:
    hour_time = time_sec // 3600
    hour_ostatok = time_sec % 3600
    min_time = hour_ostatok // 60
    sec_time = hour_ostatok % 60

    time_res = datetime.time(hour_time, min_time, sec_time)
    print(f"Вычисленное время: {time_res}")