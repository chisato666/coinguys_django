from instagrapi import Client
from instabot import Bot

import csv
import excel_setting
import random
import string
import googletrans
import my_functions

username = 'trendyground'
password = 'socool666'


excel_file='/Users/apple/Documents/Etsy/9Jan22.csv'
img_link='/Users/apple/.bitnami/stackman/machines/xampp/volumes/root/htdocs/photo/9JAN22/IMG_'
photo_ext='.JPG'

# excel_file='/Users/apple/Downloads/perfumeHK - 20OCT22.csv'
# img_link='/Users/apple/perfumeHK/'
# photo_ext='.jpeg'
currency=1
msg=""

my_functions.init()




# excel_setting.init()
# print(excel_setting.option_name)
#
# excel_file='/Users/apple/Downloads/Etsy - 5mar.csv'
#
#
# with open(excel_file) as file_obj:
#     # Skips the heading
#     # Using next() method
#     heading = next(file_obj)
#
#     # Create reader object by passing the file
#     # object to reader method
#     reader_obj = csv.reader(file_obj)
#
#     # Iterate over each row in the csv file
#     # using reader object
#     for row in reader_obj:
#
#         # printing lowercase
#         letters = string.ascii_lowercase
#         rad= ''.join(random.choice(letters) for i in range(10))
#
#         ls = row[excel_setting.image].split(",")
#
#         if (len(ls))>1:
#             ls1=ls[0]
#             ls2=ls[1]
#             diff=int(ls[1]) - int(ls[0]) +1
#             ls3 = ["" for x in range(diff)]
#
#             for x in range(1,diff):
#                 ls3[x]= x + int(ls1)
#                 #print("   x1 {} diff {} ls3 {} ls1 {} ".format(x, diff, ls3[x], ls1))
#
#             ls3[0]=int(ls[0])
#         else:
#             diff=1
#             ls3=ls[0]
#
#
#     print(row[excel_setting.title], ls3)
#
# image_dir='/Users/apple/.bitnami/stackman/machines/xampp/volumes/root/htdocs/photo/18OCT22/IMG_'
# photo_ext='.JPG'
#
# image_files = ["" for x in range(diff)]

# for x in range(0,len(ls3)):
#     image_files[x] = image_dir + "IMG_" + str(ls3[x]) + photo_ext
#
# text=row[excel_setting.title]
#
# print(image_files)



# translate of content

translator = googletrans.Translator()
#pprint(googletrans.LANGCODES)

a=my_functions.load_data(excel_file,img_link,photo_ext,currency)
c_bot = Client()
c_bot.login(username, password)


for i in range (0,len(a)):
    msg =a[i][my_functions.msg] + "\n\n"
         #+ a[i][my_functions.body]+ "\n"
    #print(msg)
    img_all=a[i][my_functions.image]
    print(img_all)
    title =a[i][my_functions.title]
    set_chinese= False
    #Change price USD to HKD
    price = (a[i][my_functions.price])
    print("i " + str(i))
    text=""

    tags = a[i][my_functions.tags].split(",")

    all_tags=""
    for x in tags:
        all_tags= all_tags + "#" + x.replace(" ", "") + ","

    #text_eng= "\n  " + title + "\n Description： " + msg.replace("<br>", "\n") + "\n Price： USD $" + str(row[
   #                                                                                                                                                 excel_setting.price]) + "\n" + all_tags
   #
   # # text_chi= "\n  " + translator.translate(row[excel_setting.title], dest='zh-tw').text + "\n 產品介紹： " + translator.translate(row[
   #                                                                                                                                excel_setting.body].replace("<br>", "\n"), dest='zh-tw').text + "\n 價錢： HKD $" + str(round(7.78 * int(row[
   #                                                                                                                                                                                                                                          excel_setting.price]))) + "\n" + all_tags

   # text= (text_eng + "\n" + text_chi)
    text=msg + all_tags
    print("xxxx" +img_all[0])
    # c_bot.album_upload(
    #     img_all,
    #     caption=text)
    print(text)


img_no=len(img_all)

print("IMG no" + str(img_no))
print(*a, sep=',')

img = ["" for x in range(len(img_all))]
for x in range(0,len(img_all)):
    img[x] = img_all[x]

print(img)

img[0]='/Users/apple/Downloads/IMG_8047.JPG'
#img[1]='/Users/apple/Downloads/IMG_8048.JPG'
# c_bot = Client()
# c_bot.login(username, password)
# b_bot = Bot()
# b_bot.login(username, password)
# if (img_no>1):
#     c_bot.album_upload(
#         img,
#         caption=text)
# else:
#     b_bot.upload_photo(img,caption=text)
