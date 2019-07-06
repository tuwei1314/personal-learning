file1 = open('winner.txt','r',encoding='utf-8')
file_lines = file1.readlines()
file1.close()

dict_scores = {}
list_scores = []
final_scores = []

for score in file_lines:
	data=score.split() #字符串分割
	for i in data[1:]:
		list_scores.append(i)
		dict_scores[i]=data[0]
list_scores.sort(reverse=True)  #列表排序，从高到低
print(list_scores)
print(dict_scores)

for i in list_scores:
	result=dict_scores[i]+str(i)+'\n'
	final_scores.append(result)
file2 = open('winner02.txt','w',encoding='utf-8')
file2.writelines(final_scores)
file1.close()

