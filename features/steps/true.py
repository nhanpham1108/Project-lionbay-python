import time
import pyperclip
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@when('copy lb')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//a[@class="lb-tooltip"]')
    e.click()
    time.sleep(1)
    
@when('Nhap username admin = {x}')
def step_impl(context, x):
    e = context.browser.find_element(By.XPATH, '//input[@type="text"]')
    e.clear()
    e.send_keys(x)

@when('Set password admin = {val}')
def step_impl(context, val):
    e = context.browser.find_element(By.XPATH,'//input[@type="password"]')
    e.clear()
    e.send_keys(val)

@when('login admin')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//button[@type="button"]')
    e.click()
    time.sleep(3)


@when('bat dau quet')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//button[@class="btn btn-info"]')
    e.click()
    time.sleep(3)




@when('dan ma LB')
def step_impl(context):
    e = context.browser.find_element(By.XPATH,'//input[@class="p-input form-control"]')
    e.clear()
    e.send_keys(pyperclip.paste())
    time.sleep(3)
    e.send_keys(Keys.RETURN)
    time.sleep(3)
    






@when('xac nhan quet')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '(//button[@class="btn btn-inline-info ml-3 text-nowrap"])[2]')
    e.click()
    time.sleep(3)


@then('kq quet = {kq}')
def step_impl(context, kq):
    e = context.browser.find_element(By.XPATH, '//span[@class="text-success"]')
    mat1 = e.text == kq 
    assert mat1 , 'Quét không thành công'

@when('dan nhan LB')
def step_impl(context):
    e = context.browser.find_element(By.XPATH,'//input[@class="p-input form-control"]')
    e.clear()
    e.send_keys(pyperclip.paste())
    time.sleep(3)
    e.send_keys(Keys.RETURN)
    time.sleep(5)


@when('huy label')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//*[text()="' + "Hủy label" + '"]')
    e.click()
    time.sleep(2)
    e1 = context.browser.find_element(By.XPATH, '//button[@class="p-button btn btn-danger"]')
    e1.click()
    time.sleep(5)

# @then('kq huy = {kq}')
# def step_impl(context, kq):
#     e = context.browser.find_element(By.XPATH, '//div[@role="alert"]/div')
#     mat1 = e.text == kq 
#     assert mat1 , 'Hủy label không thành công'


@when('tao lai label')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//*[text()="' + "In label" + '"]')
    e.click()
    time.sleep(10)

@then('label tao lai = {labelnew}')
def step_impl(context, labelnew):
    e = context.browser.find_element(By.XPATH, '(*//p[@class="col-6"])[1]')
    mat1 = e.text != labelnew 
    assert mat1 , 'tạo label không thành công'
    


@when('Click kho NY')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '(*//button[@class="choose-warehouse btn btn-default mr-8 mb-8"])[1]')
    e.click()
    time.sleep(3)


@when('button tao kien')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//*[@id="search-box"]/div[2]/button[2]')
    e.click()
    time.sleep(3)


@when('chon kho NY')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '*//select[@name="warehouseID"]')
    e.click()
    time.sleep(3)
    e1 = context.browser.find_element(By.XPATH, '*//select[@name="warehouseID"]/option[@value="1"]')
    e1.click()
    time.sleep(3)


@when('chon label ngoai')
def step_impl(context):
    e1 = context.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/select')
    e1.click()
    e = context.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/select/option[@value="2"]')
    e.click()
    time.sleep(1)
    


@when('Tao kien')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/div/div[3]/div[2]/button[2]')
    e.click()
    time.sleep(3)


@when('Click vao kien')
def step_impl(context):
    e1 = context.browser.find_element(By.XPATH, '*//button[@class="choose-warehouse btn btn-default mr-8 mb-8 active"]')
    e1.click()
    time.sleep(1)   
    e = context.browser.find_element(By.XPATH, '*//a[@class="text-no-underline"]')
    e.click()
    time.sleep(3)


@when('bat dau quet vao kien')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//*[@id="startScanButton"]')
    e.click()
    time.sleep(3)

@when('Them don vao kien')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '*//input[@class="p-input-search p-input form-control"]') 
    e.send_keys(pyperclip.paste())
    time.sleep(3)
    # e.send_keys(Keys.RETURN)
    # time.sleep(3)
    e1 = context.browser.find_element(By.XPATH, '*//button[@class="p-button btn btn-info btn-add-container ml-3"]')
    e1.click()
    time.sleep(3)



