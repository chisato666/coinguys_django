import pywhatkit
import pyautogui as p
import pyperclip as pc
import webbrowser

import cv2
import csv
import excel_setting
import random
import string
import my_functions
import os.path
import time

#https://chat.whatsapp.com/LlhnVvkq8Ze7eGHV7qXUvB

excel_setting.init()
count=0
img_count = 0

img_link='/Users/apple/perfumeHK/'
msg=""
photo_ext='.jpeg'



with open('/Users/apple/Downloads/perfumeHK - 29SEP22-1.csv', encoding='utf-8') as file_obj:
    # Skips the heading
    # Using next() method
    heading = next(file_obj)

    # Create reader object by passing the file
    # object to reader method
    reader_obj = csv.reader(file_obj)

    # Iterate over each row in the csv file
    # using reader object
    for row in reader_obj:

        # printing lowercase
        letters = string.ascii_lowercase
        rad= ''.join(random.choice(letters) for i in range(10))

        ls = row[excel_setting.image].split(",")

    #Check the photo is exist and the range between two number e.g.: 1,5

        if (len(ls))>1:
            ls1=ls[0]
            ls2=ls[1]
            diff=int(ls[1]) - int(ls[0]) +1
            ls3 = ["" for x in range(diff)]
            img_count=0
            for x in range(1,diff):
                img_num= x + int(ls1)

                v_img=img_link + str(img_num) + photo_ext
                #print(v_img)


                if (os.path.isfile(v_img)):
                    ls3[img_count]= img_num
                    img_count=img_count+1
                    #print("   v_img {} diff {} ls3 {} ls1 {} ".format(v_img, diff, ls3[x], ls1))
        else:
            ls1=ls[0]
            ls3=[""]
            img_count = 0

#This is multiple variant checking

        if row[excel_setting.option_name] !='':
            pp = row[excel_setting.price].split(",")
            ov = row[excel_setting.option_value].split(",")
            vi = row[excel_setting.variant_image].split(",")

            #print(row[excel_setting.body],row[excel_setting.tags],row[excel_setting.qty],"\n\n Variant Price " + pp[0]," Image Src "+ img_link + ls[0] + photo_ext)

            msg=row[excel_setting.body]

            for i in range(0,len(pp)):
                msg = msg + "\nPrice: $" + pp[i] + " - " + ov[i] + "\n"
                print("\nPrice: $" + pp[i] + " - " + ov[i] + "\n")


            for i in range(0, img_count):
                #print(ls[i])

                # if i>=len(vi):
                #     v_img=""
                # else:
                v_img=img_link + my_functions.isRange(i,vi) + photo_ext
                if not  (os.path.isfile(v_img)):
                    v_img=""
                #This is variant image

                src_img=img_link + str(ls3[i]) + photo_ext

                #print("\n\n  2 Variant Price " + my_functions.isRange(i, pp),"  " + my_functions.isRange(i, ov)," Image Src "  + src_img," Variant Image " + v_img)


        else:
            #print(row[excel_setting.title],row[excel_setting.body],row[excel_setting.price],img_link + str(ls[0]) + photo_ext)
            msg =row[excel_setting.title] + "\n\n" + row[excel_setting.body]+ "\n$" + row[excel_setting.price]



        img=img_link + str(ls[0]) + photo_ext
        if (os.path.isfile(img)):
            print("img  ---" + img + " Message " + msg)
            #pywhatkit.sendwhats_image("LlhnVvkq8Ze7eGHV7qXUvB", img, msg)
            #time.sleep(2)

        for i in range(0, len(ls3)):
            #print(ls[i])
            if (os.path.isfile(img_link + str(ls3[i]) + photo_ext)):
                print("ls 3 --- " + img_link + str(ls3[i]) + photo_ext)
                img=img_link + str(ls3[i]) + photo_ext

                #pywhatkit.sendwhats_image("LlhnVvkq8Ze7eGHV7qXUvB", img)
                #time.sleep(2)

print("ls0" + ls[0])
print (*ls, sep=",")

print (*ls3, sep=",")

#pywhatkit.sendwhats_image('+85291739505',img,'this is my first image',15,True,3)
#pywhatkit.sendwhatmsg_to_group('LlhnVvkq8Ze7eGHV7qXUvB','img','this is my first image',15,3)
#pywhatkit.sendwhatmsg_to_group('LlhnVvkq8Ze7eGHV7qXUvB','this is my first image',5,3)
#pywhatkit.sendwhats_image("LlhnVvkq8Ze7eGHV7qXUvB", img,"xxx 價但232323如果如果32")

text_cap='''商品編號
6913
商品特色
前調：大吉嶺茶葉、薰衣草、橘子、香檸檬、橙子花
中調：康乃馨、鳶尾、胡椒、癒創木、巴西花梨木
基調：琥珀、麝香、橡苔、雪松
商品編號:102123802001
商品重點
BVLGARI首支中性香水，簡單瓶身線條與清透顏色，配上香水清新中帶有辛辣木質香調，賦予男士親和、沈穩、紳士氣質！'''

# url="https://api.whatsapp.com/send?phone=LlhnVvkq8Ze7eGHV7qXUvB&text=test a,send message"
# webbrowser.open(url)
#pywhatkit.handwriting(text_cap,rgb=[0,0,0])
pywhatkit.sendwhats_image('LlhnVvkq8Ze7eGHV7qXUvB',img,caption=text_cap)
p.typewrite(' 1')
pc.copy(text_cap)
p.hotkey('command','v')
p.typewrite(' 1')

p.press("enter")
time.sleep(2)


# video=cv2.VideoCapture(0)
#
# ret,frame=video.read()
#
# if (ret==True):
#     img=r'/Users/apple/perfumeHK/bvlgari_pour_EDT.jpeg'
#     cv2.imwrite(img,frame)
#     pywhatkit.sendwhats_image('+85296516506',img,'this is my first image',15,True,3)
# else:
#     print('error')
# video.release()
