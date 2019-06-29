#!/usr/bin/python
# -*- coding: utf-8 -*-
#模拟用户进入银行办业务的场景
#while循环进行判断 如果用户输入有误就重新输入
import time
choice=''
while choice !='1' and choice !='2':
    choice=input('您好，欢迎光临！请问您需要帮助吗？1 需要 or 2不需要: ')

#if多条件判断和嵌套
if choice=='1':
    rechoice=''
    while rechoice !='1' and rechoice !='2' and rechoice!='3':
        rechoice=input('请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询: ')
    if rechoice=='2':

        print('''今日美元兑人民币的兑换率为1:6.9247，即1美元=6.9247人民币。
欧元兑人民币的兑换率为1:7.7605，即1欧元=7.7605人民币。''')
        print('请问你需要兑换美元还是欧元? ')
        A=''
        while A !='1' and A !='2':
            A=input('请输入你需要兑换的类型：1 美元 2 欧元: ')

        if A=='1':
            money = input('请输入您需要兑换的美元数： ')
            print('好的，我知道了，您需要兑换'+money+'美元。')
            print('那么，您需要付给我'+str(int(float(money)*6.9247))+'人民币')
            time.sleep(2)
            print('请慢走，欢迎再次光临！')
        else:
            money = input('请输入你需要兑换的欧元数： ')
            print('好的，我知道了，您需要兑换'+money+'欧元。')
            print('那么，您需要付给我'+str(int(float(money)*7.7605))+'人民币')
            time.sleep(2)
            print('请慢走，欢迎再次光临！')
    elif rechoice=='1':
        print('去存取款窗口')
    else:
        print('去咨询窗口')

else:
    print('好的，再见')
