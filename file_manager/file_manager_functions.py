import os
#from settings import work_directory as wd
wd= "C:\\Users\\Asus\\Desktop\\Test\\" #Папка для тестирования работы функций 

def dir_exists(new_path):
    if os.path.isdir(new_path):
        return True
    else:
        return False

def enter_name(s=""):
    s="Введите имя"+s+": "
    name=input(s)
    while name=="":
        print("Пустая строка не может быть именем")
        name=input(s)
    return name
    
def new_folder():#Создание папки (с указанием имени);
    folder_name= wd+enter_name()
    if not dir_exists(folder_name):
        os.mkdir(folder_name)
        return True
    return False

def del_folder():#Удаление папки по имени;
    folder_name=wd+enter_name()
    if dir_exists(folder_name):
        os.rmdir(folder_name) 
        return True
    return False

def goto_folder():#переход по имени
    folder_name=wd+enter_name()
    if dir_exists(folder_name):
        os.chdir(folder_name) 
        return True
    return False

def goup_folder():#на уровень верх
    if os.getcwd()+"\\" != wd:
        os.chdir("../") 
        return True
    return False    

def create_empty_file():#создание пустого файла
    file_name = enter_name()
    if ".txt" not in file_name:
        file_name+=".txt"
    f=open(file_name, "w")
    f.close()
    return True
    #return False    

def add_text_file():    #Запись текста в файл;
    file_name = enter_name()
    if ".txt" not in file_name:
        file_name+=".txt"
    with open(file_name, "a") as f:
        msg=""
        while msg!="0\n":
            f.writelines(msg)
            msg=input("Введите строку, для окончания записи введите 0: ")+"\n"

def viewing_text_file():#Просмотр содержимого текстового файла    
    file_name = enter_name()
    if ".txt" not in file_name:
        file_name+=".txt"
    with open(file_name, "r") as f:
        for line in f:
            print(line[:-1])

def delete_file():#удаление файла
    file_name = enter_name()
    if ".txt" not in file_name:
        file_name+=".txt"
    try:
        os.remove(file_name)
    except:
        print("не удалось")

#ДОДЕОЛАТЬ
def copying_file():#Копирует один файл
    try:
        file_name = enter_name(" копируемого файла")
        if ".txt" not in file_name:
            file_name+=".txt"
        folder_name=wd+enter_name()
        file_text=""
        with open(file_name, "r") as f:
            file_text=f.read()
        if dir_exists(folder_name):
            os.chdir(folder_name)
            with open(file_name, "w") as f:
                file_text=f.write()
    except:
        print("error")    
        
        return True
    return False

#Перемещение
def move_file():
    try:
        file_name = enter_name(" перемещаемого файла")
        if ".txt" not in file_name:
            file_name+=".txt"
        folder_name=wd+enter_name()
        file_text=""
        with open(file_name, "r") as f:
            file_text=f.read()
        delete_file()
        if dir_exists(folder_name):
            os.chdir(folder_name)
            with open(file_name, "w") as f:
                file_text=f.write()
        
    except:
        print("error")    
        
        return True
    return False

def rename_file():
    old_file_name = enter_name()
    if ".txt" not in old_file_name:
        old_file_name+=".txt"
    new_file_name = enter_name()
    if ".txt" not in new_file_name:
        new_file_name+=".txt"
    os.rename(old_file_name, new_file_name)

