import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


ser = Service('/usr/local/bin/chromedriver')
# op = webdriver.ChromeOptions()
# s = webdriver.Chrome(service=ser, options=op)

chromedriver ='/usr/local/bin/chromedriver'
#driver = webdriver.Chrome(chromedriver)

opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:9222")

# url = driver.command_executor._url       #"http://127.0.0.1:60622/hub"
# session_id = driver.session_id            #'4e167f26-dc1d-4f51-a207-f761eaf73c31'

driver = webdriver.Chrome(chromedriver)
#driver = webdriver.Chrome(service=ser,options=opt)

#driver.close()   # this prevents the dummy browser
driver.get("https://www.carousell.com.hk/sell/")

driver.implicitly_wait(2)
driver.maximize_window()

#to identify element

#login click
s = driver.find_element(By.XPATH,'/html/body/div[1]/div/header/div/div/div/div[2]/a[2]').click()


s = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/header/div/div[1]/div/div/div[2]/a[2]/p').click()
#cfhh28 116116Rm
driver.find_element_by_name('username').send_keys("bestjbid")
driver.find_element_by_name('password').send_keys("socool666")
s = driver.find_element(By.XPATH,'//*[@id="ReactModalPortal-LOGIN"]/div/div/div/div/form/button').click()

# #user name enter
s = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/form/div[1]/div/div/input').send_keys("bestjbid")
s = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/form/div[2]/div/div/input').send_keys("socool666")

s = driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div/div/form/button').click()



# #//*[@id="root"]/div/header/div[2]/div[2]/div/a/span
# s = driver.find_element(By.XPATH,'//*[@id="root"]/div/header/div[2]/div[2]/div/a/span').click()
# time.sleep(2)
#
# s = driver.find_element(By.XPATH,'//*[@id="root"]/div/header/div[2]/div[2]/div/a').click()
#/html/body/div[1]/div/main/div/div/div[2]/div/div/div/label/input

#//*[@id="main"]/div/div/div[2]/div/div/div/label/input

time.sleep(3)

s= driver.find_element_by_xpath("//input[@type='file']")
s.send_keys("/Users/apple/Downloads/IMG_7094.JPG ")


s = driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div/div/div/label/input')
s.send_keys("/Users/apple/Downloads/IMG_7094.JPG ")
#s.send_keys("/Users/apple/Downloads/IMG_7094.JPG \n" + "/Users/apple/Downloads/IMG_7093.JPG \n"+ "/Users/apple/Downloads/IMG_7092.JPG")


#s = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[89]/td[2]/span[78]/text()[1]').send_keys("/Users/apple/Downloads/IMG_7094.JPG \n" + "/Users/apple/Downloads/IMG_7093.JPG \n"+ "/Users/apple/Downloads/IMG_7092.JPG")
s = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div/div/div/label/input')
s.send_keys("/Users/apple/Downloads/IMG_7094.JPG ")
#s.send_keys("/Users/apple/Downloads/IMG_7094.JPG \n" + "/Users/apple/Downloads/IMG_7093.JPG \n"+ "/Users/apple/Downloads/IMG_7092.JPG")

print(s)

time.sleep(3)
#
#
# s = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div[2]/div/div[1]/p').click()
#
#
# s = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div[2]/div/div[2]/div[29]/div/span/span').click()
#
# s = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div[2]/div/div[2]/div[17]/div/span/span').click()

#Listing title
# time.sleep(3)
#
# s = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div[2]/div[2]/form/section/div[1]/div/div/div/div/input').send_keys("Chanel No.5 香水")
#
# s = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div[2]/div[2]/form/section/div[4]/div[3]/div[1]/div/div/input').send_keys("100")


#s = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div[1]/div/label/input')
#file path specified with send_keys

#
# s = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div/div/div/label/div[2]/button').click()
#
# s = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div[1]/div/label/input').click()
#
# s = driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div[2]/div/div/div/label/div[2]/button').click()
