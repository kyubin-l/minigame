import pandas as pd
from classes import WhiteBox, Task
import itertools


data = pd.read_excel('Numbers puzzle.xlsx', sheet_name=None, header=None)
table = data['Puzzle']

num_rows = len(table.axes[0])
num_columns = len(table.axes[1])
solution = table.copy()

# print(table)

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
                whitebox = WhiteBox(row, col, value=0)
            elif type(value) == int:
                whitebox = WhiteBox(row, col, value=value)
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
                task.calculate_combinations()
                break
            else:
                task.related_whiteboxes.append(whitebox)
                whitebox.tasks.append(task)

    if task.direction == 'r':
        for y in range(task.y+1, num_columns):
            whitebox = WhiteBox.find_whitebox(task.x, y)
            if whitebox == None:
                task.calculate_combinations()
                break
            else:
                task.related_whiteboxes.append(whitebox)
                whitebox.tasks.append(task)


for task in Task.all_tasks:
    task.calculate_combinations()



def find_empty():
    for whitebox in WhiteBox.all_whiteboxes:
        if whitebox.value == 0:
            return whitebox
    return None


def solve():
    whitebox = find_empty()
    if not whitebox:
        return True

    for i in range(1, 10):
        if whitebox.is_valid(i):
            solution.iloc[whitebox.x, whitebox.y] = i
            # print(solution)
            if solve():
                return True

            whitebox.value = 0

    return False
solve()
print(solution)
print('---------------------------------')
# print(Task.all_tasks[0].all_combinations)
# print(Task.all_tasks[0].current_combination)


# print([task.all_combinations for task in Task.all_tasks])

# print([whitebox.value for whitebox in WhiteBox.all_whiteboxes])

# print([whitebox.x for whitebox in Task.all_tasks[0].related_whiteboxes])
# print([whitebox.y for whitebox in Task.all_tasks[0].related_whiteboxes])

# for whitebox in WhiteBox.all_whiteboxes:
#     print(whitebox, whitebox.tasks[0]._text, whitebox.tasks[1]._text)
#     print()
# task = WhiteBox.all_whiteboxes[0].tasks[1]
# # print(task.all_combinations)
