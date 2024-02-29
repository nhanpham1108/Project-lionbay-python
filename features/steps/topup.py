import time
import pyperclip
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@when('Go to page2 {url}')
def step_impl(context, url):
    context.browser.get(url)
    time.sleep(10)



@when('tab nap tien')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '(//a[@href="javascript:void(0)"])[1]')
    e.click()
    time.sleep(10)




  


@then('vi')
def step_impl(context):

    e8 = context.browser.find_element(By.XPATH, '(//p[@class="money"])[1]').text
    e9 = context.browser.find_element(By.XPATH, '(//p[@class="money"])[2]').text
    x = e8.find("$")
    balancesodu = float(e8[x + 1:].replace(",", ""))
    y = e9.find("$")
    z = e9[y + 1:]
    m = z.find(" (")
    balancesono = float(z[:m].replace(",", ""))

    vicu = context.vi

    if balancesodu > balancesono:
        kq1 = balancesodu
    elif balancesodu == balancesono:
        kq1 = balancesodu 
    else:
        kq1 = balancesono * -1

    vimoi = kq1
    
    balance =  vimoi == vicu + 1000
    assert balance , 'không tính đúng'









@when('click chuyen khoan')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '(//a[@href="javascript:void(0)"])[6]')
    e.click()
    time.sleep(1)

@when('click payoner')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '(//a[@href="javascript:void(0)"])[7]')
    e.click()
    time.sleep(3)

@when('click pingpong')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '(//a[@href="javascript:void(0)"])[8]')
    e.click()
    time.sleep(3)


@when('nhap tien = {ck}')
def step_impl(context, ck):
    e = context.browser.find_element(By.XPATH, '//input[@id="money"]')
    e.clear()
    e.send_keys(ck)
    time.sleep(2)

@when('transation = {transation}')
def step_impl(context, transation):
    e = context.browser.find_element(By.XPATH, '//input[@type="text"]')
    e.clear()
    e.send_keys(transation)
    time.sleep(2)

@when('xac nhan chuyen khoan')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//button[@type="button"]')
    e.click()
    time.sleep(1)


@when('Tim kiem email topup = {timkiem}')
def step_impl(context, timkiem):
    e = context.browser.find_element(By.XPATH, '//input[@class="p-input-search p-input form-control"]')
    e.click()
    e.clear()
    e.send_keys(timkiem)
    time.sleep(1)
    e.send_keys(Keys.RETURN)
    time.sleep(1)


@when('admin xac nhan topup')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '(//button[@class="mr-2 p-button btn btn-info"])[1]')
    e.click()
    time.sleep(1)
    e = context.browser.find_element(By.XPATH, '//button[@class="p-button btn btn-info"]')
    e.click()
    time.sleep(10) 





@then('kq topup = {thanhcong}')
def step_impl(context, thanhcong):
    e = context.browser.find_element(By.XPATH, '//span[@type="transaction"]')
    kq = e.text == thanhcong
    assert kq , 'đóng kiện không thành công'
    time.sleep(5)











