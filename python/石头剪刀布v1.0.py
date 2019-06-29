import random,time
#电脑出拳只能从三个中进行随机选择
choice1 = ['石头','剪刀','布']
def coupon(b):
	a = random.choice(choice1)  #电脑选择赋值给变量a
	if a==b:
		print('电脑出的是%s，平局'% a)
	elif a=='石头' and b=='剪刀' or a=='布' and b=='石头' or a=='剪刀' and b=='布':
		print('电脑出的是%s,电脑赢了'% a)
	else:
		print('电脑出的是%s，恭喜你赢了！'% a)
while True:
	#print('比赛倒计时3')
	#time.sleep(1)
	#print('比赛倒计时2')
	#time.sleep(1)
	#print('比赛倒计时1')
	#time.sleep(1)
	choice2=['石头','剪刀','布']
	b=input('请出拳，选择出 剪刀 石头  布 或者输入n退出游戏：')
	if b=='n':
		break
	elif b not in choice2:
		print('你输错了，出拳只能出石头 剪刀或者布')
		continue
	coupon(b)