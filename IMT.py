metadata={}
id=0
while True :
    menu=input("Выбирите пунк меню: \n 1) - добавить данные\n 2) - просмотреть данные\n 3) - выход из пограммы \n Ваш выбор : ") 
    #debag:
    #print("запуск Цикла 1 ")

    if menu=="1" :
        print("_"*30,"\nВыбран пункт меню - 1")
        #пример формата ввода, прописываем первый раз при запуске.
        print("Пример Ввода данных:\n Введите Ваше ФИО : ФИО\n Введите Ваш пол : М/Ж\n Введите Ваш возраст : 22\n Введите Ваш Вес : 79 \n Введите Ваш Рост : 1.69 \n ","_"*30)
        #входные данные
        id+=1
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
        #печать "заключения" в зависимости от ИМТ
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
        #занесение полученных данных

        metadata[id]=({"ФИО" : FIO},{"ПОЛ":SEX},{"ВОЗРАСТ": AGE},{"ВЕС" : weight},{"РОСТ" : height},{"ИМТ" : IMT},{"заключение": rez})

        menu=0
    if menu=="2" :  
        print("Выбран пунк меню 2\n",'_'*30)
        if id==0:
            print("Данные пусты, выбирите пункт 1 или завершите выполение программы.\n",'_'*30)
        else:
            i=0
            while int(i) < int(id):
                i+=1
                print(metadata.get(i))
        print("_"*30)
    if menu=="3" or menu=="q":
        print("Выбра пунк меню - 3 \n Завершение работ программы")
        break
pass
#final
