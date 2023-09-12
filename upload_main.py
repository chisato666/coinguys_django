import time
import my_functions

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


ser = Service('/usr/local/bin/chromedriver')
# op = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=ser)

chromedriver ='/usr/local/bin/chromedriver'
#driver = webdriver.Chrome(chromedriver)

opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:9222")


#driver = webdriver.Chrome(service=ser,options=opt)
driver = webdriver.Chrome(service=ser)


#driver = webdriver.Chrome(chromedriver)

#driver.close()   # this prevents the dummy browser
driver.get("https://www.carousell.com.hk/sell/")

driver.implicitly_wait(2)
#driver.maximize_window()

#to identify element

#login click

img_link='/Users/apple/Downloads/'
photo_ext='.JPG'

def login(login_name,login_pw):

    try:
        s = driver.find_element(By.XPATH, '// *[ @ id = "root"] / div / header / div / div / div / div[2] / a[2]').click()
        #s = driver.find_element(By.CSS_SELECTOR, 'a[class="D_rr D_rp D_mn"][href="/login"]').click()
        time.sleep(2)
        s = driver.find_element(By.XPATH, '// *[ @ id = "ReactModalPortal-LOGIN"] / div / div / div / div / form / div[1] / div / div / input').send_keys(login_name)
        s = driver.find_element(By.XPATH, '// *[ @ id = "ReactModalPortal-LOGIN"] / div / div / div / div / form / div[2] / div / div / input').send_keys(login_pw)
        # driver.find_element(by=By.NAME, value='username').send_keys("bestjbid")
        # driver.find_element(by=By.NAME, value='password').send_keys("socool666")
        s = driver.find_element(By.XPATH, '//*[@id="ReactModalPortal-LOGIN"]/div/div/div/div/form/button').click()
        print('login')
        time.sleep(2)
    except:
        print('No login')

login('bestjbid','socool666')




try:
    s=driver.find_element(By.XPATH, "//input[@type='file']")
    if s:
        print("file")
        s.send_keys("/Users/apple/Downloads/IMG_7303.JPG \n" + "/Users/apple/Downloads/IMG_7304.JPG")
    else:
        print("no file 2")
except:
    print('file not found')


# Select the Calagouse
s=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[2]/div[2]/div/div').click()
#
time.sleep(1)

s=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/input').send_keys("fra")


s=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/p').click()
s=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[2]/div[2]/div[2]/form/section/div[1]/div/div/div/div/input')

if s:
    s.send_keys("Givenchy L'interdit EDT 50ml 1.7 oz 淡香水 ")

s=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[2]/div[2]/div[2]/form/section/div[4]/div[2]/div/div[1]/button[2]/span').click()

time.sleep(1)

s=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[2]/div[2]/div[2]/form/section/div[4]/div[4]/div[1]/div/div/input').send_keys("350")
time.sleep(1)


text_area="Givenchy L'interdit EDT 50ml 1.7 oz 淡香水 \n\n90% 滿 \n\n只限葵芳地鐵交收"
s=driver.find_element(by=By.NAME, value='field_description').send_keys(text_area)

# Select the type of perfume
s=driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div/div[2]/div[2]/div[2]/form/section/div[4]/div[6]/div/div/button[1]/span').click()

s=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[2]/div[2]/div[2]/form/section/div[4]/div[7]/div/div/div/input')
if s:
    s.send_keys("Givenchy")

time.sleep(1)
# Select the deliver method
s=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[2]/div[2]/div[2]/form/section/div[6]/div[4]/label/input').click()
time.sleep(1)

# Click the submit

s=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[2]/div[2]/div[2]/form/div/button').click()

time.sleep(2)

# Click the Sell button
s=driver.find_element(By.XPATH,'//*[@id="root"]/div/header/div/div/div/div[2]/div/a').click()




