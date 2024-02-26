import time
import csv
#import googletrans
import numpy as np
import my_functions

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support import expected_conditions as EC
#translator = googletrans.Translator()


def load_vv_photo(img_list,photo_num):

    if (photo_num==1):
        s = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/form/div[2]/div/div[2]/div[1]/fieldset[1]/div/div[2]/div[1]/div/input')
        print("file 1 " + img_list)
        s.send_keys(img_list)
    elif (photo_num == 2):
        s = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/form/div[2]/div/div[2]/div[1]/fieldset[1]/div/div[4]/div[1]/div/input')
        print("file 2 " + img_list)
        s.send_keys(img_list)
    elif (photo_num == 3):
        s = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/form/div[2]/div/div[2]/div[1]/fieldset[1]/div/div[6]/div[1]/div/input')
        print("file 3 " + img_list)
        s.send_keys(img_list)
    elif (photo_num == 4):
        s = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/form/div[2]/div/div[2]/div[1]/fieldset[1]/div/div[8]/div[1]/div/input')
        print("file 4 " + img_list)
        s.send_keys(img_list)
    elif (photo_num == 5):
        xpath = '/html/body/div[1]/div[3]/div/form/div[2]/div/div[2]/div[1]/fieldset[1]/div/div[2]/div[1]/div/input'
        s = driver.find_element(By.XPATH,'/ html / body / div[1] / div[3] / div / form / div[2] / div / div[2] / div[1] / fieldset[2] / h2')
        s.click()
        time.sleep(1)
        s = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/form/div[2]/div/div[2]/div[1]/fieldset[2]/div/div/div/div/input')
        print("file 5 " + img_list)
        s.send_keys(img_list)
        time.sleep(7)
    elif (photo_num == 6):
        s = driver.find_element(By.XPATH,'/ html / body / div[1] / div[3] / div / form / div[2] / div / div[2] / div[1] / fieldset[2] / div / div / div[2] / div / input')
        print("file 6 " + img_list)
        s.send_keys(img_list)
        time.sleep(4)

    elif (photo_num == 7):
        print("file 7 " + img_list)

        s = driver.find_element(By.XPATH,'/ html / body / div[1] / div[3] / div / form / div[2] / div / div[2] / div[1] / fieldset[2] / div / div / div[3] / div / input')
        if (s):
            print('Photo 7 loading')
            s.send_keys(img_list)
            time.sleep(4)
        else:
            print('Photo 7 not found')

    elif (photo_num == 8):
        s = driver.find_element(By.XPATH,'/ html / body / div[1] / div[3] / div / form / div[2] / div / div[2] / div[1] / fieldset[2] / div / div / div[4] / div / input')
        print("file 8 " + img_list)
        s.send_keys(img_list)
        time.sleep(4)

    elif (photo_num == 9):
        s = driver.find_element(By.XPATH,'/ html / body / div[1] / div[3] / div / form / div[2] / div / div[2] / div[1] / fieldset[2] / div / div / div[5] / div / input')
        print("file 9 " + img_list)
        s.send_keys(img_list)
        time.sleep(4)

    elif (photo_num == 10):
        s = driver.find_element(By.XPATH,'/ html / body / div[1] / div[3] / div / form / div[2] / div / div[2] / div[1] / fieldset[2] / div / div / div[6] / div / input')
        print("file 10 " + img_list)
        s.send_keys(img_list)
        time.sleep(4)

    time.sleep(2)


ser = Service('/usr/local/bin/chromedriver')
# op = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=ser)

chromedriver ='/usr/local/bin/chromedriver'
#driver = webdriver.Chrome(chromedriver)
csv_file_path='/Applications/XAMPP/xamppfiles/htdocs/photo/210224/210224.csv'
img_link = '/Applications/XAMPP/xamppfiles/htdocs/photo/210224/210224/new/210224/IMG_'
photo_ext = '.JPG'

opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:9222")

# url = driver.command_executor._url       #"http://127.0.0.1:60622/hub"
# session_id = driver.session_id            #'4e167f26-dc1d-4f51-a207-f761eaf73c31'


driver = webdriver.Chrome(service=ser,options=opt)

driver.get('https://www.vestiairecollective.com/')
# Perform necessary actions to log in to your account
# ...

# Go to the product listing page
driver.get('https://www.vestiairecollective.com/sell-clothes-online/')

# Read the CSV file

exchange_rate=7.5

with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row

    for index, row in enumerate(reader, start=1):
        # Extract data from CSV row
        title = row[0]
        tags = row[1].split(',')

        brand_name = tags[0]
        cat = tags[1]
        sex = tags[2]
        size = tags[3]

        if (len(tags)>4):
            size2 = tags[4]



        price = float(row[2]) * exchange_rate
        image = row[4]
        desc = row[5]

        # Fill in the price
        # price_input = driver.find_element_by_xpath('//*[@id="product_price"]')
        # price_input.clear()
        # price_input.send_keys(price)

        # Select the radio button for womenswear

        # womenswear_radio = driver.find_element_by_xpath('//*[@id="Womenswear-0"]')
        # womenswear_radio.click()

        time.sleep(3)

        # # Select the category watches

        print(cat)

        if (sex=='men'):
            print('Enter Men')
            s = driver.find_element(By.XPATH, '//*[@id="vc-preduct-add-form"]/fieldset[1]/ul/li[2]/label').click()
            condition_xpath='// *[ @ id = "react-information-section"] / div / div[1] / ul / li[1] / span'
            category_xpath='// *[ @ id = "preductAddCategory"] / optgroup[4] / option[7]'

        else:
            print('Enter Women')
            s = driver.find_element(By.XPATH, '//*[@id="preductAddCategory"]/optgroup[4]/option[8]').click()
            #condition_xpath='// *[ @ id = "react-information-section"] / div / div[1] / ul / li[2] / ul / li[4] / span[1]'
            #condition_xpath='/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[1] / ul / li[2] / ul / li[4] / span[1]'
            condition_xpath='// *[ @ id = "react-information-section"] / div / div[1] / ul / li[1]'
            category_xpath='// *[ @ id = "preductAddCategory"] / optgroup[4] / option[8]'


        if (cat=='watch'):
            #category_select = driver.find_element(By.XPATH, '/ html / body / div[1] / div / main / div / section[2] / form / fieldset[2] / div / select / optgroup[4] / \option[7]')
            category_select = driver.find_element(By.XPATH, category_xpath)
            if category_select:
                print('Category found ' + cat)
                category_select.click()




        elif (cat=='wallet'):
            category_select = driver.find_element(By.XPATH, '/ html / body / div[1] / div / main / div / section[2] / form / fieldset[2] / div / select / optgroup[4] /option[2]')
            if category_select:
                print('Category found ' + cat)
                category_select.click()

        elif (cat=='necklace'):
            category_select = driver.find_element(By.XPATH, '/ html / body / div[1] / div / main / div / section[2] / form / fieldset[2] / div / select / optgroup[5] /option[4]')
            if category_select:
                print('Category found ' + cat)
                category_select.click()


        # Fill in the brand name
        brand_input = driver.find_element(By.XPATH, '//*[@id="depositForm__form__brands-input"]')


        try:
            if brand_input:
                print('brand name found ')
                driver.execute_script("arguments[0].click();", brand_input)

                #brand_input.click()
                time.sleep(2)
                print('Enter brand name  ')

                brand_input.send_keys(brand_name)

                time.sleep(5)

                #brand_input = driver.find_element(By.XPATH,'// *[ @ id = "vc-preduct-add-form"] / fieldset[3] / label')

                driver.get("//html")

                print('Label found')
                brand_input = driver.find_element(By.XPATH, "//body")

                brand_input.click()
                time.sleep(2)


        except Exception as error:
            print('brand name not found ', error)


        try:





            # Wait for the blank area to be clickable
            blank_area = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))
            # Click on the blank area
            blank_area.click()
            print('click blank area')

            time.sleep(2)


        except Exception as error:

            print('Cannot click outside', error)



        try:
            # Click the continue button
            continue_button = driver.find_element(By.XPATH,'//*[@id="vc-preduct-add-submit"]')
            continue_button = driver.find_element(By.ID,'vc-preduct-add-submit')

            driver.execute_script("arguments[0].click();", continue_button)
            time.sleep(4)


        except:
            print('Continue button not found 1')
        # time.sleep(2)
        # if (continue_button):
        #     print('Continue button found')
        #
        #     try:
        #         continue_button.click()
        #         print('Continue button Click!!!!')
        #
        #         time.sleep(4)
        #     except Exception as error:
        #         # handle the exception
        #         print("An exception Continue occurred:", error)
        # else:
        #     print('Continue button not found')


        #condition_xpath='/ html / body / div[1] / div / main / div / section[2] / form / div / button'
        #condition_xpath='// *[ @ id = "vc-preduct-add-submit"]'
        s = driver.find_element(By.XPATH, "//body")

        s.click()
        time.sleep(2)

        try:
            condition_button = driver.find_element(By.XPATH, condition_xpath)
            if condition_button:
                print('condition found')
                condition_button.click()
                time.sleep(1)

                condition_button = (driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/div[2]/div/div[1]/div[1]/div/div[1]/ul/li[2]/ul/li[3]/span[1]'))
                condition_button.click()
                time.sleep(2)
            else:
                print('condition not found')
        except:
            print('Continue button not found 2')
            exit


        if (cat=='watch'):

            with_model=True

            try:
                print('1 model  found')

                model_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/form/div[2]/div/div[1]/div[1]/div/div[2]/button/span')
                if model_button:
                    model_button.click()
                    time.sleep(2)
            except Exception as error:
                # handle the exception
                print('1 model not found')
                with_model = False


            if with_model:  # With Model Watch



                try:
                    s = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div/footer/button')
                    print('with model Watch case material found')
                    s.click()
                    time.sleep(2)
                except Exception as error:
                    print('with model Watch case material not found ', error)

                s = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/div[2]/div/div[1]/div[1]/div/div[3]/div[1]/input')

                if (s):
                    print('with model Bracelet found')
                    try:
                        s.click()
                        time.sleep(2)
                    except Exception as error:
                        # handle the exception
                        print("with model An bracelet exception occurred: ", error)


                else:
                    print('with model Bracelet not found')




                try:

                    # Assuming the select box has an id of 'select_box'

                    #select_box = driver.find_element(By.ID, 'material')


                    # Find the <li> element with the label 'Other' and a specific attribute value using XPath
                    other_element = driver.find_element(By.XPATH,"//li[text()='Other' and @data-component-id='material']")

                    # Click the specific 'Other' element
                    other_element.click()

                    print('Other yes')
                except Exception as error:
                    print('Other cannot find', error)
                #/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[3] / div[1] / div[2] / ul / li[14]

                #/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[3] / div[1] / div[2] / ul / li[13]

                try:
                    mechanism_xpath='/html/body/div[1]/div[3]/div/form/div[2]/div/div[1]/div[1]/div/div[3]/div[1]/div[2]/ul/li[14]'
                    #mechanism_xpath='/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[3] / div[1] / div[2] / ul / li[13]'
                    s = driver.find_element(By.XPATH, mechanism_xpath)
                    if (s):
                        print('with model Mechanism found')
                        s.click()
                        time.sleep(2)
                    else:
                        print('with model Mechanism not found')
                except:
                    print('Except Mechanism not found')

                try:
                    s = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/div[2]/div/div[1]/div[1]/div/div[4]/div[1]/input')

                    if (s):
                        print('with model Color found')
                        s.click()
                        time.sleep(1)
                    else:
                        print('with model Color not found')
                except:
                    print('Color Xpath not found')

                try:
                    s = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/div[2]/div/div[1]/div[1]/div/div[4]/div[1]/div[2]/ul/li[17]')
                    s.click()
                    time.sleep(1)
                except:
                    print('watch case not click')


                try:
                    s = driver.find_element(By.XPATH,'/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[5] / div[1] / input')
                    s.click()
                    time.sleep(1)
                except:
                    print('bracelet not click')


                try:

                    s = driver.find_element(By.XPATH,'/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[5] / div[1] / div[2] / ul / li[2]')
                    s.click()
                    time.sleep(1)

                    s = driver.find_element(By.XPATH,'/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[6] / div[1] / input')
                    s.click()
                    time.sleep(1)

                    s = driver.find_element(By.XPATH,'/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[6] / div[1] / div[2] / ul / li[24]')
                    s.click()
                    time.sleep(1)

                    s = driver.find_element(By.XPATH,'/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[2] / button[2]')
                    s.click()
                    time.sleep(1)
                except:
                    print('Click not found')

            else:

                try:

                    #s = driver.find_element(By.XPATH, '// *[ @ id = "react-information-section"] / div / div[2] / div[1] / div[2] / ul / li[13]')
                    #a = driver.find_element(By.XPATH, '/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[2] / div[1] /div[2] / ul / li[13]')


                    button = driver.find_element(By.XPATH, '/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[2] / div[1] /div[2] / ul / li[14]')


                    time.sleep(3)
                    driver.execute_script("arguments[0].click();", button)
                    s = driver.find_element(By.XPATH, "//body")
                    time.sleep(2)

                    s.click()
                    time.sleep(2)

                    button = driver.find_element(By.ID, 'material')


                    if button:
                        print('without model Watch case material found', button)
                        button.click()
                        time.sleep(2)
                    else:
                        print('without model Watch case material not found 1')

                except Exception as error:
                    print('without model Watch case material not found 2 ', error)


                    try:

                        button = driver.find_element(By.XPATH, '/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[2] / div[1] / div[2] / ul / li[13]')
                        time.sleep(3)
                        driver.execute_script("arguments[0].click();", button)
                        s = driver.find_element(By.XPATH, "//body")
                        s.click()

                        time.sleep(2)
                    except:
                        print('material not found')

                    try:

                        button = driver.find_element(By.XPATH, '/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[2] / div[1] / input')
                        time.sleep(3)
                        driver.execute_script("arguments[0].click();", button)
                        s = driver.find_element(By.XPATH, "//body")
                        s.click()

                        time.sleep(2)
                    except:
                        print('material not found')

                try:
                    button = driver.find_element(By.ID, 'material')

                    if button:
                        button.click()
                        print('without model Watch case material found and click', button)

                        time.sleep(2)
                    else:
                        print('without model Watch case material not found 1')
                except:
                    print('Material not found 4')

                try:

                    d = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/div[2]/div/div[1]/div[1]/div/div[3]/div[1]/div[2]/ul/li[17]')

                    driver.execute_script("arguments[0].click();", d)

                    s = driver.find_element(By.XPATH, "//body")
                    time.sleep(2)

                    s.click()
                    time.sleep(2)


                    d = driver.find_element(By.ID, 'material_watch_strap')



                    if d:
                        print('without model Bracelet found')
                        d.click()
                        time.sleep(2)
                        s = driver.find_element(By.XPATH, "//body")
                        time.sleep(2)

                        s.click()
                    else:
                        print('without model Bracelet not found 1')

                except Exception as error:
                    print('without model Bracelet not found 2 ' , error)

                try:



                    s = driver.find_element(By.XPATH, '/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[4] / div[1] / div[2] / ul / li[2]')
                    time.sleep(2)

                    #s.click()
                    driver.execute_script("arguments[0].click();", s)
                    print('without model Mechanism found')

                    s = driver.find_element(By.ID, 'watch_mechanism')

                    #s = driver.find_element(By.XPATH, '/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[4] / div[1] / input')

                    s.click()

                    time.sleep(2)
                    s = driver.find_element(By.XPATH, "//body")
                    time.sleep(2)

                    s.click()
                    time.sleep(2)
                except Exception as error:
                    print('without model Mechanism not found ' , error)


                try:

                    s = driver.find_element(By.XPATH, '/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[5] / div[1] / div[2] / ul / li[24]')
                    print('without model color found')
                    time.sleep(2)

                    driver.execute_script("arguments[0].click();", s)

                    s = driver.find_element(By.ID, 'color')


                    s.click()
                    s = driver.find_element(By.XPATH, "//body")
                    time.sleep(2)

                    s.click()
                    time.sleep(2)

                except Exception as error:
                    print('without model color not found ' , error)


                try:
                    s = driver.find_element(By.XPATH, "//body")
                    time.sleep(2)

                    s.click()
                    time.sleep(2)

                    s = driver.find_element(By.XPATH, '        / html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[2] / button[2]')
                    print('Continue button here')
                    time.sleep(2)

                    driver.execute_script("arguments[0].click();", s)

                    #s.click()
                    time.sleep(2)
                except Exception as error:
                    print('Continue button not find ' , error)

        elif (cat=='necklace'):
            try:
                model_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/form/div[2]/div/div[1]/div[1]/div/div[2]/button/span')
                if model_button:
                    model_button.click()
                    time.sleep(2)
            except Exception as error:
                # handle the exception
                print('1 necklace model not found')
                with_model = False
            try:

                s = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/footer/button')
                print('with model  necklace found')
                s.click()
                time.sleep(2)
            except Exception as error:
                print('with model not necklace found ', error)

            try:


                s = driver.find_element(By.XPATH, '/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[3] / div[1] / div[2] / ul / li[21]')
                driver.execute_script("arguments[0].click();", s)
                time.sleep(2)

                button = driver.find_element(By.ID, 'material')

                if button:
                    print('without  case material found', button)
                    button.click()
                    time.sleep(2)
                else:
                    print('without  case material not found 1')

                print('with model case material necklace found')
                s.click()
                time.sleep(2)
            except Exception as error:
                print('with model case material necklace not found ', error)

            try:


                s = driver.find_element(By.XPATH, '/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[4] / div[1] / div[2] / ul / li[24]')
                driver.execute_script("arguments[0].click();", s)
                time.sleep(2)

                button = driver.find_element(By.ID, 'color')

                if button:
                    print('color  found', button)
                    button.click()
                    time.sleep(2)
                else:
                    print('without color')

                print('with model color necklace found')
                s.click()
                time.sleep(2)
            except Exception as error:
                print('with model color not necklace found ', error)

            try:
                s = driver.find_element(By.XPATH, "//body")
                time.sleep(2)

                s.click()
                time.sleep(2)

                s = driver.find_element(By.XPATH, '/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[2] / button[2]')
                print('Continue button here')
                time.sleep(2)

                driver.execute_script("arguments[0].click();", s)

                #s.click()
                time.sleep(2)
            except Exception as error:
                print('Continue button not find ' , error)

        elif (cat=='wallet'):
            try:
                model_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/form/div[2]/div/div[1]/div[1]/div/div[2]/button/span')
                if model_button:
                    model_button.click()
                    time.sleep(2)
            except Exception as error:
                # handle the exception
                print('1 wallet model not found')
                with_model = False
            try:

                s = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/footer/button')
                print('with model  wallet found')
                s.click()
                time.sleep(2)
            except Exception as error:
                print('with model not wallet found ', error)

            try:

                s = driver.find_element(By.XPATH, '/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[3] / div[1] /div[2] / ul / li[24]')
                driver.execute_script("arguments[0].click();", s)
                time.sleep(2)

                button = driver.find_element(By.ID, 'material')

                if button:
                    print('with wallet material found', button)
                    button.click()
                    time.sleep(2)
                else:
                    print('with wallet case material not found 1')

                print('with model case material wallet found')
                s.click()
                time.sleep(2)
            except Exception as error:
                print('with model case material wallet not found ', error)

            try:


                s = driver.find_element(By.XPATH, '/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[1] / div / div[4] / div[1] / div[2] / ul / li[24]')
                driver.execute_script("arguments[0].click();", s)
                time.sleep(2)

                button = driver.find_element(By.ID, 'color')

                if button:
                    print('color  found', button)
                    button.click()
                    time.sleep(2)
                else:
                    print('without color')

                print('with model color wallet found')
                s.click()
                time.sleep(2)
            except Exception as error:
                print('with model color not wallet found ', error)


            try:


                s = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/div[2]/div/div[1]/div[1]/div/div[5]/div[1]/div[2]/ul/li[13]')
                driver.execute_script("arguments[0].click();", s)
                time.sleep(2)



                button = driver.find_element(By.ID, 'pattern')

                if button:
                    print('Pattern  found', button)
                    button.click()
                    time.sleep(2)
                else:
                    print('without pattern')

                print('with pattern wallet found')
                s.click()
                time.sleep(2)
            except Exception as error:
                print('with model pattern not wallet found ', error)





            try:
                s = driver.find_element(By.XPATH, "//body")
                time.sleep(2)

                s.click()
                time.sleep(2)

                s = driver.find_element(By.XPATH, '/ html / body / div[1] / div[3] / div / form / div[2] / div / div[1] / div[2] / button[2]')
                print('Continue button here')
                time.sleep(2)

                driver.execute_script("arguments[0].click();", s)

                #s.click()
                time.sleep(2)
            except Exception as error:
                print('Continue button not find ' , error)



        # Go to step 2 Upload photo
        photo_count=10

        ls = image.split(';')
        print('ls ',ls)

        ls3 = my_functions.load_photo(ls, img_link, photo_ext)
        print('ls3 ',ls3)
        # loading photo


        for i in range(len(ls3)):
            try:
                print("The list at index", i, "contains a", ls3[i])
                load_vv_photo(ls3[i], i+1)
            except:
                print('no photo')



        # Click the continue button
        s = driver.find_element(By.XPATH,'/ html / body / div[1] / div[3] / div / form / div[2] / div / div[2] / div[2] / button[2]')
        s.click()
        time.sleep(3)

        # Step 3 Enter Description
        s = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/form/div[2]/div/div[3]/div[1]/fieldset[1]/div[1]/div')
        s.click()
        time.sleep(2)


        s.send_keys(desc)
        time.sleep(2)

        #  Enter Size
        try:

            if cat=='necklace':
               x_path= '/ html / body / div[1] / div[3] / div / form / div[2] / div / div[3] / div[1] / fieldset[2] / div / div[2] / div / div / span / input'
               s = driver.find_element(By.XPATH,x_path)
               s.click()
               s.send_keys(size)
               time.sleep(2)
            elif cat=='watch':
               x_path = '/html/body/div[1]/div[3]/div/form/div[2]/div/div[3]/div[1]/fieldset[2]/div[2]/div/div/span/input'
               s = driver.find_element(By.XPATH,x_path)
               s.click()
               s.send_keys(size)
               time.sleep(2)
            elif cat=='wallet':
               x_path = '/ html / body / div[1] / div[3] / div / form / div[2] / div / div[3] / div[1] / fieldset[2] / div[2] / div[1] / div / span / input'
               s = driver.find_element(By.XPATH,x_path)
               s.click()
               s.send_keys(size)
               time.sleep(2)
               x_path2='/ html / body / div[1] / div[3] / div / form / div[2] / div / div[3] / div[1] / fieldset[2] / div[2] / div[2] / div / span / input'
               s = driver.find_element(By.XPATH, x_path2)
               s.click()
               s.send_keys(size2)
               time.sleep(2)
        except:
            print('no size field')
        # Click the button
        s = driver.find_element(By.XPATH,'/ html / body / div[1] / div[3] / div / form / div[2] / div / div[3] / div[2] / button[2]')
        s.click()
        time.sleep(2)

        # Confirm the from address
        s = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/form/div[2]/div/div[4]/div/button[2]')
        s.click()
        time.sleep(2)


        # Enter the price
        s = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/form/div[2]/div/div[5]/div[1]/div/div/fieldset/div[2]/div[1]/input')

        s.click()
        time.sleep(1)
        print('Enter price ')
        s.clear()
        time.sleep(2)
        print(price)

        s.send_keys(int(price))
        time.sleep(2)
        s = driver.find_element(By.XPATH, "//body")

        s.click()
        time.sleep(2)

        try:
            s = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/div[2]/div/div[5]/div[2]/button[3]')
            time.sleep(2)
            s.click()

            #driver.execute_script("arguments[0].click();", s)

            print('Click Save after enter price')
            #s = driver.find_element(By.XPATH, '//*[@id="preductSection_price"]/div[2]/button[3]')
            #s = driver.find_element(By.XPATH,'//*[@id="preductSection_price"]/div[2]/button[3]')
            #s.click()
            time.sleep(6)
            print('Click Save after click')

        except Exception as error:
            # handle the exception
            print("An save exception occurred: ", error)




        # Terms of use
        try:
            # Find the <li> element with the label 'Other' and a specific attribute value using XPath


            # Find the <button> element with the class "bt medium black confirm" and the label "Yes" using XPath
            yes_button = driver.find_element_by_xpath("//button[@class='bt medium black confirm' and text()='Yes']")

            # Click the 'Yes' button
            yes_button.click()

            print('term 0 yes')
        except:
            print('term 0 not found')

        try:
            s = driver.find_element(By.XPATH,'/ html / body / div[6] / div / div / div / div / div / p[2] / button[2]').click
            print('term1  found')

        except:
            print('term1 not found')

        try:
            s = driver.find_element(By.XPATH,'/ html / body / div[7] / div / div / div / div / div / p[2] / button[2]').click
            print('term2  found')

        except:
            print('term1 not found')







        try:

            s = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/form/div[1]/div/label/span[1]/input')

            if (s):

                try:
                    s.click()
                    time.sleep(3)
                    print('term of used click')
                except:
                    print('term not found')

        except:
            print('term 2 started')

            s = driver.find_element(By.XPATH, '//*[@id="superbox-innerbox"]/div/div/p[2]/button[2]')
            if (s):

                try:
                    s.click()
                    time.sleep(10)
                    print('term of used 2 click')
                except:
                    print('term2  not found')

        # else:
        #     s = driver.find_element(By.XPATH, '//*[@id="superbox-innerbox"]/div/div/p[2]/button[2]')
        #     if (s):
        #         print('term of used 2 click')
        #         s.click()
        try:
            s = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/form/div[1]/div/button').click()
            print('Submit button found click')
            time.sleep(8)

        except:
            print('Submit button not found')


        try:
            s = driver.find_element(By.XPATH,'        / html / body / div[1] / div[3] / div / form / div[2] / div / div[5] / div[2] / button[2]').click()
            print('Submit button 2 found click')
            time.sleep(8)

        except:
            print('Submit button 2 not found')



        #s = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div[2]/a')
        try:
            s = driver.find_element(By.XPATH, '// *[ @ id = "main_v2"] / div / div[2] / a').click()
            time.sleep(8)
        except:
            print('Submit button 3 not found')

        driver.implicitly_wait(10)

# Close the browser
