# 步长 j

# 遍历一个list
def list_bianli():
    # 声明一个alist
    alist = ['啊', '第三方', '尔尔', '玩儿']
    # 将alist 放入循环, 循环次数由 list 的长度来决定, 第一次循环
    for i in alist:
        print("--遍历")
        print(i)
        print(i + '__hello')

def nei_xunhuan():
    for i in range(5):
        print('hello word')
        for j in range(2):
            print('内循环')

# 打印 九九乘法表
def chenfabiao():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%s X %s = %s ' %(i,j,i*j),end=' ')
        print('     ')
        # print('')

# 基础 if else 语法演示
def if_demo():
    a = False
    if a:
        print('a 是 对的')
    else:
        print('a 是 错的')

# 判断 a 和 b的大小
def if_demo1():
    a = 10
    b = 20
    if a>b:
        print('a 大于 b')
    else:
        print('a 小于 b')

# 输出 比较大的值
def if_demo2():
    a = 10
    b = 20
    if a>b:
        print(a)
    else:
        print(b)

def elif_demo():
    a = 4
    if a == 2:
        print('第1个if')
    elif a == 3:
        print('第2个if')
    elif a == 1:
        print('第3个if')
    else:
        print('else 分支')

# 将 1到50 的奇数 加起来
def jishu_add():
    nub = 0
    for i in range(1, 51):
        if i % 2 != 0:
            nub = nub + i
    print(nub)

# 写一个方法,传入两个 int参数, 将两个参数之间的 偶数加起来
def oushu_add(a,b):
    num = 0
    if a>b:
        b = b + 1
        for i in range(b,a):
            if i%2 ==0:
                num = num+i
    elif a<b:
        a= a+1
        for i in range(a,b):
            if i%2 ==0:
                num = num+i
    else:
        print('两值相等')

    print(num)



if __name__ == '__main__':
    a=0
    while True:
        print(a)
        a+=1
    pass

