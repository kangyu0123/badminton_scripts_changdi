# badminton_scripts_changdi
The script for the badminton court

// 使用python的pynput操纵鼠标和键盘进行工作

// 对于图形的识别，本来是想采用图像识别子区域是否出现，但是效率太低，后来想到可以识别小区域的三维坐标的数值的相同与否，这样可以大大简化计算，前提是要知道抢羽毛球场地过程中出现的图像

//1.py是自动获取鼠标的坐标，获取的坐标在4.py中被需要
//4.py是主程序，里面有很详细的注释，设置了定时抢（考虑网络延迟）、区域识别以判断下一帧的出现等，成功率高达百分之80，我一般是和舍友两个人3电脑抢，只要参与抢票，基本都可以有两个
