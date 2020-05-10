metadata={}
id=0


def main_menu(key):
    if key=='1':
        imb_imput()
    if key=='2':
        show_metadata(id)
    if key=='3':
        search_menu()
    if key=='4' :
        exit_menu()

def imb_imput():
        print("Выбран пункт меню - 1")
        #пример формата ввода, прописываем первый раз при запуске.
        print('_'*30,"\nПример Ввода данных:\n Введите Ваше ФИО : ФИО\n Введите Ваш пол : М/Ж\n Введите Ваш возраст : 22\n Введите Ваш Вес : 79\n Введите Ваш Рост : 1.69\n ","_"*30)
        #входные данные
        global id
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

        def draw_BMI(IMT):
            MIN=15
            MAX=40
            srrr="="
            #подготовка для вывода
            sr_final=(str(MIN) + srrr*(int(IMT)-MIN) + '|' + srrr*(MAX-int(IMT)-1) + str(MAX))
            print("Индекс Массы Тела для",FIO,"равен: ",IMT)
            print(sr_final)
        draw_BMI(IMT)

        #Функция для подсчёта результата
        def conclusion(IMT,AGE):
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
            #возвращаю rez для дальнейшего внесения в metadata
            return rez

        #заносим в rez_conclusion итог заключения
        rez_conclusion=conclusion(IMT,AGE)


        def buffer_metadata(FIO,SEX,AGE,weight,height,rez):
            metadata[id]={"ФИО" : FIO,"ПОЛ":SEX,"ВОЗРАСТ": int(AGE),"ВЕС" : float(weight),"РОСТ" : float(height),"ИМТ" : float(IMT),"заключение": rez_conclusion}

        buffer_metadata(FIO,SEX,AGE,weight,height,rez_conclusion)

#фукция вызываемая при выборе в меню 2 (просмотр всех данных)
def show_metadata(id):
        print("Выбран пунк меню 2\n",'_'*30)
        if id==0:
            print("Данные пусты. Выбирите пункт 1 или завершите выполение программы.")
        else:
            i=0
            while int(i) < int(id):
                i+=1
                #построчный вывод данных, опираясь на ключ
                print(metadata.get(i))
        print("_"*30)

        
while True :
    menu=input("Выбирите пунк меню: \n 1) - добавить данные\n 2) - просмотреть данные\n 3) - поиск по ID\ФИО\n 4) - выход из пограммы \n Ваш выбор : ") 
    #debag:
    #print("запуск Цикла 1 ")
    main_menu(menu)