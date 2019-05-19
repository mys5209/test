#! /usr/bin/python
# -*-coding:utf-8 -*-
#a = 4
#print(a)
#a= input ("请输入密码:")
#print(a)
#a,b,c,d,= 1,2,3,"hello"
#print(a,b,c,d)
#a='hell 我叫{},今年{}岁'
#b='缪'
#c=a.format(b)
#print(c)
#a='hello 我叫%s,今年%d岁'
#b=input('请输入你的名字')
#f=input('请输入你的年纪')
#t=int(f)
#c=a %(b,t)
#print(c)
#a=' qwer  '
#b=a.strip()
#print(b)
#a='ewqrtlen(a))
#a=(12,'er5243534'
#a=('wreq',456,789,23,45,456,45)
##print(a[1::4])
#a=[21,34,3214,45]
#import copy
# a=[1,2,13,2,[1000,[2345],2000]]
# b=copy.deepcopy(a)
# a[-1].append(120)
#a[-1].remove(9000)
# a={34,45,234,325,457,648}
# a.pop()
#print(a)
#key:value
#a=set()
#print(a)
#print(type(a))
# a=[1,2,13,1]
# b=a.copy()
# print(b)
#a=4//3
# a=0
# a+=1 #等于a=a+1
#print(a)
#print(4==3)
# a='qwewqr'
# print('c' not in a)
#\
#
# a=input('请输入一个成绩:')
# a=int(a)
# if 0<a< 70:
#     print('不合格')
# elif a<80:
#     print('一般')
# elif a< 90:
#     print('良好')
# else:
#     print('优秀')
#a=input('请输入一个数:')
#a=int(a)
#if a%6!=0 and a%2==a%3:
   # print('hello world')
#else:
#
#p
# rint(b)
#print(a)
#a=[12,4,56,7657]
#a=0
# for i in range(1,100):
#     if i==7:
#         break
#     print(i)
# else:
#     print('hello')
# a=0
# for i in range(100):
#     if i%2==0:
#         a-=i
#     else:
#         a+=i
# print(a)
#从1到10的范围里随机产生一个数
# import random
# a=random.randint(1,10)
# for i in range(3):
#  b=input('请输入一个数')
#  b=int(b)
#  if b>a:
#      print('大')
#  elif b<a:
#      print('小')
#  elif b==a:
#      print('true')
#      break
# a=[11,22,33,44,55,66,77,88,99]
# b,c=[ ],[ ]
# for i in a:
#     if i-55>0
#         b.append(i)
#     else:6
#         c.append(i)
# print(c)
# print(b)
# sum=0
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
# else:
#     if i==j:
#         sum+=i
#         print(sum)
#水仙花数
# for i in range (100,1000):
#     b=i//100
#     c=i//10%10
#     d=i%10
#     if b**3+c**3+d**3==i:
#         print(i)
# a=int(input('>>>'))
# if a%2==0:
#      if a%3==0:
#          print('hello world')
#      else:
#          print('hello')
# elif a%3==0:
#         print('world')
# else:
#     print('100')
# a=['电脑','手机','计算机']
# #enumerate:将列表中的每个数据的下标位置和数据对应显示
# for i ,j in enumerate(a):
#     print(i,j)
#
# a=int(input('请从键盘输入一个值:'))
# for i in (1,a):


#     if i>20
# b=1

# a=0
# while b<101:
#  a+=b
#  b+=1
# print(a)
# a=int(input('请从键盘上输入1个数'))
# b=[ ]
# b.append(a)
# i=(sum(b)/len(b))
# while b<i:
#     print(i)
#     print(i)
#     2
# if a<0:
#     break
#输入5 6 7 8 9 输出平均数6.5  输出低于平均数的 以输入负数结束：、
# while True:
#     c=[ ]
#     a=input('请输入一组数据，以逗号隔开：')
#     if int(a)<0:
#         break
#     else:
#         b=a.split(',')
#         for i in b:
#             c.append(int(i))
#         d=sum(c)/len(c)
#         print('平均数为{}'.format(d))
#         for j in c:
#             if d> j:
#                 print('低于平均数的有{}'.format(j))
#质数之和
#

# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(j,i,i*j),end=' \t')
#     print()
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(j,i,i*j),end=' \t')
#     print()
#
# a=0
# for i in range(2,):
#     for j in range(2,i+1):
#         if i%j==0:
#             break
#     if i==j:
#         a=a+i
# print(a)
# while True:
#     c=[ ]
#     a=input('请输入一组数据,以逗号隔开:')
#     a=int()
#     if int(a)<0:
#         break
#     else:
#         b=a.split(',')
#     for i in b:
#         c.append(int(i))
# a=('请输入一个边')
# a=int()
# b=('请出入一个边:')
# b=int()
# c=('请出入一个边:')
# c=int()
# if b+c>a or a+c>b or a+b>c:
#     print('这是一个三角形')
#     if a**2+b**2>c**2 or a**2+c**2>b**2 or c**2+b**2>a**2:
#         print('锐角三角形')
#     elif a**2+b**2>c**2 or b**2+c**2>a**2 or a**2+c**2>b**2:
#         print('钝角三角形')
#     elif a**2+b**2=c**2 or a**2+c**2=b**2 or b**2+c**2=a**2:
#         print('直角三角形')
# else:
#     print('不是三角形')
# import copy
# a={'name':'miao','age':20}
# a.popitem()                  a=input('以逗号隔开
#b=a.split()
# print(a)                     a=input('以逗号隔开
#b=a.split()
#                              a=input('以逗号隔开
# def 函数名():
#     a=input('以逗号隔开')
#     b=a.split(',')
#     for i in range(1,len(b)):
#         for j in range(0,len(b)-1-i):
#             if int(b[j]) > int(b[j+1]):
#                 b[j],b[j+1] = b[j+1],b[j]
#                 print(b)
#     print(b)
# 函数名()
# def sum(b):
#     a=input('以逗号隔开')
#     b=a.split(',')
#     for i in range(1,len(b)):
#         for j in range(0,len(b)-1-i):
#             if int(b[j]) > int(b[j+1]):
#                 b[j],b[j+1] = b[j+1],b[j]
#     print
# def sum ( a,b=10,*args):
#     print(a)
#     print(b)
#     print(args)
# sum(13,12,53)
# 
# def qwe (b):
#     a=0
#     for i in range(1,b+1):
#         a+=i
#         print(a)
#         return a
# c=qwe(10)
# print(c+2)
#
# a=input('请输入一行字符')
# if a[0]=='b':
#     if a[-1]=='c':
#         print('true')
#     else:
#         print('false')
# if a[-1]=='c':
#         print('true')

# else:
#     print('false')  # if b=a.startswitch('{}')
# a=[23,43,535,643,643]
# a.index(43)
# print(a)
#字符串变整数:
#a=[i+2 for i in range(10) if i>6 or i<9]
#print(a)
# a=lambda x=10,y=10 :print(x*y)
# a()
#
#f = open('c.txt','w',encoding='utf-8')
#
#print(f.read())for i in range(1,10):
#     for j in range(1,i+1):
#         f.write('{}*{}={}\t'.format(i,j,i*j))
#     f.write('\n')
# print(f.readline())
# print(f.readline())
# print(f.readlines())
# f.close()
# f=open('z.txt','a')
# a = input("<<<<")
# b = a.split(" ")
# c = len(b)
# for i in range(1,c):
#     for j in range(0,c-1):
#         if int(b[j]) > int(b[j+1]):
#             b[j],b[j+1]=b[j+1],b[j]
# print(b)
# product_list = [
#     ('Mac', 9000),
#     ('kindle', 800),
#     ('tesla', 900000),
#     ('python book', 105),
#     ('bike', 2000),
# ]
#
# saving = input('please enter your money: ')
# shopping_cart = []
# if saving.isdigit():
#     saving = int(saving)
#     while True:
#
#         for i, v in enumerate(product_list, 1):
#             print(i, '>>> ', v)
#         choice = input('choose the product number[quit:q]: ')
#         if choice.isdigit():
#             choice = int(choice)
#             if choice > 0 and choice <= len(product_list):
#                 p_item = product_list[choice - 1]
#                 if p_item[1] < saving:
#                     saving -= p_item[1]
#                     shopping_cart.append(p_item)
#                 else:
#                     print('you dont have enough money,and your money is %s' % saving)
#             else:
#                 print('number is not exist')
#         elif choice == 'q':
#             print('---------bought---------')
#             print(p_item)
#             print('your money is %s' % saving)
#             break
#         else:
#             print('invalid input')
# #
# a=int(input('请输入数字:'))
# x=1
# y=0
# for i in range(1,a+1):
#      x=x*i
#      y=x+y
# print(y)
# a=input['请输入一串字符串']
# b=[ ]
# c=a.split(',')
# for i in range(a):
#     if i not in b:
#         b.append(i)
# x=b.sort()
# j=max(x)
# m=j.count()
# x.remove(j)
# h=max(x)
# n=h.count()
# print((j*m),(h*n))
#f=open('cpp','r',encoding='utf-8')

# with open('z.txt','r',encoding='utf-8') as f:
#     for i in range(10):
#         if i<7:
#           print('hahaha')
#     else:

