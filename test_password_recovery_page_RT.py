import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures('get_webdriver')
class TestPasswordRecoveryPage:

    def test_password_recovery_page(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        self.driver.find_element(By.ID, 'forgot_password').click()
        assert self.driver.find_element(By.TAG_NAME, 'h1').text == 'Восстановление пароля'

    def test_tab_number(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        self.driver.find_element(By.ID, 'forgot_password').click()
        assert self.driver.find_element(By.ID, 't-btn-tab-phone').text == 'Номер'

    def test_tab_mail(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        self.driver.find_element(By.ID, 'forgot_password').click()
        assert self.driver.find_element(By.ID, 't-btn-tab-mail').text == 'Почта'

    def test_tab_login(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        self.driver.find_element(By.ID, 'forgot_password').click()
        assert self.driver.find_element(By.ID, 't-btn-tab-login').text == 'Логин'

    def test_tab_ls(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        self.driver.find_element(By.ID, 'forgot_password').click()
        assert self.driver.find_element(By.ID, 't-btn-tab-ls').text == 'Лицевой счёт'

    def test_phone_field(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        self.driver.find_element(By.ID, 'forgot_password').click()
        self.driver.find_element(By.ID, 't-btn-tab-phone').click()
        assert self.driver.find_element(By.CSS_SELECTOR, 'input[id="username"]~span').text == 'Мобильный телефон'

    def test_mail_field(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        self.driver.find_element(By.ID, 'forgot_password').click()
        self.driver.find_element(By.ID, 't-btn-tab-mail').click()
        assert self.driver.find_element(By.CSS_SELECTOR, 'input[id="username"]~span').text == 'Электронная почта'

    def test_login_field(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        self.driver.find_element(By.ID, 'forgot_password').click()
        self.driver.find_element(By.ID, 't-btn-tab-login').click()
        assert self.driver.find_element(By.CSS_SELECTOR, 'input[id="username"]~span').text == 'Логин'

    def test_ls_field(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        self.driver.find_element(By.ID, 'forgot_password').click()
        self.driver.find_element(By.ID, 't-btn-tab-ls').click()
        assert self.driver.find_element(By.CSS_SELECTOR, 'input[id="username"]~span').text == 'Лицевой счёт'

    def test_captcha(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        self.driver.find_element(By.ID, 'forgot_password').click()
        self.driver.find_element(By.ID, 't-btn-tab-ls').click()
        assert self.driver.find_element(By.ID, 'captcha')

    def test_continue_button(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        self.driver.find_element(By.ID, 'forgot_password').click()
        self.driver.find_element(By.ID, 't-btn-tab-ls').click()
        assert self.driver.find_element(By.ID, 'reset').text == 'Далее'

    def test_back_button(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'kc-login')))
        self.driver.find_element(By.ID, 'forgot_password').click()
        self.driver.find_element(By.ID, 't-btn-tab-ls').click()
        assert self.driver.find_element(By.ID, 'reset-back').text == 'Вернуться'
