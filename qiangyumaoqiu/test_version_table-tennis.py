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
    print(f"P:任务栏微信位置：{M.position}")
    M.click(mouse.Button.left, 1)
    time.sleep(0.5)
    # 第二天的位置(592, 102)
    M.position = (896, 156)
    print(f"P:第二天位置：{M.position}")
    M.click(mouse.Button.left, 1)
    time.sleep(0.5)

    sign_1 = False
    sign_2 = False
    scale = 1

    # 返回图片颜色的平均RGB三色数值
    def get_color(image_path):
        # 读取图像
        image = cv2.imread(image_path)

        # 将图像转换为RGB颜色空间
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # 获取图像的平均颜色
        average_color = np.mean(image, axis=(0, 1))

        # 返回识别到的颜色
        return tuple(average_color.astype(int))

    for i in range(100):
        time.sleep(0.03)
        print(f"第一个界面的第{i}次截图")
        img = pyautogui.screenshot(region=(709, 257, 155, 30))
        img.save('C:\\Users\\bo\\Desktop\\ultimate_version\\2_tu\\screenshot_1_{}.jpg'.format(i))
        print(f"已经截图第{i}次")
        img_path = "C:\\Users\\bo\\Desktop\\ultimate_version\\2_tu\\screenshot_1_{}.jpg".format(i)  # 要找的大图

        # 返回图片颜色的平均RGB三色数值

        color = get_color(img_path)
        print(f"color的RGB三色数值为：{color}")
        if color != (255, 255, 255):
            print("找到第一次刷新出的目标图片")
            sign_1 = True
            break
        else:
            continue

    if not sign_1:
        print("no way")
    else:
        print("第一次的目标图片已经出现")
        print(f"P:已经点击中间的空白处位置，坐标为：{M.position}")
        M.position = (896, 457)
        M.click(mouse.Button.left, 1)
        time.sleep(0.2)
        # 向下滑动鼠标
        M.scroll(0, -5)
        time.sleep(0.5)
        M.scroll(0, -5)
        time.sleep(0.5)
        M.scroll(10, 0)
        time.sleep(0.2)
        # 两个场地的位置：(799, 395)  (797, 478)
        print(f"P:场地位置：{M.position}")
        M.position = (1136, 510)
        M.click(mouse.Button.left, 1)
        time.sleep(0.2)
        M.position = (1136, 581)

        time.sleep(0.1)
        M.click(mouse.Button.left, 1)
        # 确认预约的位置(636, 663)
        time.sleep(0.2)
        M.position = (966, 993)
        print(f"P:确认预约位置：{M.position}")
        M.click(mouse.Button.left, 1)
        time.sleep(0.5)
        # 下拉后显示付款金额的 确认预约按钮位置(765, 647)后等0.2s
        M.position = (1144, 993)
        print(f"P:金额+确认预约位置：{M.position}")
        M.click(mouse.Button.left, 1)
        time.sleep(0.5)

        for i in range(100):
            time.sleep(0.03)
            print(f"P:第二个界面的第{i}次截图")
            img = pyautogui.screenshot(region=(800, 630, 10, 5))
            img.save('C:\\Users\\bo\\Desktop\\ultimate_version\\2_tu\\screenshot_2_{}.jpg'.format(i))
            print(f"P:已经截图第{i}次")
            img_path = "C:\\Users\\bo\\Desktop\\ultimate_version\\2_tu\\screenshot_2_{}.jpg".format(i)  # 要找的大图

            color = get_color(img_path)
            if color == (255, 25, 255):
                print("P:找到第二次刷新出的目标图片")
                sign_2 = True
                break
            else:
                continue

        if not sign_2:
            print("no way")
        else:
            print("P:第二次的目标图片已经出现")
            # 选择微信支付的圆圈按钮位置(486, 328)
            M.position = (728, 491)
            print(f"P:选择微信支付的圆圈按钮位置：{M.position}")
            M.click(mouse.Button.left, 1)
            time.sleep(0.2)
            # 选择微信支付圆圈后，确认支付按钮位置(645, 385)
            M.position = (955, 583)
            print(f"P:确认支付按钮位置：{M.position}")
            M.click(mouse.Button.left, 1)
            time.sleep(0.2)
            # 确认订单位置(641, 270)
            M.position = (961, 405)
            print(f"P:最后确认订单位置：{M.position}")
            M.click(mouse.Button.left, 1)
            for i in range(10):
                print("P:最后确认订单位置")
                i += 1
                time.sleep(0.1)
                M.click(mouse.Button.left, 1)
        # M.position = (1188, 644)
        # M.click(mouse.Button.left, 1)


if __name__ == '__main__':
    # def on_move(x, y):
    #     print('Pointer moved to {0}'.format(
    #         (x, y)))
    #
    #
    # def on_click(x, y, button, pressed):
    #     print('{0} at {1}'.format(
    #         'Pressed' if pressed else 'Released',
    #         (x, y)))
    #     if not pressed:
    #         # Stop listener
    #         return False
    #
    #
    # def on_scroll(x, y, dx, dy):
    #     print('Scrolled {0} at {1}'.format(
    #         'down' if dy < 0 else 'up',
    #         (x, y)))
    #
    #
    # # Collect events until released
    # with mouse.Listener(
    #         on_move=on_move,
    #         on_click=on_click,
    #         on_scroll=on_scroll) as listener:
    #     listener.join()
    #
    # # ...or, in a non-blocking fashion:
    # listener = mouse.Listener(
    #     on_move=on_move,
    #     on_click=on_click,
    #     on_scroll=on_scroll)
    # listener.start()
    # 创建新线程执行鼠标单击操作
    thread = threading.Thread(target=click)
    thread.start()

    # 在主线程中执行其他任务