#         print('hehehe')
# def qwe (b):
#     a=0
#     for i in range(1,b+1):
#         a+=i
#     return a
# # a=lambda x:x+2
# #qwe(50)
# #print(c)
# #import random
#
# print(__name__)
# #if __name__=='__main__':
#        # print('hello')
# with open('c.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
#     for line in f.readlines():
#         data=line.strip()
#         if len(data)!=0:
#             f.write(data)
#             f.write('\n')
#     f.close()
#     f.close()
#
#
# a=[15,13,13,13,14,14,14,13,12,14,14,15]
# b=a.copy()
# b=list(set(b))
# b.sort()
# for i in a:
#     if i == b[-1] or i == b[-2]:
#         print(i)
# a=input('>>>')
# a=int()
# ten=12
# sixteen=hex(ten)
# print(sixteen)
# try:
#     a=3
#     print(a)
# except Exception as e:
#     print('hello')
# #except NameError as e:
# #except MemoryError as e:
# else:
#     print(123)
# finally:
#     print(213)
# a=int(input('>>>'))
# if a>3:
#     raise NameError('hello')
# else:
#     raise TypeError('123'

# for i in range(1,5):
#     for j in range(1,5):
#         for z in range(1,5):
#             if (i!=j) and (i!=z) and (j!=z):
#                 print (i,j,z)
# product_list = [
#     ('pen', 9),
#     ('candy', 8),
#     ('table', 900),
#     ('book', 10),
#     ('bike', 2000),
# ]
#
# saving = input('please enter your money: ')
# shopping_cart = []
# if saving.isdigit():
#     saving = int(saving)
#     while True:
#
#         for i, v in enumerate(product_list, 1):
#             print(i, '>>> ', v)
#         choice = input('choose the product number[quit:q]: ')
#         if choice.isdigit():
#             choice = int(choice)
#             if choice > 0 and choice <= len(product_list):
#                 p_item = product_list[choice - 1]
#
# sal=input("请输入你的金额:")
# show=[("car","1000"),("dog","2000"),("cat","100"),("ball","200")]
# show_card=[]
# title = "True"
# if sal.isdigit():
#     sal=int(sal)
#     now_salary = sal
#     while title:
#         for i in show:
#             print(show.index(i), i)
#         choose = int(input("选择你的商品序号:"))
#         if sal >= int(show[choose][1]):
#             print("3Q，你已成功购买的商品:", show[choose][0])
#             show_card.append(show[choose])
#             now_salary -= int(show[choose][1])
#             result = input("继续购买商品吗?按q退出或者按任意键继续")
#             if result == "q":
#                 print("你的商品有:%s ,你的余额为:%s" % (show_card, now_salary))
#                 break
#             else:
#                 continue
#         else:
#             print("你的工资并不能购买这个商品")
#             break
# else:
   # print("请输入数字")
'''
a = int(input('输入你的人民币：'))
b =['直升飞机:1399','魔幻手机:9999','智能电脑:888','巴姆雷特:99999','航空母舰:88888','真爱戒指:1314520']
d =[]
z = 1
while z > 0:
    while z > 0:
        print('账户余额{}'.format(a))
        print('      商品区')
        for x,y in enumerate(b):
            print(x+1,y)
        print()
        try:
            c =int(input( '(输入序号加入购物车),(110退出),(0进入购物车)：'))
        except Exception as o:
            print('输入错误，请重新输入')
        else:
            pass
            if c == 110:
                break
            elif c > len(b):
                print('输入错误，请重新输入')
            elif c > 0:
                print('已加入购物车:{}'.format(b[c - 1]))
                d.append(b[c - 1])
            elif c == 0:
                while True :
                    print()
                    print('账户余额:{}'.format(a),       '(充值110)')
                    print ('    购物车')
                    for i,j in enumerate (d):
                        print(i+1,j)
                    e = int(input('(移除商品输入序号),(清空0),(回到商品区1001)'))
                    if e == 1001:
                        break
                    elif e == 110:
                        o = int(input('请输入要充值金额'))
                        a +=o
                    elif e == 0:
                        n=[]
                        for A in d:
                            m = A.split(':')[1]
                            n.append(int(m))
                        f = sum(n)
                        if f <= a:
                            a -=f
                            print('购买成功{},剩余{}'.format(d, a))
                            d.clear()
                            continue
                        elif f > a:
                            print('余额不足,剩余{}，请充值'.format(a) )
                            p = int(input('充值请输入1，不充值输入0：'))
                            if p == 1:
                                g = int(input('请输入充值金额'))
                                a +=g
                                print('充值{}成功'.format(g))
                            else:
                                continue
                    elif e > len(d):
                        print('输入错误！！！！请重新输入！！！')
                    elif e > 0:
                        n=[]
                        for A in d:
                            m = A.split(':')[1]
                            n.append(int(m))
                        if n[0] <= a:
                            a -=n[0]
                            print('购买成功{},剩余{}'.format(d[e-1], a))
                            d.pop(e-1)
                            continue
                        elif n[0] > a:
                            print('余额不足,剩余{}，请充值'.format(a) )
                            p = int(input('充值请输入1，不充值输入0：'))
                            if p == 1:
                                g = int(input('请输入充值金额'))
                                a +=g
                                print('充值{}成功'.format(g))
                            else:
                                continue
                    else:
                        print('把{}移除购物车'.format(d[e-1]) )
                        d.pop(e-1)
    if c == 110:
        print('余额剩余{}，欢迎下次再来'.format(a))
        break
# '''
# a =[i for i in range(10)]
# b =['{}'.format(chr(i)) for i in range(97,103)]
#
# print(a)
# ''''
# def shiliu(y):
#     b =[str(i) for i in range(0,10)]
#     a =['{}'.format(chr(i)) for i in range(97,103)]
#     b.extend(a)
#     n=[]
#     while True :
#         if y >= 16:
# /            c =y%16
#             y //=16
#         elif y < 16 and y !=0:
#             n.insert(0,y)
#             break
#         n.insert(0,c)
#     n =[b[i] for i in n]
#     n.insert(0,'0x')
#     return ("".join(n))
# d=shiliu(124235)
# print(d)
#
# a=' qweqr{}123qweqwe{} '
# b=100
# d=90
# c=a.format(2,3)
# print(b)
# print(c)
# a='hello,我叫%s,今年%d岁'
# c=a%('缪',90)
# print(c)
# b=a.lstrip()
# print(b)
#  a=[12,12,456,57,65,[5,75]]
#  j=a.copy()
#  j[-1].append(120)
#  print(j)
# a={'name':'hahah','age':'23','haha':'17'}
# print(a.items())‘

