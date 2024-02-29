import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By





#nhán action tạo đơns
@when('button tao đon le = {taodon}')
def step_impl(context, taodon):
    e1 = context.browser.find_element(By.XPATH, '//*[text()="' + taodon + '"]')
    e1.click()
    time.sleep(1)


@when('nhap form tao le')
def step_impl(context):
    fullname = context.browser.find_element(By.XPATH, '(//input[@name="name"])')
    fullname.clear()
    fullname.send_keys("KH ABC")
    time.sleep(1)

    phone = context.browser.find_element(By.XPATH, '(//input[@name="phone"])')
    phone.clear()
    phone.send_keys("0961035433")
    time.sleep(1)

    city = context.browser.find_element(By.XPATH, '(//input[@name="city"])')
    city.clear()
    city.send_keys("Tecumseh")
    time.sleep(1)

    address1 = context.browser.find_element(By.XPATH, '(//input[@name="address"])[1]')
    address1.clear()
    address1.send_keys("514 N Broadway")
    time.sleep(1)

    address2 = context.browser.find_element(By.XPATH, '(//input[@name="address"])[2]')
    address2.clear()
    address2.send_keys(" ")
    time.sleep(1)

    state = context.browser.find_element(By.XPATH, '(//input[@name="state"])')
    state.clear()
    state.send_keys("OK")
    time.sleep(1)

    postcode = context.browser.find_element(By.XPATH, '(//input[@name="postcode"])')
    postcode.clear()
    postcode.send_keys("74873")
    time.sleep(1)

    countrycode = context.browser.find_element(By.XPATH, '(//input[@name="countrycode"])')
    countrycode.clear()
    countrycode.send_keys("US")
    time.sleep(1)

    order_number = context.browser.find_element(By.XPATH, '(//input[@name="order_number"])')
    order_number.clear()
    order_number.send_keys("ordernumber1")
    time.sleep(1)

    detail = context.browser.find_element(By.XPATH, '(//input[@name="detail"])')
    detail.clear()
    detail.send_keys("Clothes1,2 Cosmetics")
    # time.sleep(1)

    weight = context.browser.find_element(By.XPATH, '(//input[@name="weight"])')
    weight.clear()
    weight.send_keys()
    # time.sleep(1)

@when('length = {length}')
def step_impl(context, length):
    e = context.browser.find_element(By.XPATH, '(//input[@name="length"])')
    e.clear()
    e.send_keys(length)
    # time.sleep(1)

@when('width = {width}')
def step_impl(context, width):
    e = context.browser.find_element(By.XPATH, '(//input[@name="width"])')
    e.clear()
    e.send_keys(width)
    # time.sleep(1)


@when('height = {height}')
def step_impl(context, height):
    e = context.browser.find_element(By.XPATH, '(//input[@name="height"])')
    e.clear()
    e.send_keys(height)
    # time.sleep(1)

@when('pin')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '(//input[@type="checkbox"])')
    e.click()
    # time.sleep(1)


@when('dich vu = {dichvu}')
def step_impl(context, dichvu):
    e = context.browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div')
    e.click()
    e1 = context.browser.find_element(By.XPATH, '//*[text()="' + dichvu + '"]')
    e1.click()
    time.sleep(3)




































@when('fullname = {fullname}')
def step_impl(context, fullname):
    e = context.browser.find_element(By.XPATH, '(//input[@name="name"])')
    e.clear()
    e.send_keys(fullname)
    # time.sleep(1)

@when('sdt kh = {sdtkh}')
def step_impl(context, sdtkh):
    e = context.browser.find_element(By.XPATH, '(//input[@name="phone"])')
    e.clear()
    e.send_keys(sdtkh)
    # time.sleep(1)

@when('city = {city}')
def step_impl(context, city):
    e = context.browser.find_element(By.XPATH, '(//input[@name="city"])')
    e.clear()
    e.send_keys(city)
    # time.sleep(1)


@when('address1 = {address1}')
def step_impl(context, address1):
    e = context.browser.find_element(By.XPATH, '(//input[@name="address"])[1]')
    e.clear()
    e.send_keys(address1)
    # time.sleep(1)


@when('address2 = {address2}')
def step_impl(context, address2):
    e = context.browser.find_element(By.XPATH, '(//input[@name="address"])[2]')
    e.clear()
    e.send_keys(address2)
    # time.sleep(1)



