from selenium import webdriver      #(1)
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
        self.fail('Finish the test!' )#(5)
        
if __name__ == '__main__':#(6)
    unittest.main(warnings='ignore')#(7)



#browser=webdriver.Firefox()         #(2)

#assert 'Django' in browser.title
#assert 'To-Do' in browser.title,"Browser title was" + browser.title     #(4)

#She is invited to enter a to-do item straight away

#She types "Buy peacock features" into a text box(Edith`s hobby
#is tying fly-fishing lures)

#when she hits enter, the page updatas, and now the page lists
#"1: Buy peacock features" as am item in a to-do list

#There is still a text boxx inviting her to add another item. She
#enters :Use peacock features to make a fly:(Edith is very methodical)

#The page updates again, and now shows both items on her list

#Edith wonders whether the site will remermber her list.Then she sees
#that the site hae generated a unique URL for her -- there is some
#exxplanatary text to that effect.

#She visits that URL - her to-do list is still there.

#Satisfied,she goes back to sleep.

#browser.quit()
