from __future__ import print_function
from pynput import mouse
from pynput import keyboard
import threading
import ctypes, sys
import time
import datetime
import pyautogui
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pynput
import sys
import os

# python C:\Users\bo\Desktop\ultimate_version\4.py


# 修改的内容
# ①运行的时间
# ②任务栏的位置
# ③灰色区域的位置（是否有、位置）
# ④场地位置
# ⑤滑轮操作


"""
①场地界面在左边，cmd窗口右边
②修改标签内容：目标时间、任务栏微信位置、第二天位置、场地位置     
③检查第二天识别的灰色区域是否被占用
④检查是否在左上角位置，左滑上滑滑轮到顶
④cmd命令：
"""

# 程序主体开始运行到点击第二天位置需要0.22~0.24s（0.24s包括程序运行时间0.04s+点击任务栏微信后等待的时间0.2s）
# 非高峰时期 点击第二天后 0.85s、0.87s、0.872s后刷新出（包括sleep0，5s）

# 提前点击刷新的代价是0.95s，包括循环一次sleep 0.5s、点击第二天按钮后等待转圈时间
# 所以设置9：59：59运行主程序+sleep 0.08s，实际是9：59：(59.22s)点击的第二天位置，非高峰时10：00：(0.01s)刷新出，高峰时
# 所以设置9：59：58运行主程序+sleep0.8s，实际是9：59：59.0点击第二天位置

