import requests
import json
from selenium import webdriver

URL_TAO = 'https://ship-api.lionnix.net/v1/customer/packages'
URL_VAN = 'https://ship-api.lionnix.net/v1/customer/packages/delivery/'
API_KEY = "ZGVtb2IxMDBAeW9wbWFpbC5jb206NmEyYThmY2YtZGJmMy00MDBlLTg1ZjMtOGJkZDc1ODg2YWNk"

MESSAGE_QUA_CAN = "The weight must be less than or equal to 31751.46 gram"

MESSAGE_DICH_VU = "The service code is invalid"

orders = [
# Đơn hợp lệ
    {
 "order_number": "",
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
  "width": 70,
  "length": 5,
  "height": 5,
  "service_code": "E",
  "ignore_address_check": True
  }
#   ,
#     {
#  "order_number": "order2",
#   "name": "TX",
#   "company": "",
#   "phone": "0961054688",
#   "address_1": "514 N Broadway",
#   "address_2": "",
#   "city": "Tecumseh",
#   "state_code": "OK",
#   "zipcode": "74873",
#   "country_code": "US",
#   "detail": "Clothes1,2 Cosmetics",
#   "weight":19000,
#   "width": 70,
#   "length": 5,
#   "height": 5,
#   "service_code": "E",
#   "ignore_address_check": True
#   },
#       {
#  "order_number": "order3",
#   "name": "TX",
#   "company": "",
#   "phone": "0961054688",
#   "address_1": "514 N Broadway",
#   "address_2": "",
#   "city": "Tecumseh",
#   "state_code": "OK",
#   "zipcode": "74873",
#   "country_code": "US",
#   "detail": "Clothes1,2 Cosmetics",
#   "weight":19000,
#   "width": 70,
#   "length": 5,
#   "height": 5,
#   "service_code": "E",
#   "ignore_address_check": True
#   },
#       {
#  "order_number": "order4",
#   "name": "TX",
#   "company": "",
#   "phone": "0961054688",
#   "address_1": "514 N Broadway",
#   "address_2": "",
#   "city": "Tecumseh",
#   "state_code": "OK",
#   "zipcode": "74873",
#   "country_code": "US",
#   "detail": "Clothes1,2 Cosmetics",
#   "weight":19000,
#   "width": 70,
#   "length": 5,
#   "height": 5,
#   "service_code": "E",
#   "ignore_address_check": True
#   },
#       {
#  "order_number": "order5",
#   "name": "TX",
#   "company": "",
#   "phone": "0961054688",
#   "address_1": "514 N Broadway",
#   "address_2": "",
#   "city": "Tecumseh",
#   "state_code": "OK",
#   "zipcode": "74873",
#   "country_code": "US",
#   "detail": "Clothes1,2 Cosmetics",
#   "weight":19000,
#   "width": 70,
#   "length": 5,
#   "height": 5,
#   "service_code": "E",
#   "ignore_address_check": True
#   }
  ]


for order in orders:
    danhsach=["order1", "order2", "order3", "order4", "order5", "order6", "order7", 'order8', 'order9', 'order10', "order11", "order12", "order13", "order14", "order15", "order16", "order17", 'order18', 'order19', 'order20']
    
    # print("### ORDER: Tạo dơn " + order["order_number"]) 
    

    for order_number in danhsach: 
        order["order_number"] = order_number
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
                print("vận đơn  thành công có mã vận đơn " + kqvandon["package_code"])
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
                     ("Lỗi quá cân sai")
            if order["service_code"] not in ["E", "Express", "AE", "Australia Express"]:
                if MESSAGE_DICH_VU in loi["messages"]:
                    print("Lỗi dịch vụ đúng")
                else:
                    print ("Lỗi dịch vụ sai")


        print("")





