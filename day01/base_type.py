# 这是一个注释
# model  模块
# main 主要的
# print 打印
# def 声明方法
# int 整数
# demo 例子
# return 返回
# 代码的层级关系 通过 缩进来表示
# class 类,类型
# str string 字符
# 合法标识符(变量名方法名) : 必须以字母或者_开头,剩下的可以是字母数字,下划线,大小写敏感, 不可用关键字做标识符
# ctrl+alt+L 格式化代码
# ctrl+K  commit 代码
# ctrl + shift + K  push 代码

# 声明一个int_demo 方法
# def int_demo():
#     # 声明aint变量 , 并赋值 1
#     aint = 1
#     # 打印 aint 的值
#     print(aint)
#     # 打印 aint 的 类型; type(aint): 获取aint的类型
#     print(type(aint))
#
#
# # 声明一个 str_demo 方法
# def str_demo():
#     # 声明astr变量 , 并赋值 '1'
#     astr = '1'
#     # 打印 astr 的值
#     print(astr)
#     # 打印 astr 的 类型; type(astr): 获取astr的类型
#     print(type(astr))
#
#     # 不写
#     print('--------------')
#     astr = 1
#     # 打印 astr 的值
#     print(astr)
#     # 打印 astr 的 类型; type(astr): 获取astr的类型
#     print(type(astr))

# 演示字符串拼接 : +
def str_demo1():
    a= 'hello'
    b= ' world'
    return a+b

# 字符串拼接: %s
def str_demo2():
    a= 'hello '
    b= 250
    # print(a+ str(b))
    print('a 是 : %s;b 是 : %s'%(a,b))

# 去掉两头空格
def str_demo3():
    astr = ' ysl '
    # astr 是变量 也叫 对象  ,对象 . 可以调用对象的方法
    print(astr)
    print(astr.strip())


# 12
# 声明一个add 方法 参数有两个 aint,bint
def add(aint, bint):
    # 打印aint参数
    print(aint)
    # 打印bint参数
    print(bint)
    # 返回 aint+bint
    return aint + bint

# 声明一个 float_demo 方法
def float_demo():
    # 声明afloat变量 , 并赋值 1.90
    afloat = 1.90
    # 打印 afloat 的值
    print(afloat)
    # 打印 afloat 的 类型; type(afloat): 获取afloat的类型
    print(type(afloat))

if __name__ == '__main__':
    print(str_demo1())
    # str_demo2()
    # print(str_demo1())
    # float_demo()
    # str_demo()
    # int_demo()
    # 提取变量  ctrl+alt+V
    # 调用add方法 传入1, 2,得到返回值 ,赋值给result变量
    # 指定参数传参
    result = add(bint=2,aint=1)
    # print(result)
    # 默认参数传参
    # add(2,1)
    pass

# 全局变量 和 局部变量 作用域不同,

# 声明全局变量 blist
blist = [7,8,33,2,1,3,4]

def list_demo():
    # alist 是局部变量
    alist = [4, 'ysl', '8', 7]

    print(alist)
    # 通过索引访问 元素
    print(alist[0])
    print(alist[1])
    # 倒序访问
    print(alist[-1])
    print(alist[-2])
    # 打印全局变量 并没有被传参blist
    print(blist)

def global_list():
    print(blist)


# 更新列表中的元素
def list_update(alist):
    alist[0] = 1
    print(alist[0])
    print(alist)

# 切片操作
def list_update1(alist):
    # 从索引2 的位置 取 到索引5
    print(alist[2:6])
    # 从索引0 的位置 取 到索引5
    print(alist[:6])
    # 从索引3 的位置 取 到索引末尾
    print(alist[3:])

# 索引 和 下标值 是从0开始数,所以取值的时候小一位
# 获取长度,size,是从1开始数,有几个元素, 就是几
def len_demo(alist):
    # len() 获取变量的长度
    print(len(alist))
    print(len(blist))

# 删除方法 list.pop()
def pop_demo(alist):
    # pop()方法两个作用 第一个取出最后一位的值,第二个从列表中删除取出的值
    print(alist.pop())
    print(alist)
    # pop()带参数 ,参数被用作 下标值/索引 , 两个作用 第一个取出下标值代表的元素,第二个从列表中删除取出的元素
    alist.pop(4)
    print(alist)

# 讲列表排序的方法
def orderBy_demo():
    print('调用正序排的方法')
    sort_demo()
    print('调用倒序排的方法')
    reverse_demo()
    pass

# 正序方法
def sort_demo():
    # 将blist 正序排
    blist.sort()
    print(blist)

# 倒序方法
def reverse_demo():
    # 将blist 倒序排
    blist.reverse()
    print(blist)

# 瞎写的
def xiaxie(alist):
    alist_5 = alist[4]
    alist__1 = alist[-1]
    alist[4]=alist__1
    alist[-1] = alist_5
# 列表/集合
if __name__ == '__main__':
    alist = [4, 'ysl', '8', 7,6,2,5]
    # 这是方法调用了 局部变量 alist
    # list_update1(blist)
    # 这个方法调用了 全局变量 blist
    # list_update1(blist)
    # print(blist)
    # list_demo()
    # len_demo(alist)
    # pop_demo(alist)
    # orderBy_demo()
    alist.append(9999)

    # print(alist)
    print(type(None))