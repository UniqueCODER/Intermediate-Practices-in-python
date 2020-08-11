import  re

file_name = open('regex_sum_733736.txt')
lst = list()
sum_of_all_values = 0
for x in file_name:
    reg = re.findall('[0-9]+',x)
    lst = lst + reg
for values in lst:
    sum_of_all_values = sum_of_all_values + int(values)
print(sum_of_all_values)