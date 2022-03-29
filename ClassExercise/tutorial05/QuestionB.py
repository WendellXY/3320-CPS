import re

string1 = 'abb29ABCLK%1CnrDBCabbbb'

print(re.search(r'[A-Z][a-z]+', string1))
print(re.search(r'[A-Z][a-z]+', string1).span())

# [A-Z] means match all Uppercase character and [a-z] means matching all lowercase characters, and the plus sign
# `+` means matching several times.
# In summary, the regular expression [A-Z][a-z]+ means:
# Matching a string that starts with an UPPERCASE character and followed by serval (more than 0) lowercase characters