import re

class WhiteBox:
    all_whiteboxes = []
    def __init__(self, x, y):
        self.options = []
        self.neighbours = []
        self.final_value = None
        self.x = x
        self.y = y
        self.related_blackboxes = []

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



    def check_xy(self, obj):
        return (obj.x == x) and (obj.y == y)
        # for whitebox in cls.all_whiteboxes:
        #     if (whitebox.x == x) and (whitebox.y == y):
        #         return whitebox
        #     else:
        #         return None
    
    
    

# class BlackBox:
#     def __init__(self):
#         self.coordinates
#         self.text
#         self.tasks

    
#     def make_tasks(self, text: str):
#         pass

class Task:
    all_tasks = []
    def __init__(self, text, x: int, y: int) -> None:
        self._text = text
        self.x = x
        self.y = y
        self.related_whiteboxes = []
        Task.all_tasks.append(self)

    
    def evaluate_text(self):
        self.value = int(re.sub('[^1-9]', '', self._text))
        self.direction = re.sub('[^a-z]', '', self._text)
