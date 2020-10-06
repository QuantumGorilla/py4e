import re
text = open("regex_sum_843083.txt")
numbers = list()
for line in text:
    number = re.findall('[0-9]+',line)
    numbers += number
sum = 0
for i in numbers:
    sum += int(i)
print(sum)