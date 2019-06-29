import time,random


while True:
	#定义三个变量并赋值，用来存放比赛结果，每次重开游戏，比赛结果清零
	i=0
	j=0
	k=0
	for n in range(1,4):
		time.sleep(2)
		# 生成随机属性
		player_life = random.randint(100,150)
		player_attack = random.randint(30,50)
		enemy_life = random.randint(100,150)
		enemy_attack = random.randint(30,50)
		# 展示双方角色的属性
		print('------现在是第{}局----------'.format(n))
		print('【玩家】\n血量：{}\n攻击：{}'.format(player_life,player_attack))
		print('------------------------')
		time.sleep(1)
		print('【敌人】\n血量：{}\n攻击：{}'.format(enemy_life,enemy_attack))
		print('-----------------------')
		time.sleep(1)

		while (player_life >0) and (enemy_life > 0):
			player_life = player_life - enemy_attack
			enemy_life = enemy_life - player_attack
			print('你发起了攻击，【敌人】剩余血量{}'.format(enemy_life))
			print('敌人向你发起了攻击，【玩家】剩余血量{}'.format(player_life))
			print('----------------------')
			time.sleep(1.5)
			#判断谁的血量先小于0，即表示谁输了
		if enemy_life<=0 and player_life>0:
			print('敌人死翘翘了，你赢了\n')
			i+=1
		elif enemy_life>0 and  player_life<=0:
			print('悲催，敌人把你干掉了!\n')
			j+=1
		else:
			print('哎呀，你和敌人同归于尽了！\n')
			k+=1

	else:
		print('【比赛结束】')

	print('本次比赛最终结果如下:')
	if j>i:
		print('玩家赢了:{}局\n敌人赢了:{}局\n双方平局为:{}局\n最终赢家是敌人'.format(i,j,k))
	elif j<i:
		print('玩家赢了:{}局\n敌人赢了:{}局\n双方平局为:{}局\n最终赢家是玩家'.format(i,j,k))
	else:
		print('最终双方战平')
	choice=input('想再来一次吗：输入n退出游戏， 输入其他继续: ')
	if choice=='n':
		print('游戏结束')
		break
	else:
		print('继续下一盘')
