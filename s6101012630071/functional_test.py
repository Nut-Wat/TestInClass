from django.test import LiveServerTestCase
from selenium import webdriver
import unittest
import time 
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class test_can_calculater (unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def history_check(self,row_text):
        history_list = self.browser.find_element_by_id('history_list')
        rows = self.history_list.find_element_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])

    def test_can_calculater(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Calculater', self.browser.title) 

        number1_box = self.browser.find_element_by_id('num_x')  
        number1_box.send_keys('1')

        op_box = Select(self.browser.find_element_by_id('op'))
        op_box.select_by_visible_text('+')

        number2_box = self.browser.find_element_by_id('num_y')  
        number2_box.send_keys('1')

        calculater_button = self.browser.find_element_by_id('calculater_button')
        calculater_button.send_keys(Keys.ENTER)
        time.sleep(1)

        result = self.browser.find_element_by_tag_name('p1').text
        self.assertIn('2',result)



        self.fail('finist the test !!')

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  