
#входные данные
weight=input("Введите Ваш Вес : ")
height=input("Введите Ваш Рост : ")

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
