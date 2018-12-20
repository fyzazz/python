# coding = utf - 8

import xlrd,xlwt,os,shutil
from xlutils.copy import copy

class opens() :

	def work(workbookss = []):
		workbook = xlrd.open_workbook('test.xls').sheets()[0]
		workbookss = []
		for i in range(0,workbook.nrows) :
			workbooks = workbook.row_values(i)
			#if len(workbooks[0]) == 0 and len(workbooks[1]) == 0 :
			workbookss.append(workbooks)
			
			i+=1
		return workbookss
		
class xlwts() :

	def write(writebooksss,x,result,filename = 'test.xls'):
	
		writebook = xlrd.open_workbook(filename)
		writebooksss = copy(writebook)
		
		
		
		if result == 'PASS':
			#print('result = '+result)
			writebooksss.get_sheet(0).write(x,6,result)

		
		else :
			#print('result = '+result)
			writebooksss.get_sheet(0).write(x,6,'FALL')
			writebooksss.get_sheet(0).write(x,7,result)
		
		writebooksss.save('testing.xls')
		
		
if __name__ == '__main__' :

	opens = opens()
	print(opens.work())
	#xlwts().write(6,7,'pass')