import file_manager_functions as fmf
from settings import work_directory as wd


session = 1
actions=[
    "exit", 
 "Создание папки", 
 "Удаление папки по имени", 
 "Заход в папку по имени", 
 "выход на уровень вверх", 
 "Создание пустых файлов с указанием имени", 
 "Запись текста в файл", 
 "Просмотр содержимого текстового файла", 
 "Удаление файлов по имени", 
 "Копирование файлов из одной папки в другую",
 "Перемещение файлов", 
 "Переименование файлов"]


#actions={
#   "0":["Выход"]
#}

fmf.os.chdir(wd)    
while session:
    
    #вывод возможных действий
    print("Выберите действие: ")
    for k,v in enumerate(actions):
        print(k," - ",v)
    #выбор действия
    print(fmf.os.getcwd())#текущая директория
    act=input("Введите номер действия: ")
    if act=="0": #выход
        print("До свидания!")
        session=False  
    elif act == "1": #"Создание папки"
        if fmf.new_folder():
            print("Папка успешно создана!")
    elif act=="2": #Удаление папки по имени
        if fmf.del_folder():
            print("Папка успешно удалена!")
    elif act=="3":#заход в папку по имени
        fmf.goto_folder()
    elif act=="4":#выход на уровень вверх
        fmf.goup_folder()
    elif act=="5":#Создание пустых файлов с указанием имени
        fmf.create_empty_file()
    elif act=="6":#Запись текста в файл
        fmf.add_text_file()
    elif act=="7":#Просмотр содержимого текстового файла
        fmf.viewing_text_file()
    elif act=="8":#Удаление файлов по имени
        fmf.delete_file()
    elif act=="9":#Копирование файлов из одной папки в другую
        fmf.copying_file()
    elif act=="10":#Перемещение файлов
        pass
    elif act=="11":#Переименование файлов
        fmf.rename_file()
    else:
        print("Этого действия пока нет") #если пользователь ввел что-то другое
