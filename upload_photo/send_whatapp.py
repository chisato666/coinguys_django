import pywhatkit
import cv2
import csv
import excel_setting
import random
import string
import my_functions
import os.path
import time
import pyautogui as p
import pyperclip as pc


#https://chat.whatsapp.com/LlhnVvkq8Ze7eGHV7qXUvB

excel_setting.init()
count=0
img_count = 0

img_link='/Users/apple/perfumeHK/'
photo_ext='.jpeg'
currency=1
msg=""

#TESTING
# whatsapp_no='JQMPkT20zUh3KJeImhYDml'


whatsapp_no='LlhnVvkq8Ze7eGHV7qXUvB'



excel_file='/Users/apple/Downloads/perfumeHK - 20OCT22.csv'
my_functions.init()
a=my_functions.load_data(excel_file,img_link,photo_ext,currency)

for i in range (0,len(a)):
    #print(a[i])
    msg =a[i][my_functions.title] + "\n\n" + a[i][my_functions.body]+ "\n"
    print(msg)
    img=a[i][my_functions.image]
    price=a[i][my_functions.price]
    option_ls=a[i][my_functions.option_value]

    for x in range(0, len(img)):
        print(img[x])
        if x == 0:
            pywhatkit.sendwhats_image(whatsapp_no, img[x], "  Product No. " + a[i][my_functions.product_id])
        else:
            pywhatkit.sendwhats_image(whatsapp_no, img[x])

        photo_found = True
        time.sleep(2)

    for x in range(0, len(price)):
        msg=msg + "\n\n $" +price[x] + " " + option_ls[x]

    for x in range(0, len(option_ls)):
        print(option_ls[x])



    if photo_found:
        p.typewrite(' ')
        pc.copy(msg)
        p.hotkey('command', 'v')
        p.press('enter')
        time.sleep(2)

# for i in range (0,len(a[0][2])):
#     print(a[0][2][i])


# with open('/Users/apple/Downloads/perfumeHK - 29SEP22 (1).csv') as file_obj:
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
#         # Check the photo is exist and the range between two number e.g.: 1,5
#
#         ls3=my_functions.load_photo(ls,img_link,photo_ext)
#
#
# #This is multiple variant checking
#
#         if row[excel_setting.option_name] !='':
#             pp = row[excel_setting.price].split(",")
#             ov = row[excel_setting.option_value].split(",")
#             vi = row[excel_setting.variant_image].split(",")
#
#             msg=row[excel_setting.title] + "\n\n"+row[excel_setting.body]
#
#             for i in range(0,len(pp)):
#                 msg = msg + "\n $" + pp[i] + " - " + ov[i] + "\n"
#        #         print("\nPrice: $" + pp[i] + " - " + ov[i] + "\n")
#
#         else:
#             msg =row[excel_setting.title] + "\n\n" + row[excel_setting.body]+ "\n$" + row[excel_setting.price]
#
#
#         for i in range(0, len(ls3)):
#             photo_found=False
#             img = ls3[i]
#
#             if i==0:
#                 pywhatkit.sendwhats_image(whatsapp_no, img,"  Product No. " + ls[0])
#             else:
#                 pywhatkit.sendwhats_image(whatsapp_no, img)
#
#             photo_found=True
#             time.sleep(1)
#
#         if photo_found:
#             p.typewrite(' ')
#             pc.copy(msg)
#             p.hotkey('command', 'v')
#             p.press('enter')
#             time.sleep(1)

    # print (*ls, sep=",")
    #
    # print (*ls3, sep=",")

