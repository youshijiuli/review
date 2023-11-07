# 输入某年某月某日，判断这一天是这一年的第几天？
# 使用datetime 模块：https://docs.python.org/zh-cn/3.6/library/datetime.html#datetime.datetime

'''
datetime的子类关系

object
    timedelta    # 用来做算数运算的，比如两个日期的差，就是这个类型
    datetime     # datetime 对象是一个包含了来自 date 对象和 time 对象所有信息的单一对象
                  class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)  
                  默认可以到达秒

    time         # class datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
    date         # class datetime.date(year, month, day)

根据表示时间的粗细，我们应该选择的是 date    
'''

import datetime

def now_day():
    print("清楚输入一个具体的年月日，中间用空格隔开")
    year, month, day = tuple(input().split(" "))
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    date2 = datetime.date(year=int(year), month=1, day=1)
    delta = date1 - date2
    print(delta)
    print(type(delta))
    print(type(delta.days))   # 转化为整数 int
    print("相聚天数为：", delta.days + 1) 
    '''
    属性
    days

    -999999999 至 999999999 ，含999999999

    seconds

    0 至 86399，包含86399

    microseconds

    0 至 999999，包含999999
    '''
    # <class 'datetime.timedelta'>

now_day()

