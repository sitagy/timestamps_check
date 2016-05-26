import re
import xlwt


fp = open("timestamp_aws_res.txt", "r")
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Received time")
data = []

for line in fp:


    if 'Pktnum' in line:
        line = line.split(":")
        data.append([word for word in line])

print(data)

for row in range(len(data)):
    for col in range(len(data[row])):
        sheet.write(row, col, data[row][col])

workbook.save("receivedtime.xls")
fp.close()