from captchaoops import *

apikey = open("/home/#checkhere/2captchakey.txt","r").read()
apikey = apikey.rstrip()
brow1 = captcha(apikey)

brow2 = captcha(apikey)

brow1.selenium()

brow2.selenium()
