# Group Member:
# 1. Wang Xinyu 1098648
# 2. Li Yiran 1098339

name = input("What is your name?\n")
age = int(input("What is your age?\n"))
address = input("What is your address?\n")
favSport = input("What is your favorite sport?\n")

ret = "Hello, my name is {0}.\nI am {1} years.\nI live in {2}.\nI like to play {3}"
print(ret.format(name, age, address, favSport))