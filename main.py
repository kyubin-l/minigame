import pandas as pd
from classes import WhiteBox, Task
import itertools

data = pd.read_excel('Numbers puzzle.xlsx', sheet_name=None, header=None)
table = data['Puzzle']

num_rows = len(table.axes[0])
num_columns = len(table.axes[1])

print(table)

for row in range(num_rows):
    for col in range(num_columns):
        value = table.iloc[row, col]

        if (row == 0) or (col == 0):
            if not pd.isna(value):
                tasks = value.split(' ')
                for task in tasks:
                    task = Task(task, row, col)
                    task.evaluate_text()
        else:
            if pd.isna(value):
                whitebox = WhiteBox(row, col)
            elif type(value) == int:
                whitebox = WhiteBox(row, col)
                whitebox.final_value = value
            else:
                tasks = value.split(' ')
                for task in tasks:
                    task = Task(task, row, col)
                    task.evaluate_text()


for task in Task.all_tasks:
    if task.direction == 'd':
        for x in range(task.x+1, num_rows):
            whitebox = WhiteBox.find_whitebox(x, task.y)
            if whitebox == None:
                break
            else:
                task.related_whiteboxes.append(whitebox)
                whitebox.related_task.append(task)

    if task.direction == 'r':
        for y in range(task.y+1, num_columns):
            whitebox = WhiteBox.find_whitebox(task.x, y)
            if whitebox == None:
                break
            else:
                task.related_whiteboxes.append(whitebox)
                whitebox.related_task.append(task)


# Find all possible numbers for a whitebox using its two tasks
def find_options(target_sum, num_cells):
    numbers = list(range(1, 10))
    result = [seq for seq in itertools.combinations(numbers, num_cells)
              if sum(seq) == target_sum]

    temp = []
    for option in result:
        temp += list(option)

    return set(temp), result


# Remove the final values from all other neighboring cells once the
# final value for a cell is set.
def remove_neighbor_option(finalbox):
    # remove an option for all neighbouring boxes once a final value is chosen
    for r_task in finalbox.related_task:
        for w_box in r_task.related_whiteboxes:
            if finalbox.final_value in w_box.options:
                w_box.options.remove(finalbox.final_value)


for box in WhiteBox.all_whiteboxes:
    all_options = []
    for task in box.related_task:
        options = find_options(task.value, len(task.related_whiteboxes))
        box.combinations.append(options[1])
        all_options.append(options[0])

    box.options = all_options[0].intersection(all_options[1])
    if len(box.options) == 1:
        # print(box.x, box.y)
        box.final_value = next(iter(box.options))



# while None in [WhiteBox.all_whiteboxes[i].final_value for i in range(51)]:
#     print([WhiteBox.all_whiteboxes[i].final_value for i in range(51)])

# If a cell's final value is determined, check if it just has one neighbor, if so assign sum - final value
# to that neighbour. At the same time we remove the final values from all other neighboring cells once a
# final value is set.
for box in WhiteBox.all_whiteboxes:
    if box.final_value is not None:
        box.options = set()
        remove_neighbor_option(box)
        for t in box.related_task:
            if len(t.related_whiteboxes) == 2:
                for white_box in t.related_whiteboxes:
                    if white_box is not box:
                        white_box.final_value = t.value - box.final_value
                        remove_neighbor_option(white_box)
                        white_box.options = set()

    # for box in WhiteBox.all_whiteboxes:
    #     if len(box.options) == 1:
    #         box.final_value = next(iter(box.options))



# Some print statements to see outputs
i = 45
box = WhiteBox.all_whiteboxes[i]
print(WhiteBox.all_whiteboxes[i].x, WhiteBox.all_whiteboxes[i].y)
print(box.options)
print(box.related_task[0].value)
print(box.related_task[1].value)
print(box.combinations)


print([WhiteBox.all_whiteboxes[i].options for i in range(51)])
print([WhiteBox.all_whiteboxes[i].final_value for i in range(51)])





# print([(whitebox.x, whitebox.y) for whitebox in WhiteBox.all_whiteboxes])
# print(WhiteBox.all_whiteboxes)

# print(WhiteBox.find_whitebox(2, 2))
# print(Task.all_tasks[15].__dict__)
# print([(whitebox.x, whitebox.y) for whitebox in Task.all_tasks[15].related_whiteboxes])


