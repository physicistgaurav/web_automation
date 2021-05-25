# #facebooklogin

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')

search_user = driver.find_element_by_xpath('//*[@id="email"]')
search_user.send_keys('your email or username')

search_pswd = driver.find_element_by_xpath('//*[@id="pass"]')
search_pswd.send_keys('your password')


search_button = driver.find_element_by_name("login")
search_button.click()
