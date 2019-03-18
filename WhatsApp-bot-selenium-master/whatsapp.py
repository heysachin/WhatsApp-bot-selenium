from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class whats:
    def __init__(self,sleeptime):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('https://web.whatsapp.com')
        time.sleep(sleeptime)

    def send_message(self,reciver,message):
        search=self.driver.find_element_by_class_name('jN-F5')
        search.send_keys(reciver + Keys.ENTER)
        message_box=self.driver.find_element_by_class_name('_2S1VP')
        message_box.send_keys(message + Keys.ENTER)
        #self.driver.save_screenshot('{0}.png'.format(time.time()))

    def quit_browser(self):
        self.driver.quit()

whats=whats(6)

user = input("Username?: ")
n = int(input("Count?: "))
for i in range(n):
     whats.send_message(user,'Automated message')
