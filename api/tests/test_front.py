import unittest
from unittest.mock import patch
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestFront(unittest.TestCase):

  def setUp(self):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enable headless mode
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("http://localhost:5173/")

  def test_title_exists(self):
    title = self.driver.find_element(by=By.CSS_SELECTOR, value=".title")
    value = title.text
    self.assertEqual(value, "PYassGen")

  def test_generate_button_exists(self):
    button = self.driver.find_element(by=By.CSS_SELECTOR, value=".button")
    value = button.text
    self.assertEqual(value, "Generate")
        
  def test_options_exist(self):
    expected_values = ["May include numbers", "May include symbols", "Must send the password hash", "Must send a salted hash"]

    options = self.driver.find_elements(by=By.CSS_SELECTOR, value=".option")
    for option in options:
      option_text = option.text
      self.assertTrue(option_text in expected_values, f"Option text '{option_text}' not in expected values")

  def test_checkboxes_are_clickable(self):
    checkboxes = self.driver.find_elements(by=By.CSS_SELECTOR, value="checkbox")
    for checkbox in checkboxes:
      checkbox.click()
      self.assertTrue(checkbox.is_selected(), f"'{checkbox}' is not clickable")

  def test_password_title_exists(self):
    password_title_element = self.driver.find_element(by=By.CSS_SELECTOR, value=".password-title")
    password_title = password_title_element.text
    self.assertEqual(password_title, "Password length")

  def test_input_length_number(self):
    input_number_element = self.driver.find_element(by=By.CSS_SELECTOR, value=".input-number")
    input_number_element.send_keys("2")
    input_number = input_number_element.get_attribute("value")
    self.assertEqual(input_number, "12")

  def test_input_length_letter(self):
    input_number_element = self.driver.find_element(by=By.CSS_SELECTOR, value=".input-number")
    input_number_element.send_keys("a")
    input_number = input_number_element.get_attribute("value")
    self.assertEqual(input_number, "1")

  def tearDown(self):
    self.driver.quit()

if __name__ == '__main__':
    unittest.main()
