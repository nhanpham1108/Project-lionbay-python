import time
import pyperclip
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By





@when('button tao tracking chi tiet')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//button[@class="ml-7 p-button btn btn-primary"]')
    e.click()
    time.sleep(1)
    e1 = context.browser.find_element(By.XPATH, '//button[@class="p-button btn btn-primary"]')
    e1.click()
    time.sleep(10)
    context.browser.refresh()
    time.sleep(5)
   



@when('Nhan tao tracking list')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//button[@class="bulk-actions__selection-status p-button btn btn-primary"]') 
    e.click()
    time.sleep(3)
    e1 = context.browser.find_element(By.XPATH, '//button[@class="p-button btn btn-primary"]')
    e1.click()
    time.sleep(10)
    # context.browser.refresh()
    # time.sleep(5)



@then('thong bao dia chi = {diachiloi}')
def step_impl(context, diachiloi):
    e = context.browser.find_element(By.XPATH, '//div[@role="alert"]/div')
    x = (e.text == diachiloi)
    assert x, 'thông báo không đúng'
    time.sleep(3)


@then('trang thai chi tiet = {pre}')
def step_impl(context, pre):
    e = context.browser.find_element(By.XPATH, '//*[text()="' + pre + '"]')
    x = (e.text == pre)
    assert x, 'trạng thái khong dung'
    time.sleep(3)

@then('trang thai list = {pre}')
def step_impl(context, pre):
    e = context.browser.find_element(By.XPATH, '//span[@class="badge badge-round badge-pending"]')
    x = (e.text == pre)
    assert x, 'trạng thái khong dung'
    time.sleep(3)

# @when('back')
# def step_impl(context):
#     context.browser.back()
#     time.sleep(3)

@when('Go to page1 {url}')
def step_impl(context, url):
    context.browser.get(url)
    time.sleep(2)

@when('Tim kiem ordernumber = {timkiem}')
def step_impl(context, timkiem):
    e = context.browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div/div[1]/input')
    e.click()
    e.clear()
    e.send_keys(timkiem)
    time.sleep(1)
    e.send_keys(Keys.RETURN)
    time.sleep(1)

@when('Icon canh bao')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//span[@class="item_name is-dark is-top is-medium p-tooltip"]')
    e.click()
    e1 = context.browser.find_element(By.XPATH, '//button[@class="ml-7 p-button btn btn-primary"]')
    e1.click()
    time.sleep(3)


@when('chi tiet don')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//a[@class="text-no-underline"]')
    e.click()
    time.sleep(3)

@when('button sua don')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//button[@class="ml-7 p-button btn btn-lb-default"]')
    e.click()
    time.sleep(3)

@when('save')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//button[@class="btn btn-primary p-button btn btn-primary"]')
    e.click()
    time.sleep(3)


@when('Click ordernumber')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '(//input[@type="checkbox"])[2]') 
    e.click()
    time.sleep(3)


@when('chon 2 don')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '(//input[@type="checkbox"])[2]') 
    e.click()
    time.sleep(3)
    e1 = context.browser.find_element(By.XPATH, '(//input[@type="checkbox"])[3]') 
    e1.click()
    time.sleep(3)






@then('tracking list = {yes}')
def step_impl(context, yes):
    e = context.browser.find_element(By.XPATH, '(//span[@class="is-dark is-top is-large p-tooltip"])[1]') 
    x = e.text != yes
    assert x, 'không có tracking'
    time.sleep(3)


@then('tracking chi tiet = {yes}')
def step_impl(context, yes):
    e = context.browser.find_element(By.XPATH, '//a[@class="tracking"]') 
    x = e.text != yes
    assert x, 'không có tracking'
    time.sleep(3)



@when('tongvanlist')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div/span/b[2]').text
    x = e.find("$")
    tonglist = float(e[x + 1:].replace(",", ""))
    context.tongvanlist = tonglist
    print(tonglist)

@then('vi sau van list')
def step_impl(context):
    e8 = context.browser.find_element(By.XPATH, '(//p[@class="money"])[1]').text
    e9 = context.browser.find_element(By.XPATH, '(//p[@class="money"])[2]').text
    x = e8.find("$")
    balancesodu = float(e8[x + 1:].replace(",", ""))
    y = e9.find("$")
    z = e9[y + 1:]
    m = z.find(" (")
    balancesono = float(z[:m].replace(",", ""))

    kq = context.tongvanlist
    vicu = context.vi

    if balancesodu > balancesono:
        vimoi = balancesodu
        balance =  vimoi == vicu + kq
        assert balance , 'không tính đúng'
    elif balancesodu == balancesono:
        vimoi  = balancesodu
        balance =  vimoi == vicu + kq
        assert balance , 'không tính đúng'
    else:
        vimoi = balancesono * -1
        balance =  vimoi == round((vicu + kq*-1),2)
        assert balance , 'không tính đúng'

    e10 = context.browser.find_element(By.XPATH, '(//a[@href="javascript:void(0)"])[3]')
    e10.click()
    time.sleep(3)
    e11 = context.browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[2]/span[1]').text
    x = e11.find("$")
    transactionvandon = float(e11[x + 1:].replace(",", ""))

    transaction =  transactionvandon ==  kq
    assert transaction , 'transaction không bằng giá trị vận list'


@when('tongvanchitiet')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div[2]').text
    x = e.find("$")
    tongchitiet = float(e[x + 1:].replace(",", ""))
    context.tongvanchitiet = tongchitiet
    print(tongchitiet)



