# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print:
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print:
# Longest substring in alphabetical order is: abc

s = 'azcbobobegghakl'

p1 = 0
p2 = 1
length = len(s)
longest = ''

for p2 in range (1, length):
  if ord(s[p2]) >= ord(s[p2 - 1]):
    if len(s[p1:p2 + 1]) > len(longest):
        longest = s[p1:p2 + 1]
    continue
  elif len(s[p1:p2]) > len(longest):
    longest = s[p1:p2]
    p1 = p2
  else:
    p1 = p2
print('Longest substring in alphabetical order is: ' + longest)
