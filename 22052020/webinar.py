#ООП
import datetime
import os
import time
from tkinter import *
# a=0
# class Human:
    # def __init__(self,name,sex,age):
        # self.name=name
        # self.sex=sex
        # self.age=age
    # def show_info(self):
        # print(f"Возраст {self.age}, Имя {self.name}, Пол {self.sex}")
# 
    # def running(self):
        # print(" {} сейчас на пробежке".format(self.name))
# 
    # def go_home(self):
        # print('_'*30)
        # self.running()
        # print("\nЗакончил(а) пробежку")
        # print("Отправился домой")
# 
# 
# human_vasya=Human('Вася','М',22)
# human_inna=Human('Инна','Ж',24)
# 
# human_inna.show_info()
# human_vasya.running()
# human_vasya.go_home()
# 
# human_inna.go_home()
# human_inna.show_info()
# 
# a="Буква А"
# print(a.__repr__())
# print(a.__str__())
# print(a)
# 
ss='⬜'

c1="⬜⬜⬜  \n    ⬜  \n    ⬜  \n    ⬜  \n⬜⬜⬜⬜⬜"
c1_l1='⬜⬜⬜  '
c1_l2='    ⬜  '
c1_l3='    ⬜  '
c1_l4='    ⬜  '
c1_l5='⬜⬜⬜⬜⬜'

c2="⬜⬜⬜⬜⬜\n        ⬜\n⬜⬜⬜⬜⬜\n⬜  \n⬜⬜⬜⬜⬜"
c2_l1='    ⬜⬜⬜⬜⬜'
c2_l2='            ⬜'
c2_l3=c2_l1
c2_l4='    ⬜  '
c2_l5='  ⬜⬜⬜⬜⬜'
# while True:
    # cnt=datetime.datetime.now()
    # os.system('cls')

symbol = '\u2593'
symbol2='■'
os.system('cls')

def c1():
    print(c1_l1)
    print(c1_l2)
    print(c1_l3)
    print(c1_l4)
    print(c1_l5)

def c2():
    cc2=c2_l1+'\n'+c2_l2+'\n'+c2_l3+'\n'+c2_l4+'\n'+c2_l5
    return cc2

def print_c():
    ss1=c1_l1+'\n'+c1_l2+'\n'+c1_l3+'\n'+c1_l4+'\n'+c1_l5
    return ss1


while True:
    # print(c1_l1,end='')
    # print(c2_l1)
    # print(c1_l2,end='')
    # print(c2_l2)
    # print(c1_l3,end='')
    # print(c2_l3)
    # print(c1_l4,end='')
    # print(c2_l4)
    # print(c1_l5,end='')
    # print(c2_l5)
    #c1()
    #print(end='')
    print(c2(),end=print_c())
    time.sleep(1)
    os.system('cls')
