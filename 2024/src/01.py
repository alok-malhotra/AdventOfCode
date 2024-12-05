# Part One
list_one, list_two = [], []
total_distance = 0 

# Part Two
list_two_freq = {}
similarity_score = 0

# Scanning
with open('2024/input/01.txt', 'r') as file:
    for line in file:
        nums_as_strs = line.strip().split(" ")
        curr_line = [int(nums_as_strs[0]), int(nums_as_strs[-1])]
        list_one.append(curr_line[0])
        list_two.append(curr_line[1])
        list_two_freq[curr_line[1]] = list_two_freq.get(curr_line[1], 0) + 1

# Part One
list_one.sort()
list_two.sort()

for i in range(len(list_one)):
    total_distance += abs(list_one[i] - list_two[i])

print("Total Distance: {0}".format(total_distance))

# Part Two
for i in range(len(list_one)):
    num_occurences = list_two_freq.get(list_one[i], 0)
    similarity_score += list_one[i] * num_occurences

print("Part Two: {0}".format(similarity_score))