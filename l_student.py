# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if 0 <= self.score <= 100:
            if 60 <= self.score < 80:
                return 'B'
            if self.score >= 80:
                return 'A'
            return 'C'
        else:
            raise ValueError()
