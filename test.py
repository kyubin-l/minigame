import itertools


numbers = list(range(1, 10))
target = 8
num_cells = 3

result = [list(seq) for seq in itertools.permutations(numbers, num_cells)
          if sum(seq) == target]

print(result)