metadata={}
import uuid
#test uuid
idd=uuid.uuid4()
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
            metadata[str(idd)]=({"id": id},{"fio" : FIO},{"sex":SEX},{"age": AGE},{"weight":weight},{"height" : height})
            if FIO == 'q':
                break
        menu=0
    if menu=="2" :  
        print("выборан пунк меню 2")
        i=0
        while int(i) < int(id):
            i+=1
            #print(metadata[1]['fio'])
            print("вся структура данных:\n",metadata)
    if menu=="3":
        print("выбран пунк меню 3")
        nd = {'id':{ 'Света Соколова': {  'пол':'женский', 'возраст': 16, 'хобби':['Цветы','Пение'],  },
        'Иван Петров': {
         'пол':'мужской',
        'возраст': 40,
        'хобби':['Рыбалка','Жим дивана лежа'],      
        }}}
        print(nd)
        print(nd['id']['Иван Петров'])

nd
    

