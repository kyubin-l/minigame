import itertools


numbers = list(range(1, 10))
target = 21
num_cells = 3

result = [seq for seq in itertools.combinations(numbers, num_cells)
          if sum(seq) == target]

print(result)