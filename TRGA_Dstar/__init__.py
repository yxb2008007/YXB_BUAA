import xlrd

file="F:\\SCI2_Result_fixed\\chart\\5faults data\\Tarantula_fixed.xls"
wb=xlrd.open_workbook(filename=file)
sheet1=wb.sheet_by_index(0)
print sheet1.cell_value(1,0)
print sheet1.nrows
list_trans=list(map(lambda x:int(x),sheet1.cell_value(1,0).split('_')))
print list_trans
