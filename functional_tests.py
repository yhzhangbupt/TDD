from selenium import webdriver      #(1)
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser=webdriver.Firefox()#(1)
        
    def tearDown(self):
        self.browser.quit()#(2)
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heard about a cool new online to-do app. She goes
        #to check out its homepage
        self.browser.get('http://localhost:8000')#(3)
        
        #she notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.browser.title)#(4)
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        
        #She is invited to enter a to-do item straight away
        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )
        
        #She types "Buy peacock features" into a text box(Edith`s hobby
        #is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock features')
        
        #when she hits enter, the page updatas, and now the page lists
        #"1: Buy peacock features" as am item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text=='1: Buy peacock features' for row in rows)
            )

        #There is still a text boxx inviting her to add another item. She
        #enters :Use peacock features to make a fly:(Edith is very methodical)
        self.fail('Finish the test!' )#(5)
        
if __name__ == '__main__':#(6)
    unittest.main(warnings='ignore')#(7)



#browser=webdriver.Firefox()         #(2)

#assert 'Django' in browser.title
#assert 'To-Do' in browser.title,"Browser title was" + browser.title     #(4)








#The page updates again, and now shows both items on her list

#Edith wonders whether the site will remermber her list.Then she sees
#that the site hae generated a unique URL for her -- there is some
#exxplanatary text to that effect.

#She visits that URL - her to-do list is still there.

#Satisfied,she goes back to sleep.

#browser.quit()