'''''
a=[str(x) for x in range(10)] + [chr(x) for x in range(97,103)]
b=int(input('>>>'))
f=[]                #f=''
while True:
    c=b%16
    b=b//16
    f.append(a[c])    #f=f+a[c]
    if b==0:
        break
f.reverse()           #f=f[::-1]
f=''.join(f)  
print('0x{}'.format(f))
'''''
# a,b=divmod(16,100)    #整除求余
# # # # # print(a,b)
#class 小爱():
    # def __init__(self,a):
    #     self.name=a
#     def asd(self,a):
#         print('打电话给{}'.format(a))
#      def 发短信(self,b):
#          print('打电话给{}'.format(b))
#     # def 播放音乐(self):
#     #     print('播放音乐789')
# class 小na(小爱):
#     pass
# xiao=小na()
# xiao.asd(3)
# xiao.发短信(4)
# a=小爱()      #赋予一个变量，以后用的方便
# # a.打电话()
# a.发短信()
# a.播放音乐()
# Asd().adsfd()

# class 小na(小爱):
#     pass
# class 小hong:
#     def asd(selfx,y=10):
#         print('hahah')

# class 小(小爱):
    # def asd(self):
    #     print('打电话')
    #     print('视频电话')

# f=open(r'c.txt','r',encoding='utf-8')
# f=f.read()
# d=f.split('\n')
# c=len(d)
# import xlwt
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('sheet1')
# for b in range(4):
#     for n in range(3):
#         m = d[]
#         m = m.split(',')
#         i = len(m)
#         sheet.write(b,n,'{}'.format(m[i]))
#从写入
'''''
import xlwt
with open('a.txt','r',encoding='utf-8') as f:
    a=f.readlines()
ff=xlwt.Workbook(encoding='utf-8')
sheet=ff.add_sheet('sheet1')
for i in range(len(a)):
     k=a[i].split(',')
     for j in range(len(k)):
         sheet.write(i,j,k[j])
ff.save('a.xls')
''''''
#从表中写入文本
'''''
'''''
import xlrd
f=xlrd.open_workbook('a.xls')
sheet=f.sheets()[0]
num=sheet.nrows
with open('b.txt','w',encoding='utf-8') as ff:
    for i in range(num):
        i=sheet.row_values(i)
        for j,k in enumerate(i):
            if j==len(i)-1:
                ff.write(k)
            else:
                ff.write(k+',')
'''
# a=int(input('请输入数字:'))
# x=1
# y=0
# for i in range(1,a+1):
#     x=x*i
#     y=y+x
# print(y)
# a='12340'
# # a=a[::-1]
# # b=0
# # for i in range(len(a)):
# #     for j in range(10):
# #         if str(j)==a[i]:
# #             b=b+j*10**i
# #     print(b)
# a=['str(x) for x in range(0,10)' + '[chr(x) for x in range(97,103)]']
# b=int(input('>>>'))
# f=[]
# while True:
#     c=b%16
#     b=b//16
#     f.append(a[c])
#     if b==0:
#         break
# f.reverse()
# f=''.join(f)
# print('ox{}.format(f)')
#
# a=['int(x) for x in range(10)' + '[chr(x) for x in range(97,103)]']
# b=int(input('请输入一个数：'))
# f=[]
# while True:
#     c=b%16
#     b=b//16
#     f.append(a[c])
#     if b==0:
#         break
# f.reverse()
# f=''.join(f)
# print('ox{}'.format(f))
# a=[str(x) for x in range(10)] + [chr(x) for x in range(97,103)]
# b=int(input('请输入一个数：'))
# f=[]
# while True:
#     c=b%16
#     b=b//16
#     f.append(a[c])
#     if b==0:
#         break
# f.reverse()
# f=''.join(f)
# print('ox{}'.format(f))
# c=[]
# a=input('请输入三条边：')
# b=a.split(',')
# for i in b:
#     c.append(int(i))
#     c.sort()
# if c[2]<c[0]+c[1]:
#     if c[2]**2 > c[0]**2 + c[1]**2:
#        print('钝角')
#     elif c[2]**2 < c[0]**2 + c[1]**2:
#        print('锐角')
#     elif c[2]**2 == c[0]**2 + c[1]**2:
#        print('直角')
# else:
#     print('输入错误')
# import xlwt
# # f=xlwt.workbook(encoding='utsf-8')
# # sheet=f.add_sheet(python_test)
# import random
# a=random.randint(1,10)
# for i in range(1,4):
#     b=input('请输入一个数')
#     b=int(b)
#     if b>a:
#         print('大了,还剩%d次机会'%(3-i))
#     elif b<a:
#         print('小了,还剩{}次机会'.format(3-i))
#     elif b==a:
#         print('正确')
#         break
# # a=str(input('请输入一个字符'))
# if a[0]=='a' or a[0]=='A':
#     if a[-1]=='c':
#         print('110')
#     else:
#         print('120')
# elif a[-1]=='c':
#     print('130')
# else:
#     print('250')
# for i in range(100,1000):
# #     a=i//100
# #     b=i//10%10
# #     c=i%10
# #     if a**3+b**3+c**3==i:
# #         print(i)
#
# a=\
#     input('以逗号隔开')
# b=a.split()
# for i in range(1,len(b)):
#     for j in range(0,len(b)-1-i):
# import time
# a=time.time()
# print(a)
#import time
# a=time.localtime(100000000)
# b=time.strftime(%ef)
# print(b)
# import time
# # a=time.strptime('2010-12-12','%Y-%m-%d')
# # print(a)
# for i in range(10):
#     print(i)
#     time.sleep(5)
# a=input('请输入一个日期以逗号隔开：')
# a=a.split(',')
# b=int(a[0])
# if b%100==0:
# #     if b%400==0:
# #         print('该年是闰年')
# #     else:
# #         print('常规年')
# # elif b%4==0 or b%400==0:
# #     print('该年是闰年')
# # else:
# #     print('常规年')
#
# import time
# i=input('请输入同样的日期以横杆隔开:')
# a=time.strptime('i','%y-%m-%d')
# print(a)
# print(a[-2])
# import time
# i=input('请输入年月日以逗号隔开:')
# i=i.split(',')
# z=i[0]
# j=i[1]
# k=i[2]
# a=time.strptime('{}-{}-{}'.format(z,j,k),'%Y-%m-%d')
# b=time.mktime(a)
# b=b-86400

