Feature: vandon



Scenario Outline: Đăng nhập đúng tài khoản KH
  Given Go to page <link>
  When Nhap username = <username>
  And Set password = <password>
  And Click button login
  Then Redirect to <link1>
  @dev
  Examples: 
      |                          link   |              username |    password |                       link1|
      | https://ship.lionnix.net/sign-in|  demoa100@yopmail.com |      123455 |   https://ship.lionnix.net/|

    
  @prod
  Examples: 
      |                                 link |                username |  password |                         link1|
      | https://ship.lionbay.express/sign-in |  laclac110897@gmail.com |    123455 | https://ship.lionbay.express/|



Scenario Outline: Vận đơn hợp lệ ở màn chi tiet
  Given Go to page <link>
  When Click button nhap excel = Nhập Excel
  And button tai len file US1
  And Go to page2 <link1>
  And kiem tra vi
  And Go to page1 <link>
  And Tim kiem ordernumber = 200
  And chi tiet don
  And tongvanchitiet
  And button tao tracking chi tiet
  And Go to page2 <link1>
  And kiemtra transaction
  Then kq van chi tiet
  @dev
  Examples: 
      |                                             link |                                     link1     |                                     
      | https://ship.lionnix.net/packages?limit=25&page=1|  https://ship.lionnix.net/bill?limit=25&page=1|

    
  @prod 
  Examples: 
      |                                                 link   |                                             link1 |
      | https://ship.lionbay.express/packages?limit=25&page=1  |  https://ship.lionbay.express/bill?limit=25&page=1|




Scenario Outline: Vận đơn không hợp lệ ở màn chi tiet
  Given Go to page <link>
  When Click button nhap excel = Nhập Excel
  And button tai len file US Pass Us fail
  And Go to page2 <link1>
  And kiem tra vi
  And Go to page1 <link>
  And Tim kiem ordernumber = 198
  And chi tiet don
  And tongvanchitiet
  And button tao tracking chi tiet
  And Go to page2 <link1>
  And kiemtra transaction
  Then kq van chi tiet
  @dev
  Examples: 
      |                                             link |                                     link1     |                                     
      | https://ship.lionnix.net/packages?limit=25&page=1|  https://ship.lionnix.net/bill?limit=25&page=1|

    
  @prod 
  Examples: 
      |                                                 link   |                                             link1 |
      | https://ship.lionbay.express/packages?limit=25&page=1  |  https://ship.lionbay.express/bill?limit=25&page=1|


      

Scenario Outline: Vận nhiều đơn US hợp lệ, đúng địa chỉ
  Given Go to page <link>
  When Click button nhap excel = Nhập Excel
  And button tai len file US
  And Go to page2 <link1>
  And kiem tra vi
  And Go to page1 <link>
  And chon 2 don
  And Gia tri van list
  And Nhan tao tracking list
  And Go to page2 <link1>
  And kiemtra transaction
  Then kq van
  @dev
  Examples: 
      |                                             link |                                     link1     |                                     
      | https://ship.lionnix.net/packages?limit=25&page=1|  https://ship.lionnix.net/bill?limit=25&page=1|

    
  @prod 
  Examples: 
      |                                                 link   |                                             link1 |
      | https://ship.lionbay.express/packages?limit=25&page=1  |  https://ship.lionbay.express/bill?limit=25&page=1|

Scenario Outline: Vận nhiều đơn US Pass + Us lỗi 
  Given Go to page <link>
  When Click button nhap excel = Nhập Excel
  And button tai len file US Pass Us fail
  And Go to page2 <link1>
  And kiem tra vi
  And Go to page1 <link>
  And Tim kiem ordernumber = 198
  And Icon canh bao
  And chon 2 don
  And Gia tri van list
  And tongvanlist
  And Nhan tao tracking list
  And Go to page2 <link1>
  And kiemtra transaction
  Then kq van
  @dev
  Examples: 
      |                                             link |                                     link1     |                                     
      | https://ship.lionnix.net/packages?limit=25&page=1|  https://ship.lionnix.net/bill?limit=25&page=1|

    
  @prod 
  Examples: 
      |                                                 link   |                                             link1 |
      | https://ship.lionbay.express/packages?limit=25&page=1  |  https://ship.lionbay.express/bill?limit=25&page=1|





##Scenario Outline: Vận đơn lỗi địa chỉ
##  Given Go to page <link>
##  when button tao đon le = Tạo đơn
##  And fullname = KH ABC
##  And sdt kh = 0961035433
##  And city = Tecumseh
##  And address1 = 514 N Broadway
##  And address2 = 514 N Broadway
##  And state = OK
##  And zipcode = 1
##  And countrycode = US
##  And ordernumber = ordernumber1
##  And detail = Clothes1,2 Cosmetics
##  And weight = 2000
##  And length = 20
##  And width = 20
##  And height = 20
##  And pin
##  And dich vu = Express
##  And button tao moi
##  And button tao tracking chi tiet
##  Then thong bao dia chi = Địa chỉ không hợp lệ
##  @dev
##  Examples: 
##      |                                             link |                                       
##      | https://ship.lionnix.net/packages?limit=25&page=1|  
##
##    
##  @prod 
##  Examples: 
##      |                                                 link   | 
##      | https://ship.lionbay.express/packages?limit=25&page=1  |
##
#
#
#
#
#
#
##Scenario Outline: Xóa cảnh báo địa chỉ xong vận
##  Given Go to page <link>
##  When button tao đon le = Tạo đơn
##  And fullname = KH ABC
##  And sdt kh = 0961035433
##  And city = Tecumseh
##  And address1 = 514 N Broadway
##  And address2 = 514 N Broadway
##  And state = OK
##  And zipcode = 1
##  And countrycode = US
##  And ordernumber = ordernumber6
##  And detail = Clothes1,2 Cosmetics
##  And weight = 2000
##  And length = 20
##  And width = 20
##  And height = 20
##  And pin
##  And dich vu = Express
##  And button tao moi
##  And Go to page1 <link>>
##  And Tim kiem ordernumber = ordernumber6
##  And Icon canh bao
##  And chi tiet don
##  And button sua don
##  And zipcode = 74873
##  And save
##  And button tao tracking chi tiet
##  Then trang thai chi tiet = Pre-transit
##  @dev
##  Examples:
##
##        |                                             link |                                       
##        | https://ship.lionnix.net/packages?limit=25&page=1|    
##  @prod  
##  Examples: 
##        |                                                  link   | 
##        | https://ship.lionbay.express/packages?limit=25&page=1   |  