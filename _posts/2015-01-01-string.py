---
layout: post
title:  "变量"
date:   2015-01-01 15:33:54 +0800
---

# 变量的定义

```py
i = 100 # 整数
f = 3.14 # 浮点数
s = "this is a string" # 字符串
b = True # 布尔
n = None # None
print i
print f
print s
print b
print n
```

# 数字

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = 5
b = 6

print a, b

a = a+1
print a  # 6

a += 2
print a  # 8

print a**2  # 64
print a  # 8

a **= 2
print a  # 64

print a/b  # 10. notice!
print divmod(a, b)  # 10 4
```

2. 字符串

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""============字符串定义============"""
s1 = 'this is a string'  # 单引号包裹
print "s1", s1

s2 = "this is a string"  # 双引号包裹
print "s2", s2

print s1 == s2  # True. 他们是一样一样的

s3 = "I am the first line;\nI am a new line"
print "s3", s3

s4 = "\\n means a new line"
print "s4", s4

s5 = r"\n means a new line"
print "s5", s5
print s5 == s4  # True. 他们是一样一样的

# 三个单引号或者双引号包裹
s6 = """I am the first line;
I am a new line"""
print "s6", s6
print s3 == s6  # True. 他们是一样一样的


"""============字符串操作============"""
s = "abcdefg1234567"
# 切片
print s[0]  # a
print s[len(s)-1]  # 7
print s[-1]  # 7
print s[1:7]  # bcdefg
print s[1:]  # bcdefg1234567
print s[1:-1]  # bcdefg123456
print s[:]  # abcdefg1234567
print s[::2]  # aceg246
print s[::-1]  # 7654321gfedcba


# format
print '{}'.format("a", "b", name="liujia")  # a
print '{},{},{name}'.format("a", "b", name="liujia")  # a,b,liujia
print '{1},{name},{0}'.format("a", "b", name="liujia")  # b,liujia,a

# liujia,66.12
print '%s,%0.2f' % ("liujia", 66.123)

# liujia,66.12
print '%(name)s,%(score)0.2f' % {"name": "liujia", "score": 66.123}

# list all oprations
print "list all str oprations:"
print ', '.join([e for e in dir(s) if not e.startswith('_')])

s = "this is a sentence"
print s.capitalize()  # This is a sentence
print s.title()  # This Is A Sentence
print s.lower()
print s.upper()

print s.count("is")  # 2
print s.count("is", 4)  # 1. same with below
print s[4:].count("is")  # 1

# index与find作用一样, 区别在于找不到子字符串的时候, index抛出异常, find返回-1
print s.index("s")  # 3
print s.find("s")  # 3
print s.index("s", 4)  # 6
print s.find("s", 4)  # 6
print s.rindex("s")  # 10
try:
    print s.index("z")
except Exception as e:
    print e  # substring not found
print s.find("z")  # -1

print s.center(40, '*')  # ***********this is a sentence***********
print s.ljust(40, "*")  # this is a sentence**********************
print s.rjust(40, "*")  # **********************this is a sentence
print s.zfill(40)  # 0000000000000000000000this is a sentence

print s.partition(" is ")  # ('this', ' is ', 'a sentence')
print s.split()  # ['this', 'is', 'a', 'sentence']
print s.split(" ", 1)  # ['this', 'is a sentence']. 只分割一次
print s.rsplit(" ", 1)  # ['this is a', 'sentence']
"""If sep is not specified or is None, any
    whitespace string is a separator and empty strings are removed
    from the result.
"""
print 'this is a  sentence'.split()  # ['this', 'is', 'a', 'sentence']
print 'this is a  sentence'.split(" ")  # ['this', 'is', 'a', '', 'sentence']

print s.startswith("this")  # True
print s.endswith("e")  # True

s1 = "  abcd   ".strip()
print s1, len(s1)  # abcd 4
s2 = "  abcd   ".rstrip()
print s2, len(s2)  # abcd 4
s3 = "* abcd ** *".strip(" *")
print s3, len(s3)  # abcd 4


# 字符串不可更改
s = "this is a sentence"
s = "T" + s[1:]
print s  # This is a sentence
s[1] = 'T'  # Error
```



3. 布尔

4. None
