# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 15:37:33 2019

@author: 19041
"""

import random
import creatName

def write_file():
    data_line=""
    list_all=[]
    for i in range(20):
        data_line=""
        data_line=data_line+creatName.getName()+","
        for j in range(6):
            if j==0:
                data_line=data_line+str(random.randint(40,150))+","
            if j==1:
                data_line=data_line+str(random.randint(70,150))+","
            if j==2:
                data_line=data_line+str(random.randint(80,150))+","
            if j==3:
                data_line=data_line+str(random.randint(30,110))+","
            if j==4:
                data_line=data_line+str(random.randint(40,100))+","
            if j==5:
                data_line=data_line+str(random.randint(40,90))+"\n"
        list_all.append(data_line)
        #print(data_line)
    
    
    f=open('student.txt',mode="w+")
    f.writelines(list_all)
    f.close