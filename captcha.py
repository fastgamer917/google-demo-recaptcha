def captcha():

    import requests
    from time import sleep

    # Add these values
    API_KEY = 'xxxxxxx'  # Your 2captcha API KEY
    site_key = '6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-'  # site-key, read the 2captcha docs on how to get this
    url = 'https://www.google.com/recaptcha/api2/demo'  # example url

    s = requests.Session()

    # here we post site key to 2captcha to get captcha ID (and we parse it here too)
    captcha_id = s.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(
        API_KEY, site_key, url)).text.split('|')[1]
    # then we parse gresponse from 2captcha response
    recaptcha_answer = s.get(
        "http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id)).text
    print("solving ref captcha...")
    while 'CAPCHA_NOT_READY' in recaptcha_answer:
        sleep(5)
        recaptcha_answer = s.get(
            "http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id)).text
    recaptcha_answer = recaptcha_answer.split('|')[1]
    return recaptcha_answer
