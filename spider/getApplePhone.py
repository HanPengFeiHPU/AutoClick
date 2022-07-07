from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options =Options()
chrome_options.add_argument('--headless')

err = 0
success = 0
hour = 60 * 60
sleep = 30
logData = open("logData.txt","a+")

# 不同版本的手机地址
url_dir = {"iPhone13ProMax": "https://www.apple.com/shop/buy-iphone/iphone-13-pro","iphone_13":"https://www.apple.com/shop/buy-iphone/iphone-13"}


def getSource():
    global success,err
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    try:
        while True:
            now = time.localtime()
            print(now.tm_hour, now.tm_min)
            driver.get(url_dir["iPhone13ProMax"])
            driver.maximize_window()
            # 监测
            monitor(driver)
            driver.quit()
            getSource()

    except Exception as e:
        logData.write(str(e)+'\n')
        err = err + 1
        # print(e)
        print(time.localtime())
        # logIn(xpath, xpathTime) # 点击未成功时再次登录
    finally:
        driver.quit()
        getSource()
        logData.close()

def monitor(driver):

    time.sleep(1)
    # 定位型号
    xpath_13ProMax = '/html/body/div[2]/div[5]/div[4]/div[2]/div[3]/div[2]/div[2]/div[1]/fieldset/div/div[2]/label'
    driver.find_element_by_xpath(xpath_13ProMax).click()

    time.sleep(1)
    # 定位颜色
    xpath_color = '/html/body/div[2]/div[5]/div[4]/div[2]/div[3]/div[2]/div[2]/div[2]/fieldset/div/div[1]/label/span[2]'  # Sierra Blue
    driver.find_element_by_xpath(xpath_color).click()

    time.sleep(1)
    # 定位内存
    xpath_capacity = '/html/body/div[2]/div[5]/div[4]/div[2]/div[3]/div[2]/div[2]/div[3]/fieldset/div/div[2]/label/span[1]'
    driver.find_element_by_xpath(xpath_capacity).click()

    time.sleep(1)
    # 定位快递
    xpath_carrier = '/html/body/div[2]/div[5]/div[4]/div[2]/div[3]/div[2]/div[2]/div[4]/fieldset/div/div[9]/label/span[1]'
    driver.find_element_by_xpath(xpath_carrier).click()

    time.sleep(1)
    # 定位YES/NO
    xpath_no = '/html/body/div[2]/div[5]/div[4]/div[2]/div[3]/div[2]/div[3]/div[1]/div/fieldset/div/div[1]/label'
    driver.find_element_by_xpath(xpath_no).click()

    # # 定位付款方式
    # xpath_payment = '//*[@id="e014cae0-2452-11ec-af61-e7949469983e"]'
    # driver.find_element_by_xpath(xpath_payment).click()

    # 上划
    time.sleep(2)
    driver.execute_script('window.scrollTo(0,1800)')
    time.sleep(1)
    # 定位检测是否有效
    xpath_availability = '/html/body/div[2]/div[5]/div[4]/div[2]/div[3]/div[2]/div[6]/div[1]/div/div[2]/div/div/div[2]/div/div/button/span'
    driver.find_element_by_xpath(xpath_availability).click()

    time.sleep(1)
    # 定位弹出页面的收入框
    xpath_search = '/html/body/div[3]/div/div/div/div/div[2]/div[1]/div[1]/form/div[1]/div/div/input'
    driver.find_element_by_xpath(xpath_search).send_keys(11355)

    # 查看是否有货物
    xpath_pick = '//*[@id="portal"]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/h3'
    msg = driver.find_element_by_xpath(xpath_pick).text

    print(msg)

    time.sleep(2)
    # 检查是否点击成功
    if ('11355' in msg):
        print("有货")
    else:
        print("缺货")

def login():
    start_time = time.time()
    if start_time < 1633314639+3600:
        logData = open("logData.txt", "a+")
        getSource()

if __name__ == '__main__':
    login()