"""
①非高峰时期，设置目标9：59：59，sleep(0.01s)，9：59：59.231点击，0.5s后开始识别第一个界面，10：00：00.0916出现第一个界面
②非高峰时期，设置目标9：59：59，sleep(0.01s)，9：59：59.231点击，0.5s后开始识别第一个界面，10：00：00.1156出现第一个界面
③非高峰时期，设置目标9：59：59，sleep(0.01s)，9：59：59.231点击，0.5s后开始识别第一个界面，10：00：00.0762出现第一个界面
④非高峰时期，设置目标9：59：59，sleep(0.01s)，9：59：59.231点击，0.5s后开始识别第一个界面，10：00：00.0974出现第一个界面
⑤非高峰时期，设置目标9：59：59，sleep(0.01s)，9：59：59.231点击，0.5s后开始识别第一个界面，10：00：00.1022出现第一个界面
⑥非高峰时期，设置目标9：59：59，sleep(0.01s)，9：59：59.231点击，0.5s后开始识别第一个界面，10：00：00.0986出现第一个界面
🔺 设置目标9：59：58s，然后sleep从0.01s改为0.01+1-0.07=0.94，0.5s后开始识别第一个界面，实际10：00：00.03出现第一个界面，
但是不知道系统采用哪一刻的数据作为之后展示的界面所以第一个界面10点整出现，未必是正确的
🔺 如果后面每天抢的时候延迟都很高，提前一段时间抢

高峰时期需要提前?s点击，测试记录每天抢的时间差：从点击第二天位置开始到页面刷新的两个时间

"""
def click():
    # 将要运行的代码加到这里
    def get_color(image_path):
        # 读取图像
        image = cv2.imread(image_path)

        # 将图像转换为RGB颜色空间
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # 获取图像的平均颜色
        average_color = np.mean(image, axis=(0, 1))

        # 返回识别到的颜色
        return tuple(average_color.astype(int))

    def wait_time():
        current_time = datetime.datetime.now()
        target_time = datetime.datetime(current_time.year, current_time.month, current_time.day, 9, 59, 59)
        if current_time < target_time:
            time_difference = target_time - current_time
            seconds_to_wait = time_difference.total_seconds()
            return seconds_to_wait

    M = mouse.Controller()

    print("距离主体程序运行还有：")
    while wait_time() > 0:
        seconds_to_wait = wait_time()
        hours = seconds_to_wait // 3600
        minutes = (seconds_to_wait % 3600) // 60
        seconds = seconds_to_wait % 60
        print(f"当前时间：{datetime.datetime.now()}")
        print(f"{int(hours)}小时 {int(minutes)}分钟 {int(seconds)}秒")
        print(f"{seconds_to_wait}秒\n")
        if seconds_to_wait >= 1:
            time.sleep(1)
            seconds_to_wait -= 1
        else:
            time.sleep(seconds_to_wait)
            break
    print("主体程序0.01s后开始运行")
    time.sleep(0.01)

    sign_1 = False
    sign_2 = False
    sign_3 = False

    M.position = (1082, 1046)
    print(f"⚪⚪⚪任务栏微信位置：{M.position}")
    M.click(mouse.Button.left, 1)
    time.sleep(0.2)

    for j in range(6):
        # 第一天位置：(792,222), 第二天的位置(905, 222)
        M.position = (905, 222)
        print(f"{datetime.datetime.now()}时第{j}次点击第二天位置：{M.position}")
        M.click(mouse.Button.left, 1)
        time.sleep(0.5)

        # 🔺 判断第二天场地是否刷新出（第一个界面）
        for i in range(300):
            time.sleep(0.02)
            img_0 = pyautogui.screenshot(region=(764, 300, 100, 20))  # 橙色字体区域
            # img_1 = pyautogui.screenshot(region=(933, 380, 10, 10))  # 灰色字体区域（2号场地第一场）
            # img_1 = pyautogui.screenshot(region=(933, 470, 10, 10))  # 灰色字体区域（2号场地第二场）
            img_1 = pyautogui.screenshot(region=(933, 796, 10, 10))  # 灰色字体区域（2号场地第五场）

            img_0.save('C:\\Users\\bo\\Desktop\\ultimate_version\\2_tu\\screenshot_0_{}.jpg'.format(i))
            img_1.save('C:\\Users\\bo\\Desktop\\ultimate_version\\2_tu\\screenshot_1_{}.jpg'.format(i))
            print(f"第一个界面已经截图第{i}次")
            img_0_path = "C:\\Users\\bo\\Desktop\\ultimate_version\\2_tu\\screenshot_0_{}.jpg".format(i)  # 橙色区域
            img_1_path = "C:\\Users\\bo\\Desktop\\ultimate_version\\2_tu\\screenshot_1_{}.jpg".format(i)  # 灰色区域

            # 返回图片颜色的平均RGB三色数值

            color_0 = get_color(img_0_path)
            color_1 = get_color(img_1_path)
            print(f"第一个界面橙色字体区域的RGB三色数值为：{color_0}\n")
            print(f"第一个界面灰色字体区域的RGB三色数值为：{color_1}\n")

            """
            一共所有的情况：
            ① 橙色区域没刷新出来，则一直刷新
            ② 橙色区域刷新出来，不能抢
            ③ 橙色区域刷新出来，能抢
            只需判断刷新出来的情况，没刷新出来就一直截图判断是否刷新出新界面，一旦刷新出，若不能抢则重新点击第二天，能抢就抢
            """
            # 如果刷新出界面（color_0不是白色）且场地不可以抢（color_1是灰色的），则说明点早了，需要退出截图判断的内层循环，重新点击第二天刷新

            if color_0 != (255, 255, 255) and color_1 == (243, 243, 243):
                break
            # 如果刷新出界面（color_0不是白色）且场地可以抢（color_1是白色的），则操纵鼠标下一步
            if color_0 != (255, 255, 255) and color_1 == (255, 255, 255):
                print("找到第一个界面的目标图片")
                sign_1 = True
                break
            # if color_0 != (255, 255, 255):
            #     print("找到第一个界面的目标图片")
            #     sign_1 = True
            #     break

        if sign_1:
            break

    if not sign_1:
        print("no way")
    else:
        print(f"{datetime.datetime.now()}时 第一个界面出现\n")
        time.sleep(0.15)
        M.position = (908, 463)
        M.click(mouse.Button.left, 1)
        print(f"⚪⚪⚪已经点击中间的空白处位置，坐标为：{M.position}")
        # 向下滑动鼠标
        # M.scroll(50, -50)
        # time.sleep(0.55)
        # 向右滑动鼠标
        # M.scroll(50, 0)
        # time.sleep(0.2)
        # 两个场地的位置：(1091, 490)  (1091, 600)
        print(f"⚪⚪⚪场地位置：{M.position}")
        M.position = (1146, 694)
        M.click(mouse.Button.left, 1)
        time.sleep(0.05)
        M.position = (1146, 790)
        time.sleep(0.05)
        M.click(mouse.Button.left, 1)

        # 确认预约的位置(978, 906)
        M.position = (978, 906)
        print(f"{datetime.datetime.now()}时点击第一个确认预约位置：{M.position}")
        # time.sleep(0.2)
        M.click(mouse.Button.left, 1)

        # 🔺 判断金额+确认预约按钮的出现（第二个界面）（判断橙色是否出现）,橙色区域：(963, 896, 30, 20)
        for i in range(200):
            time.sleep(0.01)
            img = pyautogui.screenshot(region=(963, 896, 30, 20))
            img.save('C:\\Users\\bo\\Desktop\\ultimate_version\\2_tu\\screenshot_2_{}.jpg'.format(i))
            print(f"第二个界面已经截图第{i}次")
            img_path = "C:\\Users\\bo\\Desktop\\ultimate_version\\2_tu\\screenshot_2_{}.jpg".format(i)  # 要找的大图

            # 返回图片颜色的平均RGB三色数值

            color = get_color(img_path)
            print(f"第二个界面color的RGB三色数值为：{color}\n")

            # 判断金额+确认预约按钮的出现（判断橙色是否出现）
            if color == (255, 135, 15):
                print("找到第二个界面的目标图片")
                sign_2 = True
                break
            else:
                continue

        if not sign_2:
            print("no way")
        else:
            print(f"{datetime.datetime.now()}时 第二个界面出现\n")
            time.sleep(0.02)
            M.position = (1105, 912)
            print(f"{datetime.datetime.now()}时点击第二个确认预约位置（金额+确认预约）：{M.position}")
            time.sleep(0.2)
            M.click(mouse.Button.left, 1)
            time.sleep(0.01)

            # 🔺 判断圆圈付款界面的出现（第三个界面）
            for i in range(300):
                time.sleep(0.02)
                img = pyautogui.screenshot(region=(871, 631, 20, 5))

                img.save('C:\\Users\\bo\\Desktop\\ultimate_version\\2_tu\\screenshot_3_{}.jpg'.format(i))
                print(f"第三个界面已经截图第{i}次")
                img_path = "C:\\Users\\bo\\Desktop\\ultimate_version\\2_tu\\screenshot_3_{}.jpg".format(i)  # 要找的大图

                color = get_color(img_path)
                print(f"第三次color的RGB三色数值为：{color}\n")
                if color == (255, 255, 255):
                    print("找到第三个界面的目标图片")
                    sign_3 = True
                    break
                else:
                    continue

            if not sign_3:
                print("no way")
            else:
                print(f"{datetime.datetime.now()}时 第三个界面出现\n")
                # 选择微信支付的圆圈按钮位置(486, 328)
                # 这里等待0.1s是因为识别的不是完全的最下方白色区域，会有一丢丢的延迟，所以需要等待0.1s
                time.sleep(0.2)
                M.position = (775, 523)
                print(f"⚪⚪⚪选择微信支付的圆圈按钮位置：{M.position}")
                M.click(mouse.Button.left, 1)
                time.sleep(0.1)
                # 选择微信支付圆圈后，确认支付按钮位置(645, 385)
                M.position = (955, 598)
                print(f"⚪⚪⚪确认支付按钮位置：{M.position}")
                M.click(mouse.Button.left, 1)
                time.sleep(0.2)
                # 确认订单位置(641, 270)
                M.position = (961, 456)
                print(f"⚪⚪⚪最后确认订单位置：{M.position}\n")
                M.click(mouse.Button.left, 1)
                for i in range(20):
                    print(f"{datetime.datetime.now()}  点击了一次最后确认订单位置")
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
