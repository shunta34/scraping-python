# import os
# import random
# import requests
# import pandas as pd
# from time import sleep

# IMAGE_DIR = './images/'

# df = pd.read_csv('image_urls_20210714.csv')

# if os.path.isdir(IMAGE_DIR):
#   print('すでにあります！')
# else:
#   os.makedirs(IMAGE_DIR)

# for file_name, yahoo_image_url in zip(df.filename[:5], df.yahoo_image_url[:5]):
#   image = requests.get(yahoo_image_url)
#   with open(IMAGE_DIR + file_name + '.jpg', 'wb') as f:
#     f.write(image.content)

#   sleep(2)
#   sleep(
#     random.randint(1, 10)
#   )
