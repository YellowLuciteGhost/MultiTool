import random
import requests
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


email = "example@gmail.com"
username = "exampleusername"
password = "examplepassword"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://discord.com/register')
WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
driver.find_element_by_xpath("//input[@type='email']").send_keys(email) # email
driver.find_element_by_xpath("//input[@type='text']").send_keys(username) # username
driver.find_element_by_xpath("//input[@type='password']").send_keys(password) # password
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/form/div/div[2]/div[4]/div[1]/div[1]/div/div/div/div/div[2]/div').click()

actions = ActionChains(driver)
actions.send_keys(str(random.randint(1, 12))) # Month
actions.send_keys(Keys.ENTER)
actions.send_keys(str(random.randint(1, 28))) # Day
actions.send_keys(Keys.ENTER)
actions.send_keys(str(random.randint(1989, 2000))) # Year
actions.perform()

try:
    driver.find_element_by_class_name('inputDefault-3JxKJ2').click()  # Agree to terms and conditions
except:
    pass
driver.find_element_by_class_name('button-3k0cO7').click()  # Submit button


# get captcha key
site_key = 'f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34'
url = "https://discordapp.com/register"
API_KEY = "CAPMONSTER API KEY"
s = requests.Session()
data_post = {
    "clientKey": API_KEY,
    "task":
        {
            "type": "HCaptchaTaskProxyless",
            "websiteURL": url,
            "websiteKey": site_key
        }
}
captcha_id = s.post("https://api.capmonster.cloud/createTask", json=data_post).json()
data_get = {
    "clientKey": API_KEY,
    "taskId": captcha_id['taskId']
}
captcha_answer = s.get("https://api.capmonster.cloud/getTaskResult", json=data_get).json()
while captcha_answer['status'] == "processing":
    time.sleep(5)
    captcha_answer = s.get("https://api.capmonster.cloud/getTaskResult", json=data_get).json()
captcha_token = captcha_answer["solution"]["gRecaptchaResponse"]
driver.execute_script(f'document.getElementsByName("g-recaptcha-response")[0].innerText="{captcha_token}";') # put captcha token into g-recaptcha-response textarea
driver.execute_script(f'document.getElementsByName("h-captcha-response")[0].innerText="{captcha_token}";')

# code to submit captcha token