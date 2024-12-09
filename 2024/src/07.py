from datetime import datetime as dt
from helpers.h07 import *

calibration_equations = {}

# Read input
t_0 = dt.now()
with open('2024/input/7.txt', 'r') as file:
    for line in file:
        desired_value, params = line.rstrip().split(":")
        params = [int(x) for x in params.split(" ")[1:]]
        calibration_equations[int(desired_value)] = params

t_a_s = dt.now()
reading_input_completion_time = (t_a_s - t_0).total_seconds()
print("Reading input took: {0} seconds\n".format(reading_input_completion_time))


# Part A
total_calibration_result_a = 0
for value, params in calibration_equations.items():
    if can_make_value_a(value, params, params[0], 1, len(params)):
        total_calibration_result_a += value

print("Part A: {0}".format(total_calibration_result_a))
t_a_e = dt.now()
part_a_completion_time = (t_a_e - t_a_s).total_seconds()
print("Time for Part A: {} seconds\n".format(part_a_completion_time))


# Part B
t_b_s = dt.now()
total_calibration_result_b = 0
for value, params in calibration_equations.items():
    if can_make_value_b(value, params, params[0], 1, len(params)):
        total_calibration_result_b += value

print("Part B: {0}".format(total_calibration_result_b))
t_b_e = dt.now()
part_b_completion_time = (t_b_e - t_b_s).total_seconds()
print("Time for Part B: {} seconds\n".format(part_b_completion_time))
