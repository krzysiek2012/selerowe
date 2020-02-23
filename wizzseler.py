from selenium import webdriver
import time
import unittest
#potrzeba te trzy ponizej aby efektywne 'explicity' dzialanie dzialalo
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

firstname='Kokosowe'
lastname='Misoiwe'
gender='male'
country_code = '+48'
phone='000000000'
invalid_email='koko#mysiek.com'
haslo='kiki09867K'
valid_country = "Chiny"

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
        #trzeba poczekac na efektywne zalogowanie, expicit way...
        driver = self.driver
        #tutaj funkcja to tak na prawde krotka,
        find_zaloguj_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        find_zaloguj_btn.click()

        find_rejestruj = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Rejestracja "]'))).click()

        #kliknij_rejestracja=driver.find_element_by_xpath('//button[text()=" Rejestracja "]').click()

        #tutaj uwazaj, bo jak 'send_keys' bylo po kropce w sensie jako przedluzenie tego jednego to w tedy test nie dzialal bo wywalal blad, nie byl wstanie rozpoznac w tym przypadku'wpisz_imie', czy cos takiego, poniewaz musi byc odniesienie do kokretnego elementu wiec nie po kropce, bo tak po kropce to jest jakos ze soba polaczone i nie moze tak byc.
        wpisz_imie=WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.NAME, 'firstName')))
        #wiec rozdzielilem to jako osobna funkcje i w tedy juz przeszlo. pewnie chodzi o to ze to powyzej tworzy konkretna wartosc i w tedy ti wszytko ze soba pasuje i jest gitara.
        wpisz_imie.send_keys(firstname)

        wpisz_nazwisko=WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.NAME, 'lastName'))).send_keys(lastname)
        #lub normalnie po find_element_by_name...

        #uwaga przy klikaniu mezczyzna button bo sie pojawia dymek i zaslania nam ten cholerny button, trzeba to uwzglednic
        if gender == 'male':
            m = driver.find_element_by_xpath('//label[@for="register-gender-male"]')
            #dodatkowy klik badz przy uzyciu javy scrip ale ponoc nie powinno sie tego tak uzywac
            #tutaj uwazaj, sa tuta odniesienia do wpisz imie, nie mozna wczesniej laczyc funkcji, opisalem to na gorze przy 'wpisz_imie', w kazdyn razie uwazaj tutaj
            wpisz_imie.click()
            m.click()
            #driver.execute_script('arguments[0].click()', m)
        else:
            driver.find_element_by_xpath('//label[@for="register-gender-female"]').click()


        wybierz_kraj=driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]')
        wybierz_kraj.click()
        wybierz_kraj = driver.find_element_by_xpath('//input[@name="phone-number-country-code"]')
        wybierz_kraj.send_keys(country_code)
        #mozliwe, ze sa jakies zabezpieczenia przed botami i trzeba zapodac waita, w tedy przejdzie
        country_to_choose = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, '//li[@data-test="PL"]')))

        wpisz_phone=driver.find_element_by_xpath('//input[@name="phoneNumberValidDigits"]').send_keys(phone)

        wpisz_mail=driver.find_element_by_xpath('//input[@name="email"]').send_keys(invalid_email)

        wpisz_passwd=driver.find_element_by_xpath('//input[@name="password"]').send_keys(haslo)

         # 9. Wybierz narodowość
         #tutaj mozna inne metody stosowac, w tym sensie moze sprobuj wiesz, znalec, wpisac, kliknac, cos tam, bo sam nie wiem juz jak to robic..
        country_field = driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
        country_field.click()
        # Wyszukaj kraje
        country_to_choose = driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']")
        # Poszukaj elementow "label" wewnatrz listy "countries"
        countries = country_to_choose.find_elements_by_tag_name("label")
        # Iteruj po kazdym elemencie w liscie "countries"
        for label in countries:
            # Wewnatrz "label" znajdz element "strong"
            option=label.find_element_by_tag_name('strong')
            # Jesli tekst elementu jest taki jak zadany w valid_country
            if option.get_attribute("innerText") == valid_country:
                # Przewin do tego elementu
                option.location_once_scrolled_into_view
                # Kliknij
                option.click()
                # Wyjdz z petli - juz znalazlem i kliknalem
                break


        klepnij=driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]').click()

        driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]').click()

        #lamane prze span bo bledy sa w srodku w sensie wypisane w srodku miedzy klamrami
        bledy = driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')

        # Zapisuję widoczne błędy do listy visible_error_notices
        visible_error_noticed = []
        for error in bledy:
            # Jesli jest widoczny, to dodaj do listy
            #zwraca is_displayed true or false, jak jest widoczny to nie jak tak to tak
            if error.is_displayed():
                visible_error_noticed.append(error)
        # Sprawdzam, czy widoczny jest tylko jeden błąd
        assert len(visible_error_noticed) == 1
        # Sprawdzam treść widocznego błędu
        #get_attribute pobierm sobie tresc tego tekstu i spradzam
        error_text = visible_error_noticed[0].get_attribute("innerText")
        assert error_text == "Nieprawidłowy adres e-mail"

        time.sleep(5)

if __name__=='__main__':
    unittest.main(verbosity=2)
