id=0
metadata={}
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

i=0
while int(i) < int(id):
    i+=1
    print(metadata.get(i))


