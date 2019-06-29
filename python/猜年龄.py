#!/usr/bin/python 
# _*_ coding: utf-8 _*_
import random
import time
#########3333add
###提示语部分
print('你好，我是机器人小艾，我们来玩个猜年龄的小游戏吧～(◆◡◆)')
time.sleep(2)

print('''
=============================
   猜对了有奖励喔！
=============================
''')
time.sleep(1)


print('小艾的真实年龄在18到30之间哦～')
time.sleep(1)


print('不过，你只有5次机会哦～')
time.sleep(1)


print('下面，请猜猜小艾的年龄吧：')


#从0至10产生一个随机整数，并赋值给变量age
age = random.randint(18,30)


#设置次数
for guess in range(1,6):
   
   #输入玩家猜测的年龄
    choice=int(input())
    
    #判读玩家输入的年龄是否等于正确的年龄
    if choice<age:
        print('小艾的提示：你猜小了')
                
    elif choice>age:
        print('小艾的提示：猜大了惹，奴家要生气了')
            
    else: 
        print('猜了'+str(guess)+'次，你就猜对了，真棒！')
        break   
                
#判断猜测次数 
if choice  == age:
    print('搜噶～那么小艾下线了～拜拜～（￣︶￣）↗')
    
else:
    print('哎呀～你还是木有猜对啊～但是你只有5次机会诶～怎么办啊～')
    print('那好吧～心软的小艾只好告诉你，我才'+str(age)+'岁哦～(*/ω＼*)')

