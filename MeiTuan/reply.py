from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://ecom.meituan.com/bizaccount/login.html?loginByPhoneNumber=true&isProduction=true&epassportParams=%3Fbg_source%3D1%26service%3Dcom.sankuai.meishi.fe.ecom%26part_type%3D0%26feconfig%3Dbssoify%26biz_line%3D1%26continue%3Dhttps%253A%252F%252Fecom.meituan.com%252Fbizaccount%252Fbiz-choice.html%253Fredirect_uri%253Dhttps%25253A%25252F%25252Fecom.meituan.com%25252Fmeishi%25252F%2526_t%253D1662643433457%2526target%253Dhttps%25253A%25252F%25252Fecom.meituan.com%25252Fmeishi%25252F%26leftBottomLink%3D%26signUpTarget%3Dself"

# 依据cookie进行登录
def login_cookie():
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(0.1)
        driver.maximize_window()
        driver.get(url)
        # 等待扫码登录
        input_msg = input("输入后继续：")
        # 打开沟通
        driver.get("https://g.dianping.com/app/gfe-common-pc-im-merchant/index.html#/")
        time.sleep(1)
        # 点击否
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click()

        # 检测列表中新消息
        num = 1
        while True:
            for i in range(1, 5):
                # 有新消息
                try:
                    print("第{0}_{1}个用户".format(str(num), str(i)))

                    # if num % 100 == 0:
                    #     driver.refresh()
                    #     time.sleep(2)
                    #     # 点击否
                    #     driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/button[1]").click()

                    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[5]").click()

                    is_new = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[{0}]/span".format(str(i)))
                    # is_new = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[{0}]".format(str(i)))
                    is_new.click()
                    input_text = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div[4]/div/div[2]/pre")
                    input_text.click()
                    input_text.send_keys("VX公众号At You Studyroom可自主选套餐、选座、选时间，欢迎体验！")

                    driver.find_element(By.CLASS_NAME,"send-button").click()

                    # isContinue = input("是否继续：")
                except Exception as ex:
                    # 无新消息
                    continue
                finally:
                    pass
                    # driver.refresh()
            num += 1

    except Exception as ex:
        print(ex)
    finally:
        driver.close()


if __name__ == '__main__':
    # get_cookie()
    login_cookie()
    # get_paper_list()