import time
import datetime


def wait_time():
    current_time = datetime.datetime.now()
    print(time.time())
    target_time = datetime.datetime(current_time.year, current_time.month, current_time.day, 9, 3, 50)
    if current_time < target_time:
        time_difference = target_time - current_time
        seconds_to_wait = time_difference.total_seconds()
        return seconds_to_wait


print("距离主体程序运行还有：")
while wait_time() > 0:
    seconds_to_wait = wait_time()
    print(f"误差={seconds_to_wait-wait_time()}")
    hours = seconds_to_wait // 3600
    minutes = (seconds_to_wait % 3600) // 60
    seconds = seconds_to_wait % 60
    print(f"{int(hours)}小时 {int(minutes)}分钟 {seconds}秒")
    print(f"{seconds_to_wait}秒\n")
    if seconds_to_wait >= 1:
        time.sleep(1)
        seconds_to_wait -= 1
    else:
        time.sleep(seconds_to_wait)
        break
print("主体程序开始运行")