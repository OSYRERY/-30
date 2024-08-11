from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_show_all_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('student25@mail.ru')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('12345')

   # Настраиваем неявные ожидания:
   pytest.driver.implicitly_wait(10)

   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

   # Ищем на странице все фотографии, имена, породу (вид) и возраст питомцев:
   images = pytest.driver.find_elements_by_xpath('//img[@class="card-img-top"]')
   names = pytest.driver.find_elements_by_xpath('//h5[@class="card-title"]')
   descriptions = pytest.driver.find_elements_by_xpath('//p[@class="card-text"]')

   # Проверяем, что на странице есть фотографии питомцев, имена, порода (вид) и возраст питомцев не пустые строки:
   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0


def test_show_my_pets():
   # Вводим email, пароль, открываем главную страницу сайта
   pytest.driver.find_element_by_id('email').send_keys('student25@mail.ru')
   pytest.driver.find_element_by_id('pass').send_keys('12345')
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

   #Настраиваем переменную явного ожидания:
   wait = WebDriverWait(pytest.driver, 5)

   # Проверяем, что мы оказались на главной странице сайта.
   # Ожидаем в течение 5с, что на странице есть тег h1 с текстом "PetFriends"
   assert wait.until(EC.text_to_be_present_in_element((By.TAG_NAME,'h1'), "PetFriends"))

   # Открываем страницу /my_pets.
   pytest.driver.find_element_by_css_selector('a[href="/my_pets"]').click()

   # Проверяем, что мы оказались на  странице пользователя.
   # Ожидаем в течение 5с, что на странице есть тег h2 с текстом "All" -именем пользователя
   assert wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), "All"))

   # Ищем в теле таблицы все строки с полными данными питомцев (имя, порода, возраст, "х" удаления питомца):
   css_locator = 'tbody>tr'
   data_my_pets = pytest.driver.find_elements_by_css_selector(css_locator)

   # Ожидаем, что данные всех питомцев, найденных локатором css_locator = 'tbody>tr', видны на странице:
   for i in range(len(data_my_pets)):
      assert wait.until(EC.visibility_of(data_my_pets[i]))

   # Ищем в теле таблицы все фотографии питомцев и ожидаем, что все загруженные фото, видны на странице:
   image_my_pets = pytest.driver.find_elements_by_css_selector('img[style="max-width: 100px; max-height: 100px;"]')
   for i in range(len(image_my_pets)):
      if image_my_pets[i].get_attribute('src') != '':
         assert wait.until(EC.visibility_of(image_my_pets[i]))

   # Ищем в теле таблицы все имена питомцев и ожидаем увидеть их на странице:
   name_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td[1]')
   for i in range(len(name_my_pets)):
      assert wait.until(EC.visibility_of(name_my_pets[i]))

   # Ищем в теле таблицы все породы питомцев и ожидаем увидеть их на странице:
   type_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td[2]')
   for i in range(len(type_my_pets)):
      assert wait.until(EC.visibility_of(type_my_pets[i]))

   # Ищем в теле таблицы все данные возраста питомцев и ожидаем увидеть их на странице:
   age_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td[3]')