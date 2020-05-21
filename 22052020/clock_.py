import datetime
import os
import time

#реализация -в лоб.

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
i=0

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
c=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9]
d_c=[d_c0,d_c1,d_c2,d_c3,d_c4,d_c5,d_c6,d_c7,d_c8,d_c9]

while True:
    cdt=datetime.datetime.now()
    str_cdt=datetime.datetime.strftime(cdt,'%H %M %S').split()
    column1,column2,column3,column4,column5,column6=int(str_cdt[0][0]),int(str_cdt[0][1]),int(str_cdt[1][0]),int(str_cdt[1][1]),int(str_cdt[2][0]),int(str_cdt[2][1])
    print(c[column1][0],c[column2][0],d_c[0][i],c[column3][0],c[column4][0],d_c[0][i],c[column5][0],c[column6][0])
    print(c[column1][1],c[column2][1],d_c[1][i],c[column3][1],c[column4][1],d_c[1][i],c[column5][1],c[column6][1])
    print(c[column1][2],c[column2][2],d_c[2][i],c[column3][2],c[column4][2],d_c[2][i],c[column5][2],c[column6][2])
    print(c[column1][3],c[column2][3],d_c[3][i],c[column3][3],c[column4][3],d_c[3][i],c[column5][3],c[column6][3])
    print(c[column1][4],c[column2][4],d_c[4][i],c[column3][4],c[column4][4],d_c[4][i],c[column5][4],c[column6][4])
    print(c[column1][5],c[column2][5],d_c[5][i],c[column3][5],c[column4][5],d_c[5][i],c[column5][5],c[column6][5])
    print(c[column1][6],c[column2][6],d_c[6][i],c[column3][6],c[column4][6],d_c[6][i],c[column5][6],c[column6][6])
    print(c[column1][7],c[column2][7],d_c[7][i],c[column3][7],c[column4][7],d_c[7][i],c[column5][7],c[column6][7])
    print(c[column1][8],c[column2][8],d_c[8][i],c[column3][8],c[column4][8],d_c[8][i],c[column5][8],c[column6][8])
    print(c[column1][9],c[column2][9],d_c[9][i],c[column3][9],c[column4][9],d_c[9][i],c[column5][9],c[column6][9])
    time.sleep(1)
    os.system('cls')
    i+=1
    if i>9:
        i=0