#Найдем последний файл, если его дата меньше чем на сутки от нас, скопируем его
#Подключаем модуль 
import argparse
import os
import os.path
import shutil
import sys 
import time 

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-s', '--source', default = '')
    return parser

#Каталог из которого будем брать изображения (перенести в параметр??) 
parser = createParser()
namespace = parser.parse_args(sys.argv[1:])
if '' == namespace.source:
    print("Каталог- источник не задан")
    exit()

directory = namespace.source

#Получаем список файлов в переменную files 
files = os.listdir(directory) 

#Фильтруем список 
files= filter(lambda x: x.endswith('.bak'), files) 

files = list(files)
files.sort()
files.reverse()
same_file = files[0]

current_time = time.time()
full_name = directory + '\\' + same_file
file_time = os.path.getmtime(full_name)
if current_time - file_time < 24 * 60 * 60:
    shutil.copyfile(full_name, same_file)
    print(same_file + ' скопирован')
else:
    print(same_file + ' старый, не скопирован')

#Удаление старых файлов
#Получаем список файлов в переменную files 
files = os.listdir('.') 

#Фильтруем список 
files= filter(lambda x: x.endswith('.bak'), files) 

#files = list(files)

for file in files:
    file_time = os.path.getmtime(file)
    if current_time - file_time > 4 * 24 * 60 * 60:
        os.remove(file)
        print("Удален файл " + file)