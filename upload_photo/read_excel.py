import csv
import excel_setting
import random
import string
import my_functions
import os.path
import time
import pandas as pd


excel_setting.init()


img_link='/Users/apple/perfumeHK/'
photo_ext='.jpeg'

excel_file='/Users/apple/Downloads/perfumeHK - 29SEP22 (1).csv'

def load_data(excel_file):
    columns = 10
    rows = 0

    a = [[0 for x in range(columns)] for y in range(rows)]

    row_count = 0

    with open(excel_file) as file_obj:
        # Skips the heading
        # Using next() method
        heading = next(file_obj)

        reader_obj = csv.reader(file_obj)

        # Iterate over each row in the csv file
        for row in reader_obj:

            # printing lowercase
            letters = string.ascii_lowercase
            rad= ''.join(random.choice(letters) for i in range(10))

            ls = row[excel_setting.image].split(",")

            ls3=my_functions.load_photo(ls,img_link,photo_ext)

    #This is multiple variant checking

            if row[excel_setting.option_name] !='':
                pp = row[excel_setting.price].split(",")
                ov = row[excel_setting.option_value].split(",")
                vi = row[excel_setting.variant_image].split(",")

                msg=row[excel_setting.title] + "\n\n"+row[excel_setting.body]

                for i in range(0,len(pp)):
                    msg = msg + "\n $" + pp[i] + " - " + ov[i] + "\n"
           #         print("\nPrice: $" + pp[i] + " - " + ov[i] + "\n")

            else:
                msg =row[excel_setting.title] + "\n\n" + row[excel_setting.body]+ "\n$" + row[excel_setting.price]

            img_list=[]

            for i in range(0, len(ls3)):
                img = img_link + str(ls3[i]) + photo_ext
                if (os.path.isfile(img)):
                    print("ls 3 --- " + img_link + str(ls3[i]) + photo_ext)
                    img_list.append(img)

            line=[row[excel_setting.title],row[excel_setting.tags],row[excel_setting.price],row[excel_setting.qty],ls3,row[excel_setting.body],row[excel_setting.option_name],row[excel_setting.option_value],row[excel_setting.variant_image]]
            a.append(line)

            row_count = row_count + 1

    return a
    # title = 0
    # tags = 1
    # price = 2
    # qty = 3
    # image = 4
    # body = 5
    # option_name = 6
    # option_value = 7
    # variant_image = 8

#print (*a, sep=",")
a=my_functions.load_data(excel_file,img_link,photo_ext)
for i in range (0,len(a)):
    print(a[i])
# for i in range (0,len(a[0][2])):
#     print(a[0][2][i])