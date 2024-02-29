import requests
import json
from selenium import webdriver

URL_TAO = 'https://ship-api.lionnix.net/v1/customer/packages'
URL_VAN = 'https://ship-api.lionnix.net/v1/customer/packages/delivery/'
API_KEY = "bTQwN0B5b3BtYWlsLmNvbTo2MTkwMWQ3Ny0zNjBiLTQyNzAtOTlhNi1kY2Y5OTc0NjU5MTI="

MESSAGE_QUA_CAN = "The weight must be less than or equal to 31751.46 gram"

MESSAGE_ORDER_NUMBER_RONG = "The order number is required"
MESSAGE_DICH_VU = "The service code is invalid"
MESSAGE_ADDRESS1_RONG = "The address1 is required"
MESSAGE_COUNTRY_CODE_lOI = "The service Express not support country CA"
MESSAGE_HANG_US_WIDTH_QUA_KICH_THUOC = "The width must be less than or equal to 90 cm"
MESSAGE_HANG_US_CHU_VI_LOI = "“2*(weight + width) + length” must be less than or equal to 330.2 cm"

orders = [
# Đơn hợp lệ
    {
 "order_number": "rrrr",
  "name": "TX",
  "company": "",
  "phone": "0961054688",
  "address_1": "514 N Broadway",
  "address_2": "",
  "city": "Tecumseh",
  "state_code": "OK",
  "zipcode": "74873",
  "country_code": "US",
  "detail": "Clothes1,2 Cosmetics",
  "weight":19000,
  "width": 90,
  "length": 90,
  "height": 90,
  "service_code": "E",
  "ignore_address_check": True
  }
  ]

for order in orders:
    print("### ORDER: Tạo dơn " + order["order_number"]) 
    x =  requests.post(URL_TAO, json = order, headers = {"Authorization": "Basic " + API_KEY})
    statusapi = x.status_code
    if statusapi == 200:
        ketqua = json.loads(x.text)
        id = ketqua["package"]["id"]
        print("tạo đơn thành công, ID = " + str(id))
        url = URL_VAN + str(id)

        vandon =  requests.post(url, json = id, headers = {"Authorization": "Basic " + API_KEY})
        kqvandon = json.loads(vandon.text)
        status_vandon = vandon.status_code
        if status_vandon == 200:
            print("vận đơn  thành công có mã vận đơn" + kqvandon["package_code"])
        elif   status_vandon != 200: 
            print("vận đơn không thành công")
    elif statusapi != 200:
        print("Tạo đơn không thành công")
        loi = json.loads(x.text)
        #case qua can
        if order["weight"] > 31000: 
            if MESSAGE_QUA_CAN in loi["messages"]: 
                print("Lỗi quá cân đúng")
            else:
                print ("Lỗi quá cân sai")
        if order["service_code"] not in ["E", "Express", "AE", "Australia Express"]:
            if MESSAGE_DICH_VU in loi["messages"]:
                print("Lỗi dịch vụ đúng")
            else:
                print ("Lỗi dịch vụ sai")
        if order["order_number"] == "":
            if MESSAGE_ORDER_NUMBER_RONG in loi["messages"]:
                print("Lỗi ORDER NUMBER RỖNG")
            else:
                print ("Order rỗng nhưng không báo lỗi")
        if order["address_1"] == "":
            if MESSAGE_ADDRESS1_RONG in loi["messages"]:
                print("Lỗi ADDRESS 1 RỖNG")
            else:
                print ("address1 rỗng nhưng không báo lỗi")
        if order["country_code"] == "CA":
            if MESSAGE_COUNTRY_CODE_lOI in loi["messages"]:
                print("Lỗi dịch vụ Express không hỗ trợ country_code CA ")
            else:
                print ("Nhập sai countrycode vẫn cho tạo đơn")
        if order["width"] > 90:
            if MESSAGE_HANG_US_WIDTH_QUA_KICH_THUOC in loi["messages"]:
                print("Lỗi width quá kích thước")
            else:
                print ("Width quá kích thước đi US nhưng vẫn cho tạo đơn thành công ")
        if (2*(order["width"] + order["weight"]) + order["length"])  >= 330.2 :
            if MESSAGE_HANG_US_CHU_VI_LOI in loi["messages"]:
                print("Lỗi CHU VI quá 330.2CM")
            else:
                print ("Chu vi vượt quá nhưng vẫn cho tạo đơn thành công ")


    print("")






    # chrome =  webdriver.Chrome()
    # chrome.maximize_window()
    # chrome.get("https://ship.lionnix.net")
    # chrome.quit()

