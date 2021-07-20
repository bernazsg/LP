tceloe_chislo = input("Введите целое положительное число >>> ")
kolichestvo_cifr = len(tceloe_chislo) - 1
index = 0
while kolichestvo_cifr > index:
    if int(tceloe_chislo[index]) > int(tceloe_chislo[index + 1]):
        naibolshee = int(tceloe_chislo[index])
    else:
        naibolshee = int(tceloe_chislo[index + 1])
    index += 1
print("Самая большая цифра в вашем числе", naibolshee)

