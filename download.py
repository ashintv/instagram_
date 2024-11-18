import os
from profile_id import profiles_ids
import random
import instaloader
for user_id in profiles_ids:
    l = instaloader.Instaloader()
    l.download_profile(user_id,profile_pic=False)
for user_id in profiles_ids:
    file_path = f'Downloads/{user_id}/id'
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"File has been deleted.")
    else:
        print(f"File ' does not exist.")

