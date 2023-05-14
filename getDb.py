import requests
# 0为今天工作，1为明天计划
def getDb(day):
    array =[]
    # 获取数据接口
    re = requests.get(f'https://m7145h3529.zicp.fun/wxmysql/diary_out{day}.php')
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
if __name__ == '__main__':
    print(f"今天工作：\n{getDb(0)}")
    print(f"明天计划：\n{getDb(1)}")