import csv
import random
import string
import os.path
import time
import pandas as pd
import xlsxwriter
import openpyxl

buyer_name=34

country=42
address1=36
address2=37
city=39
postal=40
state=41
phone=43

# img_link='/Users/apple/perfumeHK/'
# photo_ext='.jpeg'
#export_file='export.csv'

excel_file='orders_export.csv'

data = {
    "buyer_name": [""],
    'country':  [''],
    "address1": [''],
    "address2": [""],
    "city": [''],
    "state": [''],
    "postal": [''],
    "phone": ['']


}

df = pd.DataFrame(data)



def load_data(df,excel_file):
    columns = 100
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

            msg =row[buyer_name] + "\n" + row[country] + "\n" + row[address1]+ "\n" + row[address2]
            #print(msg)
            img_list=[]
            if row[buyer_name]!="":
                df = df.append({
                    "buyer_name": row[buyer_name],
                    "country": row[country],
                    "address1": row[address1],
                    "address2": row[address2],
                    "city":     row[city],
                    "state":    row[state],
                    "postal":   row[postal],
                    "phone":    row[phone]

                }, ignore_index=True)

         #   line=[row[excel_setting.title],row[excel_setting.tags],row[excel_setting.price],row[excel_setting.qty],ls3,row[excel_setting.body],row[excel_setting.option_name],row[excel_setting.option_value],row[excel_setting.variant_image]]

            row_count = row_count + 1

    return df
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

df=load_data(df,excel_file)
# with open('export.xlsx', 'a+', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     for i in range(len(df)):
#         writer.writerow(df.loc[i, :])
#         print(df.loc[i, :])


workbook = openpyxl.load_workbook('export1.xlsx')

# By default worksheet names in the spreadsheet will be
# Sheet1, Sheet2 etc., but we can also specify a name.
worksheet = workbook.get_sheet_by_name('Content of Shipment')

x=2
col = "A"
row = x



print(df.iat[1, 0])
DG_list=['']

for i in range(len(df)):
    y = str(row+1)
    cell = col + y

    worksheet["A" + str(y)] = df.iat[i, 0]
    worksheet["B" + str(y)] = "DealerSend"


    worksheet["C" + str(y)] = "Direct Line - Postal"

    worksheet["D" + str(y)] = "skin care"
    worksheet["E" + str(y)] = 1
    worksheet["F" + str(y)] = "USD"
    worksheet["G" + str(y)] = 10
    worksheet["H" + str(y)] = 39269099
    worksheet["I" + str(y)] = 1
    worksheet["J" + str(y)] = "Carton"
    worksheet["K" + str(y)] = "None"


    if df.iat[i, 1] in DG_list:
        worksheet["L" + str(y)] = "Liquid"
    else:
        worksheet["L" + str(y)] = "Powder"



    worksheet["M" + str(y)] = 10
    worksheet["N" + str(y)] = 10
    worksheet["O" + str(y)] = 10
    worksheet["P" + str(y)] = 0.1
    worksheet["Q" + str(y)] = 0.1
    worksheet["R" + str(y)] = "FR"
    worksheet["S" + str(y)] = "DDU"
    worksheet["T" + str(y)] = "Export"
    worksheet["U" + str(y)] = "Ryan So"
    worksheet["V" + str(y)] = "Bitcontrol Limited"
    worksheet["W" + str(y)] = "RM B1,BLK 2, 9/F,GOLDEN DRAGON"
    worksheet["X" + str(y)] = "IND CTR, 162 TAI LIN PAI RD"
    worksheet["Y" + str(y)] = "KWAI CHUNG"
    worksheet["AB" + str(y)] = "HK"
    worksheet["AC" + str(y)] = "96516506"




    worksheet["AE" + str(y)] = df.iat[i, 0]
    worksheet["AL" + str(y)] = df.iat[i, 1]
    worksheet["AG" + str(y)] = df.iat[i, 2]
    worksheet["AH" + str(y)] = df.iat[i, 3]
    worksheet["AI" + str(y)] = df.iat[i, 4]
    worksheet["AJ" + str(y)] = df.iat[i, 5]
    worksheet["AK" + str(y)] = df.iat[i, 6]
    worksheet["AM" + str(y)] = df.iat[i, 7]

    row = row + 1
    x = x + 1

# for i in range(len(df)):
#          print(df.loc[i, :])
# worksheet['B13'] = 'hello world'
# worksheet['C13'] = 'Ryan'

workbook.save('export1.xlsx')
# Some data we want to write to the worksheet.
scores = (
    ['ankit', 1000],
    ['rahul',   100],
    ['priya',  300],
    ['harshita',    50],
)

# Start from the first cell. Rows and
# columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
# for name, score in (scores):
#     worksheet.write(row, col, name)
#     worksheet.write(row, col + 1, score)
#     row += 1
#
# workbook.close()




#
# with open('export.csv', 'a+', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     for i in range(len(df)):
# for i in range (0,len(a[0][2])):
#     print(a[0][2][i])