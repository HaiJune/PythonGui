__author__ = 'youxiang'
# # #输入数据并且求和
# num1=input("请输入第一个数：")
# num2=input("请输入第二个数：")
# num=float(num1)+float(num2)
# print("第一个数 {0} 加上第二个数 {1} 的和为 {2} ".format(num1,num2,num))



# #平方根求解
# import math
# num=float(input("请输入要计算的数值："))
# # num_sqrt=num**0.5这个只适用于正数，负数、复数需要函数cmath.sqrt
# num_sqrt=math.sqrt(num)
# print("%0.3f的平方根为：%0.3f"%(num,num_sqrt))


# #计算二次方程:ax**2+2bx+c=0
# #导入复杂的数学运算模块cmath
# # import cmath
# a=float(input("请输入a: "))
# b=float(input("请输入b: "))
# c=float(input("请输入c: "))
#
# # d=(b**2)-(4*a*c)
# #
# # num1=(-b+cmath.sqrt(d))/(2*a)
# # num2=(-b-cmath.sqrt(d))/(2*a)
# #
# # print("请显示二次方程的解：{0}和{1}".format(num1,num2))
#
# #计算半周长
# s=(a+b+c)/2
# #计算三角形面积（秦九昭公式）
# area=(s*(s-a)*(s-b)*(s-c))**0.5
# print("三角形面积：%0.2f"%area)


# #摄氏温度转换华氏温度
# #用户输入摄氏温度
# celsius=float(input("请输入摄氏温度："))
# #计算华氏温度
# fahrenheit=(celsius*1.8)+32
# print('%0.1f摄氏温度转换为华氏温度%0.1f'%(celsius,fahrenheit))


# #交换变量
# x=input('输入x的值为：')
# y=input('输入y的值为：')
# # #创建临时变量
# # temp=x
# # x=y
# # y=temp
# #不用临时变量
# x,y=y,x
# print('交换后x的值为：{}'.format(x))
# print('交换后y的值为：{}'.format(y))


# #if-elif-else语句判断数字是正数，负数或者为0
# while True:
#     num=float(input("请输入你要验证的数值："))
#     if num>0:
#         print("你输入的是正数")
#     elif num==0:
#         print("你输入的是0")
#     else:
#         print("你输入的是负数")