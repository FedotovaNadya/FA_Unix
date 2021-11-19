import file_manager_functions as fmf

session = 1
actions=[
    ["Выход", "До свидания!"], 
    [ "Создание папки", fmf.new_folder], 
    ["Удаление папки по имени",fmf.del_folder], 
    ["Заход в папку по имени",fmf.goto_folder], 
    ["выход на уровень вверх",fmf.goup_folder], 
    ["Создание пустых файлов с указанием имени",fmf.create_empty_file], 
    ["Запись текста в файл", fmf.add_text_file], 
    ["Просмотр содержимого текстового файла",fmf.viewing_text_file], 
    ["Удаление файлов по имени",fmf.del_file], 
    ["Копирование файлов из одной папки в другую",fmf.copying_file],
    ["Перемещение файлов",fmf.move_file], 
    ["Переименование файлов",fmf.rename_file], 
    ["Вывод файлов в директории", fmf.view_files],
]

fmf.os.chdir(fmf.wd)    

while session:
    print("Текущая директория:",fmf.now_wd)
    #вывод возможных действий
    print("Выберите действие: ")
    for i in range(len(actions)):
        msg=" {0:2d} - {1}".format(i,actions[i][0])
        print(msg)

    act=input("Введите номер действия: ")
    if act=="0":
        print("До свидания!")
        session=False
    else:
        try:
            act=int(act)
            actions[act][1]()
        except:
            print("Что-то пошло не так")