# m=time.localtime(b)
# print(m)
# a=0
# for i in range(2,101):
#     for j in range(2,i+1):
#         if i%j==0:
#             break
#     if i==j:
#         a+=i
# print(a)
# def cc(a,b):
# #     c=0
# #     for i in range(a,b):
# #         for j in range(2,i+1):
# #             if i%j==0:
# #                 break
# #         if i==j:
# #             c+=i
# #     return c
# # a=cc(2,100)
# # print(a)
#步骤1
# https://www.qiushibaike.com/text/page/2/U
# oo={'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
#oo等于字典
# }
# for i in range(7):
# if i==6:
#     break
# else:
# import requests
# import re
# a='https://www.zhipin.com/job_detail/d692139709e14bee1XB93dS-E1I~.html?ka=search_list_22'
# # 发送请求
# b=requests.get(a)
    #读取响应 1.text(字符串)   2.content(以字节的方式接受)(以b开头)
    #得到的就是网页源代码
# print(b.text)
# print(b.content)
# c=(b.content.decode('utf-8'))  #utf-8还有大小写区分注意！！！！
# print(c)
    #步骤2过滤想要的内容
# c=b.content.decode('utf-8')
# z=re.compile('<h2>(.*)<h2>', re.S)
# p=z.findall(c)
# for j in p:
#     j=j.replace('\n','')
#     print(j)
# d=re.compile('<div class="content">(.*?)</span>',re.S)
# f=d.findall(c)
# ff=[]
# for i in f:
#     i=i.replace('<span>','')
#     i=i.strip()
#     i=i.replace('<br/>','')
#     ff.append(i)
#     with open('h.txt','w',encoding='utf-8') as g:
#         for i in ff:
#             g.write(i+'\n')
#
# import re
# import requests
# class Tupian():
#     def room(self,b):
#             url='https://www.qiushibaike.com/imgrank/page/{}/'.format(b)
#             head={'User-Agent':'Mozilla/5.0(Windows NT 10.0;Win64;x64;rv:66.0)Gecko/20100101 Firefox/66.0'
#                   }
#             res=requests.get(url,headers=head)
#             html=res.content.decode('utf-8')
#             return html
#     def gl(self,abc):
#             lianjie=[]
#             patt=re.compile(r'<div class="thumb">(.*?)</a>',re.S)
#             items=patt.findall(abc)
#             for i in items:
#                 new_a=re.compile(r'<img src="(.*?)"')
#                 aaa=new_a.findall(i)
#                 lianjie.extend(aaa)
#             return lianjie
#     def save(self,shu):
#             for a,i in enumerate(shu):
#               res=requests.get('http:'+i)
#               qq=res.content
#               with open('{}.jpg'.format(a),'wb') as f:
#                 f.write(qq)
# m=Tupian()
# abc=m.room(1)
# m.gl(abc)
# shu=m.gl(abc)
# m.save(shu)

