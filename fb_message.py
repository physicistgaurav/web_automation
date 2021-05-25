

msg_driver = webdriver.Firefox()
msg_driver.get('https://www.facebook.com/')
msg_driver.maximize_window()

email_input=msg_driver.find_element_by_id("email")
password_input=msg_driver.find_element_by_id("pass")
login_button = msg_driver.find_element_by_name("login")

email ="your email"
password = "your password"

email_input.send_keys(email)
password_input.send_keys(password)
login_button.click()



msg_button = msg_driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[2]/span/div/div[1]")
msg_button.click()


pyautogui.moveTo(1853,180)
pyautogui.click()
pyautogui.click()
pyautogui.click()
pyautogui.moveTo(1750,700)
time(3)
pyautogui.click()
pyautogui.write("Deepesh")
pyautogui.write("Deepesh")
pyautogui.click()
pyautogui.write("deepesh")
