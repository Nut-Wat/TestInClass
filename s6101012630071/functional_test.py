from django.test import LiveServerTestCase
from selenium import webdriver
import unittest
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class test_can_calculater (unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_calculater(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Calculater', self.browser.title)  

        self.fail('finist the test !!')

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  