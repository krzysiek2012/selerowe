# import bibliotek
from selenium import webdriver
from time import sleep
import unittest

email='misiek@kokos.com'
#klasa o dowolnej nazwie
class APregistration(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')

    def testCorrectRegistration(self):
        driver=self.driver
        #odnajdz sign in
        sign_in=driver.find_element_by_class_name('login')
        #kliknij
        sign_in.click()
        #wpisz adress email
        email.input=driver.find_element_by_id('email_create')
        email.input.send_keys('email')
        #kliknij przycisk 'create an account'
        create_btn=driver.find_element_by_id('SubmitCreate')
        create_btn.click()
        sleep(5)


    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
    unittest.main(verbosity=2)
