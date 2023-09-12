from instagrapi import Client
from instabot import Bot

username = 'trendyground'
password = 'socool666'

excel_file='/Users/apple/Downloads/perfumeHK - 20OCT22.csv'
img_link='/Users/apple/perfumeHK/'
photo_ext='.jpeg'

c_bot = Client()
c_bot.login(username, password)
img=[]
line='/Users/apple/Downloads/IMG_1298.JPG'
img.append(line)
line='/Users/apple/Downloads/IMG_1299.JPG'
img.append(line)

img_x='/Users/apple/Downloads/IMG_8048.JPG'

print(img)
text="Guerlain Parfum"
c_bot.album_upload(
        img,
        caption=text)

# b_bot = Bot()
# b_bot.login(username, password)
# if (img_no>1):
#     c_bot.album_upload(
#         img,
#         caption=text)
# else:
#     b_bot.upload_photo(img,caption=text)