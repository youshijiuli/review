 # read、readline 和 readlines 的区别? 
# 主要考察的是 （文件对象的操作）https://docs.python.org/zh-cn/3.6/library/io.html#io.BytesIO

'''
read(size=-1)
从对象中读取 size 个字节并将其返回。 作为一个便捷选项，如果 size 未指定或为 -1，则返回所有字节直到 EOF。 在其他情况下，仅会执行一次系统调用。 如果操作系统调用返回字节数少于 size 则此方法也可能返回少于 size 个字节。

如果返回 0 个字节而 size 不为零 0，这表明到达文件末尾。 如果处于非阻塞模式并且没有更多字节可用，则返回 None。

readall()
从流中读取并返回所有字节直到 EOF，如有必要将对流执行多次调用

readline(size=-1)
从流中读取并返回一行。 如果指定了 size，将至多读取 size 个字节。

对于二进制文件行结束符总是 b'\n'；对于文本文件，可以用将 newline 参数传给 open() 的方式来选择要识别的行结束符

readlines(hint=-1)
从流中读取并返回包含多行的列表。 可以指定 hint 来控制要读取的行数：如果（以字节/字符数表示的）所有行的总大小超出了 hint 则将不会读取更多的行。

请注意使用 for line in file: ... 就足够对文件对象进行迭代了，可以不必调用 file.readlines()

'''

'''
read:读取整个文件。
readline：读取下一行，使用生成器方法。
readlines：读取整个文件到一个迭代器以供我们遍历。
'''