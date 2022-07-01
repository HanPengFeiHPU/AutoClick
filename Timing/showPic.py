import time
import matplotlib.pyplot as plt

minute = 60


def show_pic():
    while True:
        now = time.localtime()
        if(now.tm_min in range(0,6)):
            img_path = r"preview.jpg"
            img = plt.imread(img_path)
            plt.figure("站一站")
            plt.imshow(img)
            plt.show(block=False)
            plt.pause(5 * minute)
            plt.close()
        else:
            time.sleep(5 * minute)


if __name__ == '__main__':
    show_pic()