import time
import my_functions
import csv
#import googletrans
import numpy as np

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

#translator = googletrans.Translator()

ser = Service('/usr/local/bin/chromedriver')
# op = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=ser)

chromedriver ='/usr/local/bin/chromedriver'
#driver = webdriver.Chrome(chromedriver)

opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:9222")

# url = driver.command_executor._url       #"http://127.0.0.1:60622/hub"
# session_id = driver.session_id            #'4e167f26-dc1d-4f51-a207-f761eaf73c31'


driver = webdriver.Chrome(service=ser,options=opt)
#driver = webdriver.Chrome(service=ser)


#driver = webdriver.Chrome(chromedriver)

#driver.close()   # this prevents the dummy browser
driver.get("https://www.carousell.com.hk/sell/")

driver.implicitly_wait(2)
#driver.maximize_window()

#to identify element

#login click

#<a class="D_rr D_rp D_mn" href="/login" rel="noopener noreferrer"><p class="D_ln D_iI D_lo D_lr D_lt D_lx D_l_ D_lk">Login</p></a>

#element = driver.find_element(By.LINK_TEXT,"login")

#img_path='/Users/apple/Downloads/'

def login(login_name,login_pw):

    try:

        s = driver.find_element(By.XPATH, '// *[ @ id = "root"] / div / header / div / div / div / div[2] / a[2]').click()
        button = driver.find_element(By.XPATH, "//button[contains(text(),\'Email')]")
        if button:
            print("email button found")
            button.click()
        else:
            print("email button not found")

        #s = driver.find_element(By.XPATH,'// *[ @ id = "ReactModalPortal-LOGIN"] / div / div / div / div / div[2] / button[2]').click()

        #s = driver.find_element(By.CSS_SELECTOR, 'a[class="D_rr D_rp D_mn"][href="/login"]').click()
        time.sleep(2)
        #s = driver.find_element(By.XPATH, '// *[ @ id = "ReactModalPortal-LOGIN"] / div / div / div / div / form / div[1] / div / div / input').send_keys(login_name)
        #s = driver.find_element(By.XPATH, '// *[ @ id = "ReactModalPortal-LOGIN"] / div / div / div / div / form / div[2] / div / div / input').send_keys(login_pw)
        driver.find_element(by=By.NAME, value='username').send_keys(login_name)
        driver.find_element(by=By.NAME, value='password').send_keys(login_pw)
        button = driver.find_element(By.XPATH, "//button[contains(text(),\'Log in')]")
        if button:
            print("Login button found")
            button.click()
        else:
            print("Login button not found")

       # s = driver.find_element(By.XPATH, '//*[@id="ReactModalPortal-LOGIN"]/div/div/div/div/form/button').click()
        print('login')
        time.sleep(2)
    except:
        print('No login')

def input_form(title,tag,price,body,img_list,cala):
    try:
        s=driver.find_element(By.XPATH, "//input[@type='file']")
        if s:
            print("file " + img_list)
            s.send_keys(img_list)

        else:
            print("no file 2")

    except:
        print('file not found')


    # Select the Calagouse
    s=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[2]/div[2]/div/div').click()
    print("select calagouse \n")
    time.sleep(1)

    s=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/input').send_keys(cala)
    print("find calagouse \n")

    time.sleep(1)

    print("click calagouse \n")

    s=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/p').click()


    time.sleep(1)

    # Enter the title
    print("enter the title \n")

    #s=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[2]/div[2]/div[2]/form/section/div[1]/div/div/div/div/input')
    s=driver.find_element(by=By.NAME, value='field_title')

    if s:
        s.send_keys(title)

    time.sleep(2)
   # Chromedriver.find_element_by_xpath("/html/body/header/div/nav[1]/div/ul/li[2]/a[contains(text(),\'About Us')]").click() “ // a[contains(text(),’Table''
    button = driver.find_element(By.XPATH,"//span[contains(text(),\'Like new')]")
    if button:
        print("button found")
        button.click()
    else:
        print("button not found")

    #s=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[2]/div[2]/div[2]/form/section/div[4]/div[2]/div/div[1]/button[2]/span').click()

    print("click type of perfume option \n")

    time.sleep(1)
    # Enter Price

   # s=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[2]/div[2]/div[2]/form/section/div[4]/div[4]/div[1]/div/div/input').send_keys(price)
    s=driver.find_element(by=By.NAME, value='field_price').send_keys(price)
    time.sleep(1)
    print("enter price \n")


    text_area=body
    s=driver.find_element(by=By.NAME, value='field_description').send_keys(text_area)
    print("enter text_area \n")

    # Select the type of perfume

    #If this is perfume
    if (cala=="fra"):
        button = driver.find_element(By.XPATH,"//span[contains(text(),\'Perfume')]")
        if button:
            print("Perfume button found")
            button.click()
        else:
            print("Perfume button not found")

        s=driver.find_element(by=By.NAME, value='field_brand').send_keys(tag)

        time.sleep(1)
    #Select the delivered click box

    button =driver.find_element(by=By.NAME, value='field_mailing')

    if button:
        print("Mailing button found")
        driver.execute_script("arguments[0].click();", button)

       # button.click()
    else:
        print("Mailing button not found")
    time.sleep(1)


    # Click the submit

    #s=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[2]/div[2]/div[2]/form/div/button').click()

    button = driver.find_element(By.XPATH, "//button[contains(text(),\'List now')]")
    if button:
        print("List button found")
        button.click()
    else:
        print("List button not found")

    time.sleep(8)

    # Relist and click the inbox link first

 #   button = driver.find_element(By.XPATH, "//a[contains(text(),\'inbox')]")
  #  button = driver.find_element(By.XPATH, "//a[contains(@href,'inbox')]")
  #   button = driver.find_element(By.XPATH, '// *[ @ id = "root"] / div / header / div / div / div / div[2] / div / a / span')
  #
  #   if button:
  #       print("inbox button found")
  #       button.click()
  #   else:
  #       print("inbox button not found")
  #
  #   time.sleep(2)

    # Click the Sell button
  #  s=driver.find_element(By.XPATH,'//*[@id="root"]/div/header/div/div/div/div[2]/div/a').click()
  #  button = driver.find_element(By.XPATH, "//a[contains(text(),\'sell')]")try:
    #     user_name = driver.find_element_by_name("userNam")
    #     user_name.send_keys("mercury")
    # except NoSuchElementException:
    #     print("exception handled")

    try:
        button = driver.find_element(By.XPATH, "//a[contains(@href,'sell')]")

        if button:
            print("sell button found")
            button.click()
        else:
            print("sell button not found")
    except NoSuchElementException:
        print("exception handled")



    time.sleep(2)


