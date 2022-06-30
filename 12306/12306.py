from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import threading

chrome_options = Options()
chrome_options.add_argument('--headless')

sleep = 20

driver = webdriver.Chrome(options=chrome_options)

def listen(date='2022-01-29'):
    url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E6%AD%A6%E6%B1%89,WHN&ts=%E5%95%86%E4%B8%98,SQF&date={0}&flag=N,N,Y".format(date)
    try:
        while True:

            driver.get(url)
            driver.maximize_window()
            driver.implicitly_wait(10)

            day_start = driver.find_element_by_xpath('//*[@id="date_range"]/ul/li[1]/span[1]').text
            day_end = driver.find_element_by_xpath('//*[@id="date_range"]/ul/li[15]/span[1]').text

            if day_start != '':
                print(day_start)
                thread1 = threading.Thread(target=music)
                thread2 = threading.Thread(target=stop)
                thread1.start()
                thread2.start()
                break
            else:
                tempTime = time.localtime()
                print('无：', str(tempTime.tm_mon)+'月 '+str(tempTime.tm_mday)+'日 '+str(tempTime.tm_hour)+':'+str(tempTime.tm_min)+':'+str(tempTime.tm_sec))
                time.sleep(sleep)
                continue

    except Exception as e:
        print(e)
        thread1 = threading.Thread(target=err_music)
        thread2 = threading.Thread(target=stop)
        thread1.start()
        thread2.start()
    finally:
        driver.quit()


def music():
    for i in range(10):
        mp3 = r'D:\RuanJian\PotPlayer64\PotPlayerMini64.exe D:\RuanJian\pythonProject\Auto\金玉良缘.mp3'
        os.system(mp3)


def err_music():
    for i in range(10):
        mp3 = r'D:\RuanJian\PotPlayer64\PotPlayerMini64.exe D:\RuanJian\pythonProject\Auto\听闻远方有你.mp3'
        os.system(mp3)


def stop():
    for j in range(20):
        time.sleep(60*3)
        os.system(r'taskkill /f /t /im PotPlayerMini64.exe')


if __name__ == '__main__':
    listen()