from django.test import LiveServerTestCase
from selenium import webdriver      #(1)
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
MAX_WAIT=10
import time
import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser=webdriver.Firefox()#(1)
        
    def tearDown(self):
        self.browser.quit()#(2)
        
    def wait_for_row_in_list_table(self,row_text):
        start_time=time.time()
        while True:
            try:
                table=self.browser.find_element_by_id('id_list_table')
                rows=table.find_elements_by_tag_name('tr')
                self.assertIn(row_text,[row.text for row in rows])
                return
            except(AssertionError,WebDriverException)as e:
                if time.time()-start_time>MAX_WAIT:
                    raise e
                time.sleep(0.5)
            
        
        
    #def test_can_start_a_list_and_retrieve_it_later(self):
    def test_can_start_a_list_for_one_user(self):
        #Edith has heard about a cool new online to-do app. She goes
        #to check out its homepage
        #self.browser.get('http://localhost:8000')#(3)
        self.browser.get(self.live_server_url)#(3)
        
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
        #time.sleep(1)
        '''table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        #self.assertTrue(
          #  any(row.text=='1: Buy peacock features' for row in rows),
          #  f"New to-do item did not appear in table. Contents were:\n{table.text}"
          #  )'''
        #self.assertIn('1: Buy peacock features',[row.text for row in rows])
        self.wait_for_row_in_list_table('1: Buy peacock features')

        #There is still a text boxx inviting her to add another item. She
        #enters :Use peacock features to make a fly:(Edith is very methodical)
        inputbox=self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock features to make a fly')
        inputbox.send_keys(Keys.ENTER)
        #time.sleep(1)
        
        #The page updates again, and now shows both items on her list
        '''table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock features',[row.text for row in rows])
        self.assertIn(
            '2: Use peacock features to make a fly',
            [row.text for row in rows]
            )'''
        self.wait_for_row_in_list_table('1: Buy peacock features')
        self.wait_for_row_in_list_table('2: Use peacock features to make a fly')
        
        #Edith wonders whether the site will remermber her list.Then she sees
        #that the site hae generated a unique URL for her -- there is some
        #exxplanatary text to that effect.
        #self.fail('Finish the test!' )#(5)
        
        #Satisfied,she goes back to sleep.
        
    def test_multiple_users_can_start_lists_at_different_urls(self):
        #Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox=self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock features')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock features')
        
        #She notices that her list has a unique URL
        edith_list_url=self.browser.current_url
        self.assertRegex(edith_list_url,'/lists/.+')
        
        #Now a new user,Francis. comes along to the site.
        
        ##We use a new browser session to make sure that no information
        ##of Edith`s is coming through from cookies etc
        self.browser.quit()
        self.browser=webdriver.Firefox()
        
        #Francis visits the home page. There is no sign of Edith`s list
        self.browser.get(self.live_server_url)
        page_text=self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock features',page_text)
        self.assertNotIn('make a fly',page_text)
        
        #Francis stars a new list by entering a new item. He
        #is less interesting than Edith...
        inputbox=self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        
        #Francis gets his own unique URL
        francis_list_url=self.browser.current_url
        self.assertRegex(francis_list_url,'/lists/.+')
        self.assertNotEqual(francis_list_url,edith_list_url)
        
        #Again,there is no trace of Edith's list
        page_text=self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock features',page_text)
        self.assertIn('Buy milk',page_text)
        
        #Satisfied ,they both go back to sleep
        
#if __name__ == '__main__':#(6)
  #  unittest.main(warnings='ignore')#(7)



#browser=webdriver.Firefox()         #(2)

#assert 'Django' in browser.title
#assert 'To-Do' in browser.title,"Browser title was" + browser.title     #(4)











#She visits that URL - her to-do list is still there.



#browser.quit()
