#coding:utf-8
# 导包
from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://blog.csdn.net/hanhanwanghaha/article/details/107658968'
driver.get(url)

