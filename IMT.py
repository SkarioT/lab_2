#пример формата вводи прописываем первый раз при запуске.
print("Пример Ввода данных:\n Введите Ваше ФИО : ФИО\n Введите Ваш пол : М/Ж\n Введите Ваш возраст : 22\n Введите Ваш Вес : 79 \n Введите Ваш Рост : 1.69 \n ______________________")
while True :
    while True:
    #входные данные
        FIO=input("Введите ваше ФИО : ")
        SEX=input("Введите ваш пол : ")
        while (SEX !="М") and (SEX!="Ж"): 
            print("не корректный ввода, необходимо вводить М или Ж")
            SEX=input("Введите ваш пол : ")
        AGE=input("Введите ваш возраст : ")
        weight=input("Введите ваш Вес : ")
        height=input("Введите ваш Рост : ")
        print("Ввод данных завершен! \n Спасибо за предоставленную информацию!\n\n")
        
        #подсчёт индекса
        IMT=(float(weight)/(float(height)*float((height))))
        MIN=15
        MAX=40
        srrr="="
        #подготовка для вывода
        sr_final=(str(MIN) + srrr*(int(IMT)-MIN) + '|' + srrr*(MAX-int(IMT)-1) + str(MAX))
        print("Индекс Массы Тела для",FIO,"равен: ",IMT)
        #печать "заключения"
        zaklychenie=("кушай больше","всё хорошо","хватит жрать")
        if IMT <=20 and (int(AGE)<=20):
            rez=zaklychenie[0]
            print("Заключение по результату полученных данных:",zaklychenie[0])
        elif IMT <=20 and int(AGE)>=20 :
            rez=zaklychenie[1]
            print("Заключение по результату полученных данных: ",zaklychenie[1])
        if (IMT > 20 and IMT < 25) and (int(AGE)<=15 and int(AGE) >=0):
            rez=zaklychenie[1]
            print("Заключение по результату полученных данных: ",zaklychenie[1])
        elif (IMT > 20 and IMT < 25) and (int(AGE)>=15):
            rez=zaklychenie[2]
            print("Заключение по результату полученных данных: ",zaklychenie[2])
        if IMT >= 25 and (int(AGE)>=1):
            rez=zaklychenie[2]
            print("Заключение по результату полученных данных: ",zaklychenie[2])
        print(sr_final,"\n",'____'*20)
        collection=(FIO,SEX,AGE,weight,height,IMT,rez)
        exit=input("Продолжаем ввод?")
        print(collection)
#final
