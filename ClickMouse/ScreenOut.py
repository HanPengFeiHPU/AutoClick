from pymouse import *
from pykeyboard import PyKeyboard
import time
import datetime

# 点击
def click():

    M = PyMouse()
    K = PyKeyboard()
    # 获取分辨率大小
    size = M.screen_size()
    x_s = float(size[0])
    y_s = float(size[1])
    while True:
        M.click(int(x_s/2),int(y_s/2),button=1,n=1)
        print(datetime.datetime.now())
        time.sleep(60)

if __name__ == '__main__':
    click()