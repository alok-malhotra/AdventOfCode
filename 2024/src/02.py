from datetime import datetime as dt
from helpers.h02 import *


reports = []
safe_reports_a, safe_reports_b = 0, 0

# Read input
t_0 = dt.now()
with open('2024/input/2.txt', 'r') as file:
    for line in file:
        reports.append([int(x) for x in line.split()])

t_a_s = dt.now()
reading_input_completion_time = (t_a_s - t_0).total_seconds()
print("Reading input took: {0} seconds\n".format(reading_input_completion_time))

# Part A
for report in reports:
    if report[0] > report[-1]:
        if is_strictly_dec(report):
            safe_reports_a += 1
    if report[0] < report[-1]:
        if is_strictly_inc(report):
            safe_reports_a += 1
        # If we reach this point, the first and last value were equal, and this report is not safe by default

print("Part A: {0}".format(safe_reports_a))
t_a_e = dt.now()
part_a_completion_time = (t_a_e - t_a_s).total_seconds()
print("Time for Part A: {} seconds\n".format(part_a_completion_time))


# Part B
t_b_s = dt.now()
for report in reports:
    if report[0] == report[-1]:
        if is_strictly_dec(report[1: len(report)]) or is_strictly_dec(report[0: len(report) - 1]):
            safe_reports_b += 1
        elif is_strictly_inc(report[1: len(report)]) or is_strictly_inc(report[0: len(report) -1]):
            safe_reports_b += 1
    if report[0] > report[-1]:
        if is_strictly_dec_one_error_allowed(report):
            safe_reports_b += 1
    if report[0] < report[-1]:
        if is_strictly_inc_one_error_allowed(report):
            safe_reports_b += 1

print("Part B: {0}".format(safe_reports_b))
t_b_e = dt.now()
part_b_completion_time = (t_b_e - t_b_s).total_seconds()
print("Time for Part B: {} seconds\n".format(part_b_completion_time))
