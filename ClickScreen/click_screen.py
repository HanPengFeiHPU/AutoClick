from ctypes import windll
import win32api
import win32con
import time


class AutoScreen:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __del__(self):
        print("End")

    def get_info(self):
        # 将鼠标移动到目标位置
        windll.user32.SetCursorPos(self.height, self.width)
        # 鼠标左键按下
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.height, self.width)
        time.sleep(0.05)
        # 鼠标左键释放
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.height, self.width)

    def click(self):
        for i in range(10*10):
            self.get_info()
            print("已经点击{}次".format(str(i)))


if __name__ == '__main__':
    height = 1619  # windll.user32.GetSystemMetrics(0)
    width = 815  # windll.user32.GetSystemMetrics(1)

    auto = AutoScreen(height=height, width=width)
    # 警惕，不宜尝试
    auto.click()
