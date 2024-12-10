import copy
from datetime import datetime as dt


disk_map = ''
# Read input
t_0 = dt.now()
with open('2024/input/9.txt', 'r') as file:
    for line in file: disk_map = line.rstrip()

block_representation, curr_num = [], 0 # For Part A
block_spans, indices_of_open_pos, count = {}, [], 0 # For Part B

for i in range(len(disk_map)):
    if i % 2 == 0: # Even index, use curr_num
        block_spans[curr_num] = [count, count + int(disk_map[i]) - 1]
        count += int(disk_map[i])
        for j in range(int(disk_map[i])):
            block_representation.append(curr_num)
        curr_num += 1
    else: # Odd index, add periods
        if int(disk_map[i]) != 0:
            indices_of_open_pos.append( [count, count + int(disk_map[i]) - 1] )
        count += int(disk_map[i])
        for j in range(int(disk_map[i])):
            block_representation.append(None)

block_representation_ = copy.deepcopy(block_representation) # For Part B

t_a_s = dt.now()
reading_input_completion_time = (t_a_s - t_0).total_seconds()
print("Reading input took: {0} seconds\n".format(reading_input_completion_time))

# Part A
l, r = 0, len(block_representation) - 1

while (l <= r):
    if block_representation[l] == None and block_representation[r] != None:
        block_representation[l], block_representation[r] = block_representation[r], block_representation[l]
        l, r = l + 1, r - 1
    elif block_representation[l] == None and block_representation[r] == None:
        r = r - 1
    elif block_representation[l] != None and block_representation[r] != None: 
        l = l + 1
    else:
        l, r = l + 1, r - 1

filesystem_checksum = 0
for i in range(len(block_representation)):
    if block_representation[i] != None:
        filesystem_checksum += i * int(block_representation[i])

print("Part A: {0}".format(filesystem_checksum))
t_a_e = dt.now()
part_a_completion_time = (t_a_e - t_a_s).total_seconds()
print("Time for Part A: {} seconds\n".format(part_a_completion_time))


# Part B
t_b_s = dt.now()
for key, span in reversed(list(block_spans.items())):
    for indices in indices_of_open_pos:
        if indices[0] > span[0]: 
            break
        open_slot_size = indices[1] - indices[0] + 1
        span_size = span[1] - span[0] + 1
        if open_slot_size >= span_size:
            slot_insert_start = indices[0]
            slot_insert_end = indices[0] + span_size
            for j in range(slot_insert_start, slot_insert_end):
                block_representation_[j] = key
            for j in range(span[0], span[1] + 1):
                block_representation_[j] = None
            if open_slot_size == span_size:
                indices_of_open_pos.remove(indices)
            else:
                indices[0] = indices[0] + span_size
            break

updated_checksum = 0
for i in range(len(block_representation_)):
    if block_representation_[i] != None:
        updated_checksum += i * block_representation_[i]

print("Part B: {0}".format(updated_checksum))
t_b_e = dt.now()
part_b_completion_time = (t_b_e - t_b_s).total_seconds()
print("Time for Part B: {} seconds\n".format(part_b_completion_time))
