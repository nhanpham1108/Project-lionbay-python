Feature: taole

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

    
  @prod 
  Examples: 
      |                                 link |                username |  password |                         link1|
      | https://ship.lionbay.express/sign-in |  laclac110897@gmail.com |    123455 | https://ship.lionbay.express/|


Scenario Outline: tạo đơn US thành công
  Given Go to page <link>
  When button tao đon le = Tạo đơn
  And nhap form tao le
  And fullname = KH ABC
  And sdt kh = 0961035433
  And city = Tecumseh
  And address1 = 514 N Broadway
  And address2 = 514 N Broadway
  And state = OK
  And zipcode = 74873
  And countrycode = US
  And ordernumber = ordernumber1
  And detail = Clothes1,2 Cosmetics
  And weight = 2000
  And length = 20
  And width = 20
  And height = 20
  And pin
  And dich vu = Express
  And button tao moi
  Then man hinh = Chi tiết đơn hàng
  And phi giao hang
  @dev
  Examples: 
      |                                             link |         username  |          password  |                                                                     
      | https://ship.lionnix.net/packages?limit=25&page=1|  demoa100@yopmail.com |            123455  |  

    
  @prod
  Examples: 
      |                                                 link   |                username  |            password|                                          
      | https://ship.lionbay.express/packages?limit=25&page=1  |  laclac110897@gmail.com  |      LionNB@y#2021 |

Scenario Outline: tạo đơn US thành công
  Given Go to page <link>
  When Nhap username = <username>
  And Set password = <password>
  And Click button login
  And button tao đon le = Tạo đơn
  And fullname = KH ABC
  And sdt kh = 0961035433
  And city = Tecumseh
  And address1 = 514 N Broadway
  And address2 = 514 N Broadway
  And state = OK
  And zipcode = 74873
  And countrycode = US
  And ordernumber = ordernumber1
  And detail = Clothes1,2 Cosmetics
  And weight = 2000
  And length = 20
  And width = 20
  And height = 20
  And pin
  And dich vu = Express
  And button tao moi
  Then man hinh = Chi tiết đơn hàng
  And phi giao hang
  @dev
  Examples: 
      |                                             link |         username  |          password  |                                                                     
      | https://ship.lionnix.net/packages?limit=25&page=1|  demoa100@yopmail.com |            123455  |  

    
  @prod
  Examples: 
      |                                                 link   |                username  |            password|                                          
      | https://ship.lionbay.express/packages?limit=25&page=1  |  laclac110897@gmail.com  |      LionNB@y#2021 |




Scenario Outline: Tạo đơn lỗi do Kích thước không được vượt quá 90cm với đơn US
  Given Go to page <link>
  when button tao đon le = Tạo đơn
  And fullname = KH ABC
  And sdt kh = 0961035433
  And city = Tecumseh
  And address1 = 514 N Broadway
  And address2 = 514 N Broadway
  And state = OK
  And zipcode = 74873
  And countrycode = US
  And ordernumber = ordernumber1
  And detail = Clothes1,2 Cosmetics
  And weight = 2000
  And length = 200
  And width = 20
  And height = 20
  And pin
  And dich vu = Express
  And button tao moi
  Then kich thuoc = Chiều dài không được vượt quá 90 cm
  @dev
  Examples: 
      |                                             link |                                               
      | https://ship.lionnix.net/packages?limit=25&page=1|

    
  @prod
  Examples: 
      |                                                 link   |                               
      | https://ship.lionbay.express/packages?limit=25&page=1  | 





 