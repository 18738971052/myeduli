import json
# 元组类型 和list 一样的访问
# 元组只能被读取 ： 只读

# 声明一个元组类型的全局变量
atuple = (1,3,5,7,8,4,6,9)



if __name__ == '__main__':
    # 元组不可悲修改
    print()
    atuple[0] = 5
    json.loads(atuple)





