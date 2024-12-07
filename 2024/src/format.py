# ANY IMORTS HERE
# import {}
# from {} import {}
from datetime import datetime as dt

# DECLARE ANY GLOBAL VARS HERE
# x = y
# a = b

# Read input
t_0 = dt.now()
with open('<FILE_LOCATION>', 'r') as file:
    for line in file:
        continue # REPLACE THIS LINE WITH PARSING LOGIC

t_a_s = dt.now()
reading_input_completion_time = (t_a_s - t_0).total_seconds()
print("Reading input took: {0} seconds\n".format(reading_input_completion_time))

# Part A
# IMPLEMENT HERE


print("Part A: {0}".format("<PART_A_VAR_NAME>"))
t_a_e = dt.now()
part_a_completion_time = (t_a_e - t_a_s).total_seconds()
print("Time for Part A: {} seconds\n".format(part_a_completion_time))


# Part B
t_b_s = dt.now()
# IMPLEMENT HERE


print("Part B: {0}".format("<PART_B_VAR_NAME>"))
t_b_e = dt.now()
part_b_completion_time = (t_b_e - t_b_s).total_seconds()
print("Time for Part B: {} seconds\n".format(part_b_completion_time))
