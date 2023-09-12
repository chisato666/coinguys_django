import pywhatkit

import pyautogui as p
import pyperclip as y
import time

text_cap='''商品編號
6913222
商品特色
前調：大吉嶺茶葉、薰衣草、橘子、香檸檬、橙子花
中調：康乃馨、鳶尾、胡椒、癒創木、巴西花梨木
基調：琥珀、麝香、橡苔、雪松
商品編號:102123802001
商品重點
BVLGARI首支中性香水，簡單瓶身線條與清透顏色，配上香水清新中帶有辛辣木質香調，賦予男士親和、沈穩、紳士氣質！'''


img='/Users/apple/perfumeHK/6913.jpeg'
pywhatkit.sendwhatmsg_to_group_instantly("LlhnVvkq8Ze7eGHV7qXUvB", "Hey All!")
y.copy(text_cap)
p.hotkey('command','v')
time.sleep(2)

pywhatkit.sendwhats_image('LlhnVvkq8Ze7eGHV7qXUvB',img)


#p.press("enter")