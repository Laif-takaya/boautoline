# PythonでSeleniumのwebdriverモジュールをインポート
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 1.操作するブラウザを開く
#WebDriverを格納しているディレクトリを指定
def highLow(date):
    currency_pair=date[:7]
    stop=date[0:2]
    up_down=date[-2:]
    try:
        # chromedriverのPATHを指定(herokuにおけるパスを指定しています)
        driver_path = '/app/.chromedriver/bin/chromedriver'
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        #driverに設定 ※optionsを指定しないとheadlessにならないので注意
        driver = webdriver.Chrome(options=options, executable_path=driver_path)
        driver.set_window_size(1280, 720)
        # 2.操作するページを開く
        driver.get('https://trade.highlow.com')
        # 基本設定はここまで。↑は使い回し可能。ここから下は、やりたい動作によって増える
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div/div/div/div/div/span/span/a[1]/i')))
        # 3.操作する要素を指定
        # 4.その要素を操作する
        driver.find_element_by_xpath('//*[@id="header"]/div/div/div/div/div/span/span/a[1]/i')

        result ="Ye"

        driver.quit()

        return result
    except:
        result ="errow"
        driver.quit()
        return result
