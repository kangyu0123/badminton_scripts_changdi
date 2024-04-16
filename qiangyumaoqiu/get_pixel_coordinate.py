from __future__ import print_function
from pynput import mouse
from pynput import keyboard
from pynput import mouse
import threading
import ctypes, sys
import time
import pyautogui
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pynput, time
import sys
import os

def click():
    # 将要运行的代码加到这里

    M = mouse.Controller()
    k = keyboard.Controller()

    # print(M.position)

    # 微信位置: (876, 697)
    # 对话框位置：(401, 597)
    # 任务栏微信位置: (769, 698)
    # 发送按钮位置：(1188, 644)
    # 聊天框表情位置(343, 560)
    # 表情里面的表情位置(163, 223)

    # 任务栏微信位置(768, 697)
    # 第二天羽毛球场日期的位置(592, 102)
    # 中间空白处位置(596, 333)
    # 两个场地的位置：(674, 346)  (672, 424)
    # 确认预约的位置(636, 663)
    # 下拉后显示付款金额的 确认预约按钮位置(765, 647)后等0.2s
    # 选择微信支付的圆圈按钮位置(486, 328)
    # 选择微信支付圆圈后，确认支付按钮位置(645, 385)
    # 确认订单位置(641, 270)




    # 任务栏微信位置(751, 697)
    M.position = (1131, 1055)
    print(f"任务栏微信位置：{M.position}")
    M.click(mouse.Button.left, 1)
    time.sleep(0.1)
    # 第二天的位置(592, 102)
    M.position = (896, 156)
    print(f"第二天位置：{M.position}")
    M.click(mouse.Button.left, 1)
    # time.sleep(0.5)

    scale = 1
    for i in range(400):
        time.sleep(0.01)
        print(f"第{i}次截图")
        img = pyautogui.screenshot(region=(622, 185, 700, 200))
        img.save('screenshot_1.jpg')
        print(f"已经截图第{i}次")
        img = cv2.imread('screenshot_1.jpg')  # 要找的大图
        img = cv2.resize(img, (0, 0), fx=scale, fy=scale)

        target_screenshot = cv2.imread(
            'C:\\Users\\bo\\Desktop\\over_5.16\\target_image_1.jpg')  # 图中的小图
        target_screenshot = cv2.resize(target_screenshot, (0, 0), fx=scale, fy=scale)
        target_screenshot_size = target_screenshot.shape[:2]

        # 找图 返回最近似的点
        def search_returnPoint(img, target_screenshot, target_screenshot_size):
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            target_screenshot_ = cv2.cvtColor(target_screenshot, cv2.COLOR_BGR2GRAY)
            result = cv2.matchTemplate(img_gray, target_screenshot_, cv2.TM_CCOEFF_NORMED)
            threshold = 0.9
            # res大于70%
            loc = np.where(result >= threshold)
            # 使用灰度图像中的坐标对原始RGB图像进行标记
            point = ()
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img, pt, (pt[0] + target_screenshot_size[1], pt[1] + + target_screenshot_size[0]),
                              (7, 249, 151), 2)
                point = pt
            if point == ():
                return None, None, None
            return img, point[0] + target_screenshot_size[1] / 2, point[1]

        img, x_, y_ = search_returnPoint(img, target_screenshot, target_screenshot_size)
        if img is None:
            continue
        else:
            break

    if (img is None):
        print("no way")
    else:
        print("找到图片 位置:" + str(x_) + " " + str(y_))
        # plt.figure()
        # plt.imshow(img, animated=True)
        # plt.show()
        # 中间空白处位置(596, 333)
        print(f"中间空白处位置：{M.position}")
        M.position = (896, 457)
        M.click(mouse.Button.left, 1)
        time.sleep(0.1)
        # 向下滑动鼠标
        M.scroll(0, -5)
        time.sleep(0.5)
        M.scroll(0, -5)
        time.sleep(0.5)
        M.scroll(10, 0)
        # 两个场地的位置：(799, 395)  (797, 478)
        print(f"场地位置：{M.position}")
        M.position = (1100, 534)
        M.click(mouse.Button.left, 1)
        time.sleep(0.1)
        M.position = (1136, 634)
        time.sleep(0.1)
        M.click(mouse.Button.left, 1)
        # 确认预约的位置(636, 663)
        time.sleep(0.2)
        M.position = (966, 993)
        print(f"确认预约位置：{M.position}")
        M.click(mouse.Button.left, 1)
        time.sleep(0.5)
        # 下拉后显示付款金额的 确认预约按钮位置(765, 647)后等0.2s
        M.position = (1144, 980)
        print(f"金额+确认预约位置：{M.position}")
        M.click(mouse.Button.left, 1)
        time.sleep(1.4)
        # 选择微信支付的圆圈按钮位置(486, 328)
        M.position = (728, 491)
        print(f"选择微信支付的圆圈按钮位置：{M.position}")
        M.click(mouse.Button.left, 1)
        time.sleep(0.2)
        # 选择微信支付圆圈后，确认支付按钮位置(645, 385)
        M.position = (955, 583)
        print(f"确认支付按钮位置：{M.position}")
        M.click(mouse.Button.left, 1)
        time.sleep(0.2)
        # 确认订单位置(641, 270)
        M.position = (961, 405)
        print(f"确认订单位置：{M.position}")
        M.click(mouse.Button.left, 1)
        for i in range(10):
            print("zuihou")
            i += 1
            time.sleep(0.1)
            M.click(mouse.Button.left, 1)
    # M.position = (1188, 644)
    # M.click(mouse.Button.left, 1)


if __name__ == '__main__':
    def on_move(x, y):
        print('Pointer moved to {0}'.format(
            (x, y)))


    def on_click(x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        if not pressed:
            # Stop listener
            return False


    def on_scroll(x, y, dx, dy):
        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y)))


    # Collect events until released
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
    listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll)
    listener.start()
    # 创建新线程执行鼠标单击操作
    # thread = threading.Thread(target=click)
    # thread.start()

    # 在主线程中执行其他任务
