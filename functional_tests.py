from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Theo wants to create a new To-Do lists; so, he visits
        self.browser.get('http://localhost:8000')
        # Theo notices page title and header mention "To-Do" lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # Theo is invited to add a item straight-away
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # Theo types "Buy peacock feathers" into a text box
        input_box.send_keys('Buy peacock feathers')
        # When Theo hits enter the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        # There's still a textbox that invites Theo to enter
        # another item in the to-do list
        # Theo enters "Use peacock feathers to make a fly"
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Use peacock feather to make a fly')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        # Theo notices that the page updates and he
        # sees both the items on the list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly',
                      [row.text for row in rows])

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
