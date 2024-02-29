Feature: topup

Scenario Outline: Đăng nhập đúng tài khoản KH
  Given Go to page <link>
  When Nhap username = <username>
  And Set password = <password>
  And Click button login
  Then Redirect to <link1>
  @dev
  Examples: 
      |                          link   |              username |    password |                       link1|
      | https://ship.lionnix.net/sign-in|      demoa100@yopmail.com |      123455 |   https://ship.lionnix.net/|

    
  @prod
  Examples: 
      |                                 link |                username |  password |                         link1|
      | https://ship.lionbay.express/sign-in |  laclac110897@gmail.com |    123455 | https://ship.lionbay.express/|


Scenario Outline: Chuyển khoản thành công
  Given Go to page <link>
  When tab nap tien
  And kiem tra vi
  And click chuyen khoan
  And nhap tien = 1000
  And xac nhan chuyen khoan
  And Go to page1 <link1>
  And Nhap username admin = <username>
  And Set password admin = <password>
  And login admin
  And Go to page1 <link2>
  And Tim kiem email topup = <email>
  And admin xac nhan topup
  And Go to page2 <link>
#  Then kq topup = Thành công
  then vi
  @dev
  Examples: 
      |                                       link   |                                 link1 |            username |      password |  link2 |                                                                                            email |
      | https://ship.lionnix.net/bill?limit=25&page=1| https://ship-admin.lionnix.net/sign-in|   admin@yopmail.com |        123455 |  https://ship-admin.lionnix.net/transactions?limit=30&search_by=account&type=1&page=1  | demoa100@yopmail.com |

    
  @prod
  Examples: 
      |                                              link |                                  link1 |         username   |         password | link2  |                                                                                                       email |            
      | https://ship.lionbay.express/bill?limit=25&page=1 |  https://admin.lionbay.express/sign-in |   admin@lionnix.vn |    LionNB@y#2021 | https://admin.lionbay.express/transactions?limit=30&search_by=account&type=1&page=1&tester=1 |laclac110897@gmail.com |


Scenario Outline: payoner thành công
  Given Go to page <link>
  When tab nap tien
  And kiem tra vi
  And click payoner
  And transation = xxx
  And nhap tien = 1000
  And xac nhan chuyen khoan
#  And Go to page1 <link1>
#  And Nhap username admin = <username>
#  And Set password admin = <password>
#  And login admin
  And Go to page1 <link2>
  And Tim kiem email topup = <email>
  And admin xac nhan topup
  And Go to page2 <link>
#  Then kq topup = Thành công
  Then vi
  @dev
  Examples: 
      |                                       link   |                                 link1 |            username |      password |  link2 |                                                                                            email |   
      | https://ship.lionnix.net/bill?limit=25&page=1| https://ship-admin.lionnix.net/sign-in|   admin@yopmail.com |        123455 |  https://ship-admin.lionnix.net/transactions?limit=30&search_by=account&type=1&page=1  | demoa100@yopmail.com |

    
  @prod
  Examples: 
      |                                              link |                                  link1 |         username   |         password | link2  |                                                                                                       email |       
      | https://ship.lionbay.express/bill?limit=25&page=1 |  https://admin.lionbay.express/sign-in |   admin@lionnix.vn |    LionNB@y#2021 | https://admin.lionbay.express/transactions?limit=30&search_by=account&type=1&page=1&tester=1 |laclac110897@gmail.com |


Scenario Outline: pingpong thành công
  Given Go to page <link>
  When tab nap tien
  And kiem tra vi
  And click pingpong
  And transation = xxx
  And nhap tien = 1000
  And xac nhan chuyen khoan
#  And Go to page1 <link1>
#  And Nhap username admin = <username>
#  And Set password admin = <password>
#  And login admin
  And Go to page1 <link2>
  And Tim kiem email topup = <email>
  And admin xac nhan topup
  And Go to page2 <link>
#  Then kq topup = Thành công
  Then vi
  @dev
  Examples: 
      |                                       link   |                                 link1 |            username |      password |  link2 |                                                                                             email |
      | https://ship.lionnix.net/bill?limit=25&page=1| https://ship-admin.lionnix.net/sign-in|   admin@yopmail.com |        123455 |  https://ship-admin.lionnix.net/transactions?limit=30&search_by=account&type=1&page=1  |  demoa100@yopmail.com |

    
  @prod
  Examples: 
      |                                              link |                                  link1 |         username   |         password | link2  |                                                                                                        email |   
      | https://ship.lionbay.express/bill?limit=25&page=1 |  https://admin.lionbay.express/sign-in |   admin@lionnix.vn |    LionNB@y#2021 | https://admin.lionbay.express/transactions?limit=30&search_by=account&type=1&page=1&tester=1 | laclac110897@gmail.com |
