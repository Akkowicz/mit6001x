# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

count = 0
s = 'azcbobobegghakl'

while True:
  pos = s.find('bob')
  if pos != -1:
    count += 1
    s = s[pos + 1:]
  else:
    break
print('Number of times bob occurs is: ' + str(count))
