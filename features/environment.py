from selenium import webdriver
import pymysql

def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.mysql = pymysql.connect(host='localhost',
                             port=3308,
                             user='dev',
                             password='$7=SgXa]5(j(dLAs',
                             database='shipment_dev',
                             cursorclass=pymysql.cursors.DictCursor).cursor()

def after_all(context):
    context.browser.quit()