#login('cfhh28','116116rm')

#login('trendyground','socool666')


#img_link='https://971e-210-6-94-85.ap.ngrok.io/photo/12SEP22-2/IMG_'

excel_file='/Users/apple/Documents/Documents/Etsy/180723-2.csv'
img_link='/Applications/XAMPP/xamppfiles/htdocs/photo/180723/IMG_'
photo_ext='.JPG'
currency=6
msg=""
cala="fra"

my_functions.init()
a=my_functions.load_data(excel_file,img_link,photo_ext,currency)



for i in range (0,len(a)):
    #print(a[i])
    msg =a[i][my_functions.msg] + "\n\n"
         #+ a[i][my_functions.body]+ "\n"
    #print(msg)
    img=a[i][my_functions.image]
    tags = a[i][my_functions.tags]
    title = a[i][my_functions.title]
    set_chinese= False
    #Change price USD to HKD
    price = (a[i][my_functions.price])

    #c = x.astype(np.int) * 6
    # print("PRICE !!! =" )
    # result = [int(item) * 5 for item in x]

    # price=result
    # print(*price,sep=",")


    img_list=[]
    total=0

    #Translator the message to chinese format
    if set_chinese:
        title=translator.translate(title, dest='zh-tw').text
    #msg=translator.translate(msg, dest='zh-tw').text
    #option_ls=translator.translate(option_ls, dest='zh-tw').text

    print("LEN" + str(len(img)) )

    for x in range(0, len(img)):
        #print(img[x])
        #s.send_keys("/Users/apple/Downloads/IMG_7303.JPG \n" + "/Users/apple/Downloads/IMG_7304.JPG")

        if x == 0:
            img_list=img[x]
        else:
            img_list=img_list + " \n" + img[x]

        photo_found = True

    max_len = 0

    #print("OV IMG LIST " + img_list)
    #print(*img_list,sep=',')
    # print(*a[i][my_functions.option_value],sep=",")
    # print(len(a[i][my_functions.option_value]))
    #
    # if len(a[i][my_functions.option_value]) >1 :
    #     option_ls = a[i][my_functions.option_value]
    #
    #     if (len(price) >= len(option_ls)):
    #         max_len = len(option_ls)
    #     else:
    #         max_len = len(price)
    #
    #     for x in range(0, max_len):
    #         total=total + int(price[x])
    #
    #         if set_chinese:
    #             option_ls[x] = translator.translate(option_ls[x], dest='zh-tw').text
    #
    #         msg=msg + "\n\n $" + str(price[x]) + " -- " + option_ls[x]

    # for x in range(0, len(option_ls)):
    #     print(option_ls[x])
    #
    #     print(img_list)

    #price=total
    tags = tags.split(",")

    input_form(title, tags[0], int(price[0]), msg, img_list,cala)




