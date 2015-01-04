---
layout: post
title:  "对象和引用"
date:   2015-01-04 11:49:37 +0800
---

在Python中, 一切都是对象.

person是一个对象, 数字5也是一个对象, 字符串"ABCD"也是.

每个对象都存在于内存, 我们用id(person)可以得到它在内存的中的地址(其实不是内存中的地址, 只是可以大概这么认为), 如果两个对象的id是一样的, 那么他们其实就是同一个变量.

两个变量, x y. 如果他们只是值一样的话, 满足x == y.  
如果他们指向同一块内存, 还满足 x is y

# 初步印象

- 两个变量指向同一个对象

    比如说 

    ```py
    d1 = {1:1,2:4}
    d2 = {1:1,2:4}
    print "id(d1):", id(d1)
    print "id(d2):", id(d2)I
    # 值一样, 但不是同一个东西
    print d2 == d1  # True
    print d2 is d1  # False

    d2 = d1
    print "id(d1):", id(d1)
    print "id(d2):", id(d2)
    print d2 == d1  # True
    #d2和d1就是同一个东西, 他们指向同一块内存
    print d2 is d1  # False
    ```

- 一个更新, 另一个跟着变化 

    ```py
    del d[1]
    #如果del d1[1], d2也会跟着变.
    print d2
    ```

- 重新赋值呢?

    如果对d1重新赋值呢? d2会跟着变化吗?  不会.

    ```py
    d1 = {}
    print d2
    ```

    上面这段程序可以证明, 把d1重新赋值了空字典, d2还是原来的内容.


# 发生了什么

[whathappend.py]

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 内存中创建了一个字典对象, 并把d1指向这块内存
d1 = {1: 1, 2: 4}

# d2和d1是同一个东西, 他们指向同一块内存, 就是引用的概念. d2是d1的引用, 其实也可以反过来说, d1是d2的引用.
d2 = d1
print "id(d1):", id(d1)
print "id(d2):", id(d2)
print id(d1) == id(d2)  # True


print "="*20, "del d1[1]",  "="*20
del d1[1]  # 在这块内存上进行数据操作, 是个self update. d1 d2还是指向这块内存.
print "d2:", d2
print "id(d1):", id(d1)
print "id(d2):", id(d2)
print id(d1) == id(d2)  # True


print "="*20, "对d1新赋值",  "="*20
d1 = {}  # 在内存中重新生成一个空字典对象, 把d1指向这块内存
print "d2:", d2
print "id(d1):", id(d1)  # d1的地址变化了
print "id(d2):", id(d2)  # d2还是指向原来的地址
print id(d1) == id(d2)  # False
```

运行结果:

```
% python whathappened.py
id(d1): 4300471264
id(d2): 4300471264
True
==================== del d1[1] ====================
d2: {2: 4}
id(d1): 4300471264
id(d2): 4300471264
True
==================== 对d1新赋值 ====================
d2: {2: 4}
id(d1): 4300477824
id(d2): 4300471264
False
```

# 数字字符串  数组字典等数组结构

数字和字符串有些特别.

## 先说数字

python启动的时候, 已经为M以下的小数字预先分配了内存, 因为python认为这些数字是经常被用到的, 频繁的创建和销毁会浪费资源. M的范围是[-5, 257)

**d1 = {1:1,2:4}; d2 = {1:1,2:4}** 是运行时创建了两个对象, 虽然值相同, 但不是同一个对象.  
**x = 10; y = 10** 是把xy都指向了早就创建好的同一个数字对象


## 再来说下字符串
字符串不是开始就初始化好的, 是程序中定义的时候临时创建的. 但python会把创建的字符串放在一个缓冲池里面.  之后创建相同字符串的时候, 就会直接返回.    

所以**x ="abcd"; y ="abcd"** xy是同一个对象, 也就是 x is y

参考[http://search.aol.com/aol/search?q=python+%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%AF%B9%E8%B1%A1+%E5%88%9D%E5%A7%8B%E5%8C%96+%E5%86%85%E5%AD%98](http://search.aol.com/aol/search?q=python+%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%AF%B9%E8%B1%A1+%E5%88%9D%E5%A7%8B%E5%8C%96+%E5%86%85%E5%AD%98)


# 嵌套

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

pool = {
    "department": {
        "organization_id": 43,
        "alias": "\u673a\u7968",
        "name": "FLT"
        },
    "productline": {
        "organization_id": 43,
        "alias": "\u673a\u7968",
        "name": "FLT"
        },
    "pool": {
        "pool_type": "0",
        "id": 350,
        "name": "gds.engine.flight"
        },
    "servers": [
        {
            "ip": "10.8.89.60",
            "hostname": "VMS01860",
            "idc": "SHAJQ"
            },
        {
            "ip": "10.8.89.59",
            "hostname": "VMS01859",
            "idc": "SHAJQ"
            },
        {
            "ip": "10.8.89.58",
            "hostname": "VMS01858",
            "idc": "SHAJQ"
            }
        ]
}

# 这里并没有生成新的对象! 
# 只是把department指向了pool["department"]这个已经存在的东西.
department = pool["department"]

department["organization_id"] = 44

print pool  # department.organization_id变化了
```

# 传参
前面讲全局变量的时候, 我们知道下面的函数不能改变n的值.

```py
def testfunc(n):
    n = 2
    print n
```

如果传的参是个字典, 我们对字典update, 函数过后, 会不会改变传的这个参数? 

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def info_supplement(pool):
    if len(pool['servers']) >= 20:
        pool['big'] = True
    else:
        pool['big'] = False

def main():
    pool = {
        "department": {
            "organization_id": 43,
            "alias": "\u673a\u7968",
            "name": "FLT"
        },
        "productline": {
            "organization_id": 43,
            "alias": "\u673a\u7968",
            "name": "FLT"
        },
        "pool": {
            "pool_type": "0",
            "id": 350,
            "name": "gds.engine.flight"
        },
        "servers": [
            {
                "ip": "10.8.89.60",
                "hostname": "VMS01860",
                "idc": "SHAJQ"
            },
            {
                "ip": "10.8.89.59",
                "hostname": "VMS01859",
                "idc": "SHAJQ"
            },
            {
                "ip": "10.8.89.58",
                "hostname": "VMS01858",
                "idc": "SHAJQ"
            }
        ]
        }
    info_supplement(pool)

if __name__ == '__main__':
    main()
```

## 不想在函数在改变对象的值, 只想返回一个新的对象

```py
def func(obj):
    newobj = obj[:]  # 列表. 注意不是元组,元组不能改变, 基本上不存在这个问题..
    newobj = obj.copy()  # 字典
    from copy import deepcopy
    newobj = deepcopy(obj) #列表 字典 或者其他对象
```
