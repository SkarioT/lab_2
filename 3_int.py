a=input("Введите первое число : ")
b=input("Введите второе число : ")
c=input("Введите третье число : ")
z="-"
#1)Если нет ни ондого нуля - вывести: "Нет нулевых значений!!!"
rez1=((int(a)!=0  and (int(b)!=0 and int(c)!=0) and "Нет нулевых значений")) or "Присутствуют нули"
print(z*30,"\nРезультат условия  1 : ",rez1,"\n")

#2)Вывести первое ненулевое значение. Если введены все нули - вывести "Введены все нули!" (цикл не использовать)
rez2=(int(a)!=0  and "первое не нулевое ->  a = {}".format(a)) or (int(b)!=0  and "первое не нулевое ->  b = {}".format(b)) or (int(c)!=0  and "первое не нулевое ->  c = {}".format(c)) or "Введены все нули"
print("Результат условия 2 : ",rez2,"\n")

#3)Если первое значение больше чем сумма второго и третьего вывести a - b - c
#4)Если первое значение меньше чем сумма второго и третьего вывести b + c - a
rez3_4=(int(a)>(int(b)+int(c)) and "a>b+c -> a - b - c = {}".format(int(a)-int(b)-int(c))) or ("a<(b+c) -> b + c - a = {}".format(int(b)+int(c)-int(a)))

print("Результат уловия 3/4 : ",rez3_4,"\n")


#Если первое значение больше 50 и при этом одно из оставшихся значение больше первого вывести "Вася"
rez5=(int(a)>50 and (int(b)>int(a) or int(c)>int(a)) and "Вася") or "условия не соблюдены"
print("Результат уловия  5 : ",rez5,"\n")

#Если первое значение больше 5 или оба из оставшихся значений равны 7 вывести "Петя"
rez6=((int(a)>5 or (int(b)==7 and int(c)==7)) and "Петя") or "условия не соблюдены"
print("Результат уловия  6 : ",rez6,"\n")