import xlwt
from xlwt import Workbook
data=[]
file=open("elcin.txt","r+")
for line in file:
    data.append([word for word in line.split(" ") if word])
    wb=xlwt.Workbook(encoding="latin-1")
    my_sheet=wb.add_sheet('sheet')
    for row_index in range(len(data)):
        for colum_index in range(len(data[row_index])):
            my_sheet.write(row_index,colum_index,data[row_index][colum_index])
            wb.save("C:\Users\huseyn\data\StudentsData")