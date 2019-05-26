# 一个很正常的函数
def func(val):
    print('value is: ', val)
    pass


# 一个稀奇古怪的函数
def xixi():
	# 语法错误
    xsdisudiskjfkdjfkdjfkdfjkdjfdkfjk


# 一个缩进略多的函数，缩进是为了代替大括号？区分语法块
def func1(val):
    if val >= 5:
        print('>5')


def func2():
	val = 5
	print(type(val))
	val = 'a'
	print(type(val))	


if __name__ == '__main__':
	value = 5
	func(value)

	# # 动态指啥
	# xixi()
	# func2()
	del value
	func(value)