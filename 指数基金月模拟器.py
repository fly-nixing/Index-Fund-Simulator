import time
import random
import sys
#导入库
e = input("每月定投：")
w = int(e)*0.4431
year = input("多少年：")
years = int(year)*12
#输入和新增变量
if int(year) <= 20:
    print(year,"年日月轮转…")
    time.sleep(0.5)
    end = years*w
    print("共收益",end,"元")
    time.sleep(0.5)
#年份判断
if int(year) >= 50:
    print(year,"年沧海桑田…")
    time.sleep(0.5)
    end = years*w
    print("共收益",end,"元")
    time.sleep(0.5)
sys.exit()