---
layout: post
title:  "函数:修饰器"
date:   2015-01-03 16:02:34 +0800
---
    
定义一个函数,叫做process_data,用来模拟处理数据,需要耗时3-5秒.
我们在项目的各处都调用了这个函数.

```py
def process_data():
    time.sleep(random.randint(3,5))
```

现在我们需要看一下函数调用开始时的时间, 和调用结束时的时间. 类似下面这样. OK, 搞定了.

```py
def process_data():
    print "start porcess data", time.time()
    time.sleep(random.randint(3,5))
    print "porcess data done!", time.time()
```

但是, 现在又有一个函数也需要打印开始和结束时间. 然后又有两个!   
我们不会在每一个函数里面添加这两个, 我们需要一个更好的办法.

来看一下用修饰器怎么实现. 我们只需要在每一个函数前面加一个 @print_time 就可以了.  
程序看起来更加清晰明了,意义明确.

```py
import random
import time


def print_time(func):
    def inner():
        print "start porcess data", time.time()
        func()
        print "porcess data done!", time.time()
    return inner


@print_time
def process_data():
    """定义一个函数,模拟处理数据,需要耗时3-5秒."""
    time.sleep(random.randint(3, 5))


process_data()
process_data()
process_data()
```

# 发生了什么事情?

其实, 函数前面添加修饰器, 相当于:
> process\_data = print\_time(process\_data)

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time


def print_time(func):
    def inner():
        print "start porcess data", time.time()
        func()
        print "porcess data done!", time.time()
    return inner


def process_data():
    """定义一个函数,模拟处理数据,需要耗时3-5秒."""
    time.sleep(random.randint(3, 5))

process_data = print_time(process_data)


process_data()
process_data()
process_data()
```


# 来一个更复杂的例子
我们在porcess_data的时候启用缓存, 如果缓存过期了, 我们需要重要加载数据到缓存.(都是模拟的..), 另外也需要打印开始和结束时间.

有哪些新东西:

1. 函数有多个修饰器.
2. 修饰器也有参数了. 
3. 修饰器中把args, kargs传递到内层的函数 

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time

last_update_time = None


def print_time(func):
    def inner(*args, **kargs):
        print "start porcess data", time.time()
        func(*args, **kargs)
        print "porcess data done!", time.time()
    return inner


def update_data():
    global last_update_time
    print "data expired; update it"
    last_update_time = time.time()


def use_cache(expire_time=30*60):
    def wrapper(func):
        if last_update_time is None or time.time() - last_update_time > expire_time:
            update_data()

        def inner(*args, **kargs):
            func(*args, **kargs)
        return inner
    return wrapper


@use_cache(5*60)
@print_time
def process_data(*args, **kargs):
    """定义一个函数,模拟处理数据,需要耗时3-5秒."""
    time.sleep(random.randint(3, 5))


process_data()
process_data()
process_data()
```

# 又发生了什么
> process\_data = use\_cache(5*60)(process\_data)
