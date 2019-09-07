import math


def func(x,arr):
    y=0
    for i in arr:
        y=y+math.fabs(i-x)
    return y


def func_calc_absolute(arr):
    result=0
    count=0
    a=0
    for i in arr:
        x=func(i, arr)
        if count==0:
            a=x
            result=i
            count=+1
        elif x<a:
            a=x
            result=i
            
    return result


arr = [2,4,7,6,9]
print(func_calc_absolute(arr))