---
layout: post
title:  "hello python"
date:   2015-01-01 15:23:50 +0800
---

- Hello 1

简单的打印一句话

    ```py
    print "hello, python"
    ```

- Hello 2

接受键盘输入, 并输出

    ```py
    msg  = raw_input("hello,")
    print msg
    ```

- Hello 3

打印出程序运行时跟的参数

    ```py
    import sys
    msg  = sys.argv[1:]
    print ' '.join(msg)
    ```

- Hello 4

第一行 代表用哪个程序来解释这个脚本  
第二行 说明这个脚本用什么编码保存的  
第三行 定义一个函数,叫做main   
第四行 打印一句话, u代表请把后面这个字符串用utf8编码  
第五行 如果是直接运行的这个脚本, 而不是被别的程序引用, 执行main函数

    ```py
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    def main():
        print u"你好,python"
    if __name__ == '__main__':
        main()
    ```
