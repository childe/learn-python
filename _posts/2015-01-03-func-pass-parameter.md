---
layout: post
title:  "函数-传参"
date:   2015-01-03 15:03:25 +0800
---

参数在函数定义的圆括号对内指定，用逗号分割。当我们调用函数的时候，我们以同样的方式提供值。
> 我们使用过的术语——函数中的参数名称为 形参 而你提供给函数调用的值称为 实参 。

每一个参数都有一个名字, 这种传参叫做关键参数. 可以结合下面的kargs使用.


```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def add(x, y):  # 普通的传参
    """传进来的第一个参数就是x,第二个参数就是y"""
    print "x=%s,y=%s" % (x, y)
    return x+y


def power(base, exponent=2):  # 默认参数,没有默认值的参数一定要写在前面
    """调用的时候,base一定要传进来.
exponent可以传或者不传. 不传的时候, exponent就是2"""
    return base ** exponent

def request(host, port=80, path="/"):  # 再来一个
    return '%s:%s%s' % (host, port, path)

print add(10, 20)
print add(y=10, x=20)
print power(10)
print power(10, 3)
print request('www.ctrip.com')
print request('www.ctrip.com', path="/login")
```

运行结果:

```
% python passparam.py
x=10,y=20
30
x=20,y=10
30
100
1000
www.ctrip.com:80/
www.ctrip.com:80/login
```

# args, kargs
有时候, 函数可能需要传递未知个数的参数, 比如说对所有参数求和,可能是对两个数求和, 也可能是对10个.

对于kargs的使用, 常见于一个函数中再调用另外一个函数, 或者是所有参数存在于一个已经存在的字典中, 我一直也想不到比较好的例子. 到后面的修饰器我们会再给比较实际的例子.

大家看例子理解下吧:


```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mysum(scale, *args):  # args
    return sum(args)*scale

print mysum(2, 1, 2, 3, 4, 5)
print mysum(2, *range(5))


def f(**kargs):  # kargs
    print type(kargs)
    print kargs

# 想不到合适的例子, 简单感受下
f(x=1, y=2, z=3)
d = dict(x=1, y=2, z=3)
f(**d)


def f(scale, *args, **kargs):  # args, kargs混合的
    print scale
    print args
    print kargs

f(1,*range(5),**d)
```

运行结果:

```
30
20
<type 'dict'>
{'y': 2, 'x': 1, 'z': 3}
<type 'dict'>
{'y': 2, 'x': 1, 'z': 3}
1
(0, 1, 2, 3, 4)
{'y': 2, 'x': 1, 'z': 3}
```
