def div(num1,num2):
	growth=(num1-num2)/num2
	percent=str(growth*100)+'%'
	return percent

def warning():
	print('error:确定上月一分钱都没有赚吗')

def main():
	while True:
		num1=float(input('请输入本月利润'))
		num2=float(input('请输入上月利润'))
		if num2==0:
			warning()
			continue
		else:
			print('利润增长率为：' +div(num1,num2))
			break
main()