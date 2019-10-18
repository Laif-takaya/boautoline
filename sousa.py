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
        options.add_argument('--disable-gpu')
        options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36')
        #driverに設定 ※optionsを指定しないとheadlessにならないので注意
        driver = webdriver.Chrome(options=options, executable_path=driver_path)
        driver.set_window_size(1280, 720)
        # 2.操作するページを開く
        driver.get('https://demotrade.highlow.com/')
        # 基本設定はここまで。↑は使い回し可能。ここから下は、やりたい動作によって増える
        sleep(2)
        # 3.操作する要素を指定
        # 4.その要素を操作する
        driver.find_element_by_xpath('//*[@id="header"]/div/div/div/div/div/span/span/a[1]/i').click()

        result ="Yes"

        driver.quit()

        return result
    except:
        result ="errow"
        driver.quit()
        return result
