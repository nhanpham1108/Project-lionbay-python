Feature: Login

Scenario Outline: Đăng nhập sai tài khoản
  Given Go to page <link>
  When Nhap username = <username>
  And Set password = <password>
  And Click button login
  Then show headup alert = Số điện thoại/Email hoặc mật khẩu không chính xác. Vui lòng thử lại!
  @dev
  Examples: 
      | link   |                              username |       password |      
      | https://ship.lionnix.net/sign-in|       123456 |      123455777 |  
  @prod
  Examples: 
      | link   |                                     username |       password |  
      | https://ship.lionbay.express/sign-in|          123456 |      123455777 |  


Scenario Outline: Bỏ trống trường password
  Given Go to page <link>
  When nut enter bo trong password
  Then show text alert = Vui lòng không để trống!
  @dev
  Examples: 
      | link  |
      | https://ship.lionnix.net/sign-in|
  @prod
  Examples: 
      | link   |
      | https://ship.lionbay.express/sign-in|


Scenario: Đăng nhập tk chưa kích hoạt
  Given Go to page <link>
  When Nhap username = <username>
  And Set password = <password>
  And Click button login  
  Then show headup alert = Tài khoản đang được xác thực. Vui lòng chờ chúng tôi liên hệ với bạn.
  @dev
  Examples: 
      | link   |                                                   username |       password |      
      | https://ship.lionnix.net/sign-in|       lehuuhung21051998@gmail.com |         123455 |  
  @prod
  Examples: 
      | link   |                                                username |       password |  
      | https://ship.lionbay.express/sign-in|         tktest@yopmail.com |         123455 | 

Scenario: Đăng nhập tk bị deactive
  Given Go to page <link>
  When Nhap username = <username>
  And Set password = <password>
  And Click button login
  Then show headup alert = Tài khoản của bạn đã ngừng hoạt động
  @dev
  Examples: 
      | link   |                                                   username |       password |      
      | https://ship.lionnix.net/sign-in|                kimthu@yopmail.com |         123455 |  
  @prod
  Examples: 
      | link   |                                                 username |       password |  
      | https://ship.lionbay.express/sign-in|         kimthu1@yopmail.com |         123455 | 

Scenario: Bỏ trống trường username
  Given Go to page <link>
  When nut enter bo trong username
  Then show text alert = Vui lòng không để trống!
  @dev
  Examples:
      | link   |                                                   
      | https://ship.lionnix.net/sign-in|                
  @prod
  Examples: 
      | link   |                                                
      | https://ship.lionbay.express/sign-in|   




Scenario Outline: Đăng nhập đúng tài khoản
  Given Go to page <link>
  When Nhap username = <username>
  And Set password = <password>
  And Click button login
  Then Redirect to <link1>
  @dev
  Examples:
      | link   |                                         username   |             password |                             link1|
      | https://ship.lionnix.net/sign-in|      demoa100@yopmail.com |               123455 |         https://ship.lionnix.net/|

    
  @prod
  Examples: 
      | link   |                                                 username   |  password |                        link1 |
      | https://ship.lionbay.express/sign-in  |      laclac110897@gmail.com |    123455 | https://ship.lionbay.express/|

Scenario: logout thành công
  Given Go to page <link1>
  When Click logout = Đăng xuất
  Then Redirect to <link>
  @dev
  Examples:
      | link   |                                                          link1|
      | https://ship.lionnix.net/sign-in|             https://ship.lionnix.net/|

    
  @prod
  Examples: 
      | link   |                                                            link1 |
      | https://ship.lionbay.express/sign-in  |      https://ship.lionbay.express/|


