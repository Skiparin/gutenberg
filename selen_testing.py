from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import unittest


class selen_testing(unittest.TestCase):

	def setUp(self):
		self.options = Options()
		self.options.add_argument("--headless")

		self.driver = webdriver.Firefox(options=self.options, executable_path="geckodriver")
		self.driver.get("http://46.101.61.244:5000/")

	def tearDown(self):
		self.driver.close()

	def testFindCity(self):
		print("testing testFindCity")
		self.elem = self.driver.find_element_by_name("city")
		self.elem.clear()
		self.elem.send_keys("Odense")
		self.driver.find_element_by_xpath("//input[@value='Find titles']").click()

		#Asserts to get the first book title
		self.result = self.driver.find_element_by_xpath('//tbody/tr[2]/td[1]').text
		self.expected = "A Danish Parsonage"
		self.assertEqual(self.result, self.expected)

		#Asserts to get the first author
		self.result1 = self.driver.find_element_by_xpath('//tbody/tr[2]/td[2]').text
		self.expected1 = "['John Fulford Vicary']"
		self.assertEqual(self.result1, self.expected1)

		#Asserts to get the twelfth book title
		self.result2 = self.driver.find_element_by_xpath('//tbody/tr[13]/td[1]').text
		self.expected2 = "Denmark"
		self.assertEqual(self.result2, self.expected2)

		#Asserts to get the twelfth author
		self.result3 = self.driver.find_element_by_xpath('//tbody/tr[13]/td[2]').text
		self.expected3 = "['M. Pearson Thomson']"
		self.assertEqual(self.result3, self.expected3)

		#Asserts to get the last book title
		self.result4 = self.driver.find_element_by_xpath('//tbody/tr[last()]/td[1]').text
		self.expected4 = "What the Moon Saw: and Other Tales"
		self.assertEqual(self.result4, self.expected4)

		#Asserts to get the last author
		self.result5 = self.driver.find_element_by_xpath('//tbody/tr[last()]/td[2]').text
		self.expected5 = "['Hans Christian Andersen']"
		self.assertEqual(self.result5, self.expected5)

	"""
	def testPlotCities(self):
		print("testing testPlotCities")
		self.elem = self.driver.find_element_by_name("title")
		self.elem.clear()
		self.elem.send_keys("A Danish Parsonage")
		self.driver.find_element_by_xpath("//input[@value='Plot cities']").click()

		self.result = self.driver.find_element_by_xpath("//div[@id='view-side']")
		print(self.result)
	"""

	def testPlotTitlesAndCities(self):
		print("testing testPlotTitlesAndCities")
		self.elem = self.driver.find_element_by_name("author")
		self.elem.clear()
		self.elem.send_keys("Hans Christian Andersen")
		self.driver.find_element_by_xpath("//input[@value='Plot titles and cities']").click()

		#Asserts to get the first book title
		self.result = self.driver.find_element_by_xpath('//tbody/tr[2]').text
		self.expected = "A Christmas Greeting"
		self.assertEqual(self.result, self.expected)

		#Asserts to get the last book title
		self.result = self.driver.find_element_by_xpath('//tbody/tr[last()]').text
		self.expected = "Wonderful Stories for Children"
		self.assertEqual(self.result, self.expected)

	def testErrorHandling(self):
		print("testing testErrorHandling")
		self.elem = self.driver.find_element_by_name("city")
		self.elem.clear()
		self.driver.find_element_by_xpath("//input[@value='Find titles']").click()
		self.result = self.driver.find_element_by_class_name("alert").text
		self.expected = "Please enter a city name"
		self.assertEqual(self.result, self.expected)

if __name__ == '__main__':
    unittest.main()