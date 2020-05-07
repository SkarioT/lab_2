metadata={}
print(metadata)
id=0
while True :
    menu=input("Выбирите пунк меню: \n 1) - добавить данные\n 2) - просмотреть данные\n 3) - поиск по ID\ФИО\n 4) - выход из пограммы \n Ваш выбор : ") 
    #debag:
    #print("запуск Цикла 1 ")

    if menu=="1" : 
        print("Выбран пункт меню - 1")
        #пример формата ввода, прописываем первый раз при запуске.
        print('_'*30,"\nПример Ввода данных:\n Введите Ваше ФИО : ФИО\n Введите Ваш пол : М/Ж\n Введите Ваш возраст : 22\n Введите Ваш Вес : 79\n Введите Ваш Рост : 1.69\n ","_"*30)
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

        metadata[id]={"ФИО" : FIO,"ПОЛ":SEX,"ВОЗРАСТ": int(AGE),"ВЕС" : float(weight),"РОСТ" : float(height),"ИМТ" : float(IMT),"заключение": rez}
        menu=0
    if menu=="2" :  
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
    if menu=="4" or menu=="q":

        print("Выбра пунк меню - 3 \n Завершение работ программы")
        break
    if menu=="3":
        while True:
            print("\n","_"*20)
            find_menu=input("Выбирите пунк меню:\n1)Поиск по ID\n2)Поиск по ФИО\n3)Возврат в предыдущее меню\nВаш выбор: ")
            if find_menu=="1":
                print('_'*20,"\nВыбран поиск по ид")
                find_id=input("Введите ID для поиска :")
                if (metadata.get(int(find_id)))==None:
                    print("ID не существует")
                else:
                    print(metadata.get(int(find_id)),"\n","_"*30)
                find_menu=0
            if find_menu=="2":
                print('_'*20,"\nпоиск по ФИО")
                find_FIO=input("Введите ФИО для поиска :")
                if int(id)==0:
                    print("Нет даныых. Введите хотя бы одного пользователя.")
                i_i=1
                while int(i_i) <= int(id):
                    f_name="ФИО: " + metadata[i_i]["ФИО"] +"ПОЛ: "+ metadata[i_i]["ПОЛ"]+"ВЕС:"+ str(metadata[i_i]["ВЕС"])+"РОСТ:"+ str(metadata[i_i]["РОСТ"])+"ИМТ:"+ str(metadata[i_i]["ИМТ"])+"заключение:"+ str(metadata[i_i]["заключение"])
                    if find_FIO in f_name:
                        print(f_name)
                    i_i+=1
                find_menu=0
            if find_menu=="3":
                break

pass
#final
