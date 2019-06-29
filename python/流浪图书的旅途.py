'''第一种用法是使用类生成实例对象。类作为实例对象的模版，每个实例创建后，都将拥有类的所有属性和方法。
第二种用法是用类将多个函数（方法）打包封装在一起，让类中的方法相互配合。
回到项目：我们的处理对象是每本具体的书，而每本书都有自己的属性信息，所以我们可以定义一个Book类，利用Book类创建一个个书的实例，绑定属性（对应用法1）。
而这个管理系统的运行主体，是多个可供选择的功能的叠加，所以我们可以创建一个系统运行类BookManager，将查询书籍、添加书籍等功能封装成类中的方法以供调用（对应用法2）。
我们的预期效果是当实例化这个系统运行类的时候，会出现一个菜单，能让用户选择不同的功能，如下所示：
1.查询所有书籍
2.添加书籍
3.借阅书籍
4.归还书籍
5.退出系统
请输入数字选择对应的功能：'''

class Book:
	def __init__(self,name,author,comment,state = 0):
#为了后续方便参数传递，借阅状态state采用默认参数，用0来表示'未借出'，1来表示'已借出'。
		self.name = name
		self.author = author
		self.comment = comment
		self.state = state
  # 分别表示书名、作者、推荐语和借阅状态
'''只要在类中定义了__str__(self)方法，那么当使用print打印实例对象的时候，
就会直接打印出在这个方法中return的数据'''
	def __str__(self):
		if self.state == 0:
			status = '未借出'
		else:
			status = '已借出'
		return '书籍名称：《%s》 作者：%s 推荐语：%s\n状态：%s ' % (self.name,self.author,self.comment,status)
class BookManager:
	# 存储书籍的列表，每一个元素都是Book的实例对象
	books = []
	def __init__(self):
		book1 = Book('惶然录','费尔南多·佩索阿','一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
		book2 = Book('以箭为翅','简媜','调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
		book3 = Book('心是孤独的猎手','卡森·麦卡勒斯','我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。',1)
		self.books.append(book1)
		self.books.append(book2)
		self.books.append(book3)
	def menu(self): #定义一个菜单方法
		print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地！\n')
		while True:
			print('1.查询所有书籍\n2.添加书籍\n3.借阅书籍\n4.归还书籍\n5.退出系统\n')
			choice = int(input('请输入数字选择对应的功能：'))
			if choice == 1:
				self.show_all_book()
				# 调用对象方法时self不能忘
			elif choice == 2:
				self.add_book()
			elif choice == 3:
				self.lend_book()
			elif choice == 4:
				self.return_book()
			elif choice == 5:
				print('感谢使用！愿你我成为爱书之人，在茫茫书海里相遇。')
				break
	#查询所有书籍
	def show_all_book(self):
		print('目前图书馆总的书籍数量是%d本,书籍信息如下：'% len(self.books))
		for book in self.books:
			print(book)

	#添加书籍
	def add_book(self):
		new_book =input('请输入书籍信息： ')
		new_author=input('请输入书籍作者：')
		new_comment=input('请输入推荐语：')
		abook=Book(new_book,new_author,new_comment)
		self.books.append(abook)

		print('书籍:<<%s>> 添加成功！\n'% new_book)
		#额外定义一个方法，用来检测书籍是否存在，这样在还书的时候就可以减少代码量，
	def check_book(self,name):
		for book in self.books:
			if book.name == name:
				return book      #Book实例
		else:
			return None
	#借阅书籍
	def lend_book(self):
		name=input('请输入你需要借的书籍名称：')
		res = self.check_book(name) #调用check_book方法，并把返回值赋值给res
		if res != None:
		# 如果返回值不等于None值，即返回的是实例对象
			if res.state == 1:
			# 如果实例对象的属性state为1，即借阅状态为已租借
				print('你来晚了一步，这本书已经被借走了噢')
			else:
			# 如果state为0
				print('借阅成功，借了不看会变胖噢～')
				res.state = 1
				# 书籍借出后属性state变为1
		else:
		# 如果返回值为None值
			print('这本书暂时没有收录在系统里呢')
	 #归还书籍
	def return_book(self):
		name=input('请输入你需要归还书籍的名字：')
		res = self.check_book(name) #调用check_book
		if res != None:
			if res.state==0:
				print('这本书还没有借出哟!')
			else:
				print('书籍 <<%s>>归还成功'% name)
				res.state=0
		else:
			print('这不是我们图书馆的书哟！')
manager = BookManager()
manager.menu()

