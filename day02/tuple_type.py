#import json
# 元组类型 和list 一样的访问
# 元组只能被读取 ： 只读

# 声明一个元组类型的全局变量
#atuple = (1,3,5,7,8,4,6,9)



#if __name__ == '__main__':
    # 元组不可悲修改
    #rint()
    #atuple[0] = 5
    #json.loads(atuple)


#import json
# 声明一个全量 dict 变量 (字典)

#adict = {"name":"ysl","pwd":"123456"}

# 这是一个字符串 不过他是json 格式 ,也是字典的格式
#adictStr = '{"name":"ysl","pwd":"123456"}'

#def zhuanhuanleixin():
    #print(type(adictStr))
    #dict_str = json.loads(adictStr)
   #print(type(dict_str))
    #print(dict_str['name'])

#if __name__ == '__main__':
    # print(adict)
    # adict.pop('name')
    # print(adict['name'])
    # print(adict)
    #print(type(adict))
    #print(type(adictStr))
    # str --> dict
    #loads = json.loads(adictStr)
    #print(type(loads))

    # dict --> str
    #dumps = json.dumps(adict)
    #print(type(dumps))
    #dumps = json.dumps(loads, ensure_ascii=false)
    #print(json_dumps)


def jisuan(a,b):
    print(a+b)
    print(a - b)
    print(a * b)
    print(a / b)

if __name__ == '__main__':
    a = 10
    b = 3
    c = 10
    print(a>b)
    print(a < b)
    print(a == c)
    print(a == b)

from day01 import base_type

if __name__ == '__main__':
    result = base_type.add(4, 5)
    print(result)



# 元组类型 与 list 一样的访问方式;元组中的元素不可以被更改
# 元组只可以被读取 ; 只读

# 声明一个元组类型的全局变量
atuple = (1,23,5,2,3)

if __name__ == '__main__':
    # 元组不可以被修改
    print(atuple[0])
    atuple[0] = 5


# 取余

def jisuan(a,b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)

def duibi(a,b,c):
    print(a > b)
    print(a < b)
    print(a == b)
    print(a == c)
    print(a >= b)
    print(a != b)

def deng(a):
    a += 1  # a = a+1
    print(a)
    a *= 2  # a = a*2
    print(a)
    a -= 5  # a = a-5
    print(a)
    a /= 2  # a = a/2
    print(a)

if __name__ == '__main__':

