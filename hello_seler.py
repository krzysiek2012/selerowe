# import bibliotek
from selenium import webdriver
from time import sleep
import unittest


# Tworzymy klase WsbPLcheck dziedziczaca po TestCase
# z modulu unittest

class WsbPLcheck(unittest.TestCase):


    #Warunki wstepne
    #(przygotowanie testu)
        def setUp(self):
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()

    #tutaj wlasciwe testy
        def testWsb(self):
            #tworze skrot driver = self driver i dalej nie trzeba tyle pisac
            driver=self.driver
        #wejdz na strone
            driver.get('http://www.wsb.pl')
        #sprawdz, czy "Bankowe" znajduja sie w tytule strony, funkcja assert sprawza
            self.assertIn('Bankowe', driver.title)
            print(driver.title)

    #sprzatanie po testach
        def tearDown(self):
            self.driver.quit()

    #jesli to glowny plik
        if __name__=='__main__':
        #uruchom metode main, ktora uruchomi testy
            unittest.main(verbosity=2)
