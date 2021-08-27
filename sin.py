import threading
import os
import pyautogui
import math
import time
pyautogui.FAILSAFE = False

# Change all co-ordinates as per your window size so as to see result in correct manner


def init():
    os.system("mspaint")


def red(wt, ht):
    pyautogui.moveTo(1196, 88)
    pyautogui.click()
    pyautogui.moveTo(wt, ht)


def green(wt, ht):
    pyautogui.moveTo(1292, 85)

    pyautogui.click()
    pyautogui.moveTo(wt, ht)


def paint():
    pyautogui.moveTo(53, 601)
    pyautogui.click()
    pyautogui.dragTo(1800, 601, duration=0.1)
    pyautogui.moveTo(53, 601)
    for i in range(0, 200):
        pyautogui.move(7, 0)
        wt, ht = pyautogui.position()
        if(abs(math.sin(i)) <= 0.5):
            red(wt, ht)
        else:
            green(wt, ht)
        pyautogui.dragRel(0, -(math.sin(i)*300), duration=0.000001)
        pyautogui.dragRel(0, (math.sin(i)*600), duration=0.000001)
        pyautogui.dragRel(0, -(math.sin(i)*300), duration=0.000001)
        print(i, (math.sin(i)))


if __name__ == "__main__":
    t1 = threading.Thread(target=init)
    t2 = threading.Thread(target=paint)
    t1.start()
    time.sleep(1)
    t2.start()
    t1.join()
    t2.join()
    print("Done!")
