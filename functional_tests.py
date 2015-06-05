from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	
	def tearDown(self):
		self.browser.quit()
		
	def test_can_start_a_list_and_retrieve_it_later(self):
		
#go to the homepage
		self.browser.get('http://localhost:8000')
#put in a title and header mentioning to do lists
		self.assertIn( 'To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		

#invite to enter an item
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'), 
			'Enter a to-do item')
			
		
#enter an item
		inputbox.send_keys('Buy peacock feather')
		
		
#when enter is pushed, page updates showing the list
		inputbox.send_keys(Keys.ENTER)
		
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows),
			"New to-do item did not appear in table")
#still a text box for another entry
		self.fail('Finish the test')
#do another entry
#page updates after enter
#site generates a unique url to save list, explains that
#url still has the list
if __name__ == '__main__':
	unittest.main(warnings='ignore')
