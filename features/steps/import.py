import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#nhán action NHẬP EXCEL
@when('Click button nhap excel = {excel}')
def step_impl(context, excel):
    e1 = context.browser.find_element(By.XPATH, '//*[text()="' + excel + '"]')
    e1.click()
    time.sleep(3)


@when('button tai len file AU')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '(//input[@type="file"])')
    e.send_keys("D:\kho\Lionbay\File_Autotest\AU_auto.xlsx")
    e1 = context.browser.find_element(By.XPATH, '(//button[@class="p-button btn btn-primary"])')
    e1.click()
    time.sleep(2)

@when('button tai len file US')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '(//input[@type="file"])')
    e.send_keys("D:\kho\Lionbay\File_Autotest\Zone 1_auto.xlsx")
    e1 = context.browser.find_element(By.XPATH, '(//button[@class="p-button btn btn-primary"])')
    e1.click()
    time.sleep(2)


@when('button tai len file US1')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '(//input[@type="file"])')
    e.send_keys("D:\kho\Lionbay\File_Autotest\Test US.xlsx")
    e1 = context.browser.find_element(By.XPATH, '(//button[@class="p-button btn btn-primary"])')
    e1.click()
    time.sleep(2)

@when('button tai len file US Pass Us fail')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '(//input[@type="file"])')
    e.send_keys("D:\kho\Lionbay\File_Autotest\Fail Pass US.xlsx")
    e1 = context.browser.find_element(By.XPATH, '(//button[@class="p-button btn btn-primary"])')
    e1.click()
    time.sleep(2)



@then('text thanh cong')
def step_impl(context):
    e1 = context.browser.find_element(By.XPATH, '//*[@id="preview"]/div[2]/div/div[2]/table/tr[2]/td[2]')
    e2 = context.browser.find_element(By.XPATH, '//*[@id="preview"]/div[2]/div/div[2]/table/tr[3]/td[2]')
    mat1 = e1.text == e2.text
    assert mat1, 'kq khong dung'
    time.sleep(3)  


