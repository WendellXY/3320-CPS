# Group Member:
# 1. Wang Xinyu 1098648
# 2. Li Yiran 1098339
#

grade = int(input("What's your grade number?"))

result = 'DND' # Does Not Define

if grade > 65 and grade < 70:
    result = 'C'
elif grade > 85 and grade < 90:
    result = 'B+'

print(result)