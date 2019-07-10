# -*- coding: utf-8 -*-
"""
Created on Wed May 15 14:58:10 2019

@author: 1
"""
# In[文件重命名]
import os
import json

os.chdir(r'I:\AI\B站\52922519')
for num_dir in os.listdir('.'):
    os.chdir(num_dir)
    for name in os.listdir('.'):
        if os.path.splitext(name)[1] == '.info':
            f = open(name,'r',encoding= 'utf-8')
            data = f.read()
            json_data = json.loads(data)
            title = json_data['PartName']
            f.close()
            break
    for name in os.listdir('.'):
        if os.path.splitext(name)[1] == '.flv':
            os.rename(name,title+'.flv')
            print(title+'：命名成功')
            break
    os.chdir('..')

# In[文件转移]
import shutil
os.chdir(r'I:\AI\B站\52922519')
dst = r'I:\AI\万门大学大数据\\'
for num_dir in os.listdir('.'):
    os.chdir(num_dir)
    for name in os.listdir('.'):
        if os.path.splitext(name)[1] == '.flv':
            shutil.move(name,dst+name)
            print(name+'：移动完成')
            break
    os.chdir('..')