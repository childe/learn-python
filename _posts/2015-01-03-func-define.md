---
layout: post
title:  "函数-定义"
date:   2015-01-03 14:23:29 +0800
---

我们把可以重用的程序段封闭在一个函数里面, 以后重用函数的时候,可以直接调用函数,而不是cCtrl+C, Ctrl+V。  
我们已经使用了许多内建的函数，比如len和range. 还有list, dict等对象的函数.

函数通过def关键字定义。def关键字后跟一个函数的 标识符 名称，然后跟一对圆括号。圆括号之中可以包括一些变量名，该行以冒号结尾。接下来是一块语句，它们是函数体。并且可以用return返回一个**或者多个**值.


```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 定义,传参,返回值
def add(x, y):
    """define一个函数,叫add, 需要两个参数x和y.
    这里只是定义,并不会执行."""
    return x+y

rst = add(10, 20)  # 这里函数执行
print rst


# 没有明确的返回值, 其实是返回了None
def hello():
    print "hello, python"

rst = hello()
print rst is None #True
```