@when('Gia tri van list')
def step_impl(context):
    e = context.browser.find_element(By.XPATH, '//*[@id="tbl-packages"]/tbody/tr[1]/td[9]').text
    x = e.find("$")
    tien1 = float(e[x + 1:].replace(",", ""))
    context.tien1 = tien1
    print(tien1)
    
    e1 = context.browser.find_element(By.XPATH, '//*[@id="tbl-packages"]/tbody/tr[2]/td[9]').text
    x1 = e1.find("$")
    tien2 = float(e1[x1 + 1:].replace(",", ""))
    context.tien2 = tien2
    print(tien2)


    tongvan = tien1 + tien2
    context.tongvan = tongvan
    print(tongvan)


@when('kiem tra vi')
def step_impl(context):
    e1 = context.browser.find_element(By.XPATH, '(//p[@class="money"])[1]').text
    e2 = context.browser.find_element(By.XPATH, '(//p[@class="money"])[2]').text
    x = e1.find("$")
    balancesodu = float(e1[x + 1:].replace(",", ""))
    y = e2.find("$")
    z = e2[y + 1:]
    m = z.find(" (")
    balancesono = float(z[:m].replace(",", ""))

    if balancesodu > balancesono:
        kq = balancesodu
    elif balancesodu == balancesono:
        kq = balancesodu
    else:
        kq = round((balancesono * -1),2)
    context.vi = kq

    print(kq)





@when('kiemtra transaction')
def step_impl(context):
    e10 = context.browser.find_element(By.XPATH, '(//a[@href="javascript:void(0)"])[3]')
    e10.click()
    time.sleep(3)
    e11 = context.browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[2]/span[1]').text
    x = e11.find("$")
    transaction = float(e11[x + 1:].replace(",", ""))
    context.transaction = transaction
    print(transaction)
    time.sleep(3)
    context.browser.refresh()
    time.sleep(3)



@then('kq van chi tiet')
def step_impl(context):
    e8 = context.browser.find_element(By.XPATH, '(//p[@class="money"])[1]').text
    e9 = context.browser.find_element(By.XPATH, '(//p[@class="money"])[2]').text
    x = e8.find("$")
    balancesodu = float(e8[x + 1:].replace(",", ""))
    y = e9.find("$")
    z = e9[y + 1:]
    m = z.find(" (")
    balancesono = float(z[:m].replace(",", ""))

    tongchitiet = context.tongvanchitiet
    transaction = context.transaction 
    vicu = context.vi

    if transaction == tongchitiet:
        if balancesodu > balancesono:
            vimoi = balancesodu
            balance =  vimoi == vicu + tongchitiet
            assert balance , 'không tính đúng 1'

        elif balancesodu == balancesono:
            vimoi  = balancesodu
            balance =  vimoi == vicu + tongchitiet
            assert balance , 'không tính đúng 2'

        else:
            vimoi = balancesono * -1
            balance =  vimoi == round((vicu + tongchitiet*-1),2)
            print(vimoi)
            print(vicu)
            print(vicu + tongchitiet*-1)
            print(balance)
            assert balance , 'không tính đúng 3'
            
    elif transaction != tongchitiet:
        if balancesodu > balancesono:
            vimoi = balancesodu
            balance =  vimoi == vicu + 0
            assert balance , 'ví trừ tiên dù vận không thành công'

        elif balancesodu == balancesono:
            vimoi  = balancesodu
            balance =  vimoi == vicu + 0
            assert balance , 'ví trừ tiên dù vận không thành công'

        else:
            vimoi = balancesono * -1
            balance =  vimoi == vicu + 0
            assert balance , 'ví trừ tiên dù vận không thành công'



@then('kq van')
def step_impl(context):
    e8 = context.browser.find_element(By.XPATH, '(//p[@class="money"])[1]').text
    e9 = context.browser.find_element(By.XPATH, '(//p[@class="money"])[2]').text
    x = e8.find("$")
    balancesodu = float(e8[x + 1:].replace(",", ""))
    y = e9.find("$")
    z = e9[y + 1:]
    m = z.find(" (")
    balancesono = float(z[:m].replace(",", ""))

    tien2 = context.tien2
    tongvan = context.tongvan
    vicu = context.vi
    transaction = context.transaction 
   

    if transaction == tongvan:
        if balancesodu > balancesono:
            vimoi = balancesodu
            balance =  vimoi == vicu + tongvan
            assert balance , 'không tính đúng'

        elif balancesodu == balancesono:
            vimoi  = balancesodu
            balance =  vimoi == vicu + tongvan
            assert balance , 'không tính đúng'

        else:
            vimoi = balancesono * -1
            balance =  vimoi == round((vicu + tongvan*-1),2)
            assert balance , 'không tính đúng'
    elif transaction != tongvan:
        if balancesodu > balancesono:
            vimoi = balancesodu
            balance =  vimoi == vicu + tien2
            assert balance , 'ví trừ cả đơn không hợp lệ'

        elif balancesodu == balancesono:
            vimoi  = balancesodu
            balance =  vimoi == vicu + tien2
            assert balance , 'ví trừ cả đơn không hợp lệ'

        else:
            vimoi = balancesono * -1
            balance =  vimoi == round((vicu + tien2*-1),2)
            assert balance , 'ví trừ cả đơn không hợp lệ'
    