# import pymysql
#连接数据库
# conn=pymysql.connect(host='192.168.1.19',port=3306,
#                 user='root',passwd='123456')
#创建游标 :类似于vim里面的光标
# abc=conn.cursor()
#执行sql语句(execute)('show database;')
# abc.execute('create database pmys;')
# abc.execute('show databases;')
#fetchall 获取上一个sql语句的结果(注意上一个！！！！)
#fetchmany获取上一个sql语句的结果（默认只获取结果中的第一个数据获取）
#fetchone每次获取一条结果,有迭代的功能每次读取一行都是从上一次读过的基础相加
# abc.execute('use pmys;')
# for i in range(1000):
   # abc.execute('create table haha(姓名 char(255),性别 char(255),年龄 int);')
   #  abc.execute('insert into haha values("{}","{}","{}");'.format('小缪','男',10,))
   #  abc.execute('select *from haha;')
# conn.commit()#提交(更新，删除，添加)（最好提交）
# a=abc.fetchone()
# b=abc.fetchone()
# print(a,b)
# # len(abc(fetchall())
# # abc.execute('show tables;')
# print(abc.fetchall())
# a=abc.fetchmany(10)
# print(a)#传入的参数是一个数字，数字是几就获取几条sql语句的结果
#断开连接conn.close()
# import pymysql
# room=pymysql.connect(host='192.168.1.19',port=3306,user='root',passwd='123456')
# mys=room.cursor()



#自带的模块，是与操作系统交互的
#通过os模块来控制操作
# import os
#删除文件
#os.remove('a.txt')
#执行windows命令
# b=os.popen('ping 192.168.1.11')
# print(b.read())
# b=os.popen('ipconfig/all')
# print(b.read())
#获取当前所在的位置
#print(os.getcwd())
#切换目录
# os.chdir(r'D:')
# print(os.getcwd())
#获取当前文件夹下面有多少文件(想看什么目录就在引号中间改)
# import re
# a=(os.listdir('.'))
# b=re.compile('(.*.py)')
# for i in a:
#     c=b.findall(i)
#     print(c)
# t=open('j.txt,''w')
# print(t)
#


