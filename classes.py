import re
import itertools
class WhiteBox:
    all_whiteboxes = []
    def __init__(self, x, y, value):
        self.value = value
        self.x = x
        self.y = y
        self.tasks = []
        self.options = None
        WhiteBox.all_whiteboxes.append(self)


    def __str__(self) -> str:
        return f'{self.x}, {self.y}'


    @classmethod
    def find_whitebox(cls, x, y):
        whitebox = list(filter(lambda obj:(obj.x == x) & (obj.y == y), cls.all_whiteboxes))
        if len(whitebox) == 0:
            return None
        else:
            return whitebox[0]


    def is_valid(self, value):
        old = self.value
        self.value = value
        if (self.tasks[0].is_valid() and self.tasks[1].is_valid()):
            return True

        else:
            self.value = old
            return False


class Task:
    all_tasks = []
    def __init__(self, text, x: int, y: int) -> None:
        self._text = text
        self.x = x
        self.y = y
        self.related_whiteboxes = []
        Task.all_tasks.append(self)

    
    def evaluate_text(self):
        self.value = int(re.sub('[^0-9]', '', self._text))
        self.direction = re.sub('[^a-z]', '', self._text)


    def values_filled(self):
        for whitebox in self.related_whiteboxes:
            if whitebox.value is None:
                return False
        return True

    
    def calculate_combinations(self):
        numbers = list(range(1, 10))
        self.all_combinations = [list(seq) for seq in itertools.permutations(numbers, len(self.related_whiteboxes)) if sum(seq) == self.value]


    @property
    def current_combination(self):
        return [whitebox.value for whitebox in self.related_whiteboxes if whitebox.value != 0]


    def complete(self):
        return (0 not in self.current_combination)


    def is_valid(self):
        for i, combination in enumerate(self.all_combinations):
            if self._single_list_validation(combination):
                # self.all_combinations = self.all_combinations[i:]
                return True
        else:
            return False


    def _single_list_validation(self, ls):
        return self.current_combination == ls[:len(self.current_combination)]


         


