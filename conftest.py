import pytest
from selenium import webdriver


@pytest.fixture
def get_webdriver(request):
    driver = webdriver.Chrome('C/Users/ilyas/chromedriver/chromedriver.exe')
    driver.get('https://b2c.passport.rt.ru')
    request.cls.driver = driver
    yield driver
    driver.quit()
