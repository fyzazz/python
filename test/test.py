# coding = utf - 8

from selenium import webdriver
import excel,time,re

class testing():

	def __init__(self,x,xpaths,inputs,driver) :
		self.x = x
		self.xpaths = xpaths
		self.inputs = inputs
		self.driver = driver
	def time(self):
		
		time.sleep(3)
	def setup(self):

		self.driver = webdriver.Chrome()
		driver = self.driver
		driver.maximize_window()
		driver.get('http://bms.hongkedou.com:9001/')
		driver.implicitly_wait(8)
		return self.driver
	def keys(self):
		
		driver = self.driver
		driver.find_element_by_xpath(self.xpaths).clear()
		driver.find_element_by_xpath(self.xpaths).send_keys(str(self.inputs))
		
	def clicks(self):

		driver.find_element_by_xpath(self.xpaths).click()
	
	def assertequals(self) :
	
		result = driver.find_element_by_xpath(self.xpaths).text
		print(result)
		if result == str(self.inputs) :
			print('PASS')
			excel.xlwts().write(self.x,'PASS')
			#excel.xlwts().write(self.x,result)
		else :
			
			#excel.xlwts().write(self.x,'FALL')
			excel.xlwts().write(self.x,result)
			print('FALL')
			
	def assertequal(self) :

		page = driver.page_source
		result = re.findall(self.xpaths,page,re.S)
		#print(self.xpaths)
		#print(result)
		if result[0] == str(self.inputs) :
			print('PASS')
			excel.xlwts().write(self.x,'PASS')
			#excel.xlwts().write(self.x,result)
		else :
			
			#excel.xlwts().write(self.x,'FALL')
			excel.xlwts().write(self.x,result)
			print('FALL')
			
	def batch(self):
	
		page = driver.page_source
		result = re.findall(self.xpaths,page,re.S)
		#print(r for r in result)
		s = 'true'
		for r in result :
		
			if r != str(self.inputs) :
			
				s = 'false'
				print(s)
				break
				
		if s == 'true' :
			print('PASS')
			excel.xlwts().write(self.x,'PASS')
			#excel.xlwts().write(self.x,result)
		else :
			
			#excel.xlwts().write(self.x,'FALL')
			excel.xlwts().write(self.x,result)
			print('FALL')
			
			
if __name__ == '__main__' :
	
	x = 0
	xpaths = ''
	inputs = ''
	driver = '233'
	
	driver = testing(x,xpaths,inputs,driver).setup()
	for i in excel.opens().work() :
	
		if len(i[1]) == 0 and len(i[0]) == 0 :
			xpaths = i[4]
			try :
				inputs = int(i[5])
			except :
				inputs = i[5]
			print(i[3])
			if i[3] == 'keys' :
				#print(driver)
				testing(x,xpaths,inputs,driver).keys()
			elif i[3] == 'click' :
				
				testing(x,xpaths,inputs,driver).clicks()
			
			elif i[3] == 'assertequals' :
				
				testing(x,xpaths,inputs,driver).assertequals()
			elif i[3] == 'assertequal' :
			
				testing(x,xpaths,inputs,driver).assertequal()
			elif i[3] == 'batch' :
			
				testing(x,xpaths,inputs,driver).batch()
			elif i[3] == 'time' :
			
				testing(x,xpaths,inputs,driver).time()
		x += 1	





		