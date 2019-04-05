from selenium import webdriver

import unittest

class AutoTest(unittest.TestCase):

    def test_visit_page(self):

        #Navigate to Home Page
        driver = webdriver.Chrome(executable_path='/Applications/chromedriver')
        driver.get("https://www.weightwatchers.com/us/")
        self.assertEqual(driver.title, 'WW (Weight Watchers): Weight Loss & Wellness Help')
        the_text = driver.find_element_by_css_selector(".masthead-homepage__headline.typog-headline2").text
        self.assertEqual(the_text, "Join for free + Lose 10 lbs on us")

        #Navigate to Find a Studio
        driver.find_element_by_class_name("find-a-meeting").click()
        studio_text = driver.find_element_by_css_selector(".meeting-finder__header-headline-title.spice-translated")\
            .text
        self.assertEqual("Find a Studio", studio_text)

        #Find location 10011
        inputElement = driver.find_element_by_tag_name("input")
        inputElement.send_keys('10011')
        driver.find_element_by_css_selector('.input-item.input-group.arrow-btn')\
            .find_element_by_tag_name('button').click()

        print(driver.find_element_by_css_selector('.location__name').text)
        print(driver.find_element_by_css_selector('.location__distance').text)
        element = driver.find_element_by_css_selector('.meeting-location__top')
        element.find_element_by_tag_name('a').click()