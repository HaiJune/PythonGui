# __author__ = 'youxiang'
# #coding=utf-8
#
# # import tkinter
# # top=tkinter.Tk()
# # #进行消息循环
# # top.mainloop()
#
# #打入tkinter库
# from tkinter import *
# #创建窗口对象的背景色
# root=Tk()
# #创建两个列表
# list1=['c','java','python','php','html','sql','oracle']
# list2=['css','div','js','bootstrap']
# #创建两个列表组件
# listtb1=Listbox(root)
# listtb2=Listbox(root)
# #第一个小部件插入数据
# for item in list1:
#     listtb1.insert(0,item)
#
# for item in list2:
#     listtb2.insert(0,item)
#
# #将小部件放置在主窗口中
# listtb1.pack()
# listtb2.pack()
# root.mainloop()

# def add(str1,str2):
#     return str1+str2
# print(add(1,2))

# str=input("name:")
# print('your name is:{}'.format(str))
#

# f=open("d:\\Users\\youxiang\\Desktop\\plus.docx","w")
# f.write("python是一个非常好的语言。\n是的，非常好！")
# f.close()


# f=open("d:\\Users\\youxiang\\Desktop\\plus.docx",'w')
# # str=f.read()
#
# # str=f.readline()#只读取一行
#
# # str=f.readlines()#读取包含的所有行
#
# # for line in f:
# #     print(line,end='')
# # str=f.write("测试一下Python的相关输出功能",14)
# value=("测试一下Python的相关输出功能",14)
# s=str(value)
# f.write(s)
#
# print(s)
# f.close()


# class MyClass:
#     """ 一个简单的类实例 """
#     i=1234
#     def addNum(self):
#         return 'hello world'
#
# #实例化类
# x=MyClass()
#
# #访问类的属性和方法，
# 类的方法与普通函数的方法有一个区别就是，类的方法额外的第一个参数，就是self
# print("MyClass类的属性i值为：",x.i)
# print("MyClass类的方法addNum的输出值为：",x.addNum())


# class Complex:
#     '''定义一个__init__()方法，实例化方法会自动调用__init__()方法，
#      如果有参数，会在调用该方法时传递到实例化上
#     '''
#     def __init__(self,realpart,imagpart):
#         #self代表类的实例，而非类
#         self.r=realpart
#         self.i=imagpart
# #实例化类
# x=Complex(2.0,-3.0)
#
# print("显示复合函数的实部和虚部：",x.r,"和",x.i)


# class Test:
#     def ptr(baidu):
#         print(baidu)
#         print(baidu.__class__)
# t=Test()
# t.ptr()


# class People:
#      '''下面定义一个简单的属性'''
#      name=""
#      age=0
#      __weight=0
#      def __init__(self,n,a,w):
#          self.name=n
#          self.age=a
#          self.__weight=w
#      def speak(self):
#          print("%s说，我今年%d岁，我%d公斤重"%(self.name,self.age,self.__weight))
# x=People('baidu',10,30)
# x.speak()

# #方法重写
# class Parent:
#     def myMehod(self):
#         print("父类的方法")
# class Children(Parent):
#     def myMehod(self):
#         print("子类的方法")
# test=Children()#子类实例
# test.myMehod()#子类调用重写方法

# #方法重载
# class Reload:
#
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __str__(self):
#         return "Reload(%d,%d)"%(self.a,self.b)
#
#     def __add__(self, other):
#         return Reload(self.a+other.a,self.b+other.b)
# v1=Reload(2,10)
# v2=Reload(5,-2)
# print(v1+v2)



# from datetime import date
# now=date.today()
# # S=now.strftime("%y/%m/%d")#小写
# # print(S)
# birthday=date(1991,11,1)
# age=now-birthday
# # print(birthday)
# # # age=now.year-birthday.year
# # age=now.month-birthday.month
# # print(abs(age))#abs()取绝对值
# print("%.1f"%(age.days/365))#保留一位小数
# print(round(age.days/365,1))#保留一位小数

import doctest
def average(value):
    return sum(value)/len(value)
doctest.testmod()