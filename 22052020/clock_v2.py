import datetime
import os
import time
import random

c0=['▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓','▓▓    ▓▓','▓▓    ▓▓','▓▓    ▓▓','▓▓    ▓▓','▓▓    ▓▓','▓▓    ▓▓','▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓']
c1=['▓▓▓▓▓▓  ','▓▓▓▓▓▓  ','    ▓▓  ','    ▓▓  ','    ▓▓  ','    ▓▓  ','    ▓▓  ','    ▓▓  ','▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓']
c2=['▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓','      ▓▓','      ▓▓','▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓','▓▓      ','▓▓      ','▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓']
c3=['▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓','      ▓▓','      ▓▓','▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓','      ▓▓','      ▓▓','▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓']
c4=['▓▓    ▓▓','▓▓    ▓▓','▓▓    ▓▓','▓▓    ▓▓','▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓','      ▓▓','      ▓▓','      ▓▓','      ▓▓']
c5=['▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓','▓▓      ','▓▓      ','▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓','      ▓▓','      ▓▓','▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓']
c6=['▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓','▓▓      ','▓▓      ','▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓','▓▓    ▓▓','▓▓    ▓▓','▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓']
c7=['▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓','▓▓    ▓▓','      ▓▓','      ▓▓','      ▓▓','      ▓▓','      ▓▓','      ▓▓','      ▓▓']
c8=['▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓','▓▓    ▓▓','▓▓    ▓▓','▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓','▓▓    ▓▓','▓▓    ▓▓','▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓']
c9=['▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓','▓▓    ▓▓','▓▓    ▓▓','▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓','      ▓▓','      ▓▓','▓▓▓▓▓▓▓▓','▓▓▓▓▓▓▓▓']

gg='        '
sym='   ▓▓   '

d_c0=[sym,gg,gg,gg,gg,gg,gg,gg,gg,gg]
d_c1=[gg,sym,gg,gg,gg,gg,gg,gg,gg,gg]
d_c2=[gg,gg,sym,gg,gg,gg,gg,gg,gg,gg]
d_c3=[gg,gg,gg,sym,gg,gg,gg,gg,gg,gg]
d_c4=[gg,gg,gg,gg,sym,gg,gg,gg,gg,gg]
d_c5=[gg,gg,gg,gg,gg,sym,gg,gg,gg,gg]
d_c6=[gg,gg,gg,gg,gg,gg,sym,gg,gg,gg]
d_c7=[gg,gg,gg,gg,gg,gg,gg,sym,gg,gg]
d_c8=[gg,gg,gg,gg,gg,gg,gg,gg,sym,gg]
d_c9=[gg,gg,gg,gg,gg,gg,gg,gg,gg,sym]

d_c=[d_c0,d_c1,d_c2,d_c3,d_c4,d_c5,d_c6,d_c7,d_c8,d_c9]

c=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9]

i=0 #для первой точки
j=0 #для цикла отрисовки
k=9 #для второй точки(реверсной)
# вторая верcия реализация, без грамоздкого принта
os.system('cls' if os.name=='nt' else 'clear')
while True:
    r=random.randrange(90,99)
    start_color = '\033[{}m'.format(r)
    finish_color = '\033[0m'
    cdt=datetime.datetime.now()
    #получаю из текущей даты часы/минуты/секунды
    str_cdt=datetime.datetime.strftime(cdt,'%H %M %S').split()
    #заношу часы/минуты/секунды в соответсвующие по позиция колоны, использя за(рас)паковку
    column1,column2,column3,column4,column5,column6=int(str_cdt[0][0]),int(str_cdt[0][1]),int(str_cdt[1][0]),int(str_cdt[1][1]),int(str_cdt[2][0]),int(str_cdt[2][1])
    print(start_color)
    for j in range(len(c)):
        print(c[column1][j],c[column2][j],d_c[j][i],c[column3][j],c[column4][j],d_c[j][k],c[column5][j],c[column6][j])
        j+=1
    time.sleep(1)
    os.system('cls' if os.name=='nt' else 'clear')
    print(finish_color)
    i+=1
    if i>9:
        i=0
    k-=1
    if k<0:
        k=9
