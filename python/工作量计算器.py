import math
key=1 #设置一个循环开关
#定义数据采集函数
def myinput():
    choice = input('请选择计算类型：（1-人力计算，2-工时计算）')
    if choice == '1':
        size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
        number = None
        time = float(input('请输入工时数量：（请输入小数）'))
        return size,number,time
    elif choice == '2':
        size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
        number = int(input('请输入人力数量：（请输入整数）'))
        time = None
        return size,number,time  #返回类型为元组

def estimated(my_input):
    size = my_input[0]   #从元组中取数据
    number = my_input[1]
    time = my_input[2]
    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)#利用math模块完成向上取整
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number))
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))
def again():
		global key #定义一个全局变量，可以进行修改，让其他函数也可以使用
		choice=input('需要再来一次吗,输入y继续，其他推出：')
		if choice !='y':
			key=0


def main():
	print('欢迎使用工作量计算小程序！')
	while key==1:
		my_input = myinput()
		estimated(my_input)
		again()
	print('感谢使用工作量计算器')

main()
