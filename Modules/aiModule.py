#Dependencies
import openai as ai
from pathlib import Path
from sys import exit as term
from time import sleep
from pathlib import Path as path


#Check api key
def getKey():
    api = Path('api_key.dat')
    if (api.exists):
        key = api.read_text().lstrip().lstrip(" ").split(" ")[0].rstrip("\n")
        if (len(key) > 30):
            global Key
            Key = key
        else:
            pwd = path("api_key.dat").absolute()
            print(f"Invalid key or keyformat, please check {pwd} and make sure there is nothing in there except the key, and that the key itself is correct.")
            sleep(2)
            input("Press enter to exit now.")
            term("Invalid key.")
    else:
        path("api_key.dat").touch()
        pwd = path("api_key.dat").absolute()
        print(f"API keyfile not found, created file {pwd}, please enter your openai api key in the file.")
        sleep(2)
        input("Press enter to exit now.")
        term("File not found.")


#Connecting API
def gptResponse():

    while True:
        #read the lines in the gptPrompt file and use those as a prompt
        with open('.ignore/gptPrompt','r') as file:
            prompt = file.read()

        getKey()
        ai.api_key = Key
        response = ai.Edit.create(
        model="code-davinci-edit-001",
        input=prompt,
        instruction=f"Make the $username and $password use mysqli_real_escape_string  ",
        temperature=0,
        top_p=1
        )
        
        return response.choices[0].text

