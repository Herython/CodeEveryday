print("hello world")
for i in range(5):
    i += 2
    print(f"i = {i}")

'''
输出为：
hello world
i = 2
i = 3
i = 4
i = 5
i = 6

说明在for循环中，每再进一次循环，i会被range先赋值一次，所以i += 2 对循环的次数不会造成影响
'''