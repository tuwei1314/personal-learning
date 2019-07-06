with open('./photo1.jpg','rb') as file1:

	file_content=file1.read()

with open('../test1/photo4.png','wb') as file2:
	file2.write(file_content)
#另一种写法:
#读文件
file1=open('./photo1.jpg','rb')
file_content=file1.read()
file1.close()
#根据读的文件写文件，进行复制，文件没有会自动创建
file2=open('../test1/photo4.png','wb')
file2.write(file_content)
file2.close()
