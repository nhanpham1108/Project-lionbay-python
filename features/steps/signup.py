import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Đi tới trang

# @given('Go to page {url}')
# def step_impl(context, url):
#     context.browser.get(url)

# Tên tk

@when('Ten tai khoan = {tentk}')
def step_impl(context, tentk):
    e = context.browser.find_element(By.XPATH, '(//input[@type="text"])[1]')
    e.clear()
    e.send_keys(tentk)
    time.sleep(1)

#quy mô
@when('Quy mo = {quymo}')
def step_impl(context, quymo):
    e = context.browser.find_element(By.XPATH, '//div[@class="multiselect__select"]')
    e.click()
    e1 = context.browser.find_element(By.XPATH, '//*[text()="' + quymo + '"]')
    e1.click()
    time.sleep(1)
  
  



# email thay đổi
@when('email auto')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '(//input[@type="text"])[4]')
    e.clear()
    email = str(int(time.time())) + '@yopmail.com'
    e.send_keys(email)
    time.sleep(1)

# email cố định
@when('email = {email}')
def step_impl(context, email):
    e = context.browser.find_element(By.XPATH, '(//input[@type="text"])[4]')
    e.clear()
    e.send_keys(email)
    time.sleep(1)

#sdt thay đổi
@when('Sdt auto')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '(//input[@type="text"])[3]')
    e.clear()
    Sdt = int(time.time())
    e.send_keys(Sdt)
    time.sleep(1)


#sdt cố định
@when('Sdt = {sdt}')
def step_impl(context, sdt):
    e = context.browser.find_element(By.XPATH, '(//input[@type="text"])[3]')
    e.clear()
    e.send_keys(sdt)
    time.sleep(1)


    # Password



@when('Click button signup')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//button[@type="button"]')
    e.click()
    time.sleep(5)





@then('kiemtra = {text1} va {text2}')
def step_impl(context, text1, text2):
    e1 = context.browser.find_element(By.XPATH, '//div[@class="text-center request-noti"]')
    e2 = context.browser.find_element(By.XPATH, '//p[@class="text-center thank_use_sevice"]')
    mat1 = text1 == e1.text
    mat2 = text2 == e2.text

    assert mat1 and mat2, 'Redirect khong dung'
    



# @then('kiemtrahoten = {text1}')
# def step_impl(context, text1):
#     e1 = context.browser.find_element(By.XPATH, '//p[@class="alert active error"]')
#     mat1 = text1 == e1.text

#     assert mat1 , 'Redirect khong dung'


@then('alert email = {text1}')
def step_impl(context, text1):
    e1 = context.browser.find_element(By.XPATH, '//span[@class="helper-text"]')
    mat1 = text1 == e1.text
    assert mat1, 'Redirect khong dung'



@then('kiemtrasdtemail = {text1} va {text2}')
def step_impl(context, text1, text2):
    e1 = context.browser.find_element(By.XPATH, '//p[@class="alert active error"]')
    mat1 = text1 in e1.text
    mat2 = text2 in e1.text

    assert mat1 and mat2 , 'Redirect khong dung'


@then('alert hoten = {text1}')
def step_impl(context, text1):
    e1 = context.browser.find_element(By.XPATH, '//p[@class="alert active error"]')
    mat1 = text1 == e1.text

    assert mat1 , 'Redirect khong dung'