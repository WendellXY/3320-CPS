import re

string1 = 'abb29ABCLK%1CnrDBCabbbb'

print(re.search(r'abbbb', string1).span())

print(re.search(r'ab{4}', string1).span())

# The regular expression could be directly 'abbbb' or 'ab{4}'. The first one means matching the whole string
# 'abbbb' and the last one means find the string which starts with 'a' and followed four 'b'.