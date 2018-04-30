# 假设班里有3名同学：Adam，Lisa和Bart，他们的成绩分别是 95.5，85 和 59，请按照 名字, 分数, 名字, 分数... 的顺序按照分数从高到低用一个list表示，然后打印出来。
# l=['Adam','95.5','Lisa','85','Bart','59']
# print(l)

# 三名同学的成绩可以用一个list表示：
# L = [95.5, 85, 59]
# # 请按照索引分别打印出第一名、第二名、第三名，同时测试 print L[3]。
# L = [95.5, 85, 59]
# print(L[0])
# print(L[1])
# print(L[2])
# print(L[3])

# 三名同学的成绩可以用一个list表示：
# L = [95.5, 85, 59]
# 请按照倒序索引分别打印出倒数第一、倒数第二、倒数第三。
# L = [95.5, 85, 59]
# print(L[-1])
# print(L[-2])
# print(L[-3])

# 假设新来一名学生Paul，Paul 同学的成绩比Bart好，但是比Lisa差，他应该排到第三名的位置，请用代码实现。
# l=['Adam','Lisa','Bart']
# l.insert(2,'Paul')
# print(l)

# 注意右边编辑器代码中 list 如下：
# L = ['Adam', 'Lisa', 'Paul', 'Bart']
# Paul的索引是2，Bart的索引是3，如果我们要把Paul和Bart都删掉，请解释下面的代码为什么不能正确运行：
# L.pop(2)
# L.pop(3)
# 怎样调整代码可以把Paul和Bart都正确删除掉
# L = ['Adam', 'Lisa', 'Paul', 'Bart']
# L.pop(2)
# L.pop(2)

# 班里的同学按照分数排名是这样的：
# L = ['Adam', 'Lisa', 'Bart']
# 但是，在一次考试后，Bart同学意外取得第一，而Adam同学考了倒数第一。
# 请通过对list的索引赋值，生成新的排名。
# L = ['Adam', 'Lisa', 'Bart']
# L[0]='bart'
# L[2]='Adam'
# print(L)


# 创建一个tuple，顺序包含0 - 9这10个数。
# A = (0,1,2,3,4,5,6,7,8,9)
# print(A)

# 请指出右边编辑器中代码为什么没有创建出包含一个学生的 tuple：
# t = ('Adam')
# print t
# 请修改代码，确保 t 是一个tuple。
# t = ('Adam',)
# print(t)

# 定义了tuple：
# t = ('a', 'b', ['A', 'B'])
# 由于 t 包含一个list元素，导致tuple的内容是可变的。能否修改上述代码，让tuple内容不可变？
t = ('a', 'b', 'A', 'B')
print(t)