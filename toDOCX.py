import datetime
from docx import Document
from getTQ import date_info
from getDb import *

def toDOCX():
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
if __name__ == '__main__':
    toDOCX()