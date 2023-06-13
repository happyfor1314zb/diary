import datetime,requests,time
def date_info():
    r = requests.get('https://query.asilu.com/weather/baidu/?city=%E5%AE%9C%E6%98%A5')
    d_tianqi = r.json()
    # print(d_tianqi)
    tianqi = d_tianqi["weather"][0]["weather"]+" ["+d_tianqi["weather"][0]["temp"]+"] "+d_tianqi["weather"][0]["wind"]
    # 头部内容
    week_list = ["", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    wkday = week_list[time.localtime().tm_wday + 1]
    str1 = f"{(datetime.date.today()).strftime('%Y年%m月%d日')} {wkday} {tianqi}"
    return str1
if __name__ == '__main__':
    date_info()
    print(date_info())