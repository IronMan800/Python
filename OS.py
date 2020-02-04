# -*- coding: utf-8 -*-
import os
import shutil

# Имя пользователя
user = os.getlogin()
print("Пользователь:", user)

# Где запущена программа
b = os.getcwd()
print("Программа запущена по директории:", b)

# Список файлов где запущена программа
c = os.listdir(path=".")
print("Спсисок файлов в директории:", c)


# Древо пользователя
for i in os.walk(r"C:\Users\{}".format(user)):
   print(i)

#Резервное копирование данных

source = input("Введите путь к папке откуда копировать содержимое: ")
files = os.listdir(path=source)
target = input("Введите путь к папке куда скопировать содержимое: ")
for i in source:
    shutil.copy(source+"\{}".format(i) , target)