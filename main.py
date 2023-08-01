# 1
value1 = int(input("Введите первое число: "))
value2 = int(input("Введите второе число: "))
value3 = int(input("Введите третье число: "))
print(" 1 - вывести сумму трех чисел;\n 2 - вывести произведение трех чисел.")
value4 = input("Что необходимо сделать: ")
if(value4=='1'):
    print(value1,"+",value2,"+",value3,"=",value1+value2+value3)
elif(value4=='2'):
    print(value1,"*",value2,"*",value3,"=",value1*value2*value3)
else:
    print("Введите корректное значение!")

# 2
value7 = int(input("Введите первое число: "))
value8 = int(input("Введите второе число: "))
value9 = int(input("Введите третье число: "))
print(" 1 - вывести максимум из трёх;\n 2 - вывести минимум из трёх;\n 3 - вывести среднеарифметическое трёх чисел.")
value10 = input("Что необходимо сделать: ")
if(value10=='1'):
    print(max(value7,value8,value9))
elif(value10=='2'):
    print(min(value7,value8,value9))
elif(value10=='3'):
    print((value7+value8+value9)/3)
else:
    print("Введите корректное значение!")

# 3
value5 = int(input("Введите количество метров: "))
print(" 1 - перевести в мили;\n 2 - перевести в дюймы;\n 3 - перевести в ярды.")
value6 = input("Что необходимо сделать: ")
if(value6=='1'):
    print(value5, "метра(ов), равно", value5*0.00062,"миль")
elif(value6=='2'):
    print(value5, "метра(ов), равно", value5*39.37,"дюйм")
elif(value6=='3'):
    print(value5, "метра(ов), равно", value5*1.09, "ярд")
else:
    print("Введите корректное значение!")
