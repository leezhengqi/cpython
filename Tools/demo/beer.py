#!/usr/bin/env python3

"""
A Python version of the classic "bottles of beer on the wall" programming
example.

By Guido van Rossum, demystified after a version by Fredrik Lundh.
"""

import sys

n = 100
#以下两行代码用来表示：当程序外部有参数输入时，使用外部输入的参数（因为外部输入的参数可能是多个，可被看作是一个列表，sys.argv[0]指代的是这个程序本身，sys.argv[1:]则表示
#从索引1开始到列表最后，sys.argv[1]的意思是提取列表中第1个元素），此外部输入参数是处于CMD命令窗口时输入使用（如：c:\>test1.py 2 3）
if sys.argv[1:]:
    n = int(sys.argv[1])

def bottle(n):
    if n == 0: return "no more bottles of beer"
    if n == 1: return "one bottle of beer"
    return str(n) + " bottles of beer"

for i in range(n, 0, -1):
    print(bottle(i), "on the wall,")
    print(bottle(i) + ".")
    print("Take one down, pass it around,")
    print(bottle(i-1), "on the wall.")
