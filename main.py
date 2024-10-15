import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
import mechanize
from seleniumbase import Driver
from proxy_checker import ProxyChecker
import urllib
import requests

a = input("видите email: ")
b = input("видите пароль от аккаунта: ")
z = input("видите ip и порт прокси сервера: ")
def Login(passwordVal, emailVal, proxyServer):
    try:
        proxy = proxyServer
        try:
            proxyCheck = {'https': f"{proxy}"}
            response = requests.get("https://stackoverflow.com/questions/765305/proxy-check-in-python", proxies=proxyCheck)
            if response.status_code == 200:
                print('Прокси рабочий')
                try:
                    options = uc.ChromeOptions()
                    options.add_argument('--blink-settings=imagesEnabled=false')
                    options.add_argument(f'--proxy-server={proxy}')
                    driver = uc.Chrome(options=options)
                    driver.implicitly_wait(5)
                    driver.get("https://www.ipqualityscore.com/login")
                    time.sleep(20)
                    email = driver.find_element(By.ID, "email")
                    password = driver.find_element(By.ID, "password")
                    email.clear()
                    email.send_keys(emailVal)
                    password.clear()
                    password.send_keys(passwordVal)
                    button = driver.find_element(By.XPATH, "//button[text()='Login']")
                    print(button)
                    button.click()
                    time.sleep(10)
                    parsingFraudeScore(driver)
                    print("end")
                except Exception as e:
                    print(e)
                    driver.close()
                    driver.quit()
            else:
                print('Прокси не рабочий')
        except Exception as e:
            print(e)

    except:
        print("adadasd")

def parsingFraudeScore(driver):
    driver.get("https://www.ipqualityscore.com/user/proxy-detection-api/lookup")
    fraudMain = driver.find_element(By.CLASS_NAME, "fraud_score")
    print(fraudMain)

def main():
    Login(b, a, z)


if __name__ == "__main__":
    main()