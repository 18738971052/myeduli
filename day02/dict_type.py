
import json
# 声明一个全量 dict 变量 (字典)

adict = {"name":"ysl","pwd":"123456"}

# 这是一个字符串 不过他是json 格式 ,也是字典的格式
adictStr = '{"name":"ysl","pwd":"123456"}'

def zhuanhuanleixin():
    print(type(adictStr))
    dict_str = json.loads(adictStr)
    print(type(dict_str))
    print(dict_str['name'])

if __name__ == '__main__':
    # print(adict)
    # adict.pop('name')
    # print(adict['name'])
    # print(adict)
    print(type(adict))
    print(type(adictStr))
    # str --> dict
    # json.loads(adictStr) 按 Ctrl+alt+V  返回值
    loads = json.loads(adictStr)
    print(type(loads))

    # dict --> str
    json_dumps = json.dumps(adict)
    print(type(dumps))