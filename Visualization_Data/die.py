from random import randint

class Die():
    """ 表示一个筛子的类"""

    def __init__(self, num_sides=6):
        """筛子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和筛子面之间的随机"""
        return randint(1, self.num_sides)