import tkinter as tk
import webbrowser
import subprocess
import datetime
import time

# 调用函数打开网页
webbrowser.open("http://edbk74c94w.hknw133.51jz.top/diary.php")

def execute_script():
    subprocess.Popen(["pythonw", "E:/pyGit/05日报/日报.pyw"])

def close_program():
    exit()  # 关闭程序

def create_window():
    # 创建窗体
    window = tk.Tk()
    window.title("")
    window.attributes("-topmost", True)  # 置顶显示
    window.overrideredirect(True)  # 无标题栏
    window.attributes("-alpha", 0.5)  # 设置透明度
    window.configure(bg="magenta")  # 设置背景颜色

    # 创建按钮
    submit_button = tk.Button(window, text="提 交", command=execute_script)
    submit_button.pack(side=tk.LEFT)
    submit_button.configure(bg="green")  # 设置按钮背景颜色
    submit_button.configure(fg="white")  # 设置字体颜色
    submit_button.configure(font=("Arial", 20))  # 设置字体大小

    close_button = tk.Button(window, text="关 闭", command=close_program)
    close_button.pack(side=tk.LEFT)
    close_button.configure(bg="red")  # 设置按钮背景颜色
    close_button.configure(fg="white")  # 设置字体颜色
    close_button.configure(font=("Arial", 20))  # 设置字体大小

    # 运行窗体
    window.mainloop()

# 获取当前时间
current_time = datetime.datetime.now().time()

# 当前时间小于18:00时，程序启动1秒后自动退出
if current_time.hour < 18:
    time.sleep(1)
    exit()

# 创建窗体
create_window()