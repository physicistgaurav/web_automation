from selenium import webdriver
import pyautogui
import time


msg_driver = webdriver.Firefox()
msg_driver.get('https://www.facebook.com/')

email_input=msg_driver.find_element_by_id("email")
password_input=msg_driver.find_element_by_id("pass")
login_button = msg_driver.find_element_by_name("login")

email ="your email"
password = "your password"

email_input.send_keys(email)
password_input.send_keys(password)
login_button.click()

#status work garxa

status_button = msg_driver.find_element_by_css_selector('div.a5q79mjw:nth-child(1) > span:nth-child(1)')
status_button.click()
pyautogui.moveTo(800,480)
pyautogui.click()
pyautogui.write("Kyun Chauk Gaye na")
pyautogui.write("kyun Chauk Gaye na")
status_button.click()
