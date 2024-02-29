Feature: true

Scenario Outline: Đăng nhập đúng tài khoản KH
  Given Go to page <link>
  When Nhap username = <username>
  And Set password = <password>
  And Click button login
  Then Redirect to <link1>
  @dev
  Examples: 
      |                          link   |              username |    password |                       link1|
      | https://ship.lionnix.net/sign-in|      demob100@yopmail.com |      123455 |   https://ship.lionnix.net/|

    
  @prod @prodquetvaokho
  Examples: 
      |                                 link |                username |  password |                         link1|
      | https://ship.lionbay.express/sign-in |  laclac110897@gmail.com |    123455 | https://ship.lionbay.express/|

#Scenario Outline: Đăng nhập  tài khoản admin
#  Given Go to page <link>
#  When Nhap username admin = <username>
#  And Set password admin = <password>
#  And login admin
#  Then Redirect to <link1>
#  @dev
#  Examples: 
#      |                                  link |            username |      password |                              link1|
#      | https://ship-admin.lionnix.net/sign-in|   admin@yopmail.com |        123455 |    https://ship-admin.lionnix.net/|
#
#    
#  @prod
#  Examples: 
#      |                                  link |         username   |         password |                         link1 |
#      | https://admin.lionbay.express/sign-in |   admin@lionnix.vn |    LionNB@y#2021 | https://admin.lionbay.express/|



#Scenario Outline: tạo đơn thành công
#  Given Go to page <link>
#  When button tao đon le = Tạo đơn
#  And fullname = KH ABC
#  And sdt kh = 0961035433
#  And city = Tecumseh
#  And address1 = <address1>
#  And address2 = 514 N Broadway
#  And state = OK
#  And zipcode = 74873
#  And countrycode = US
#  And ordernumber = ordernumber1
#  And detail = Clothes1,2 Cosmetics
#  And weight = 2000
#  And length = 20
#  And width = 20
#  And height = 20
#  And pin
#  And dich vu = Express
#  And button tao moi
#  Then man hinh = Chi tiết đơn hàng
#  @dev
#  Examples: 
#      |                                             link |                                               
#      | https://ship.lionnix.net/packages?limit=25&page=1|
#
#    
#  @prod
#  Examples: 
#      |                                                 link   |                               
#      | https://ship.lionbay.express/packages?limit=25&page=1  | 


#Scenario Outline Outline: import đơn AU
#  Given Go to page <link>
#  And Click button nhap excel = Nhập Excel
#  And button tai len file AU
#  Then text thanh cong
#  @dev
#  Examples: 
#      |                                             link |                                               
#      | https://ship.lionnix.net/packages?limit=25&page=1|
#
#    
#  @prod
#  Examples: 
#      |                                                 link   |                               
#      | https://ship.lionbay.express/packages?limit=25&page=1  | 

Scenario Outline: import đơn US
  Given Go to page <link>
  When Click button nhap excel = Nhập Excel
  And button tai len file US
  Then text thanh cong
  @dev
  Examples: 
      |                                             link |                                               
      | https://ship.lionnix.net/packages?limit=25&page=1|

    
  @prod @prodquetvaokho
  Examples: 
      |                                                 link   |                               
      | https://ship.lionbay.express/packages?limit=25&page=1  |  


Scenario Outline: Vận đơn ở màn list đơn US
  Given Go to page <link>
  when Tim kiem ordernumber = 198
  And Click ordernumber
  And Nhan tao tracking list
  Then trang thai list = Pre-transit
  And tracking list = N/A
  @dev
  Examples: 
      |                                             link |                                               
      | https://ship.lionnix.net/packages?limit=25&page=1|

    
  @prod @prodquetvaokho
  Examples: 
      |                                                 link   |                               
      | https://ship.lionbay.express/packages?limit=25&page=1  | 


#Scenario Outline: Vận đơn ở màn Chi tiết đơn US
#  Given Go to page <link>
#  When Tim kiem ordernumber = 85
#  And chi tiet don
#  And button tao tracking chi tiet
#  Then trang thai chi tiet = Pre-transit
#  And tracking chi tiet = N/A
#  @dev
#  Examples: 
#      |                                             link |                                               
#      | https://ship.lionnix.net/packages?limit=25&page=1|
#
#    
#  @prod
#  Examples: 
#      |                                                 link   |                               
#      | https://ship.lionbay.express/packages?limit=25&page=1  |  


Scenario Outline: Quét mã LB
  Given Go to page <link>
  When Tim kiem ordernumber = 198
  And copy lb
  And Go to page1 <link1>
  And Nhap username admin = <username admin>
  And Set password admin = <password admin>
  And login admin
  And Go to page1 <link2>
  And bat dau quet
  And dan ma LB
  And xac nhan quet
  Then kq quet = Thành công
  @dev
  Examples: 
      |                                             link |                                   link1 |     username admin  |    password admin  |                                             link2  |                          
      | https://ship.lionnix.net/packages?limit=25&page=1|  https://ship-admin.lionnix.net/sign-in |  admin@yopmail.com  |            123455  |  https://ship-admin.lionnix.net/warehouse/scan-in  |

    
  @prod @prodquetvaokho
  Examples: 
      |                                                 link   |                                 link1 |   username admin  |     password admin |                                            link2 |  
      | https://ship.lionbay.express/packages?limit=25&page=1  | https://admin.lionbay.express/sign-in | admin@lionnix.vn  |      LionNB@y#2021 |  https://admin.lionbay.express/warehouse/scan-in |

#Scenario Outline: dán nhãn hủy label cũ tạo lại label mới
#  Given Go to page <link>
#  When dan nhan LB
#  And huy label
#  And tao lai label 
#  Then label tao lai = N/A
#  @dev
#  Examples: 
#      |                                                  link |                                               
#      | https://ship-admin.lionnix.net/warehouse/check-package|
#
#    
#  @prod
#  Examples: 
#      |                                                 link   |                               
#      | https://admin.lionbay.express/warehouse/check-package  |  


Scenario Outline: cho đơn vào kiện ny, fedex
  Given Go to page <link>
  When button tao kien
  And chon kho NY
  And chon label ngoai
  And Tao kien
  And Click vao kien
  And bat dau quet vao kien
  And Them don vao kien
  And button dong kien
  And Chon loai kich thuoc kien
  And nhap can nang kien = 12
  And nhap can nang kien thuc te = 15
  And xac nhan dong kien
  And Copy kien
  Then Dong kien thanh cong = Đã đóng
  @dev
  Examples: 
      |                                                            link |                                               
      | https://ship-admin.lionnix.net/containers?limit=30&page=1&type=3|

    
  @prod
  Examples: 
      |                                                           link   |                               
      | https://admin.lionbay.express/containers?limit=30&page=1&type=3  | 


Scenario Outline: cho kiện vào lô và đóng thành công LOẠI FEDEX
  Given Go to page <link>
  When button tao lo
  And chon kho lo ny
  And Tao lo
  And Click hub NY
  And vao chi tiet lo
  And bat dau quet vao lo
  And Them kien vao lo
  And button dong lo
  And chuyen ups
  Then Chuyen ups thanh cong = Đang giao
  @dev
  Examples: 
      |                                                    link |                                               
      | https://ship-admin.lionnix.net/shipments?limit=30&page=1|

    
  @prod
  Examples: 
      |                                                   link   |                               
      | https://admin.lionbay.express/shipments?limit=30&page=1  |   










