import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@given('Go to page {url}')
def step_impl(context, url):
    context.browser.get(url)
    time.sleep(2)

@when('Nhap username = {x}')
def step_impl(context, x):
    e = context.browser.find_element(By.XPATH, '//input[@type="text"]')
    e.clear()
    e.send_keys(x)

@when('Set password = {val}')
def step_impl(context, val):
    e = context.browser.find_element(By.XPATH,'//input[@type="password"]')
    e.clear()
    e.send_keys(val)

@when('Click button login')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//button[@type="button"]')
    e.click()
    time.sleep(3)

@then('Show headup alert = {val}')
def step_impl(context, val):
    e = context.browser.find_element(By.XPATH, '//div[@role="alert"]')
    matches = (e.text == val)
    assert matches, 'Headup alert khong dung'

@then('Redirect to {url}')
def step_impl(context, url):
    matches = context.browser.current_url == url
    assert matches, 'Redirect khong dung'


@then('show text alert = {val}')
def step_impl(context, val):
    e = context.browser.find_element(By.XPATH, '//span[@class="helper-text"]')
    matches = (e.text == val)
    assert matches, 'text báo khong dung'
    time.sleep(3)

@when('nut enter bo trong username')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//input[@type="text"]')
    e.clear()
    e.send_keys(Keys.RETURN)


@when('nut enter bo trong password')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//input[@type="password"]')
    e.clear()
    e.send_keys(Keys.RETURN)

#logout
@when('Click logout = {logout}')
def step_impl(context, logout):
    e = context.browser.find_element(By.XPATH, '//span[@class="username"]')
    e.click()
    e1 = context.browser.find_element(By.XPATH, '//a[@href="/logout"]')
    e1.click()
    time.sleep(1)