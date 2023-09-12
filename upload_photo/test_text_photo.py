from PIL import Image, ImageDraw, ImageFont

width = 1024
height = 1024
message = "Hello boss!"

message='''商品編號
6913
商品特色
前調：大吉嶺茶葉、薰衣草、橘子、香檸檬、橙子花
中調：康乃馨、鳶尾、胡椒、癒創木、巴西花梨木
基調：琥珀、麝香、橡苔、雪松
商品編號:102123802001
商品重點
BVLGARI首支中性香水，簡單瓶身線條與清透顏色，配上香水清新中帶有辛辣木質香調，賦予男士親和、沈穩、紳士氣質！'''


font = ImageFont.truetype("/Users/apple/Library/Fonts/PangMenZhengDaoCuShuTi-2.ttf", size=30)

img = Image.new('RGB', (width, height), color='white')

imgDraw = ImageDraw.Draw(img)

textWidth, textHeight = imgDraw.textsize(message, font=font)
xText = (width - textWidth) / 2
yText = (height - textHeight) / 2

imgDraw.text((10, 10), message, font=font, fill=(0, 0, 0))

img.save('result.png')