from instabot import Bot
import os

os.system("rm -rf config")

bot = Bot()

bot.login(username = "trendyground",
		password = "socool666")

dir_image = "../photo/chanel/"

# Recommended to put the photo
# you want to upload in the same
# directory where this Python code
# is located else you will have
# to provide full path for the photo

for image in os.listdir(dir_image):
	bot.upload_photo(dir_image + image,
				caption ="Perfume #edt #chanel")
