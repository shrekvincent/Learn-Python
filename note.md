Python Learning Note
https://www.anaconda.com/products/individual
使用anaconda管理平台下载python3.7

课工场 Python基础课
IDE:
PyCharm 最流行的ide客户端
功能强大 
适合开发复杂项目

Jupyter NoteBook
交互式笔记本
非常适合数据分析领域
有一定的基础

将Pycharm 与Anaconda 关联，可以使用Anaconda自带的包
就是在创建工程的时候注意添加anaconda的python编译器
Python 变量
变量y:用于存储数据
Python 变量的命名规则
由字母、数字、下划线组成
不能以为数字开头
不能使用Python关键字
英文字母大小写敏感

Python运算符
赋值运算符 =
算数运算符 加+  减-  乘*  除/
比较运算
大于>
小于<
...
等于==
不等于!=

Python 字符串
一组可以包含数字、字母、符号的集合
''  "" 等价，嵌套使用可以避免使用转义符
字符串拼接  +  
混合拼接  new_str = '%s%d%f'%(a_str, a_int, a_float)
print(new_str)

字符串内键方法
upper()/lower将英文字符设置大/小写 string = '你好Python'
print(string.upper())

去除字符串首尾空格
lstrip()将字符串最左边空格去掉
rstrip()将字符串最右边空格去掉
strip()将字符串首尾空格去掉
...
拆分字符串
split()
string = 'Hello&Python'
print(string.split('&'))
查找子字符串位置  
find()一旦匹配，立即返回
string = 'Hello Python 3'
print(string.find('Py'))
字符串替换
replace()  所有的都替换
获取字符串长度
len() 

类型转换
判断类型
type()
类型转换函数
转换为字符串  str()
转换为浮点型 float()
转换为整型   int()

print()方法
print()默认换行
print(str,end='')


条件判断（按顺序判断，前面满足，后面不再判断）
if 条件判断
if 条件1：
    语句块1
elif 条件2：
    语句块2
else：
     语句块3

循环
用于解决大量数据的处理
   设置循环条件，遍历数据
for 循环：遍历表达式全部的值
for item in sequence:
   循环操作
range(num1,num2)
遍历[num1,num2)左闭右开
for y in range(4, 20):
    print(y, end = " ")

Python的行缩进
Python用行缩进来区分代码块
缩进方式不一致：indentationError:unindent does not match any outer indentation level
格式错误，可能是TAB和空格没对齐的问题
IndentationError:undexpected indent

循环嵌套：
for/while 可以相互嵌套
条件判断语句和循环可以相互嵌套

循环控制：
循环控制语句可以改变循环正常的执行顺序
循环控制语句
break语句 跳出整个循环
continue 跳出当前循环，不执行后续，接着下一个循环
循环控制语句只对最近的循环起作用

集合
集合的使用场景
网购的订单、与商品ID
Python内置类型
List  Tuple(只读的List)  Dictionary
for循环可以用来遍历表达式
for item in list:
使用索引


添加列表
list.append(obj)
list.insert(index, obj)
删除列表
del List[index]

元组（tuple）
与列表类似，不同之处在于元组的元素不能修改
创建元组
元组 = （元素1，元素2，...）
ppp = (123, 122.5,'mayun')


字典
一种可变容器模型，且可存储任意类型对象
创建字典
字典 = {键1：值1， 键2：值2}
dict = {"ali":"马云","腾讯":"马化腾"}
for item in dict:
    print(item)
for value in dict.values():
    print(value)
for key,value in dict.items():
    print(key + '：' + value)

字典的操作
print(dict['ali'])  打印马云
相同键，后面会覆盖前面

添加修改字典红的值
dict['ali']= 'wangxiaoer'
删除字典中的值
del dict['腾讯']

判断键是否存在于字典中
k in dict


集合
储存形式与列表相似
    集合中保存的数据具有唯一性，不可重复
    集合中保存的数据是无序的
    往集合中添加重复数据，集合将只保留一个
集合常被用来去重或者过滤
创建集合
    集合 = set()
        add()方法添加元素
    集合 = {123,122.5,'马云'}

函数
有组织的、可重复使用的代码块
用于执行一个单一的、相关动作的代码块
函数的使用

定义函数
def 函数块（参数列表）：
    函数代码块
    [return]
调用函数
[变量]=函数名（传入的参数）
注意事项
向前引用：必须先定义，在引用或调用
return 可以终止函数，也可以给函数一个返回值

有参函数
参数列表-定义函数
    形参
参数列表-调用函数
    实参
传入函数的参数个数必须和定义的参数个数一致

匿名函数


迭代器  生成器
可迭代对象
list tuple dict str
for item in X:
生成器
yield

def get_even(n):
    for i in range(n):
        if i % 2 == 0
            yield i

for item in get_even(19):
    print(item)

Python 程序调试
逻辑错误
单步调试
    设置断点
    Debug模式启动
    监控变量
Python异常处理
认识常见异常类型
理解异常处理机制
掌握Try-except处理异常
掌握Try-except-finally处理异常

常见异常
NameError 使用未申明变量
ZeroDivisionError 除数为0
SyntaxError 程序出现语法错误
IndexError 访问序列中不存在的
KeyError 键不存在
BaseException 程序运行，遇到任何异常


认识最常见的文件类型：
.CSV   逗号分隔的值，与表格类似  CSV、pandas.read_csv()
.json  网上传输结构数据，解析后类似字典与列表的嵌套 json
        pandas.read_json()
.xlsx  电子表格格式  pandas.read_excel()
.zip    压缩文件   zipfile
.txt    纯文本格式  open()
.xml    扩展标记语言，具有编码数据规则  xml






Django
console下：pip install virtualenv
各种报错


爬虫
基于B/S模式的数据采集技术
按照一定的规则，自动地抓取外围网信息的程序
关于爬虫
    以一个或多个页面为爬取起点
    从页面中提取链接实现深度爬取

爬虫举例
    第三方抢票软件
    机器学习（微软小冰/百度机器人）
    数据调研

爬虫在做什么
    网络请求
    网页解析
        目标数据抓取
        爬取驱动逻辑
    数据保存

Scarpy爬虫框架
什么是框架
    一个半成品的软甲项目
    实现了软件的基础功能
    规定了一系列实现功能的规则和接口
框架的优势
    提高开发效率
    专注于业务逻辑的实现
Scarpy：
一款基于Python语言的爬虫框架
上手简单
多线程，爬取效率高
简介高效

配置环境：（scrapy）
Anaconda prompt 命令行：scrapy
安装好之后将 Anaconda prompt 下的Scrpts路径添加到环境变量path下面
win+r cmd命令行输入:scrapy 出现版本信息证明环境变量修改成功
命令行:scrapy startproject 工程名称
进入到自己创建的文件夹目录下
命令行：cd 工程名称
命令行：scrapy genspider spiderexample www.qq.com
然后用Pycharm启动工程
命令行:scrapy crawl spiderexample (启动爬虫)

让pycharm能够debug scrapy
script path:  D:\Softwarsetup\SoftWare\Anaconda\Lib\site-packages\scrapy\cmdline.py
paremeters:
crawl spiderexample
working directory:
C:\Users\27367\SCRAPY\ScrapyExample
