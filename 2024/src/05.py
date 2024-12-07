from datetime import datetime as dt

nums_after_rules = {}
updates = []
update_toggle = False

# Read input
t_0 = dt.now()
with open('2024/input/5.txt', 'r') as file:
    for line in file:
        if line == '\n':
            update_toggle = True
        else:
            if update_toggle:
                updates.append([ int(x) for x in line.split(',') ])
            else:
                num_one, num_two = line.split('|')
                num_one, num_two = int(num_one), int(num_two)
                nums_after_rules[num_one] = nums_after_rules.get(num_one, [])
                nums_after_rules[num_one].append(int(num_two))

t_a_s = dt.now()
reading_input_completion_time = (t_a_s - t_0).total_seconds()
print("Reading input took: {0} seconds\n".format(reading_input_completion_time))

# Helper Function
def validate_update(update: list, swap: bool) -> bool:
    for i in range(1, len(update)):
        curr_num = update[i]
        for j in range(0, i):
            curr_iter = update[j]
            if curr_iter in nums_after_rules[curr_num]:
                if swap:
                    update[i], update[j] = update[j], update[i]
                else:
                    return False
    return True

invalid_updates = [] # Part B Variable Created in Part A
# Part A
middle_value_valid_updates_sum = 0
for update in updates:
    if validate_update(update, False):
        n = len(update)
        middle_value_valid_updates_sum += update[int(n/2)]
    else:
        invalid_updates.append(update)

print("Part A: {0}".format(middle_value_valid_updates_sum))
t_a_e = dt.now()
part_a_completion_time = (t_a_e - t_a_s).total_seconds()
print("Time for Part A: {} seconds\n".format(part_a_completion_time))


# Part B
t_b_s = dt.now()
middle_value_invalid_updates_sum = 0

for update in invalid_updates:
    validate_update(update, True)
    n = len(update)
    middle_value_invalid_updates_sum += update[int(n/2)]

print("Part B: {0}".format(middle_value_invalid_updates_sum))
t_b_e = dt.now()
part_b_completion_time = (t_b_e - t_b_s).total_seconds()
print("Time for Part B: {} seconds\n".format(part_b_completion_time))
