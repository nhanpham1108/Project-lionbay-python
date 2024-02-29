Feature: import

Scenario: import đơn thành công
  Given Go to page https://ship.lionnix.net/packages?limit=25&page=1
  When Nhap username = <username>
  And Set password = <password>
  And Click button login
  And Click button nhap excel = Nhập Excel
  And button tai len file US
  Then text thanh cong
  @dev
  Examples: 
      |                          link   |              username |    password |                    
      | https://ship.lionnix.net/sign-in|      demob100@yopmail.com |      123455 |  

    
  @prod 
  Examples: 
      |                                 link |                username |  password |                      
      | https://ship.lionbay.express/sign-in |  laclac110897@gmail.com |    123455 | 
