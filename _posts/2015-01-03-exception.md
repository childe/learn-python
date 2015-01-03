---
layout: post
title:  "异常"
date:   2015-01-03 10:26:06 +0800
---

# 异常示例
## Exception 1
引入了不存在的模块

```py
import simplejson
```
运行结果:

```
% python e1.py                                                              ✭
Traceback (most recent call last):
  File "e1.py", line 1, in <module>
    import simplejson
ImportError: No module named simplejson
```

## Exception 2
除数是0.

```py
print 1/0
```

运行结果:

```
% python e2.py
Traceback (most recent call last):
  File "e2.py", line 1, in <module>
    print 1/0
ZeroDivisionError: integer division or modulo by zero
```

## Exception 3
字典中没有这个key

```py
d ={
    "liujia":28,
    "zn":29
}

print d['trh']
```

运行结果:

```
% python e3.py
Traceback (most recent call last):
  File "e3.py", line 6, in <module>
    print d['trh']
KeyError: 'trh'
```

# 捕获异常
有时候, 我们知道这块代码中可能会有异常, 比如我们要取的key有可能不在字典中, 或者除数有可能为0, 或者我们要引用的模块不存在. 

这时我们不希望程序就地崩溃, 而是能够捕获这个异常, 进而处理这个异常, 比如把值置为None,或者把相除的结果置为最大整数, 或者引用另外一个相似的模块,然后再错误打印到日志中, 最后让程序继续进行下去.

```py
try:
    import simplejson as json
except:
    import json
print  json

try:
    n = 1/0
except:
    n = 0xffffffff
print n

d ={
    "liujia":28,
    "zn":29
}
try:
    print d['trh']
except:
    print None
```

运行结果:

```
% python handle.py
<module 'json' from '/Users/liujia/Applications/anaconda/lib/python2.7/json/__init__.pyc'>
4294967295
None
```

# Else Finally

```py
d = {
    "liujia": 28,
    "zn": 29
}

try:
    age = d['trh']
except IOError as e:
    print "Exception occured"
    print type(e), str(e)
except KeyError as e:
    print "Exception occured"
    print type(e), str(e)
else:
    print "Other type of Exception occured"
finally:
    print "print this no matter what happend"
```

运行结果:

```
% python elsefinally.py                                                     ✭
Exception occured
<type 'exceptions.KeyError'> 'trh'
print this no matter what happend
```

# 抛出自己的异常

```py
d ={
    "liujia":28,
    "zn":29
}

name = "trh"

if name not in d:
    raise Exception("we lost trh's age")
else:
    print d['trh']
```

运行结果:

```
% python raiseException.py                                                  ✭
Traceback (most recent call last):
  File "raiseException.py", line 12, in <module>
    raise Exception("we lost trh's age")
Exception: we lost trh's age
```
