import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures('get_webdriver')
class TestAuthPage:

    def test_auth_page(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        auth = self.driver.find_element(By.TAG_NAME, 'h1')
        assert auth.text == 'Авторизация'

    def test_tab_number(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        number = self.driver.find_element(By.ID, 't-btn-tab-phone')
        assert number.text == 'Номер'

    def test_tab_mail(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        mail = self.driver.find_element(By.ID, 't-btn-tab-mail')
        assert mail.text == 'Почта'

    def test_tab_login(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        login = self.driver.find_element(By.ID, 't-btn-tab-login')
        assert login.text == 'Логин'

    def test_tab_ls(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        login = self.driver.find_element(By.ID, 't-btn-tab-ls')
        assert login.text == 'Лицевой счёт'

    def test_auth_with_phone(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        self.driver.find_element(By.ID, 't-btn-tab-phone').click()
        self.driver.find_element(By.ID, 'username').send_keys('89090516784')
        self.driver.find_element(By.ID, 'password').send_keys('Ilias0709')
        self.driver.find_element(By.ID, 'kc-login').click()
        assert self.driver.find_element(By.ID, 'logout-btn')

    def test_auth_with_mail(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        self.driver.find_element(By.ID, 't-btn-tab-mail').click()
        self.driver.find_element(By.ID, 'username').send_keys('ilyasbadrik@mail.ru')
        self.driver.find_element(By.ID, 'password').send_keys('Ilias0709')
        self.driver.find_element(By.ID, 'kc-login').click()
        assert self.driver.find_element(By.ID, 'logout-btn')

    def test_auth_phone_invalid_password(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        self.driver.find_element(By.ID, 't-btn-tab-phone').click()
        self.driver.find_element(By.ID, 'username').send_keys('89090516784')
        self.driver.find_element(By.ID, 'password').send_keys('Ilias0')
        self.driver.find_element(By.ID, 'kc-login').click()
        assert self.driver.find_element(By.ID, 'form-error-message')

    def test_auth_mail_invalid_password(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        self.driver.find_element(By.ID, 't-btn-tab-mail').click()
        self.driver.find_element(By.ID, 'username').send_keys('ilyasbadrik@mail.ru')
        self.driver.find_element(By.ID, 'password').send_keys('Ilias0')
        self.driver.find_element(By.ID, 'kc-login').click()
        assert self.driver.find_element(By.ID, 'form-error-message')

    