import csv
##读取excle中的内容
with open('some.csv', newline='') as f:
	reader = csv.reader(f)

	for row in reader:
		print(row)
#写文件到excle中
with open('some.csv', 'a', newline='') as f1:
	writer = csv.writer(f1)
	writer.writerow(['4', '猫砂', '25', '1022', '886'])
	writer.writerow(['5', '猫罐头', '18', '2234', '3121'])