#将文件与路径分隔开
# import os
# # a=os.path.split(r'c:\User\join\Desktop\abc.csv')
# # print(a)
# # #将文件后缀名跟与路径分隔开
# # a=os.path.splitext(r'c:\User\join\Desktop\abc.csv')
# # print(a)
#
# #判断是否是个目录
# # c=os.path.isdir('aaa')
# # print(c)
# #判断文件是否是个普通文件
# # d=os.path.isfile('room.py')
# # print(d)
# #
# #
# #创建文件夹
# # os.mkdir('aaa')
# #创建递归文件夹
# # os.makedirs('bbb/ccc/vvv')
# #删除空文件夹
# # os.rmdir('aaa')
# #删除递归文件夹
# # os.removedirs('bbb/ccc/vvv')
# #封装ssh协议可实现远程控制
# # import paramiko
#
# #包和模块的区别
# #模块；是一个.py的文件，，分装的代码
# #包：是一个目录，分装的是模块，必须含有__init_.py文件
# #面向对象跟面向过程的区别
# # 面向对象:将函数分类分装,使开发更高效 易扩展 易维护 性能低
# # 面向过程:一步一步的实现解决问题的步骤 性能高  不易扩展
# # import paramiko
# # #创建一个客户端
# # ssh123=paramiko.SSHClient()
# # #跳过验证,不到know_hosts文件中去查找
# # ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # #连接主机
# # ssh123.connect(hostname='192.168.1.19',port=22,username='root',password='123456')
# # #执行命令
# # # a=stuin=执行的命令(只能执行有结果的命令)
# # # b=stuout=执行的结果
# # # c=stuerr=执行的报错
# # while True:
# #     i=input('请输入语句:')
# #     a,b,c=ssh123.exec_command(i)
# #     print(b.read().decode())
# #     if i=='exit':
# #         ssh123.close()
# #         break
# #
# # #用paramiko传输文件
# #建立一个传输通道
# # ssh123=paramiko.Transport(('192.168.1.19',22))
# # sftp=paramiko.SFTPClient()
# # #连接主机
# # ssh123.connect(username='root',password='123456')
# #创建一个sftp的客户端
# # sftp=paramiko.SFTPClient.from_transport(ssh123)
# #从linux上下载文件到windows
# #要下载文件
# # sftp.get('anaconda-ks.cfg','aaa.cfg')
# #从window上上传文件到linux
# # ftp.put(r'day2.py','/home/day1.py')
# # sssh123.close()
#
#
# # import smtplib                 #封装了smtp协议
# # import email.mime.multipart    #处理邮件中的组成部分
# # import email.mime.text         #处理邮件中的正文
# #
# # #定义一个发件人
# # fr ='mys15225453394@163.com'
# # #定义一个收件人
# # res='18317822978@163.com'
# # #服务器
# # server='smtp.163.com'
# # #授权码:授予登录客户端的权限的密码
# # passwd='mys5209'
# # #创建一个空邮件
# # message=email.mime.multipart.MIMEMultipart()
# # #给邮寄里添加一个发件人
# # message['From']=fr
# # #添加一个收件人
# # message['To']=res
# # #添加邮件主题
# # message['Subject']='python learn'
# # #写的邮件正文
# # text="河南印花护肤 \n 我是安徽人"
# # #处理正文
# # txt=email.mime.text.MIMEText(text)
# # message.attach(txt)
# # # 添加附件(附加的文件)
# # att2 = email.mime.text.MIMEText(open('b.xls', 'rb').read(), 'base64', 'utf-8')
# # att2["Content-Type"] = 'application/octet-stream'
# # att2["Content-Disposition"] = 'attachment; filename="abc_new1.html"'
# # ## 头部字段
# # message.attach(att2)
# #
# # #定义一个服务器
# # smtp123=smtplib.SMTP_SSL(server,465)
# # #登录服务器
# # smtp123.login(fr,passwd)
# # #发送邮件
# # smtp123.sendmail(fr,res,message.as_string())
# # import xlwt
# # with open('t..txt','r',encoding='utf-8') as f:
# #     a=f.readlines()
# # ff=xlwt.Workbook(encoding='utf-8')
# # sheet=ff.add_sheet('mys')
# # for i in range(len(a)):
# #     k=a[i].split(',')
# #     for j in range(len(k)):
# #         sheet.write(i,j,k[j])
# # ff.save('t.xls')
# # import xlrd
# # f=xlrd.open_workbook('t.xls')
# # sheet=f.sheets()[0]
# # num=sheet.nrows
# # with open('p.txt','w',encoding='utf-8') as ff:
# #       for i in range(num):
# #           i=sheet.row_values(i)
# #           for j,k in enumerate(i):
# #               if j==len(i)-1:
# #                   ff.write(k)
# #               else:
# #                   ff.write(k+',')
# #判断字符串是否回文
# #
# # a=input('请输入一串字符:')
# # for i in range(len(a)//2):
# #     if a[i]!=a[-i-1]:
# #         print('不是回文')
# #         break
# # else:
# #     print('是回文')
# # import pymysql
# # conn=pymysql.connect(host='',user='',passwd='',passwd='')
# # abc=conn.cursor('create database pmys')
#
# #服务器
#
# #socket:套接字,提供了通信双方最底层的功能（发送，接受）
# #tcp/ip  通信
# #两台主机实现通信(server 端)
# import socket
# #创建一个套接字，创建一个有接受能力和发送能力的
# #默认使用tcp,(SOCK_STREAM)     UDP(SOCK_DGRAM)
# #使用的是ipv4和tcp协议
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #绑定ip地址和端口
# s.bind(('192.168.1.10',30))#接收的是个元组
# #监听服务有没有开启
# s.listen(5)   #最大等待个数
# while True:
#     #接受建立连接
#     #第一个值是建立链接的信息 第二个值是客户端的ip地址和端口号
#     client,addr=s.accept()
#     # print(client)
#     # print(addr)
#     #接受客户端发送的请求
#     #1024每次接受的最大数据
#     msg=client.recv(1024)
#     print(msg.decode('utf-8'))
#     #发送响应
#     reg=input('<<<')
#     client.send(reg.encode('utf-8'))
#
# import r""''''"e import requests headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'} def parse_douyin(url): r = requests.get(url, allow_redirects=True) redirecturl = r.url rct = requests.get(redirecturl, headers=headers) playurl = re.findall('playAddr:(.*?)\,', str(rct.text))[0] playurl = playurl.replace('playwm', 'play') playurl = playurl.replace("\"", "") print(playurl) # 请求要下载的url地址 html = requests.get(playurl) # content返回的是bytes型也就是二进制的数据。 html = html.content print(html) try: with open('D:/douyin.mp4', 'wb') as f: f.write(html) f.flush() print("下载完成！！！！") except: print("下载失败！！！！") if __name__ == '__main__': url = 'http://v.douyin.com/JkNaor/' parse_douyi
# str='runoob'
# print(str[-1:
# a1 #b=1 #b=2
#     print(b) #b=1 #b=1 #b=2
#     a,b=b,a+b #a=1 b=0+1=1 #a=1 b=2 #a=2 b=2+
# python3--version
# help()#Jinru交互模式

