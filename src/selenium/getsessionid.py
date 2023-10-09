from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

service = Service('/home/lon8/python/projects/steambuy/chromedriver') # Изменить значение

chrome_options = Options()

driver = webdriver.Chrome(options=chrome_options, service=service)

def get_sessionid(cookies : list) -> int | None:
    sessionid = None

    for cookie in cookies:
        if cookie['name'] =='sessionid':
            sessionid = cookie['value']
    
    return sessionid

def get_cookies(bot_number : int = 0) -> list:
    
    chrome_options.add_argument(f'--user-data-dir=./temp/profiles/bot{bot_number}')
    # Лучше изменить значение
    chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.717 Yowser/2.5 Safari/537.36')
    # Для невидимости
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=chrome_options, service=service)
        
    driver.get("https://steamcommunity.com/")

    driver.refresh()

    sleep(2)

    cookies = driver.get_cookies()

    return cookies

print(get_sessionid())