import os


def kill_process():
    cmd = 'taskkill /f /im python.exe'
    os.system(cmd)


if __name__ == '__main__':
    kill_process()