# import smtplib
# import email.mime.multipart
# import email.mime.text
# fr='mys15225453394@163.com'
# res='1763396139@163.com'
# server='smtp.163.com'
# passwd='mys5209'
# message=email.mime.multipart.MIME.Mulitpart()
# message['From']=fr
# message['To']=res
# message['subject']='python learn'
# a=3.1415926e8
# print(1,2,3,seq=',')
# import requests
# import json
# import unittest

# url = "http://120.132.8.33:9000/api/Account/LoginByPhone"
#
# payload = "{\n    \"phone\": \"15993835273\",\n    \"password\": \"111111\",\n    \"zone\": \"86\",\n    \"loginType\": 0,\n    \"isAuto\": 0,\n    \"deviceId\": \"ec:89:14:54:93:007\"\n}"
# headers = {
#     'Content-Type': "application/json",
#     'PhoneInfo':'{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
#     'AppInfo':'{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
#     'Language': "zh_CN",
#     'APIVersion': "3.0",
#     'accessToken': "6116d5cb49f14897937f95cd7e5002ef",
#     'User-Agent': "PostmanRuntime/7.11.0",
#     'Accept': "*/*",
#     'Cache-Control': "no-cache",
#     'Postman-Token': "acfc3b1a-e92c-457a-8c1b-9bb740fbc9c9,f2654bae-916e-45dc-bf37-a03f5ec0d187",
#     'Host': "120.132.8.33:9000",
#     'accept-encoding': "gzip, deflate",
#     'content-length': "149",
#     'Connection': "keep-alive",
#     'cache-control': "no-cache"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
# res=response.text
# msg=json.loads(res)
# if msg['code']==0:
#      print('成功')
#res=response.json()
#if res['code']==0:
 #   print('成功')
# class qwe(unittest.TestCase):
#     def test_1(self):
#         a=4+5
#         print(123)
#         self.assertEqual(a,9)
#     def test_2(self):
#         b=6-5
#         print(456)
#         self.assertEqual(b,1)
#     def setUp(self):#执行每一个测试用例前都要执行一次 初始化测试环境
#
#         print('开始')
#     def tearDown(self):#执行每个测试用例之后都要执行一次 清理测试环境
#         print('结束')
# if __name__=='__main__':
#     #统一测试测试的函数必须以test开头否则不执行
#      unittest.main()
import unittest
import xlrd
import requests
import HTMLTestRunner #产生测试报告
def execl():
    ff=xlrd.open_workbook("mm.xls")
    sheet=ff.sheets()[0]
    mm=[sheet.row_values(i) for i in range(sheet.nrows)]
    return mm
class denglu(unittest.TestCase):
    kk=execl()
    def deng(self,user,password):
        url = "http://120.132.8.33:9000/api/Account/LoginByPhone"
        payload ='{"phone":"%s","password":"%s","zone": "86","loginType": 0,"isAuto": 0,"deviceId":"ec:89:14:54:93:007"}'%(user,password)
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language':"zh_CN",
            'APIVersion':"3.0",
            'accessToken':"6116d5cb49f14897937f95cd7e5002ef",
            'User-Agent':"PostmanRuntime/7.11.0",
            'Accept': "*/*",
            'Cache-Control':"no-cache",
            'Postman-Token':"d0fed1e3-e0a6-4928-87cb-1356d8e4cad6,1e099271-fb9c-4696-9f1d-0f262aeab353",
            'Host':"120.132.8.33:9000",
            'accept-encoding':"gzip, deflate",
            'content-length':"149",
            'Connection':"keep-alive",
            'cache-control':"no-cache"
            }
        response = requests.request("POST", url, data=payload, headers=headers)
        res=response.json()
        return res
    def setUp(self):
        print('open')
    def tearDown(self):
        print('close')
    def test_1(self):
        aa=self.deng(int(self.kk[0][0]),int(self.kk[0][1]))
        self.assertEqual(aa['code'],0)
    def test_2(self):
        bb=self.deng(int(self.kk[1][0]),int(self.kk[1][1]))
        self.assertNotEqual(bb['code'],0)
if __name__ == '__main__':
    # unittest.main()
#创建一个测试套件
    suit=unittest.TestSuite()
#方法一#添加用例将测试用例添加到测试套件中
   # suit.addTest(denglu('test_1'))
    #suit.addTest(denglu('test_2'))
#方法二#将denglu类中所有以test开头的函数都添加到测试套件中
    suit.addTests(unittest.makeSuite(denglu))
#打开一个空文件
    f=open('abc.html','wb')
#定义测试报告的信息
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='接口测试报告',tester='缪永生',description='结果如下')
#执行测试套件
    runner.run(suit)
    f.close()


#两个参数1，路径 2 参数
#dis=unittest.defaultTestLoader.discover()

























