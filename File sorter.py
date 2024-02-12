#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os, shutil
import schedule
import time as tm
from datetime import time, timedelta, datetime

def job():
    def files_sorting(path):

        file_name = os.listdir(path)

        Folder_name_1 = list(set( list(i.split('.')[-1] for i in file_name if '.' in i)))

        Folder_name_Final = list(I + " Files" for I in Folder_name_1)


        for i in Folder_name_Final:
            Folder_path = os.path.join(path, i)
            if not os.path.exists(Folder_path):
                os.makedirs(Folder_path)    

            for x in file_name:
                if i.split(' ')[0] == x.split('.')[-1] and '.' in x:
                    File_path_before = os.path.join(path, x)
                    File_path_later = os.path.join(Folder_path, x)
                    shutil.move(File_path_before, File_path_later)


    path = "E:/Fields/Python/Projects/File Sorter"
    files_sorting(path)

schedule.every().day.at("04:00").do(job)

while True:
    schedule.run_pending()
    tm.sleep(1)

