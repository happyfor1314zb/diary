import datetime,requests,time
def date_info():
    r = requests.get('http://t.weather.sojson.com/api/weather/city/101240503')
    d_tianqi = r.json()
    tianqi = d_tianqi["data"]["forecast"][0]["type"]+" ["+d_tianqi["data"]["forecast"][0]["high"].split(" ")[1]+"/"+d_tianqi["data"]["forecast"][0]["low"].split(" ")[1]+"] "+d_tianqi["data"]["forecast"][0]["fx"]+d_tianqi["data"]["forecast"][0]["fl"]
    # 头部内容
    week_list = ["", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    wkday = week_list[time.localtime().tm_wday + 1]
    str1 = f"{(datetime.date.today()).strftime('%Y年%m月%d日')} {wkday} {tianqi}"
    return str1
if __name__ == '__main__':
    print(date_info())