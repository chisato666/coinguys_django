import random
import string
import my_functions

# Import necessary packages
import csv
import yfinance as yf
import numpy as np
import talib
import pandas as pd

# Open file

# defined the column of input file

title=0
tags=1
price=2
qty=3
image=4
body=5
option_name=6
option_value=7
variant_image=8

count=0

img_link='https://9c05-182-239-122-133.ngrok-free.app/photo/watch/gucci/IMG_'
excel_file='/Users/apple/Documents/Documents/Etsy/251023.csv'
photo_ext='.JPG'

data = {
    "Handle": [""],
    "Title": [''],
    "Body": [""],
    "Vendor": "",
    "Standardized Product Type": '',
    "Custom Product Type": '',
    "Tags": [''],
    "Published": [''],
    "Option1 Name": [''],
    "Option1 Value": [''],
    "Option2 Name": [''],
    "Option2 Value": [''],
    "Option3 Name": [''],
    "Option3 Value": [''],
    "Variant SKU": [''],
    "Variant Grams": [''],
    "Variant Inventory Tracker": [''],
    "Variant Inventory Qty": [''],
    "Variant Inventory Policy": [''],
    "Variant Fulfillment Service": [''],
    "Variant Price": [0],
    "Variant Compare At Price": [0],
    "Variant Requires Shipping": [''],
    "Variant Taxable":['FALSE'],
    "Variant Barcode":[''],
    "Image Src":[''],
    "Image Position":[0],
    "Image Alt Text":[''],
    "Gift Card":['FALSE'],
    "SEO Title":[''],
    "SEO Description":[''],
    "Google Shopping / Google Product Category": [''],
    "Google Shopping / Gender": [''],
    "Google Shopping / Age Group": [''],
    "Google Shopping / MPN": [''],
    "Google Shopping / AdWords Grouping": [''],
    "Google Shopping / AdWords Labels": [''],
    "Google Shopping / Condition": [''],
    "Google Shopping / Custom Product": [''],
    "Google Shopping / Custom Label 0": [''],
    "Google Shopping / Custom Label 1": [''],
    "Google Shopping / Custom Label 2": [''],
    "Google Shopping / Custom Label 3": [''],
    "Google Shopping / Custom Label 4": [''],
    "Variant Image": [''],
    "Variant Weight Unit": [''],
    "Variant Tax Code":[''],
    "Cost per item":[''],
    "Price / china":[''],
    "Compare At Price / china": [''],
    "Price / international": [''],
    "Compare At Price / International": [''],
    "Status":['']

}

df = pd.DataFrame(data)


w, h = 50, 200
data = [["" for x in range(w)] for y in range(h)]

#The spec
sepa=";"

with open(excel_file) as file_obj:
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

        ls = row[image].split(sepa)
        print("   len ls {}  ls {} ".format( len(ls),ls))

        if (len(ls))>1:
            ls1=ls[0]
            ls2=ls[1]
            diff=int(ls[1]) - int(ls[0]) +1
            ls3 = ["" for x in range(diff-1)]
            img_count=0
            for x in range(1,diff):
                img_num= x + int(ls1)

                v_img=img_link + str(img_num).zfill(4) + photo_ext
                print(v_img)
                if (my_functions.isvalid(v_img)):
                    ls3[img_count]= img_num
                    img_count=img_count+1
                    print("   v_img {} diff {} ls3 {} ls1 {} ".format(v_img, diff, ls3, ls1))
        elif (len(ls)==1):
            ls3=""
            img_count=1

        else:
            ls1=ls[0]
            img_count=0




        #For more than 1 variant
        if row[option_name] !='':
            print("Mult variant" + row[option_name])
            pp = row[price].split(sepa)
            ov = row[option_value].split(sepa)
            vi = row[variant_image].split(sepa)

            df = df.append({
                "Handle": rad + row[title],
                "Title": row[title],
                "Body": row[body],
                "Vendor": 'me',
                "Tags": row[tags],
                "Published": "TRUE",
                "Variant Inventory Tracker": "shopify",
                "Variant Inventory Qty": row[qty],
                "Variant Inventory Policy": "deny",
                "Variant Fulfillment Service": "manual",
                "Variant Price": pp[0],
                "Image Src": img_link + str(ls[0]).zfill(4) + photo_ext,
                "Image Position": 1,
                "Variant Requires Shipping": 'TRUE',
                "Variant Taxable": 'FALSE',
                "Option1 Name": row[option_name],
                "Option1 Value": ov[0],
                "Variant Image": img_link + str(vi[0]).zfill(4)  + photo_ext,
                "Status": 'active'
            }, ignore_index=True)

            print("IMG_count  : " + str(img_count))
            if img_count<len(pp):
                img_count=len(pp)

            for i in range(1, img_count):
                #print(ls[i])
                print("IMG_count " + str(img_count))
                # if i>=len(vi):
                #     v_img=""
                # else:
                v_img=img_link + str(my_functions.isRange(i,vi)).zfill(4) + photo_ext
                if not (my_functions.isvalid(v_img)):
                    v_img=""
                #This is variant image
                try:
                    src_img=img_link + str(ls3[i-1]).zfill(4) + photo_ext
                except IndexError:
                    src_img=""
                    print("Index out of range")


                if i>=len(pp):
                    df = df.append({
                        "Handle": rad + row[title],
                        "Image Position": i + 1,
                        "Variant Inventory Tracker": "",
                        "Variant Inventory Qty": "",
                        "Variant Inventory Policy": "",
                        "Variant Fulfillment Service": "",
                        "Variant Price": my_functions.isRange(i, pp),
                        "Option1 Value": my_functions.isRange(i, ov),
                        "Image Src": src_img,
                        "Variant Image": v_img
                    }, ignore_index=True)
                else:
                    df = df.append({
                        "Handle": rad + row[title],
                        "Image Position": i+1,
                        "Variant Inventory Tracker": "shopify",
                        "Variant Inventory Qty": row[qty],
                        "Variant Inventory Policy": "deny",
                        "Variant Fulfillment Service": "manual",
                        "Variant Price": my_functions.isRange(i,pp),
                        "Option1 Value": my_functions.isRange(i,ov),
                        "Image Src": src_img,
                        "Variant Image": v_img
                    }, ignore_index=True)
        else:    #Single item
            df = df.append({
                "Handle":  rad + row[title],
                "Title": row[title],
                "Body": row[body],
                "Vendor": 'me',
                "Tags": row[tags],
                "Published": "TRUE",
                "Variant Inventory Tracker": "shopify",
                "Variant Inventory Qty": row[qty],
                "Variant Inventory Policy": "deny",
                "Variant Fulfillment Service": "manual",
                "Variant Price": row[price],
                "Image Src": img_link + str(ls[0]).zfill(4) + photo_ext,
                "Image Position": 1,
                "Variant Requires Shipping": 'TRUE',
                "Variant Taxable": 'FALSE',
                "Status": 'active'
            }, ignore_index=True)

            for i in range(0, len(ls3)):
                #print(ls[i])
                if (my_functions.isvalid(img_link + str(ls3[i]).zfill(4) + photo_ext)):
                    df = df.append({
                        "Handle": rad + row[title],
                        "Image Position": i+1,
                        "Image Src": img_link + str(ls3[i]).zfill(4) + photo_ext
                    }, ignore_index=True)



df = df.replace({np.nan: None})
print(df)

with open('products_export.csv', 'a+', newline='') as f:
    writer = csv.writer(f)
    for i in range(len(df)):
        writer.writerow(df.loc[i, :])
        #print(df.loc[i, :])
    # for x in df:
    #     writer.writerows(x)
