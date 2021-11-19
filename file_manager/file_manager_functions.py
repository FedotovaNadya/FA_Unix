import os
from file_manager_settings import work_directory as wd
#wd= "C:\\Users\\Asus\\Desktop\\Test\\" #Папка для тестирования работы функций 
r_wd=""
now_wd=""
if wd[-1] == "\\":
    if "\\" in wd[:-1]:
        ind = wd[:-1].rindex("\\")
        r_wd = wd[ind+1:]
    else:
        r_wd = wd
else:
    r_wd=wd
now_wd = r_wd

def __dir_exists(new_path):
    if os.path.isdir(new_path):
        return True
    else:
        return False

def __enter_name(s=""):
    s="Введите имя"+s+": "
    name=input(s)
    while name=="":
        print("Пустая строка не может быть именем")
        name=input(s)
    return name

def __valid_folder(folder_name):
    if "\\" not in folder_name:
        folder_name=os.getcwd()+"\\"+folder_name
    elif os.getcwd()+"\\" in wd+folder_name:
        folder_name=os.getcwd()+"\\"+folder_name
    else:
        Exception

    #print(folder_name)
    assert (wd in folder_name), "Не рабочая директория"
    return folder_name



def new_folder():#Создание папки (с указанием имени);
    folder_name = __enter_name()
    #folder_name = __valid_folder(folder_name)
    assert "\\" not in folder_name
    if not __dir_exists(folder_name):
        os.mkdir(folder_name)
        return True
    return False

def del_folder():#Удаление папки по имени;
    folder_name=__enter_name()
    folder_name = __valid_folder(folder_name)

    if __dir_exists(folder_name):
        os.rmdir(folder_name) 
        return True
    return False

def goto_folder():#переход по имени
    folder_name=__enter_name()
    new_folder_name = __valid_folder(folder_name)

    if __dir_exists(new_folder_name):
        os.chdir(new_folder_name)
        global now_wd
        now_wd+=folder_name
        return True
    return False

def goup_folder():#на уровень верх
    if os.getcwd()+"\\" != wd:
        os.chdir("../") 
        return True
    return False    

def create_empty_file():#создание пустого файла
    file_name = __enter_name()

    if ".txt" not in file_name:
        file_name+=".txt"
    f=open(file_name, "w")
    f.close()
    return True
    #return False    

def add_text_file():    #Запись текста в файл;
    file_name = __enter_name()
    if ".txt" not in file_name:
        file_name+=".txt"
    with open(file_name, "a") as f:
        msg=""
        while msg!="0\n":
            f.writelines(msg)
            msg=input("Введите строку, для окончания записи введите 0: ")+"\n"

def viewing_text_file():#Просмотр содержимого текстового файла    
    file_name = __enter_name()
    if ".txt" not in file_name:
        file_name+=".txt"
    with open(file_name, "r") as f:
        for line in f:
            print(line[:-1])

def del_file():#удаление файла
    file_name = __enter_name()
    if ".txt" not in file_name:
        file_name+=".txt"
    try:
        os.remove(file_name)
    except:
        print("не удалось")

def copying_file():#Копирует один файл
    try:
        file_name = __enter_name(" копируемого файла")
        if ".txt" not in file_name:
            file_name+=".txt"
        folder_name=__enter_name()
        folder_name = __valid_folder(folder_name) 
        file_text=""
        with open(file_name, "r") as f:
            file_text=f.read()
            f.close()
        if __dir_exists(folder_name):
            os.chdir(folder_name)
            with open(file_name, "w") as f:
                f.write(file_text)
                f.close()
    except:
        print("error")    
        
        return True
    return False

#Перемещение
def move_file():
    wd_now=os.getcwd()
    try:
        file_name = __enter_name(" перемещаемого файла")
        if ".txt" not in file_name:
            file_name+=".txt"
#        print("point1")
        folder_name=__enter_name()
        folder_name = __valid_folder(folder_name)
#        print("point2")
        file_text=""
        with open(file_name, "r") as f:
            file_text=f.read()
            f.close()
#        print("point3")
        if __dir_exists(folder_name):
#            print("point4")
            os.chdir(folder_name)
            with open(file_name, "w") as f:
#                print("point5")
                f.write(file_text)
            os.chdir(wd_now)
#            print("point6")
        os.remove(file_name)
#        print("point7")
    except:
        print("error")    
        
        return True
    return False

def rename_file():
    old_file_name = __enter_name()
    if ".txt" not in old_file_name:
        old_file_name+=".txt"
    new_file_name = __enter_name()
    if ".txt" not in new_file_name:
        new_file_name+=".txt"
    os.rename(old_file_name, new_file_name)
#просмотр файлов
def view_files():
    for i in  os.listdir(path="."):
        print(i)

