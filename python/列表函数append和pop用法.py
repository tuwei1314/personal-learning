students = ['小明', '小红', '小刚']
for i in range(3):
	print(students)
	students1=students.pop(0)
	students.append(students1)
print('以上是函数pop实现方法\n')

#append函数追加方式实现
print('下面是append函数实现方法')
students2 = ['小明', '小红', '小刚']
for i in range(3):
	print(students2)
	students3=students2[0]
	students2=students2[1:]
	students2.append(students3)
