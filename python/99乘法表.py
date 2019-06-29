#两次循环即循环嵌套使用
for i in range(1,10):
	for j in range(1,i+1):   #j的值在i的基础上自增1
        #格式化字符串
		print('%d X %d = %d' % (j,i,j*i),end='  ') #end是print函数的一个参数是用来控制换行行数和结尾字符
	print(' ')  #打印换行




