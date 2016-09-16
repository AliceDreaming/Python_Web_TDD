from selenium import webdriver
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
        self.assertIn('TO-DO', self.browser.title)
        self.fail('Finish the test')

        # Add a new to-do item 'Buy peacock feathers'

        # The page refeshed with a new item '1. Buy peacock feathers'

        #Add another to-do item 'Use peacock feathers to make a fly'

        # The page refreshed with 2 to-do items

        # Check if the to-do list is stored in the website by access the URL for the to-do list
        # check the two to-do items is still there
        # Quit

if __name__ == '__main__':
    unittest.main()