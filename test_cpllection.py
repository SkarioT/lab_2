metadata={}
id=0
while True :
    menu=input("выбирите пунк меню: \n 1) - добавить данные\n 2) - просмотреть данные\n Ваш выбор : ")
    print("основной цик")
    if menu=="1" :
        print("выбрн пункт меню - 1")
        print("цикл ввода")
        while int(id)<(int(id)+1):
            id+=1
            FIO=input("Введите ваше ФИО : ")
            SEX=input("Введите ваш пол : ")     
            AGE=input("Введите ваш возраст : ")
            weight=input("Введите ваш Вес : ")
            height=input("Введите ваш Рост : ")
            metadata[id]=({"fio" : FIO},{"sex":SEX},{"age": AGE},{"weight",weight},{"height" : height})
            if FIO == 'q':
                break
        menu=0
    if menu=="2" :  
        print("выборан пунк меню 2")
        i=0
        while int(i) < int(id):
            i+=1
            print(metadata.get(i))

