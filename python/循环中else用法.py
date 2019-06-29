#用一句话总结，当循环中没有碰到break语句，就会执行循环后面的else语句，否则就不会执行。
for i in range(5):
    a = int(input('请输入0来结束循环，你有5次机会:'))
    if a == 0:
        print('你触发了break语句，循环结束，导致else语句不会生效。')
        break
else:
    print('5次循环你都错过了，else语句生效了。')