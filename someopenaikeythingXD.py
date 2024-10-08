

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

def generate_random_key(total_length):
  """
  Generates a random key of specified total length with 1-3 hyphens, 1-3 underscores, and 'sk-' at the end.

  Args:
      total_length (int): The desired total length of the final string (including symbols).

  Returns:
      str: The generated random key.
  """

  # Define the characters to choose from
  characters = string.ascii_letters + string.digits

  # Calculate the length of the base random string
  base_length = total_length - 3  # Account for 'sk-'

  # Ensure enough space for at least one hyphen and one underscore
  max_hyphens = max(1, min(3, base_length - 1))  # Leave space for at least one underscore
  max_underscores = max(1, min(2, base_length - 1))  # Leave space for at least one hyphen

  # Determine the number of hyphens and underscores to insert
  num_hyphens = random.randint(1, max_hyphens)
  num_underscores = random.randint(1, max_underscores)

  # If there's not enough space for both minimum hyphens and underscores, adjust
  if num_hyphens + num_underscores > base_length:
      if num_hyphens > num_underscores:
          num_hyphens = base_length - num_underscores
      else:
          num_underscores = base_length - num_hyphens

  # Generate the base random string, accounting for space needed for symbols
  adjusted_base_length = base_length - num_hyphens - num_underscores

  # Convert characters to ASCII codes and create a CUDA tensor
  char_codes = torch.tensor([ord(c) for c in characters], dtype=torch.int32, device='cuda')

  # Generate random indices within the range of available characters
  random_indices = torch.randint(0, len(characters), (adjusted_base_length,), dtype=torch.int32, device='cuda')

  # Use the random indices to select characters from the char_codes tensor
  random_char_codes = char_codes[random_indices]

  # Convert the ASCII codes back to characters and join them into a string
  base_string = ''.join([chr(code) for code in random_char_codes.cpu().numpy()])

  # Create a list to hold all characters (base string + symbols)
  all_chars = list(base_string)

  # Insert hyphens at random positions
  hyphen_positions = random.sample(range(len(all_chars)), num_hyphens)
  for pos in hyphen_positions:
      all_chars.insert(pos, '-')

  # Insert underscores at random positions
  underscore_positions = random.sample(range(len(all_chars)), num_underscores)
  for pos in underscore_positions:
      all_chars.insert(pos, '_')

  # Add 'sk-' at the end
  final_string = ''.join(all_chars)
  return final_string


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
        test_the_key =  generate_random_key(98)
        try:
            client = OpenAI(
            api_key =  test_the_key
            )
            prompt = "hi"

            
            completion = client.completions.create(
            model = "gpt-4o",
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

