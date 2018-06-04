# import openpyxl
# import s

#
# # Openthe xlsx file in Python
# xlsx_file = openpyxl.load_workbook(filename)
#
# # List with all the worksheets in the workbook
# lst_worksheets = xlsx_file.get_sheet_names()
#
# # Change the active worksheet in the workbook
# xlsx_file._active_sheet_index = lst_worksheets.index(wsToOpen)
#
# # Save the workbook open in the chosen sheet_active_sheet_index
#
# xlsx_file.save(filename)
#
# #Open the workbook in MS Excel
# subprocess.Popen([filename], shell=True)
import openpyxl
import xlrd
import os
from openpyxl import Workbook
from scripts.weather import weather
from xlutils.copy import copy

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# filename = "./Excelsheets/AIML.xls"
workbookpath=ROOT_DIR.replace("scripts","Excelsheets")
wsToOpen = "Weather"
workbookold = openpyxl.load_workbook(os.path.join(workbookpath,'AIML.xlsx'),data_only=True)
# workbook=copy(workbookold)
worksheet = workbookold['Weather']
print(worksheet.cell(1, 1).value)
for i in range(1,1000):
        ZIPCODE=worksheet.cell(i+1,1).value
        weather(ZIPCODE)
        mainweatherReport=weather(ZIPCODE)
        worksheet.cell(i+1,2).value=mainweatherReport
        savepath=workbookpath+"\\"+'AIML.xlsx'
        workbookold.save(savepath)
        # workbookold.save()
        if(worksheet.cell(i+1,1).value==None):
            break

