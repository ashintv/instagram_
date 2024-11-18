#choose a random profile and post
import random
from profile_id import profiles_ids
directory_path = random.choice(profiles_ids)

import os
import random
# Define the directory path (adjust to the path of your choice)
 # Change this to the target directory
# List all files in the directory
files = [f for f in os.listdir(directory_path)
         if os.path.isfile(os.path.join(directory_path, f)) and not f.endswith(".txt") and not f.endswith(".json.xz")]

# Check if there are any files in the directory
if files:
    # Select a random file
    random_file = random.choice(files)
    print(type(random_file))
    print(f"Randomly selected file: {random_file}")
else:
    print("No files found in the directory.")

#create a dictionary of post to be posted
caption_name = random_file.split('.')[0]+'.txt'
caption = open(f'{directory_path}/{caption_name}').read()
post =  random_file.split('.')[0]
print(caption)

from instabot import Bot
bot = Bot(save_logfile= False,)
user = input('Enter user name : ')
passw = input('Enter instagram pass : ')
bot.login(username=user,password=passw,use_cookie=False)

try:
    
    if random_file.endswith('.mp4'):
        print(f'{directory_path}/{random_file}')
        bot.upload_video(video=f'{directory_path}/{random_file}',caption=caption)
        
    elif random_file.endswith('.jpg'):
        print(f'{directory_path}/{random_file}')
        bot.upload_photo(video=f'{directory_path}/{random_file}',caption=caption)

except:
    print(Exception)