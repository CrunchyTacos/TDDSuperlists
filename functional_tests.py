from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(5)
	
	def tearDown(self):
		self.browser.quit()
		
	def test_can_start_a_list_and_retrieve_it_later(self):
		
#go to the homepage
		self.browser.get('http://localhost:8000')
#put in a title and header mentioning to do lists
		self.assertIn( 'To-Do', self.browser.title)
		self.fail('Finish the test!')
		

#invite to enter an item
#enter an item
#when enter is pushed, page updates showing the list
#still a text box for another entry
#do another entry
#page updates after enter
#site generates a unique url to save list, explains that
#url still has the list
if __name__ == '__main__':
	unittest.main(warnings='ignore')
