

import openai
from openai import OpenAI
import time 
import random
import string
import time
import torch

import subprocess


def check_internet_connection():
    try:
        subprocess.check_output("ping -n 1 www.google.com", shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

def generate_random_letters(length):

  # Define the characters to choose from
  characters = string.ascii_letters + string.digits

  # Convert characters to ASCII codes and create a CUDA tensor
  char_codes = torch.tensor([ord(c) for c in characters], dtype=torch.int32, device='cuda')

  # Generate random indices within the range of available characters
  random_indices = torch.randint(0, len(characters), (length,), dtype=torch.int32, device='cuda')

  # Use the random indices to select characters from the char_codes tensor
  random_char_codes = char_codes[random_indices]

  # Convert the ASCII codes back to characters and join them into a string
  random_characters = ''.join([chr(code) for code in random_char_codes.cpu().numpy()])

  return random_characters

print('''

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#:....:-+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.      ....:-*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%##*=: ...-*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*+=---+@@%*#%@@%*-. ..+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+-..   ....+@@+. ..-*%@@+:. .*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@+.. ..:=*%@@@@@@@%*-...  :%@@+...-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@-....=%@@@@#+--::-=*%@@@#:  .:@@@:...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@=...:#@@%=:..      .   .+@@@%-. .*@@-...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@#:. :#@@*:. ..-+*#%%%##*=:*@@@@@*. .+@@-. -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@#...=@@#:. .=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@#...+@@=  .=@@@@@@@*======+*%@@@@@@@@@#+-::-+#@@@@@+=*@@@@@@%==#@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@.  =@@-. .%@@@@@@@@=         .=@@@@@-.. .::.  .+@@@.  :@@@@@#  +@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@=. :@@=. .%@@@@@@@@@=  #@@@@%+..:@@@:..*@@@@@@*..-@@.   .*@@@#  +@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@.. *@%. .#@@@@@@@@@@=. %@@@@@@*  +@+..*@@@@@@@@+ .*@. .+..-@@#  +@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@*  .@@=  :@@@@@@@@@@@=..%@@@@@@%..-@-..@@@@@@@@@#..=@. .@#:..*#  +@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@+. :@@-. =@@@@@@@@@@@=..#@@@@@@*..+@=..#@@@@@@@@+..*@. .@@@=. :  +@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@+  :@@-  =@@@@@@@@@@@=..#@@@@@+..:@@@...#@@@@@@*..:@@. .@@@@#..  +@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@*  .@@=  :@@@@@@@@@@@=  ........=@@@@@-...:--....=@@@. .@@@@@@:. +@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@.  #@%  .#@@@@@@@@@@*======+*#@@@@@@@@%*=-::-=#%@@@@+=+@@@@@@@*=#@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@=. :@@=. .%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@. .+@@-. .#@@@@@+-+##%%%%##+-. ..-*@@*.  :%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@#.  +@@=.  +@@@@-.      .   ..:=@@@#:...+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@#.  =@@#.  .-@@@@#+-::::-+#@@@@%-..  -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@%.  :#@@*.. ..:=*@@@@@@@@%*=:.....*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@=. .-*@@#+:..  #@@=:.....  .-+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@%-.. :+#@@@#*+@@@-::--=+*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@=:. ..:+*#%%%@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+:...   ... . #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*=-:....:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

''''Copyright 2024 Don Arrington, I bear no responsability for what you do with this program or'
'anything you do with it, This should never be used for any reason at any time with your vpn'
'to hide your ip and any keys you may accidently acquire should never be used for any reason')

input('press enter to continue...')


def add_text_to_file(text):
    file_path = 'openai_keys.txt'
    with open(file_path, 'a') as file:
        file.write(text + '\n')

while True:
    if check_internet_connection() is True:
        test_the_key = 'sk-' + generate_random_letters(48)
        try:
            client = OpenAI(
            api_key =  test_the_key
            )
            prompt = "hi"

            
            completion = client.completions.create(
            model = "gpt-4o-mini",
            prompt = "Test",
            max_tokens = 7,
            temperature = 0
            )
            print(f'we have a winner. ( {test_the_key} ) is good. saving it to openai_keys.txt')

            import os
            if not os.path.exists(file_path):
                open(file_path, 'w').close()

            add_text_to_file(test_the_key)
            time.sleep(0.000000001)
        except:
            print(f'KEY {test_the_key} this key is no good, continuing on..')
    else:
        print('Internet issues check connection...')
        time.sleep(1)
    time.sleep(0.000000001)

