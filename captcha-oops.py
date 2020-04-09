class captcha:
 def __init__(self,apikey):
        self.API_KEY = apikey
        self.sitekey = "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-"




 def captcha(self):

    import requests
    from time import sleep

    # Add these values
    self.url = "https://www.google.com/recaptcha/api2/demo"  # example url

    self.s = requests.Session()

    # here we post site key to 2captcha to get captcha ID (and we parse it here too)
    self.captcha_id = self.s.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(
        self.API_KEY, self.sitekey, self.url)).text.split('|')[1]
    # then we parse gresponse from 2captcha response
    print(f"captcha id is {self.captcha_id}")
    self.recaptcha_answer = self.s.get(
        "http://2captcha.com/res.php?key={}&action=get&id={}".format(self.API_KEY, self.captcha_id)).text
    print("solving ref captcha...")
    while 'CAPCHA_NOT_READY' in self.recaptcha_answer:
        sleep(5)
        self.recaptcha_answer = self.s.get(
            "http://2captcha.com/res.php?key={}&action=get&id={}".format(self.API_KEY, self.captcha_id)).text

    self.recaptcha_answer = self.recaptcha_answer.split('|')[1]
    return self.recaptcha_answer


 def selenium(self):
     from selenium import webdriver
     from selenium.webdriver.common.keys import Keys

     # opening firefox and navigating
     self.driver = webdriver.Chrome()
     self.driver.get("https://www.google.com/recaptcha/api2/demo")

     # getting the recapthca responce
     print("recaptcha starting")
     self.result = self.captcha()
     print("solving done")
     print(self.result)

     # entering the response long way. doesnt work in chrome
     # driver.execute_script("document.getElementById('g-recaptcha-response').setAttribute('style', 'width: 250px; height: "
     #                      "40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none;');")
     # response_box = driver.find_element_by_id('g-recaptcha-response')
     # response_box.send_keys(result)

     # entering responce short way with js element and working both firefox and chrome
     self.driver.execute_script("document.getElementById('g-recaptcha-response').innerHTML=arguments[0];", self.result)
     submit_button = self.driver.find_element_by_id('recaptcha-demo-submit').click()
