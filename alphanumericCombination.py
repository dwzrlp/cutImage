# -*- coding: UTF-8 -*-
'''
@author: mengting gu
@contact: 1065504814@qq.com
@time: 2020/11/3 下午9:04
@file: random_num.py
@desc:
    Get the combination of n numbers and upper and lower case letters.
'''

import random

n = 6


def v_code_nums_letters(n=6):
    """
        Returns:
            ret:random six num and letter
    """
    ret = ""
    for i in range(n):
        num = random.randint(0, 9)
        # num = chr(random.randint(48,57))#ASCII表示数字
        letter = chr(random.randint(97, 122))  # 取小写字母
        Letter = chr(random.randint(65, 90))  # 取大写字母
        s = str(random.choice([num, letter, Letter]))
        ret += s
    return ret


def v_code_letters(n=6):
    """
        Returns:
            ret:random six letter
    """
    ret = ""
    for i in range(n):
        letter = chr(random.randint(97, 122))  # 取小写字母
        Letter = chr(random.randint(65, 90))  # 取大写字母
        s = str(random.choice([letter, Letter]))
        ret += s
    return ret


def v_code_nums(n=6):
    """
        Returns:
            ret:random six num
    """
    ret = ""
    for i in range(n):
        num = random.randint(0, 9)
        s = str(random.choice([num]))
        ret += s
    return ret


print("v_code_nums_letters result: " + v_code_nums_letters())
print("v_code_letters result: " + v_code_letters())
print("v_code_nums result: " + v_code_nums())
