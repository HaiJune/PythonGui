# 
# #单继承
# class People:
#     name=''
#     age=0
#     __weight=0
# 
#     def __init__(self,n,a,w):
#         self.name=n
#         self.age=a
#         self.__weight=w
#     def speak(self):
#         print("我的名字叫%s，今年%d岁，体重%d公斤"%(self.name,self.age))
# #单继承实例
# class Student(People):
#     grade=''
#     def __init__(self,n,a,w,g):
#         '''调用父类的构造函数'''
#         People.__init__(self,n,a,w)
#         self.grade=g
#         #覆盖父类中的方法
#     def speak(self):
#         print("我的名字叫%s，今年%d岁，%s年级"%(self.name,self.age,self.grade))
# 
# s=Student('runoob',10,30,4)
# s.speak()


#多继承
class People:
    name=''
    age=0
    __weight=0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w
    def speak(self):
        print("我的名字叫%s,今年%d岁"%(self.name,self.age))
        
class Student(People):
    grade=''
    def __init__(self,n,a,w,g):
        People.__init__(self,n,a,w)
        self.grade=g
    def speak(self):
        print("我的名字叫%s，今年%d岁，上%s年级"%(self.name,self.age,self.grade))
#另一个类
class Speaker:
    topic=''
    name=''
    def __init__(self,n,t):
        self.name=n
        self.topic=t
    def speak(self):
        print("我的名字叫%s，我今天演讲的主题是%s"%(self.name,self.topic))
#多重继承
class Sample(Speaker,Student):
    a=''
    def __init__(self,n,a,w,g,t):
        Student.__init__(self,n,a,w,g)
        Speaker.__init__(self,n,t)
test=Sample('wowo',10,30,4,'python')
test.speak()#方法名称相同，默认调用排在前面的类的方法