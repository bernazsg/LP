a_km = int(input("Введите количество километров в первый день >>> "))
b_km = int(input("Введите количество километров, которое должен достигнуть спортсмен в день Х >>> "))
dni = 1
km_den = a_km
km_den_fl = a_km
print(f"{dni}-й день:", km_den)
while True:
    if km_den >= b_km:
        break
    km_den_fl = km_den_fl * 1.1
    km_den = int(km_den_fl / 1)
    dni += 1
    print(f"{dni}-й день:{km_den_fl:.2f}")
    continue
print(f"Ответ: на {dni}-й день спортсмен достиг результата - не менее {b_km} км.")
