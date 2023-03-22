import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures('get_webdriver')
class TestRegisterPage:

    def test_check_register_page(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        register = self.driver.find_element(By.TAG_NAME, 'h1')
        assert register.text == 'Регистрация'

    def test_register_user_by_email(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="firstName"]').send_keys('Ильяс')
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]').send_keys('Бадретдинов')
        self.driver.find_element(By.ID, 'address').send_keys('ilyasbadrik@yandex.ru')
        self.driver.find_element(By.ID, 'password').send_keys('Testpass123')
        self.driver.find_element(By.ID, 'password-confirm').send_keys('Testpass123')
        self.driver.find_element(By.CSS_SELECTOR, 'button[name="register"]').click()
        code_page = self.driver.find_element(By.TAG_NAME, 'h1')
        assert code_page.text == 'Подтверждение email'

    def test_register_user_by_phone(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="firstName"]').send_keys('Ильяс')
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]').send_keys('Бадретдинов')
        self.driver.find_element(By.ID, 'address').send_keys('89********')
        self.driver.find_element(By.ID, 'password').send_keys('Testpass123')
        self.driver.find_element(By.ID, 'password-confirm').send_keys('Testpass123')
        self.driver.find_element(By.CSS_SELECTOR, 'button[name="register"]').click()
        code_page = self.driver.find_element(By.TAG_NAME, 'h1')
        assert code_page.text == 'Подтверждение телефона'

    def test_name_field(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        name_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='firstName']~span")
        assert name_field.text == 'Имя'

    def test_lastname_field(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        last_name_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='lastName']~span")
        assert last_name_field.text == 'Фамилия'

    def test_region_field(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        region = self.driver.find_element(By.CLASS_NAME, 'rt-input__placeholder--top')
        assert region.text == 'Регион'

    def test_email_phone_field(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        email_phone_field = self.driver.find_element(By.CSS_SELECTOR, 'input[id="address"]~span')
        assert email_phone_field.text == 'E-mail или мобильный телефон'

    def test_password_field(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        password_field = self.driver.find_element(By.CSS_SELECTOR, 'input[id="password"]~span')
        assert password_field.text == 'Пароль'

    def test_password_confirm_field(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        password_confirm_field = self.driver.find_element(By.CSS_SELECTOR, 'input[id="password-confirm"]~span')
        assert password_confirm_field.text == 'Подтверждение пароля'

    def test_button_continue(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        continue_button = self.driver.find_element(By.CSS_SELECTOR, 'button[name="register"]')
        assert continue_button.text == 'Продолжить'

    def test_field_name_two_symbols(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='firstName']").send_keys('Ян')
        self.driver.find_element(By.CSS_SELECTOR, "input[name='lastName']").click()
        with pytest.raises(NoSuchElementException):
            self.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')

    def test_field_name_one_symbol(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='firstName']").send_keys('Я')
        self.driver.find_element(By.CSS_SELECTOR, "input[name='lastName']").click()
        assert self.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')

    def test_field_name_thirty_symbols(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='firstName']").send_keys('Здесьнаходитсятридцатьсимволов')
        self.driver.find_element(By.CSS_SELECTOR, "input[name='lastName']").click()
        with pytest.raises(NoSuchElementException):
            self.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')

    def test_field_name_twenty_nine_symbols(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='firstName']").send_keys('Сейчас-двадцатьдевятьсимволов')
        self.driver.find_element(By.CSS_SELECTOR, "input[name='lastName']").click()
        with pytest.raises(NoSuchElementException):
            self.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')

    def test_field_name_thirty_one_symbols(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='firstName']").send_keys('Атеперьздесь-тридцатьодинсимвол')
        self.driver.find_element(By.CSS_SELECTOR, "input[name='lastName']").click()
        assert self.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')

    def test_field_last_name_two_symbols(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='lastName']").send_keys('Ус')
        self.driver.find_element(By.CSS_SELECTOR, "input[name='firstName']").click()
        with pytest.raises(NoSuchElementException):
            self.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')

    def test_field_last_name_one_symbol(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='lastName']").send_keys('Я')
        self.driver.find_element(By.CSS_SELECTOR, "input[name='firstName']").click()
        assert self.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')

    def test_field_last_name_twenty_nine_symbols(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='lastName']").send_keys('Сейчас-двадцатьдевятьсимволов')
        self.driver.find_element(By.CSS_SELECTOR, "input[name='firstName']").click()
        with pytest.raises(NoSuchElementException):
            self.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')

    def test_field_last_name_thirty_one_symbols(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='lastName']").send_keys(
            'Атеперьздесь-тридцатьодинсимвол')
        self.driver.find_element(By.CSS_SELECTOR, "input[name='firstName']").click()
        assert self.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')

    def test_field_name_english_symbols(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='firstName']").send_keys('John')
        self.driver.find_element(By.CSS_SELECTOR, "input[name='lastName']").click()
        assert self.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')

    def test_field_last_name_english_symbols(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='lastName']").send_keys('Lock')
        self.driver.find_element(By.CSS_SELECTOR, "input[name='firstName']").click()
        assert self.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')

    def test_register_user_without_email_field(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="firstName"]').send_keys('Ильяс')
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]').send_keys('Бадретдинов')
        self.driver.find_element(By.ID, 'password').send_keys('Testpass123')
        self.driver.find_element(By.ID, 'password-confirm').send_keys('Testpass123')
        self.driver.find_element(By.CSS_SELECTOR, 'button[name="register"]').click()
        assert self.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')

    def test_password_field_seven_symbols(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[id="password"]').send_keys('Pass123')
        self.driver.find_element(By.ID, 'password-confirm').click()
        assert self.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')

    def test_incorrect_password_field(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-register'))).click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[id="password"]').send_keys('Pass1234')
        self.driver.find_element(By.ID, 'password-confirm').send_keys('1234PASS')
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="firstName"]').click()
        assert self.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error')
