from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import json
import time

# 获取cookie，第一次运行时登录，获取Cookie后不再执行
def get_cookie():
    driver = webdriver.Chrome()
    driver.get('https://passport.csdn.net/login?code=public')
    time.sleep(60)
    with open('cookies.txt','w') as cookief:
        #将cookies保存为json格式
        cookief.write(json.dumps(driver.get_cookies()))
    driver.close()

# 依据cookie进行登录
def login_cookie():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://www.csdn.net/')
    #首先清除由于浏览器打开已有的cookies
    driver.delete_all_cookies()
    with open('cookies.txt','r') as cookief:
        cookieslist = json.load(cookief)
        # 方法1 将expiry类型变为int
        for cookie in cookieslist:
            #并不是所有cookie都含有expiry 所以要用dict的get方法来获取
            if isinstance(cookie.get('expiry'), float):
                cookie['expiry'] = int(cookie['expiry'])
            driver.add_cookie(cookie)
        #方法2删除该字段
        # for cookie in cookieslist:
        #     #该字段有问题所以删除就可以  浏览器打开后记得刷新页面 有的网页注入cookie后仍需要刷新一下
        #     if 'expiry' in cookie:
        #         del cookie['expiry']
        #     driver.add_cookie(cookie)
    driver.refresh()

    # 获取文章列表
    get_paper_list()

    driver.close()


# 获取文章列表，无需登录
def get_paper_list():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    paper_list_url = 'https://blog.csdn.net/hanxia159357?t=1&type=blog'
    try:
        driver.get(paper_list_url)
        number = driver.find_element_by_xpath('//*[@id="floor-user-profile_485"]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/span').text
        # 获取文章href
        href_list = []
        for i in range(1, int(number)+1):
            href_xpath = '//*[@id="floor-user-profile_485"]/div/div[2]/div/div[2]/div/div[2]/div/article[%d]/a'%i
            driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_xpath(href_xpath))
            time.sleep(0.5)
            href_list.append(driver.find_element_by_xpath(href_xpath).get_attribute('href'))
            print(i,driver.find_element_by_xpath(href_xpath).get_attribute('href'))

        driver.maximize_window()
        temp_number = 0
        while temp_number <= 6000:
            for link in href_list:
                driver.get(link)
                temp_number += 1
                print(temp_number)
                time.sleep(2)
    except Exception as e:
        print(e)
    finally:
        driver.quit()


if __name__ == '__main__':

    get_paper_list()