# import bibliotek
from selenium import webdriver
from time import sleep
import unittest
#importuje to cos ponizek, zeby przy seleccie daty nie trzebabylo tam przepisywac, nie ladnie i zdecydowanie trudniej
#Klasa z duzej litery
from selenium.webdriver.support.ui import Select
email = 'misiek@kokos.com'
fristname = 'Misiowe'
secondname = 'Kokosowe'
invalid_password = 'jakies_haslo'
birthday='1'
birthmont='1'
birthyear='1900'


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
        #to tak na marginesie, 'str' object has no attribute 'input' to znaczy ze po kropce wchodzi do atrybutw w kazdym razie uwarzaj na to, tam jest po prostu nazwa
        email_input=driver.find_element_by_id('email_create')
        email_input.send_keys(email)
        #kliknij przycisk 'create an account'
        create_btn=driver.find_element_by_id('SubmitCreate')
        create_btn.click()
        sleep(2)
        #Wybierz tytule - odnajduje i klika od razu
        driver.find_element_by_id('id_gender1').click()
        sleep(5)
        #Wpisuje imie
        driver.find_element_by_id('customer_firstname').send_keys(fristname)
        #wpisuje nazwisko
        driver.find_element_by_id('customer_lastname').send_keys(secondname)
        #Sprawdzam email
        email_text=driver.find_element_by_id('email').get_attribute('value')
        assert email_text == email
        #wpisz niepoprawne haslo
        driver.find_element_by_id('passwd').send_keys(invalid_password)
        #wybierz date urodzenia
        #tworze obiekt klasy Select - odniesienie na gorze(odnajduje web element)
        day_of_birth_select=Select(driver.find_element_by_id('days'))
        day_of_birth_select.select_by_value(birthday)
        sleep(6)


    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
    unittest.main(verbosity=2)
