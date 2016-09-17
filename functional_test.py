from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class functional_test(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # check the home page title contains "TO-DO"
        self.browser.get(r'http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        input_box = self.browser.find_element_by_id('add_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

        # Add a new to-do item 'Buy peacock feathers'
        input_box.send_keys('Buy peacock feathers')
        input_box.send_keys(Keys.ENTER)

        # The page refeshed with a new item '1. Buy peacock feathers'T
        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(rows.text == '1: Buy peacock feathers')
        )

        #Add another to-do item 'Use peacock feathers to make a fly'

        # The page refreshed with 2 to-do items

        # Check if the to-do list is stored in the website by access the URL for the to-do list
        # check the two to-do items is still there
        # Quit
        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main()