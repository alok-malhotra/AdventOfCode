from datetime import datetime as dt


list_one, list_two = [], []
total_distance = 0

list_two_freq = {}
similarity_score = 0

# Read input
t_0 = dt.now()
with open('2024/input/1.txt', 'r') as file:
    for line in file:
        nums_as_strs = line.strip().split(" ")
        curr_line = [int(nums_as_strs[0]), int(nums_as_strs[-1])]
        list_one.append(curr_line[0])
        list_two.append(curr_line[1])
        list_two_freq[curr_line[1]] = list_two_freq.get(curr_line[1], 0) + 1

t_a_s = dt.now()
reading_input_completion_time = (t_a_s - t_0).total_seconds()
print("Reading input took: {0} seconds\n".format(reading_input_completion_time))

# Part A
list_one.sort()
list_two.sort()

for i in range(len(list_one)):
    total_distance += abs(list_one[i] - list_two[i])

print("Part A: {0}".format(total_distance))
t_a_e = dt.now()
part_a_completion_time = (t_a_e - t_a_s).total_seconds()
print("Time for Part A: {} seconds\n".format(part_a_completion_time))


# Part B
t_b_s = dt.now()
for i in range(len(list_one)):
    num_occurences = list_two_freq.get(list_one[i], 0)
    similarity_score += list_one[i] * num_occurences

print("Part B: {0}".format(similarity_score))
t_b_e = dt.now()
part_b_completion_time = (t_b_e - t_b_s).total_seconds()
print("Time for Part B: {} seconds\n".format(part_b_completion_time))
