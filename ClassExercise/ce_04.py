# Group Member:
# 1. Wang Xinyu 1098648
# 2. Li Yiran 1098339
#
# Tutorial 02

pNumber = int(input('Please enter a positive number: '))

while pNumber <= 0:
    print('The number must be POSITIVE, try again.')
    pNumber = int(input('Please enter a positive number: '))


def isMultipleOf234(n):
    return (n // 2) * 2 == n and (n // 4) * 4 == n and (n // 3) * 3 == n

if isMultipleOf234(pNumber):
    print('The number {0} is multiple of 2,3,4'.format(pNumber))
else:
    print('The number {0} is not a multiple of 2,3,4'.format(pNumber))

print('End of Program')