# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from PIL import Image
import random

chrome_options =Options()
chrome_options.add_argument('--headless')

err = 0
success = 0
hour = 60 * 60
sleep = 30
logData = open("logData.txt","a+")

def logIn(xpath,xpathTime):
    global success,err
    driver = webdriver.Chrome(options=chrome_options)
    url = "https://mis.ccshcc.cn/#"
    userName = "hanpf"
    passWord = "Hanxia34"
    driver.implicitly_wait(10)
    try:
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="_username"]').send_keys(userName)
        driver.find_element_by_xpath('//*[@id="_password"]').send_keys(passWord)

        source = driver.find_element_by_xpath('//*[@id="btn"]')
        actions = ActionChains(driver)
        time.sleep(2)

        # 模拟滑动
        actions.drag_and_drop_by_offset(source, 500, 0).perform()

        # 点击登录
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="btnlogon"]').click()

        time.sleep(2)
        # 先定位到iframe
        elementi = driver.find_element_by_xpath('//*[@id="tabs"]/div[2]/div/div/iframe')

        # 再将定位对象传给switch_to_frame()方法
        driver.switch_to.frame(elementi)
        time.sleep(int(random.random() * 100))
        driver.find_element_by_xpath(xpath).click()

        time.sleep(2)
        # 检查是否点击成功
        clickTime = driver.find_element_by_xpath(xpathTime).text
        if (len(clickTime)==0):
            raise Exception
        if ((len(clickTime))!=0):
            success = success+1
            print("成功",success,clickTime)

    except Exception as e:
        logData.write(str(e)+'\n')
        err = err + 1
        I = Image.open('./red.jpg')
        I.show()
        print(e)
        logIn(xpath, xpathTime) # 点击未成功时再次登录
    finally:
        # I = Image.open('./green.jpg')
        # I.show()
        driver.quit()

def click(tm_hour,tm_min):
    global success,err
    tempdate = time.localtime()
    logData.write(str(tempdate.tm_mon)+' '+str(tempdate.tm_mday)+' '+str(tempdate.tm_hour)+' '+str(tempdate.tm_min)+'\tsuccess\t'+ str(success)+'\t err\t'+str(err)+'\n')
    if err == 0:
        # 签到和签退
        # 上午签到
        if (tm_hour==8 and (tm_min > 0 and tm_min < 60)):
            xpath = '//*[@id="imgMorningIn"]/a/img'
            xpathTime = '//*[@id="morningIn"]'
            logIn(xpath,xpathTime)
            time.sleep(2*hour)

            # 上午签退
        if (tm_hour==12 and (tm_min > 30 and tm_min < 40)):
            xpath = '//*[@id="imgMorningOut"]/a/img'
            xpathTime = '//*[@id="morningOut"]'
            logIn(xpath,xpathTime)
            time.sleep(0.5*hour-sleep)

           # 下午签到
        if (tm_hour==13 and (tm_min > 26 and tm_min < 40)):
            xpath = '//*[@id="imgAfternoonIn"]/a/img'
            xpathTime = '//*[@id="afternoonIn"]'
            logIn(xpath,xpathTime)
            time.sleep(2*hour)

            # 下午签退
        if (tm_hour==17 and (tm_min > 30 and tm_min < 60)):
            xpath = '//*[@id="imgAfternoonOut"]/a/img'
            xpathTime = '//*[@id="afternoonOut"]'
            logIn(xpath,xpathTime)
            time.sleep(0.5*hour)

            # 晚上签到18,40
        if (tm_hour==18 and (tm_min > 20 and tm_min < 40)):
            xpath = '//*[@id="imgNightIn"]/a/img'
            xpathTime = '//*[@id="nightIn"]'
            logIn(xpath,xpathTime)
            time.sleep(hour-sleep)

            # 晚上签退
        if (tm_hour==20 and (tm_min > 0 and tm_min < 40)):
            I = Image.open('./yell.jpg')
            I.show()
            xpath = '//*[@id="imgNightOut"]/a/img'
            xpathTime = '//*[@id="nightOut"]'
            logIn(xpath,xpathTime)
            time.sleep(hour)
    elif err > 0:
        logData.write("运行出现问题"+'\n')
        # print("运行出现问题")

    logData.close()

if __name__ == '__main__':
    while True:
        now = time.localtime()
        print(now.tm_hour,now.tm_min)
        logData = open("logData.txt", "a+")
        click(now.tm_hour,now.tm_min)
        time.sleep(sleep)
        if now.tm_hour >= 20 and now.tm_min > 40:
            logData.close()
            break