from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('/Users/akshajraut/Downloads/chromedriver')
driver.get("https://web.whatsapp.com/")
wait = input('Press Enter after scanning QR Code: ')
name=["Enter names here"]


msg = """Enter message here"""
count = len(name)

n = 0
for i in range(count):
    search = driver.find_element_by_class_name('_3FRCZ')
    search.send_keys(name[n])
    sleep(1)
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name[n]))
    user.click()
    n += 1

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_1U1xa')
    #sleep(1)
    button.click()