# PythonでSeleniumのwebdriverモジュールをインポート
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
from time import sleep

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
        #driverに設定 ※optionsを指定しないとheadlessにならないので注意
        driver = webdriver.Chrome(options=options, executable_path=driver_path)
        #driver = webdriver.Chrome()
        driver.set_window_size(1280, 720)
        # 2.操作するページを開く
        driver.get('https://demotrade.highlow.com/')
        # 基本設定はここまで。↑は使い回し可能。ここから下は、やりたい動作によって増える
        sleep(2)

        result ="かち"

        driver.quit()

        return result
    except:
        result ="errow"
        driver.quit()
        return result