@when('state = {state}')
def step_impl(context, state):
    e = context.browser.find_element(By.XPATH, '(//input[@name="state"])')
    e.clear()
    e.send_keys(state)
    # time.sleep(1)


@when('zipcode = {zipcode}')
def step_impl(context, zipcode):
    e = context.browser.find_element(By.XPATH, '(//input[@name="postcode"])')
    e.clear()
    e.send_keys(zipcode)
    # time.sleep(1)


@when('countrycode = {countrycode}')
def step_impl(context, countrycode):
    e = context.browser.find_element(By.XPATH, '(//input[@name="countrycode"])')
    e.clear()
    e.send_keys(countrycode)
    # time.sleep(1)


@when('ordernumber = {ordernumber}')
def step_impl(context, ordernumber):
    e = context.browser.find_element(By.XPATH, '(//input[@name="order_number"])')
    e.clear()
    e.send_keys(ordernumber)
    # time.sleep(1)

@when('detail = {detail}')
def step_impl(context, detail):
    e = context.browser.find_element(By.XPATH, '(//input[@name="detail"])')
    e.clear()
    e.send_keys(detail)
    # time.sleep(1)

@when('weight = {weight}')
def step_impl(context, weight):
    e = context.browser.find_element(By.XPATH, '(//input[@name="weight"])')
    e.clear()
    e.send_keys(weight)
    # time.sleep(1)

@when('length = {length}')
def step_impl(context, length):
    e = context.browser.find_element(By.XPATH, '(//input[@name="length"])')
    e.clear()
    e.send_keys(length)
    # time.sleep(1)

@when('width = {width}')
def step_impl(context, width):
    e = context.browser.find_element(By.XPATH, '(//input[@name="width"])')
    e.clear()
    e.send_keys(width)
    # time.sleep(1)


@when('height = {height}')
def step_impl(context, height):
    e = context.browser.find_element(By.XPATH, '(//input[@name="height"])')
    e.clear()
    e.send_keys(height)
    # time.sleep(1)

@when('pin')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '(//input[@type="checkbox"])')
    e.click()
    # time.sleep(1)


@when('dich vu = {dichvu}')
def step_impl(context, dichvu):
    e = context.browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div')
    e.click()
    e1 = context.browser.find_element(By.XPATH, '//*[text()="' + dichvu + '"]')
    e1.click()
    time.sleep(3)



@when('button tao moi')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//a[@class="btn btn-primary"]')
    e.click()
    time.sleep(3)
    

# @then('tao don thanh cong = {val}')
# def step_impl(context, val):
#     e = context.browser.find_element(By.XPATH, '//div[@class="p-notices is-top is-dash"]')
#     x = (e.text == val)
#     assert x, 'Headup alert khong dung'
   

@then('man hinh = {mhdetail}')
def step_impl(context, mhdetail):
    e = context.browser.find_element(By.XPATH, '//div[@class="title"]')
    x = (e.text == mhdetail)
    assert x, 'Man hinh khong dung'
    time.sleep(10)



@then('kich thuoc = {chinmuoicm}')
def step_impl(context, chinmuoicm):
    e = context.browser.find_element(By.XPATH, '//div[@role="alert"]')
    x = (e.text == chinmuoicm)
    assert x, 'thông báo không đúng'


@then('phi giao hang')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/div[5]')
    p = e.text  
    id = context.browser.current_url.split("/")[4]
    sql = "SELECT  weight, width, length, height from packages WHERE id =" + id
    ketnoi = context.mysql
    ketnoi.execute(sql)
    result = ketnoi.fetchone()
    weight = int(result["weight"])
    width = int(result["width"])
    length = int(result["length"])
    height = int(result["height"])
    thetich = width * length * height / 5

    sql2 = "SELECT price, weight from prices WHERE service_id = 12 and user_class = 1 "
    ketnoi.execute(sql2)
    result2 = ketnoi.fetchall()
    ket_qua = ''
    if weight > thetich:
        for x in range(0, 55):
            if result2[x]["weight"] <= weight and weight < result2[x+1]["weight"]  :
                ket_qua = "$" + str(result2[x+1]["price"])
    else: 
        for x in range(0, 55):
            if result2[x]["weight"] <= thetich and thetich < result2[x+1]["weight"]:
                ket_qua = "$" + str(result2[x+1]["price"])
    mat = p == ket_qua
    assert mat, 'phi giao hang không đúng'