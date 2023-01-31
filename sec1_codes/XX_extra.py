# or operator
a = 0b110
b = 0b001

print(a | b)  # 111


# or operator
feature_1 = 0b100
feature_2 = 0b001
feature_3 = 0b010

print("{0:b}".format(feature_1 | feature_2 | feature_3))  # 111




# callback functions
def func(message): # consumer
    print(message)


def caller(callback): # library designer
    # SOME LONG TASK
    callback("I'm done")

print(func)
caller(func)
