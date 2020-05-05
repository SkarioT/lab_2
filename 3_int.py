a=input("Введите первое число : ")
b=input("Введите второе число : ")
c=input("Введите третье число : ")

#rez1= (a!=0 and b!=0 and c!=0) 
rezz = (int(a)!=0  and a) or (int(b)!=0 and b) or (int(c)!=0 and c) or ((int(a)==0  and (int(b)==0 and int(c)==0)  and "введены все нули") or "нет нулевых значений")
print(rezz)