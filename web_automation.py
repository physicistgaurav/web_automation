# Chromium ma

# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://youtube.com')
#
# searchbox = driver.find_element_by_xpath('//*[@id="search"]')
# searchbox.send_keys('Gaurav Rijal')
#
# searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
# searchButton.click()




#firefox

# from  selenium import webdriver
#
# driver = webdriver.Firefox()
# driver.get('https://youtube.com')
#
# searchbox = driver.find_element_by_xpath('//*[@id="search"]')
# searchbox.send_keys('Gaurav Rijal')
#
# searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
# searchButton.click()



# #facebooklogin

# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://www.facebook.com/')
#
# search_user = driver.find_element_by_xpath('//*[@id="email"]')
# search_user.send_keys('physicistgaurav')
#
# search_pswd = driver.find_element_by_xpath('//*[@id="pass"]')
# search_pswd.send_keys('hello')
#
#
# search_button = driver.find_element_by_name("login")
# search_button.click()

# #Meroshare

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get('https://meroshare.cdsc.com.np/#/login')
#
#
# # search_dp_button= driver.find_element_by_xpath('//*[@id="select2-uumj-container"]')
# # search_dp_button.click()
# # search_dp_button.send_keys('11100')
#
#
#
# search_dp_button= driver.find_element_by_name('username')
# search_dp_button.send_keys('00482651')
#
# search_dp_button= driver.find_element_by_name('password')
# search_dp_button.send_keys('lizardking@27')
#
#
#
# # search_dp_button= driver.find_element_by_class_name('select2-selection__rendered')
# # search_dp_button.click()
# # search_dp_button=driver.find_element_by_class_name('select2-search__field')
# # search_dp_button.send_keys('11100')
#
# search_dp_button= driver.find_element_by_class_name('select2-selection__rendered')
# search_dp_button.click()
# # search_dp_button=driver.find_element_by_class_name('select2-search__field')
#
#
# sel=Select(driver.find_element_by_class_name('select2-hidden-accessible'))
# # search_dp_button.send_keys('11100')
#
#
# sel.select_by_visible_text("BANK OF KATHMANDU LIMITED (11100)")
#
# search_dp_button= driver.find_element_by_class_name('select2-selection__rendered')
# search_dp_button.click()
#
#
# search_dp_button= driver.find_element_by_css_selector('.btn')
# search_dp_button.click()




# #Send automatic message

