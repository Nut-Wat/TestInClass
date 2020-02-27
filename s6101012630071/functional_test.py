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

    def test_can_calculater_post(self):
        #มี
        self.browser.get('http://localhost:8000/calpost')
        #self.assertIn('Calculater', self.browser.title) 

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

        number1_box = self.browser.find_element_by_id('num_x')  
        number1_box.send_keys('2')

        op_box = Select(self.browser.find_element_by_id('op'))
        op_box.select_by_visible_text('-')

        number2_box = self.browser.find_element_by_id('num_y')  
        number2_box.send_keys('2')

        calculater_button = self.browser.find_element_by_id('calculater_button')
        calculater_button.send_keys(Keys.ENTER)
        time.sleep(1)

        result = self.browser.find_element_by_tag_name('p1').text
        self.assertIn('0',result)

        number1_box = self.browser.find_element_by_id('num_x')  
        number1_box.send_keys('5')

        op_box = Select(self.browser.find_element_by_id('op'))
        op_box.select_by_visible_text('*')

        number2_box = self.browser.find_element_by_id('num_y')  
        number2_box.send_keys('2')

        calculater_button = self.browser.find_element_by_id('calculater_button')
        calculater_button.send_keys(Keys.ENTER)
        time.sleep(1)

        result = self.browser.find_element_by_tag_name('p1').text
        self.assertIn('10',result)

        number1_box = self.browser.find_element_by_id('num_x')  
        number1_box.send_keys('14')

        op_box = Select(self.browser.find_element_by_id('op'))
        op_box.select_by_visible_text('/')

        number2_box = self.browser.find_element_by_id('num_y')  
        number2_box.send_keys('7')

        calculater_button = self.browser.find_element_by_id('calculater_button')
        calculater_button.send_keys(Keys.ENTER)
        time.sleep(1)

        result = self.browser.find_element_by_tag_name('p1').text
        self.assertIn('2',result)



        self.fail('finist the test !!')

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  