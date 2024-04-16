import requests, json
import time
cookies = {
    'gr_user_id': '0fbafe23-8c0c-4b06-987a-607911f89c65',
    'PHPSESSID': '待填',
    'think_language': 'zh-CN',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://reservation.bupt.edu.cn',
    'Connection': 'keep-alive',
    'Referer': 'https://reservation.bupt.edu.cn/index.php/Wechat/Booking/choose_template/template/1/area_id/5983/country_id/0/from/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}
day = "tomorrow"
today = "{0}{1:0>2d}{2:0>2d}".format(*time.localtime(time.time()))
tomorrow = "{0}{1:0>2d}{2:0>2d}".format(*time.localtime(time.time() + 86400))
check_period = {11,12,13,14,15}  # 11是5-6

data = {
    'now_area_id': '5982',
    'query_date': today if day == "today" else tomorrow,
    'first_room_id': '0',
    'start_date': today,
    'the_ajax_execute_times': '1',
}


if __name__ == '__main__':
    while True:
        response = requests.post(
            'https://reservation.bupt.edu.cn/index.php/Wechat/Booking/get_one_day_one_area_state_table_html',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        rooms = json.loads(response.text).get('data').get('rooms')
        time.sleep(1)
        response.close()
        print(rooms)
        for room in rooms:
            for period in check_period:
                if room.get("already_reserve").get(f"{period}") == "0":
                    print(room.get("id"))
                    #send()
                    input("有空场")
        time.sleep(30)




