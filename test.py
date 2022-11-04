import itertools


numbers = list(range(1, 10))
target = 39
num_cells = 6

result = [seq for seq in itertools.combinations(numbers, num_cells)
          if sum(seq) == target]

temp = []
for option in result:
    temp += list(option)


print(set(temp))

