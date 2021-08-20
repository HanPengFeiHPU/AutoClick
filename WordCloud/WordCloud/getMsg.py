import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# 获取数据
def get_msg():
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    url = 'http://live.baidu.com/m/media/pclive/pchome/live.html?room_id=4562770581'
    url_2 = 'https://live.baidu.com/m/media/pclive/pchome/live.html?room_id=4594190830'
    driver.get(url=url_2)
    time.sleep(30)  # 用来登录
    file = open('msg.txt', 'a')
    try:
        while True:
            msg = driver.find_elements(By.CLASS_NAME, 'msg-box')
            for temp in msg:
                print(temp.text)

                # 去除emoji表情
                try:
                    # res = re.compile(u'[\u2300-\uffff]')
                    # temp_msg = res.sub('', temp.text)
                    file.write(temp.text+'\n')
                except Exception as e2:
                    continue

            time.sleep(2)

    except Exception as e:
        print('报错：', e)
    finally:
        driver.quit()
        file.close()


# 数据预处理
def pre_file():
    pretreatment_file = open('msg.txt')
    # 去重
    msg_set = set()
    for line in pretreatment_file.readlines():
        msg_set.add(line)
    # 去重后写入文件、去重后进一步仅将言论写入文件
    duplicate_removal_file = open('msg_duplicate_removal.txt', 'w')
    just_word_file = open('just_word.txt', 'w', encoding='utf-8')
    for line in msg_set:
        duplicate_removal_file.write(line)
        just_word_file.write(line.split('：')[1])

    pretreatment_file.close()
    duplicate_removal_file.close()
    just_word_file.close()


# 展示词云
def word_cloud():
    mytext = open('just_word.txt', encoding='utf-8').read()
    mask_image = np.array(Image.open('drink.png'))
    wordcloud = WordCloud(font_path="楷体_GB2312.ttf",background_color="white",width=600, max_words=100, mask=mask_image).generate(mytext)

    # 提取mask颜色
    image_colors = ImageColorGenerator(mask_image)
    image = wordcloud.to_image()

    # 显示图像
    # fig, axes = plt.subplots(1, 2)
    # axes[0].imshow(wordcloud)  # 不设置颜色
    # # axes[1].imshow(wordcloud.recolor(color_func=image_colors))  # 将词云颜色设置为mask的颜色
    # for ax in axes:
    #     ax.set_axis_off()  # 给每幅图都去坐标轴
    plt.axis("off")
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.show()


if __name__ == '__main__':
    get_msg()
    # pre_file()
    # word_cloud()
