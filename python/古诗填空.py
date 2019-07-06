list_test = ['一弦一柱思华年。\n','蓝田日暖玉生烟。\n']  # 将要默写的诗句放在列表里。
f=open('test.txt','r',encoding='utf-8')
lines = f.readlines()
f.close()
print(list_test)
print(lines)
new=open('poem2.txt','w',encoding='utf-8')
for line in lines:
    if line in list_test:  # 属于默写列表中的句子，将其替换成横线。
        new.write('____________。\n')
    else:
        new.write(line)
new.close()

