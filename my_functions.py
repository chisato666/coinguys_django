import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import os.path
import csv
import random
import string


def init():
    global title,tags,price,qty,image,body,option_name,option_value,variant_image,product_id,msg,sepa
    title = 0
    tags = 1
    price = 2
    qty = 3
    image = 4
    body = 5
    option_name = 6
    option_value = 7
    variant_image = 8
    msg = 9
    product_id = 10
    sepa=';'

#Load excel File into a list which

def load_data(excel_file,img_link,photo_ext,currency):
    columns = 10
    rows = 0
    sepa=";"
    init()
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

            ls = row[image].split(sepa)

            ls3=load_photo(ls,img_link,photo_ext)
            #print("LS3 XXXX = ")
            #print(*ls3, sep=',')
            pp = row[price].split(sepa)
            pp = [int(item) * currency for item in pp]

            #pp = [num * currency for num in range(1, len(pp))]
            ov = row[option_value].split(sepa)
            vi = row[variant_image].split(sepa)
    #This is multiple variant checking

            if row[option_name] !='':


                msg=row[title] + "\n\n"+row[body]
                max_len=0

                if (len(pp)>=len(ov)):
                    max_len=len(ov)
                else:
                    max_len=len(pp)

                for i in range(0,max_len):
                    msg = msg + "\n $" + str(int(pp[i])) + " - " + ov[i] + "\n"
                    #print("\nPrice: $" + str(round(currency * int(pp[i]))) + " - " + ov[i] + "\n")

            else:
                msg =row[title] + "\n\n" + row[body]+ "\n$" + str(pp[0])

            img_list=[]
            # print (*ls3, sep=",")
            # print("LS3 XXXX XXXXX - " + str(len(ls3)))

            for i in range(0, len(ls3)):
                #img = img_link + str(ls3[i]) + photo_ext
                #print("IMG XXXXX" + img)
                if (os.path.isfile(ls3[i])):
                    #print("ls 3 --- "  + str(ls3[i]))
                    img_list.append(ls3[i])

            #print(" msg !!! " + msg)
            # print(" Tags " + row[tags])
            #
            # print (*pp, sep=",")
            # print (*ov, sep=",")
            # print (*vi, sep=",")
            #
            # print (*ls3, sep=",")
            # print(" Body " + row[body])
            # print(" Option name " + row[option_name])
           # print(" Product ID " + row[product_id])

            try:
                pd_id=(row[product_id])
                line=[row[title],row[tags],pp,row[qty],img_list,row[body],row[option_name],ov,vi,msg,row[product_id]]
            except :
                line=[row[title],row[tags],pp,row[qty],img_list,row[body],row[option_name],ov,vi,msg]


            a.append(line)

            row_count = row_count + 1

    return a

# Load the photo from two different number
def load_photo(ls,img_link,photo_ext):


    if (len(ls)) > 1:
        diff = int(ls[1]) - int(ls[0]) + 1
        ls3 = ["" for x in range(diff)]
        img_count = 0

        for x in range(0, diff):
            img_num = x + int(ls[0])

            v_img = img_link + str(img_num).zfill(4) + photo_ext
            #print("Load photo " + v_img)
            if (os.path.isfile(v_img)):
                ls3[img_count] = v_img
                if (x!=diff):
                    img_count = img_count + 1
                print("   v_img {} diff {} ls3 {} ls1 {} ".format(v_img, diff, ls3[x], ls))
    else:
        ls3 = [""]
        v_img = img_link + str(ls[0]).zfill(4) + photo_ext
        if (os.path.isfile(v_img)):
            ls3[0] = v_img
        img_count = 1
        #print( "len " + str(len(ls3)))
    return ls3

def isvalid(url):
	return requests.head(url).status_code < 400

def check_photo_valid(url,photo_ext):
    pp = photo_ext.split(sepa)

    return requests.head(url).status_code < 400
#check the array is in range
def isRange(i,pp):

    if i >= len(pp):
        #print("out")
        return ""
    else:
        #print(pp[i])
        #print("Sell   i {} pp {} len{}".format(i, pp[i], len(pp)))
        return pp[i]


def send_email(toaddr):
    smtp_name = "smtp.gmail.com"
    login_name = 'bitcontrol2018'
    pwd = 'xgvgtothglqfqhag'

    server = smtplib.SMTP(smtp_name, 587)
    server.starttls()
    server.login(login_name, pwd)
    cc = ['kenji_so@yahoo.com']
    fromaddr = 'kenji_so@yahoo.com'

    subject = "The RSI is under 30 or above 75"
    toaddrs = [toaddr]
    msg="Please check"

    body = f"Subject: {subject}\nFrom: {fromaddr}\nTo: {toaddrs}\nContent-Type: text/html\n\n{msg}"  # This is where the stuff happens

    message_text = " "
    message = "From: %s\r\n" % fromaddr + "To: %s\r\n" % toaddr + "CC: %s\r\n" % ",".join(
        cc) + "Subject: %s\r\n" % subject + "\r\n" + msg
    server.sendmail(fromaddr, toaddrs, body)
