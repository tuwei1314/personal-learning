#类的定制，在父类的基础上修改代码，即在子类中直接用父类的方法，然后通过参数的调整进行定制
class Chinese:
    #初始化方法
    def __init__(self, greeting = '你好', place = '中国'):
        self.greeting = greeting
        self.place = place

    def greet(self):
        print('%s！欢迎来到%s。' % (self.greeting, self.place))

class Cantonese(Chinese):

    def __init__(self, greeting = '雷猴', place = '广东'):
        Chinese.__init__(self, greeting, place)  #继承父类方法

yewen = Cantonese()
yewen.greet()


class Chinese:

    def land_area(self,area):
        print('我们居住的地方，陆地面积是%d万平方公里左右。' % area)

class Cantonese(Chinese):
    # 为参数 area 设置默认值。
    def land_area(self, area = 960, rate = 0.0188):
        Chinese.land_area(self, area * rate) ##继承父类方法，然后调整参数

yewen = Cantonese()
yewen.land_area()
# 两个参数都有默认值，所以可以这么调用。