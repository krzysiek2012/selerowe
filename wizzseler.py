from selenium import webdriver
import time
import unittest

class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        """
        Warunki wstepne
        """
        #przegladarka wlaczona
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl#/")

    def tearDown(self):
        """
        sprzatanie po tescie
        """
        self.driver.quit()


    def testWrongemail(self):

        """
        TC = 01: niekompletny email, brak '@'
        """
        pass

        sleep(5)

if __name__=='__main__':
    unittest.main(verbosity=2)
