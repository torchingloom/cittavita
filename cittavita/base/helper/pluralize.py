# -*- coding: utf-8 -*-

def pluralize(value, arg=u"один,два,ноль/много"):
    args = arg.split(",")
    if not value:
       return args[2]
    number = abs(int(value))
    a = number % 10
    b = number % 100
    if (a == 1) and (b != 11):
        return args[0]
    elif (a > 1) and (a < 5) and ((b < 10) or (b > 20)):
        return args[1]
    else:
        return args[2]