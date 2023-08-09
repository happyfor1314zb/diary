from docx import Document
import datetime,requests
import requests
import pyautogui,pyperclip,time,sys,datetime
def date_info():
    print("查天气……")
    r = requests.get('https://query.asilu.com/weather/baidu/?city=%E5%AE%9C%E6%98%A5')
    d_tianqi = r.json()
    print(d_tianqi)
    tianqi = d_tianqi["weather"][0]["weather"]+" ["+d_tianqi["weather"][0]["temp"]+"] "+d_tianqi["weather"][0]["wind"]
    # tianqi = "wind"
    # 头部内容
    week_list = ["", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    wkday = week_list[time.localtime().tm_wday + 1]
    str1 = f"{(datetime.date.today()).strftime('%Y年%m月%d日')} {wkday} {tianqi}"
    return str1

# 0为今天工作，1为明天计划
def getDb(day):
    print("查询数据库……")
    array =[]
    # 获取数据接口
    re = requests.get(f'http://edbk74c94w.hknw133.51jz.top/wxmysql/diary_out{day}.php')
    # 中文unicode 解码
    str= eval("u"+"\'"+re.text+"\'")
    array=str.replace('[','').replace(']','').replace('"','').split(",")
    # 遍历内容
    i = 0
    txt=''
    for ar in array:
        i +=1
        txt += f"{i}、{ar}\n"
    return txt

def toDOCX():
    print("打开模板……")
    doc = Document(r"D:\公司汇报\日报\d0.docx")

    # 获取文档中的所有表格
    tables = doc.tables
    # 取第一个表格
    table = tables[0]
    table.cell(1, 0).text=date_info()

    # 侧行垂直居中
    table.cell(5,1).text=getDb(0)
    table.cell(6,1).text=getDb(1)
    # 保存,日月用0补齐8位长
    todayName = (datetime.date.today()).strftime('%Y%m%d')
    doc.save(f"D:\\公司汇报\\日报\\{todayName}宜丰宝梁城张斌日报.docx")


def click(img,fangfa="0"):
    i=10
    while i > 0:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.95)
        # print(location)
        #  如果有内容
        if location is not None:
            #  调用鼠标事件，点击时长，间隔，时长，左键
            if fangfa=="2": # 双击
                pyautogui.doubleClick(location.x, location.y, duration=0.2)
            else:   # 默认单击
                pyautogui.click(location.x, location.y, duration=0.2)
            print(f"已点{img}")
            #  回到上一层
            break
        i -= 1
        print(f"再尝试{i}次,寻找{img}")
        if i==0:
            sys.exit(0)
        time.sleep(1)

def send_to():
    pyautogui.hotkey("ctrl","s")
    # 启动钉钉
    pyautogui.hotkey("win","r")
    pyperclip.copy("C:\\Program Files (x86)\\DingDing\\DingtalkLauncher.exe")
    print("启动钉钉……")
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.hotkey("win","up")
    click("img/2sousuo.png")
    pyperclip.copy("宝梁城日报协调群")
    # pyperclip.copy("张斌")
    time.sleep(1)
    pyautogui.hotkey("ctrl","v")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")
    click("img/3wenjian.png")
    click("img/4fawenjian.png")
    tday =  (datetime.date.today()).strftime('%Y%m%d')
    name =f"{tday}宜丰宝梁城张斌日报.docx"
    pyperclip.copy(f"d:\\公司汇报\\日报\\{name}")
    time.sleep(1)
    pyautogui.hotkey("ctrl","v")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("enter")

if __name__ == '__main__':
    toDOCX()
    send_to()
    # date_info()