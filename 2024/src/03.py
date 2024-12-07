import re
from datetime import datetime as dt


matches = []

# Read input
t_0 = dt.now()
with open('2024/input/3.txt', 'r') as file:
    for line in file:
        line_matches = re.findall(r"(mul\(\d+,\d+\)|(do\(\))|(don't\(\)))", line)
        for match in line_matches: matches.append(match[0])

t_ab_s = dt.now()
reading_input_completion_time = (t_ab_s - t_0).total_seconds()
print("Reading input took: {0} seconds\n".format(reading_input_completion_time))

# Part A and B
sum_of_products_a = 0
sum_of_products_b, use_product = 0, True

for match in matches:
    if match == 'do()':
       use_product = True
    elif match == 'don\'t()':
       use_product = False
    else:
        match = match.replace('mul(', '')
        match = match.replace(')', '')
        numbers = [ int(x) for x in match.split(',') ]
        sum_of_products_a += numbers[0] * numbers[1]
        sum_of_products_b += numbers[0] * numbers[1] if use_product else 0

print("Part A and B: {0}, {1}".format(sum_of_products_a, sum_of_products_b))
t_ab_e = dt.now()
part_ab_completion_time = (t_ab_e - t_ab_s).total_seconds()
print("Time for Part A and B: {} seconds\n".format(part_ab_completion_time))