# 
# Создание папки (с указанием имени); +
#Удаление папки по имени;
#Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх;
#Создание пустых файлов с указанием имени;
#Запись текста в файл;
#Просмотр содержимого текстового файла;
#Удаление файлов по имени;
#Копирование файлов из одной папки в другую;
#Перемещение файлов;
#Переименование файлов.

import os
#from settings import work_directory as wd
wd= "C:\\Users\\Asus\\Desktop\\Test\\"

def enter_name():
    name=input("Введите имя: ")
    while name=="":
        pass
    return name
    

def new_folder():#Создание папки (с указанием имени);

    folder_name= wd+enter_name()
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)




def del_folder():#Удаление папки по имени;
    folder_name=wd+enter_name()
    if os.path.isdir(folder_name):
        os.rmdir(folder_name) 


session = 1
actions=[
    "exit", 
 "Создание папки", 
 "Удаление папки по имени", 
 "Перемещение между папками - заход в папку по имени", 
 "выход на уровень вверх", 
 "Создание пустых файлов с указанием имени", 
 "Запись текста в файл", 
 "Просмотр содержимого текстового файла", 
 "Удаление файлов по имени", 
 "Копирование файлов из одной папки в другую",
 "Перемещение файлов", 
 "Переименование файлов"]

    
while session:
    print("Выберите действие: ")
    for k,v in enumerate(actions):
        print(k," - ",v)

    act=input("Введите номер действия: ")
    if act=="0": #выход
        print("До свидания!")
        session=False  
    elif act == "1": #"Создание папки"
        new_folder()
    elif act=="2": #
        del_folder()
    elif act=="3":
        pass
    elif act=="4":
        pass
    elif act=="5":
        pass
    elif act=="6":
        pass
    elif act=="7":
        pass
    elif act=="8":
        pass
    elif act=="9":
        pass
    elif act=="10":
        pass
    else:
        print("Этого действия пока нет")
