from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import unittest


class selen_testing(unittest.TestCase):

	#Settin up the driver in headless mode
	@classmethod
	def setUpClass(cls):
		options = Options()
		options.add_argument("--headless")

		cls.driver = webdriver.Firefox(options=options, executable_path="geckodriver")
		cls.driver.get("http://46.101.61.244:5000/")

	#This returns us to the start page every time a test finished.
	def tearDown(self):
		self.driver.get("http://46.101.61.244:5000/")

	#Closing the driver when we are finnished testing.
	@classmethod
	def tearDownClass(cls):
		cls.driver.close()

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
		self.elem.send_keys("Denmark")
		self.driver.find_element_by_xpath("//input[@value='Plot cities']").click()

		result = self.driver.find_element_by_xpath("//div[@class='gmnoprint']").location
		print(result)
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

	def testCoordinates(self):
		print("testing testCoodinates")
		self.elem = self.driver.find_element_by_name("x")
		self.elem.clear()
		self.elem.send_keys("50")
		self.elem = self.driver.find_element_by_name("y")
		self.elem.clear()
		self.elem.send_keys("20")
		self.elem = self.driver.find_element_by_name("r")
		self.elem.clear()
		self.elem.send_keys("0.5")
		self.driver.find_element_by_xpath("//input[@value='Find titles for coordinates']").click()

		#Asserts book title from first table row
		self.result = self.driver.find_element_by_xpath("//tbody/tr[2]/td").text
		self.expected = "U.S. Copyright Renewals, 1956 January - June"
		self.assertEqual(self.result, self.expected)

		#Asserts book title from the 40th table row
		self.result1 = self.driver.find_element_by_xpath("//tbody/tr[40]/td").text
		self.expected1 = "Sweden"
		self.assertEqual(self.result1, self.expected1)

		#Asserts book title from last table row
		self.result2 = self.driver.find_element_by_xpath("//tbody/tr[last()]/td").text
		self.expected2 = "The Story of the Great War, Volume II (of VIII) History of the European War from Official Sources"
		self.assertEqual(self.result2, self.expected2)

	#Asserts a message response when we dont type anthing in the input field
	def testCityEmptyInput(self):
		print("testing testCityEmptyInput")
		self.elem = self.driver.find_element_by_name("city")
		self.elem.clear()
		self.driver.find_element_by_xpath("//input[@value='Find titles']").click()
		self.result = self.driver.find_element_by_class_name("alert").text
		self.expected = "Please enter a city name"
		self.assertEqual(self.result, self.expected)

	#Asserts a message response when we cant find a book mentioning the given city name
	def testCityInvalidInput1(self):
		print("testing testInvalidInput1")
		self.elem = self.driver.find_element_by_name("city")
		self.elem.clear()
		self.elem.send_keys("This is not a city")
		self.driver.find_element_by_xpath("//input[@value='Find titles']").click()
		self.result = self.driver.find_element_by_class_name("alert").text
		self.expected = "Can't find titles mentioning that city"
		self.assertEqual(self.result, self.expected)

	#Asserts a message response when we cant find a book mentioning the given city name
	def testCityInvalidInput1(self):
		print("testing testInvalidInput2")
		self.elem = self.driver.find_element_by_name("city")
		self.elem.clear()
		self.elem.send_keys("123456789!#%&/()=")
		self.driver.find_element_by_xpath("//input[@value='Find titles']").click()
		self.result = self.driver.find_element_by_class_name("alert").text
		self.expected = "Can't find titles mentioning that city"
		self.assertEqual(self.result, self.expected)

	def testTitleEmptyInput(self):
		print("testing testTitleEmptyInput")
		self.elem = self.driver.find_element_by_name("title")
		self.elem.clear()
		self.driver.find_element_by_xpath("//input[@value='Plot cities']").click()
		self.result = self.driver.find_element_by_class_name("alert").text
		self.expected = "Please enter a book title"
		self.assertEqual(self.result, self.expected)

	#Asserts a message response when we cant find the cities mentioned in that book title
	def testTitleInvalidInput1(self):
		print("testing testTitleInvalidInput1")
		self.elem = self.driver.find_element_by_name("title")
		self.elem.clear()
		self.elem.send_keys("This is not a city")
		self.driver.find_element_by_xpath("//input[@value='Plot cities']").click()
		self.result = self.driver.find_element_by_class_name("alert").text
		self.expected = "Can't find a book title with that name"
		self.assertEqual(self.result, self.expected)

		#Asserts a message response when we cant find the cities mentioned in that book title
	def testTitleInvalidInput1(self):
		print("testing testTitleInvalidInput1")
		self.elem = self.driver.find_element_by_name("title")
		self.elem.clear()
		self.elem.send_keys("123456789!#%&/()=")
		self.driver.find_element_by_xpath("//input[@value='Plot cities']").click()
		self.result = self.driver.find_element_by_class_name("alert").text
		self.expected = "Can't find a book title with that name"
		self.assertEqual(self.result, self.expected)

	def testAuthorEmptyInput(self):
		print("testing testAuthorEmptyInput")
		self.elem = self.driver.find_element_by_name("author")
		self.elem.clear()
		self.driver.find_element_by_xpath("//input[@value='Plot titles and cities']").click()
		self.result = self.driver.find_element_by_class_name("alert").text
		self.expected = "Please enter an author name"
		self.assertEqual(self.result, self.expected)

	def testRadiusEmptyInput(self):
		print("testing testRadiusEmptyInput")
		self.elem = self.driver.find_element_by_name("x")
		self.elem.clear()
		self.elem = self.driver.find_element_by_name("y")
		self.elem.clear()
		self.elem = self.driver.find_element_by_name("r")
		self.elem.clear()
		self.driver.find_element_by_xpath("//input[@value='Find titles for coordinates']").click()
		self.result = self.driver.find_element_by_class_name("alert").text
		self.expected = "Please enter x and y coordinates with a radius"
		self.assertEqual(self.result, self.expected)

if __name__ == '__main__':
    unittest.main()
