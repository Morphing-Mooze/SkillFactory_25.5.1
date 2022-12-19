from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://petfriends.skillfactory.ru")
element = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.ID, "myDynamicElement"))
)

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://petfriends.skillfactory.ru")
myDynamicElement = driver.find_element_by_id("myDynamicElement")


import pytest


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome(executable_path='c:/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')


def test_show_my_pets():
   # driver.implicitly_wait(0.5)
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('morphing-mooze@rambler.ru')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('12345')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"


def testing_all_pets():
   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0


# driver.quit()