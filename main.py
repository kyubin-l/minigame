import pandas as pd
from classes import WhiteBox, Task

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
                # whitebox.related_blackboxes.append(task)

    if task.direction == 'r':
        for y in range(task.y+1, num_columns):
            whitebox = WhiteBox.find_whitebox(task.x, y)
            if whitebox == None:
                break
            else:
                task.related_whiteboxes.append(whitebox)
                # whitebox.related_blackboxes.append(task)


# print([(whitebox.x, whitebox.y) for whitebox in WhiteBox.all_whiteboxes])
# print(WhiteBox.all_whiteboxes)

# print(WhiteBox.find_whitebox(2, 2))
print(Task.all_tasks[15].__dict__)
print([(whitebox.x, whitebox.y) for whitebox in Task.all_tasks[15].related_whiteboxes])


# for i in row1 


def create_options(value, num_cells):
    max_number = value - sum(range(1, num_cells))
    if max_number > 9:
        max_number = 9

    smallest_number = value - sum(range(max_number, max_number-num_cells+1, -1))
    if smallest_number < 0:
        return 1

    return list(range(smallest_number, max_number+1))


print(create_options(4, 2))

