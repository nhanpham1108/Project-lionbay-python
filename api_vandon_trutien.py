import requests
import json
from selenium import webdriver

URL_TAO = 'https://ship-api.lionnix.net/v1/customer/packages'
URL_VAN = 'https://ship-api.lionnix.net/v1/customer/packages/delivery/'
URL_BALANCE = 'http://ship-api.lionnix.net/v1/customer/users/balance'
API_KEY = "ZGVtb2IxMDBAeW9wbWFpbC5jb206NmEyYThmY2YtZGJmMy00MDBlLTg1ZjMtOGJkZDc1ODg2YWNk"

MESSAGE_QUA_CAN = "The weight must be less than or equal to 31751.46 gram"

MESSAGE_DICH_VU = "The service code is invalid"

balance = ''

kiemtravi =  requests.get(URL_BALANCE, headers = {"Authorization": "Basic " + API_KEY})
statusapivi = kiemtravi.status_code

vicu = ''

if statusapivi == 200:
        ketqua = json.loads(kiemtravi.text)

        if ketqua["balance"] == 0:
            vicu = float(ketqua["debt"])

        elif ketqua["balance"] != 0:
            vicu = float(ketqua["balance"])

        print(vicu)
     


elif statusapivi != 200:
        print("Không get được ví")






orders = [
# Đơn hợp lệ
    {
 "order_number": "Kiểm tra ví",
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
  ]


for order in orders:
    print("### ORDER: Tạo dơn " + order["order_number"]) 
    x =  requests.post(URL_TAO, json = order, headers = {"Authorization": "Basic " + API_KEY})
    statusapi = x.status_code
    if statusapi == 200:
        ketqua = json.loads(x.text)
        id = ketqua["package"]["id"]
        total_cost = float(ketqua["package"]["total_cost"])
        
        print("tạo đơn thành công, ID = " + str(id))
        print ("total_cost: " + str(total_cost))
        url = URL_VAN + str(id)

        vandon =  requests.post(url, json = id, headers = {"Authorization": "Basic " + API_KEY})
        kqvandon = json.loads(vandon.text)
        status_vandon = vandon.status_code
        if status_vandon == 200:
            print("vận đơn  thành công có mã vận đơn" + kqvandon["package_code"])
            kiemtravi =  requests.get(URL_BALANCE, json = balance, headers = {"Authorization": "Basic " + API_KEY})
            statusapivi = kiemtravi.status_code
            if statusapivi == 200:
                ketqua = json.loads(kiemtravi.text)
                vimoi = ''
                if ketqua["balance"] == 0:
                    vimoi = float(ketqua["debt"])
                
                elif ketqua["balance"] != 0:
                    vimoi = float(ketqua["balance"])

                www = vimoi == round((vicu - total_cost),2)
                if www == True:
                    print("Vận đơn trừ đúng tiền")
                elif www != True:
                    print("Vận đơn trừ sai tiền")
                



            elif statusapivi != 200:
                ("Không get được ví")
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



    print("")












