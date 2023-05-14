import pyautogui,pyperclip,time,sys,datetime

def click(img,fangfa="0"):
    i=88
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
    time.sleep(0.5)
    pyautogui.press("enter")
if __name__ == '__main__':
    send_to()