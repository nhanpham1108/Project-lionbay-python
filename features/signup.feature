Feature: Signup


Scenario: Đăng ký không thành công do nhập sdt,email đã có trên hệ thống
  Given Go to page <link>
  When Ten tai khoan = m sau tram
  And Quy mo = Dưới 150 đơn hàng / tháng
  And Sdt = 55
  And email = <username>
  And Set password = <password>
  And Click button signup
  Then kiemtrasdtemail = Số điện thoại đã được sử dụng, vui lòng chọn số điện thoại khác va Email đã được sử dụng, vui lòng chọn email khác
  @dev
  Examples:
      | link   |                                               username   |             password |                      
      | https://ship.lionnix.net/sign-up|      m6001444121r11@yopmail.com |               123455 |        

    
  @prod
  Examples: 
      | link   |                                                 username   |  password |                      
      | https://ship.lionbay.express/sign-up  |      laclac110897@gmail.com |    123455 | 

Scenario: Nhập email không hợp lệ
  Given Go to page <link>
  When email = <username>
  Then alert email = Email không hợp lệ
  @dev
  Examples:
      | link   |                             username |                               
      | https://ship.lionnix.net/sign-up|      h12231 |                      

    
  @prod
  Examples: 
      | link   |                                 username   |                        
      | https://ship.lionbay.express/sign-up  |      h12231 |    

Scenario: Đăng ký không thành công do nhập sdt,email đã có trên hệ thống
  Given Go to page <link>
  When Ten tai khoan = nhan@
  And Quy mo = Dưới 150 đơn hàng / tháng
  And Sdt auto
  And email auto
  And Set password = 123455
  And Click button signup
  Then alert hoten = Tên tài khoản không hợp lệ
  @dev
  Examples:
      | link   |                                                       
      | https://ship.lionnix.net/sign-up|                      

    
  @prod
  Examples: 
      | link   |                                                                
      | https://ship.lionbay.express/sign-up  |    


Scenario: Đăng ký thành công
  Given Go to page <link>
  When Ten tai khoan = m sau tram
  And Quy mo = Dưới 150 đơn hàng / tháng
  And Sdt
  And email
  And Set password = 123455
  And Click button signup
  Then kiemtra = Yêu cầu của bạn đã được gửi va Cảm ơn bạn đã sử dụng dịch vụ của Lionbay. Chúng tôi sẽ sớm liên hệ với bạn để thiết lập tài khoản.
  @dev
  Examples:
      | link   |                                                       
      | https://ship.lionnix.net/sign-up|                      

    
  @prod
  Examples: 
      | link   |                                                                
      | https://ship.lionbay.express/sign-up  |
