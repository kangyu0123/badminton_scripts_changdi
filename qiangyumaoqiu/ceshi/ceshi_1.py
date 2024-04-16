import pytesseract
from PIL import Image
import time

"""识别图片中文字，一帧需要0.36s左右"""
start_time = time.time()
# 指定 Tesseract OCR 的安装路径和 LSTM 模型文件路径
pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract.exe'
lstm_model_path = 'D:\\Tesseract-OCR\\tessdata'

# 读取图像文件
image_path = "C:\\Users\\bo\\Desktop\\ultimate_version\\reference_image.jpg"
image = Image.open(image_path)

# 使用 Tesseract OCR 进行文字识别
text = pytesseract.image_to_string(image, lang='chi_sim',
                                   config='--oem 1 --psm 6 --tessdata-dir "{}"'.format(lstm_model_path))

# 打印识别到的文字
print(text)
end_time = time.time()
run_time = end_time - start_time
print("程序运行时间：", run_time, "秒")