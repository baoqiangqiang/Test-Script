# -*- coding:utf-8 -*-
# !/usr/bin/python3

import datetime
# # 1.导包
# import time
# from selenium import webdriver
# # 2.创建浏览器驱动对象
# driver = webdriver.Chrome()
# # 3.打开京东首页
# driver.get("https://www.jd.com/")
# # driver.maximize_window()
# # 4.暂停5秒
# time.sleep(5)
# # 5.关闭驱动对象
# driver.quit()



# 当前日期加某些天为哪个日期
# now_time = datetime.datetime.now()   # 获取当前
now_time = datetime.datetime.strptime('2034-02-05', '%Y-%m-%d')  # 随机输入日期
future_time = now_time + datetime.timedelta(days=11)  # 日期加天数
fu = future_time.strftime('%Y-%m-%d')  # 输出结果
# print(int(fu))    `
print(fu)

# 两个日期的间隔天数
d1 = datetime.datetime.strptime('2022-12-14', '%Y-%m-%d')
d2 = datetime.datetime.strptime('2034-04-08', '%Y-%m-%d')
delta = d1 - d2
print(delta.days)
# # print(delta)

#
# import wheel.pep425tags
# print(wheel.pep425tags.get_supported())