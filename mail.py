from captcha import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# opening firefox and navigating
driver = webdriver.Chrome()
driver.get("https://www.google.com/recaptcha/api2/demo")


# getting the recapthca responce
print("recaptcha starting")
result = captcha()
print("solving done")
print(result)

# entering the response long way. doesnt work in chrome
#driver.execute_script("document.getElementById('g-recaptcha-response').setAttribute('style', 'width: 250px; height: "
#                      "40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none;');")
# response_box = driver.find_element_by_id('g-recaptcha-response')
# response_box.send_keys(result)

# entering responce short way with js element and working both firefox and chrome
driver.execute_script("document.getElementById('g-recaptcha-response').innerHTML=arguments[0]",result);
submit_button = driver.find_element_by_id('recaptcha-demo-submit').click()
