import cv2
import numpy as np
import time

start_time = time.time()
"""得到图片中的平均颜色的RGB三色数值"""


def get_color(image_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 将图像转换为RGB颜色空间
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 获取图像的平均颜色
    average_color = np.mean(image, axis=(0, 1))

    # 返回识别到的颜色
    return tuple(average_color.astype(int))


# 图像路径
image_path = "C:\\Users\\bo\\Desktop\\ultimate_version\\ceshi\\x.jpg"

# 获取识别到的颜色
color = get_color(image_path)

# 打印识别到的颜色
if color == (255, 255, 255):
    print(color)
end_time = time.time()
run_time = end_time - start_time
print("程序运行时间：", run_time, "秒")
