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
        #po tej funkcji ponizej usuwamy wszystkie sleep'y
        #po kazdym kroku CHYBA czeka max 2s
        #mozesz mozesz dodac linijke ponizej z wartoscia 0 i w tedy tak jak by wylaczasz, to taki workaround
        #dzieki temu nie musimy dawac sleepa ale na koncu mozna sobie dodac aby wiedzie gdzie jestesmy
        self.driver.implicitly_wait(2)

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

        #Wybierz tytule - odnajduje i klika od razu
        driver.find_element_by_id('id_gender1').click()

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
        #to ci pomoze zrozumiec jak to dziala
        print(type(day_of_birth_select))
        #day_of_birth_select=driver.find_element_by_id('days')
        #day_of_birth_select=Select(day_of_birth_select)
        #day_of_birth_select.select_by_value(birthday)
        #magi pajtona, nie wiem juz sam, mozesz sprawdzic w budowie tej klasy
        #bo nie wiem jak inaczej

        month_of_birth_select=Select(driver.find_element_by_id('months'))
        month_of_birth_select.select_by_value(birthmont)

        Select(driver.find_element_by_id('years')).select_by_value(birthyear)
        #to samo jest ponizej a wyzej jest po prostu krotsze
        #year_of_birth_select=Select(driver.find_element_by_id('years'))
        #year_of_birth_select.select_by_value(birthyear)

        #ma inny id dlatego ok w porownaniu do tego pierwszego firstname
        name_address=driver.find_element_by_id('firstname').send_keys(firstname)
        print(name_address)


        sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
    #vervosity- apt help w teminalu, super moc krowy? tak jak by cos bylo wiecej widziec, wypisuje ktory test robi i ze jest ok, jak bym to usunal to nic nie widzialbym co byloby slabe, po prostu dodatkowa informacja, mozna dac wartosc 1, cos sie zmieni
    unittest.main(verbosity=2)
