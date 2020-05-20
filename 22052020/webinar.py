#ООП
import datetime
import os
import time
from tkinter import *
a=0
class Human:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
    def show_info(self):
        print(f"Возраст {self.age}, Имя {self.name}, Пол {self.sex}")

    def running(self):
        print(" {} сейчас на пробежке".format(self.name))

    def go_home(self):
        print('_'*30)
        self.running()
        print("\nЗакончил(а) пробежку")
        print("Отправился домой")


human_vasya=Human('Вася','М',22)
human_inna=Human('Инна','Ж',24)

human_inna.show_info()
human_vasya.running()
human_vasya.go_home()

human_inna.go_home()
human_inna.show_info()

a="Буква А"
print(a.__repr__())
print(a.__str__())
print(a)
