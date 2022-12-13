#Dependencies
import os
import re
import tempfile
import numpy
from linecache import getline
import shutil as sh
from pathlib import Path as path



#Write Into A Text
def write(file, write):
    
    f = file
        
    with open(file, 'r') as file :
        file.read()

    with open(f, 'a') as file :    
        return file.write('\n' + write)


    #Replace a Text from a file
def rewrite(file):
    write = file
    with open(file, 'r') as file :
        filedata = file.read() 
        replace1 = '#output of openai'
        vuln = 'nice'
        resub = re.sub(vuln,replace1, filedata)

    with open(write, 'w') as file :    
        return file.write(resub)

#Copy files 
def cp(file,path):
    src = file
    dst = path
    return sh.copy(src,dst)
            
#Backup PHP Files
def backup():
    path = input("Path: ")
    files = [x for x in os.listdir(path) if x.endswith('.php')]
    for i in range(len(files)):
        cp(f'{path}/{files[i]}','.ignore/backup/')
        i+=1
    print(f"Done! {files} has been backed up.")



#Write the lines scanned with the word "mysqli"
def identifyFileLines():
    path = input('Path: ')
    file = [x for x in os.listdir(path) if x.endswith('.php')]
    php_sql1 = '$query = '
    lines = []
    FILES = []
    for i in range(len(file)):
        with open(str(path) + '/' + str(file[i])) as myFile:
            for num, line in enumerate(myFile,1):
                if php_sql1 in line:
                    lines.append(num)
                    global Line 
                    Line = lines
                    global Files
                    FILES.append(str(file[i]))
                    Files = FILES


#Write SQL Vulnerability
def wSQLVuln():
    identifyFileLines()
    line_numbers = Line 
    x = 0
    while x < len(line_numbers):
        vuln = getline(f'.ignore/backup/{Files[x]}', line_numbers[x])
        x+=1
        write('.ignore/gptPrompt', vuln)