@when('button dong kien')
def step_impl(context):
    e1 = context.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/button[2]')
    e1.click()
    time.sleep(3)
    e = context.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[3]/div[2]/div/div[2]/div/div[4]/div/div/input')
    e.send_keys('11111111111')
    time.sleep(3)    

@when('Chon loai kich thuoc kien')
def step_impl(context):
    e1 = context.browser.find_element(By.XPATH, '*//select[@class="floating p-select form-control"]')
    e1.click()
    e = context.browser.find_element(By.XPATH, '*//option[@value="2"]')
    e.click()
    time.sleep(1)

@when('nhap can nang kien = {x}')
def step_impl(context, x):
    e = context.browser.find_element(By.XPATH, '(*//input[@type="number"])[1]')
    e.clear()
    e.send_keys(x)
    time.sleep(1)

@when('nhap can nang kien thuc te = {x}')
def step_impl(context, x):
    e = context.browser.find_element(By.XPATH, '(*//input[@type="number"])[2]')
    e.clear()
    e.send_keys(x)
    time.sleep(1)

@when('xac nhan dong kien')
def step_impl(context):
    e1 = context.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[3]/div[2]/div/div[3]/div[2]/button[2]')
    e1.click()
    time.sleep(10)

@when('Copy kien')
def step_impl(context):
    e1 = context.browser.find_element(By.XPATH, '//div[@class="package-code"]')
    pyperclip.copy(e1.text)
    time.sleep(5)


@then('Dong kien thanh cong = {dadong}')
def step_impl(context, dadong):
    e1 = context.browser.find_element(By.XPATH, '//span[@type="container"]')
    x = e1.text == dadong
    assert x , 'đóng kiện không thành công'


@when('button tao lo')
def step_impl(context):
    e1 = context.browser.find_element(By.XPATH, '//*[@id="search-box"]/button')   
    e1.click()
    time.sleep(3)


@when('chon kho lo ny')
def step_impl(context):
    e1 = context.browser.find_element(By.XPATH, '//select[@name="warehouseID"]')
    e1.click()
    time.sleep(1)
    e1 = context.browser.find_element(By.XPATH, '//option[@value="1"]')
    e1.click()
    time.sleep(1)

@when('Tao lo')
def step_impl(context):
    e1 = context.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/button[2]')
    e1.click()
    time.sleep(3)

@when('Click hub NY')
def step_impl(context):
    e1 = context.browser.find_element(By.XPATH, '//button[@class="btn btn-warehouse mb-8 active"]')
    e1.click()
    time.sleep(3)
    



@when('vao chi tiet lo')
def step_impl(context):
    e1 = context.browser.find_element(By.XPATH, '//a[@class="text-no-underline"]')
    e1.click()
    time.sleep(3)



@when('bat dau quet vao lo')
def step_impl(context):
    e1 = context.browser.find_element(By.XPATH, '//button[@class="mr-3 p-button btn btn-info"]')
    e1.click()
    time.sleep(3)


@when('Them kien vao lo')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//input[@class="p-input-search p-input form-control"]') 
    e.send_keys(pyperclip.paste())
    time.sleep(3)
    e.send_keys(Keys.RETURN)
    time.sleep(3)
    e1 = context.browser.find_element(By.XPATH, '//button[@class="p-button btn btn-info btn-add-container ml-3"]')
    e1.click()
    time.sleep(8)




@when('button dong lo')
def step_impl(context):
    e1 = context.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/button[2]')
    e1.click()
    time.sleep(3)



# @when('nhap gia tri = {x}')
# def step_impl(context, x):
#     e = context.browser.find_element(By.XPATH, '//input[@class="p-input form-control"]')
#     e.clear()
#     e.send_keys(x)
#     time.sleep(3)
    

@when('Dong lo')
def step_impl(context):
    e1 = context.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/button[2]')
    e1.click()
    time.sleep(15)


@then('Dong lo thanh cong = {dadong}')
def step_impl(context, dadong):
    e1 = context.browser.find_element(By.XPATH, '//span[@type="shipment"]')
    x = e1.text == dadong
    assert x , 'đóng lô không thành công'


@when('chuyen ups')
def step_impl(context):
    e1 = context.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/button[2]')
    e1.click()
    time.sleep(2)
    e = context.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div/button[2]')
    e.click()
    time.sleep(5)


@then('Chuyen ups thanh cong = {chuyenups}')
def step_impl(context, chuyenups):
    e1 = context.browser.find_element(By.XPATH, '//span[@type="shipment"]')
    x = e1.text == chuyenups
    assert x , 'Chuyển ups không thành công'