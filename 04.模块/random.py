# 1.将列表随机打乱位置
'''
random.shuffle(x[, random])¶
将序列 x 随机打乱位置。

random.shuffle(x[, random])
将序列 x 随机打乱位置。

可选参数 random 是一个0参数函数，在 [0.0, 1.0) 中返回随机浮点数；默认情况下，这是函数 random() 。

要改变一个不可变的序列并返回一个新的打乱列表，请使用``sample(x, k=len(x))``。

请注意，即使对于小的 len(x)，x 的排列总数也可以快速增长，大于大多数随机数生成器的周期。 这意味着长序列的大多数排列永远不会产生。 例如，长度为2080的序列是可以在 Mersenne Twister 随机数生成器的周期内拟合的最大序列。
'''
# 2.
'''
random.sample(population, k)
返回从总体序列或集合中选择的唯一元素的 k 长度列表。 用于无重复的随机抽样。
'''

'''
random.choice(seq)
从非空序列 seq 返回一个随机元素。 如果 seq 为空，则引发 IndexError。

random.choices(population, weights=None, *, cum_weights=None, k=1)
从*population*中选择替换，返回大小为 k 的元素列表。 如果 population 为空，则引发 IndexError
'''