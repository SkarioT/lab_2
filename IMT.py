
#входные данные
print("Пример Ввода данных:\n Введите Ваш Вес : 79 \n Введите Ваш Рост : 1.69 \n ______________________")
FIO=input("Введите ваше ФИО : ")
SEX=input("Введите ваш пол : ")
weight=input("Введите ваш Вес : ")
height=input("Введите ваш Рост : ")

#подсчёт индекса

IMT=(float(weight)/(float(height)*float((height))))

MIN=15
MAX=40
srrr="="
#подготовка для вывода
sr_final=(str(MIN) + srrr*(int(IMT)-MIN) + '|' + srrr*(MAX-int(IMT)-1) + str(MAX))
print("Индекс Массы Тела рамен: ",IMT)
print(sr_final)
#final
