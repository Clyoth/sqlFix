print("""
.------------------------------------------------------------------------------------------------------------------------.
|.----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  |
|| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. ||
|| |    _______   | || |    ___       | || |   _____      | || |  _________   | || |     _____    | || |  ____  ____  | ||
|| |   /  ___  |  | || |  .'   '.     | || |  |_   _|     | || | |_   ___  |  | || |    |_   _|   | || | |_  _||_  _| | ||
|| |  |  (__ \_|  | || | /  .-.  \    | || |    | |       | || |   | |_  \_|  | || |      | |     | || |   \ \  / /   | ||
|| |   '.___`-.   | || | | |   | |    | || |    | |   _   | || |   |  _|      | || |      | |     | || |    > `' <    | ||
|| |  |`\____) |  | || | \  `-'  \_   | || |   _| |__/ |  | || |  _| |_       | || |     _| |_    | || |  _/ /'`\ \_  | ||
|| |  |_______.'  | || |  `.___.\__|  | || |  |________|  | || | |_____|      | || |    |_____|   | || | |____||____| | ||
|| |              | || |              | || |              | || |              | || |              | || |              | ||
|| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' ||
| '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' |
| ---------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                        |
| This software is provided "as is" without any warranty of any kind. The author of the software shall not be liable for |
| any claim, damages, or other liability arising from the use of the software. The user of the software assumes all risk |
| and responsibility for the use of the software.                                                                        |
|                                                                                                                        |   
| If you run into any errors make sure you have installed the dependencies required. You can do this by running          |   
| this command:                                                                                                          |
|      $ pip install -r requirements.text                                                                                |
|                                                                                                                        |
| Make sure to Backup the files first, for safety purposes the program wont work if you dont backup your files.          |                                                                                                                
| Options:                                                                                                               |
|  [0]Exit                                                                                                               |   
|  [1]Backup Files                                                                                                       |           
|  [2]Setup API                                                                                                          |                           
|  [3]Fix SQL Vulnerabilities                                                                                            |
|  [4]Documentation                                                                                                      |
'------------------------------------------------------------------------------------------------------------------------'                                                                                                                                 
    """)

import sys

sys.path.insert(0, 'Modules/')

from aiModule import *
from funcModule import *


def identityFileLines():
    path = '.ignore/backup'
    file = [x for x in os.listdir(path) if x.endswith('.php')]
    php_sql1 = '$query = '
    lines = []
    FILES = []
    for i in range(len(file)):
        with open(str(path) + '/' + str(file[i])) as myFile:
            for num, line in enumerate(myFile,1):
                if php_sql1 in line:
                    lines.append(num)
                    global Lines 
                    Lines = lines
                    global Files
                    FILES.append(str(file[i]))
                    Files = FILES

def writeFixedCode(input):
    identityFileLines()
    x = 0

    while True:
        with open('.ignore/gptPrompt','r') as file:
            global prompt
            prompt = file.read()

            text = []

            text.append(prompt)

        while x < len(Files):


            with open(f'.ignore/backup/{Files[x]}', 'r') as fIle:
                filedata = fIle.read()

            # Replace the target string
            filedata = filedata.replace(text[x],input)

            with open(f'.ignore/backup/{Files[x]}', 'w') as fiLe:
                fiLe.write(filedata)

            x+=1
        break

def wKey():
    with open("api_key.dat",'r+') as file:
        file.truncate(0)
    inp = input('Enter your OpenAI API key: ')
    write('api_key', inp)
    print("API has been written to the file (api_key.dat)")
    
    
def fixSQL():
    wSQLVuln()
    getKey()
    response = str(gptResponse())
    writeFixedCode(response)

    print(f'SQL Vulnerability fixed at line/s{Lines}')

    with open("Modules/gptPrompt",'r+') as file:
        file.truncate(0)

def exit():
    exit

def document():
    print("""

SYSTEM REQUIREMENTS:
This software requires the following:

    Minimum:
    Processor : i3 - 2500S  
    OS : Linux x32 (Windows not Tested)
    Memory: 4GB RAM 
    Graphics: None
    Sound Card: None

    Recommended(For Bigger Servers):
    Processor : i7 - 4790K  
    OS : Linux x64 (Windows not Tested)
    Memory: 16GB RAM 
    Graphics: None
    Sound Card: None

INSTALLATION:
To install this software, follow these steps:

#Clone the project

```bash
git clone https://github.com/Clyoth/GPT-3-Vulenrability-Scanner
```

#Go to the project directory

```bash
cd GPT-3-Vulenrability-Scanner
```

#Install dependencies

```bash
pip install -r requirements.txt
```

#Start the app

```bash
python3 main.py



TROUBLESHOOTING:


Troubleshoot errors:

    If you encounter any issues while using this software, try the following solutions:

     - Check if dependencies are installed, use 'pip install -r requirements.txt' to install them.

     - Try to use a Virtual Environment and use Python 3.11

    If above solutions don't work;

     - Submit a ticket to us via https://github.com/Clyoth/GPT-3-Vulnerability-Scanner-DEVELOPMENT/issues.

 Troubleshoot Corrupted PHP Files:

    If your PHP files don't work as they used to before try to retrieve the original files at '.ignore/backup'


KNOWN ISSUES:
Currently, the following issues are known:

None

CONTACT INFORMATION:
If you have any further questions or concerns, please contact us at .

        """)


COMMANDS  ={
    '0' : exit,
    '1' : backup,
    '2' : wKey,
    '3' : fixSQL,
    '4' : document
}

while True:
    command = input('> ')
    COMMANDS[command]()

