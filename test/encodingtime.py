import re
import xlwt


fw = open("obs_log_res_aws.txt", "r")
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Encode time")
data = []

for line in fw:


    if 'Encoding' in line:
        line = line.split(":")
        data.append([word for word in line])

print(data)

for row in range(len(data)):
    for col in range(len(data[row])):
        sheet.write(row, col, data[row][col])

workbook.save("encodingtime.xls")
fw.close()